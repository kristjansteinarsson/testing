import os
from utils import load_json_data

STAFF_FILE = "staff.json"

class NaNAirSystems:
    def __init__(self):
        self.user = None  # Store the logged-in user's data
        self.running = True  # Controls whether the application runs

    def clear_screen(self):
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def log_in(self):
        """Handles the login process."""
        while self.running:
            self.clear_screen()
            print("=== Welcome to NaN Air Systems ===")
            print("1. Log in\n2. Quit")
            try:
                val = int(input("Enter: "))
            except ValueError:
                print("Error: Please enter a number.")
                input("\nPress Enter to continue...")
                continue

            if val == 2:
                self.clear_screen()
                self.running = False
                break

            self.clear_screen()
            print("=== Log In ===")
            username = input("Name: ").strip()
            try:
                user_id = int(input("ID: "))
            except ValueError:
                print("Error: ID must be a number.")
                input("\nPress Enter to continue...")
                continue

            staff = load_json_data(STAFF_FILE)

            for user in staff:
                if user['name'] == username and user['id'] == user_id:
                    self.user = user  # Save the logged-in user
                    if user['role'].lower() == 'superior':
                        self.superior_main()
                    else:
                        self.employee_main()
                    break  # Return to login menu after session ends
            else:
                print("Error: User or ID doesn't exist.")
                input("\nPress Enter to return to the menu...")

    def employee_main(self):
        """Handles the employee workflow."""
        while self.running:
            self.clear_screen()
            print(f"=== Welcome {self.user['name']} | Employee ===")
            print("1. Log Out")
            try:
                val = int(input("Enter: "))
            except ValueError:
                print("Error: Please enter a number.")
                input("\nPress Enter to continue...")
                continue

            if val == 1:
                self.user = None  # Log out the user
                break  # Return to the login menu
            else:
                print("Invalid option. Try again.")
                input("\nPress Enter to continue...")

    def superior_main(self):
        """Handles the superior workflow."""
        while self.running:
            self.clear_screen()
            print(f"=== Welcome {self.user['name']} | Superior ===")
            print('''
1. Destinations
2. All Employees / Users
3. All Properties
4. All Work Orders
5. All Maintenance Reports
6. Log Out
            ''')
            try:
                val = int(input("Enter: "))
            except ValueError:
                print("Error: Please enter a number.")
                input("\nPress Enter to continue...")
                continue

            if val == 6:
                self.user = None  # Log out the user
                break  # Return to the login menu

            elif val == 2:
                staff = load_json_data(STAFF_FILE)
                self.clear_screen()
                print("=== All Employees / Users ===")
                for user in staff:
                    print(f"Name: {user['name']} | ID: {user['id']} | Role: {user['role']}")
                input("\nPress Enter to return...")
            else:
                print("Feature not implemented yet.")
                input("\nPress Enter to continue...")

# Program entry point
if __name__ == "__main__":
    system = NaNAirSystems()
    system.log_in()