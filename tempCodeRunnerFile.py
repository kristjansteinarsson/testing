

    def clear_screen(self):
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def log_in(self):
        """Handles the login process."""
        while self.running:
            self.clear_screen()
            print("=== Welcome to NaN Air Systems ===")
            print("\n1. Log in\n2. Quit\n")
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
            username = input("\nName: ").strip()
            try:
                user_id = int(input("ID: "))
            except ValueError:
                print("Error: ID must be a number.")
                input("\nPress Enter to continue...")
                continue

            staff = load_json_data(STAFF_FILE)

            for user in staff:
                if user['name'] == username and user['id'] == user_id:
                    self.user = user
                    if user['role'].lower() == 'superior':
                        self.superior_main()
                    else:
                        self.employee_main()
                    break
            else:
                print("Error: User or ID doesn't exist.")
                input("\nPress Enter to return to the menu...")

    def superior_main(self):
        """Handles the superior workflow."""
        while self.running:
            self.clear_screen()
            print(f"=== Welcome {self.user['name']} | Superior ===")
            print('''