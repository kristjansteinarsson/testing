import os
from utils import load_json_data

STAFF_FILE = "staff.json"

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def log_in():
    clear_screen()
    print("=== Welcome to NaN Air Systems ===")
    print("1. Log in\n2. Quit")
    val = int(input("Enter: "))
    
    clear_screen()

    if val == 2:
        pass
    else:
        print("=== Log In ===")
        username = input("Name: ").strip()
        try:
            id = int(input("ID: "))
        except ValueError:
            print("Error: ID must be a number.")
            return

        staff = load_json_data(STAFF_FILE)

        for user in staff:
            if user['name'] == username and user['id'] == id:
                if user['role'].lower() == 'superior':
                    superior_main(username)
                else:
                    employee_main(username)
                return

        print("Error: User or ID doesn't exist.")

def employee_main(user):
    clear_screen()
    print(f"Welcome {user} | Employee")
    print("1. Log Out")
    val = int(input("Enter: "))
    if val == 1:
        log_in()


def superior_main(user):
    clear_screen()
    print(f"Welcome {user} | Superior")
    print("1. Log Out")
    val = int(input("Enter: "))
    if val == 1:
        log_in()

if __name__ == "__main__":
    log_in()