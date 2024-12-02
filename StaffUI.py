import random
from utils import *
from MainUI import *

STAFF_FILE = "staff.json"

def clear_screen():
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

def load_all_users():
    clear_screen()
    print("USERS:\n")
    staff = load_json_data(STAFF_FILE)
    for user in staff:
        print(f"Name: {user['name']} | ID: {user['id']} | Role: {user['role']}")
    print()

def inspect_user():
    pass

def create_user():
    load_all_users()
    staff = load_json_data(STAFF_FILE)

    name = input("Name of User: ")

    while True:
        role = input("Employee or Superior? (E/S): ")
        if role != "E" and role != "S":
            print("ERROR\nType in either E or S")
        else:
            if role == "E":
                role = "Employee"
            elif role == "S":
                role = "Superior"
            break

    id = random.randint(1000, 9999)
    new_user = {"id" : id, "name": name, "role": role}
    
    staff.append(new_user)
    save_user(STAFF_FILE, staff)

def staff_ui_main():
    while True:
        load_all_users()
        print("=== Employees / Users ===")
        print("\n1. Inspect User\n2. Create User\n3. Go Back\n")
        val = int(input("Enter: "))
        if val == 3:
            break
        elif val == 1:
            pass
        elif val == 2:
            create_user()