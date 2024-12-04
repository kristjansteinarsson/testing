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
    clear_screen()
    search = input("\nSearch for User: ")
    staff = load_json_data(STAFF_FILE)
    for user in staff:
        if search == user['name']:
            print(f"Name: {user['name']} | ID: {user['id']} | Role: {user['role']}")
    input("\nPress enter to go back...")

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

def delete_user():
    clear_screen()
    staff = load_json_data(STAFF_FILE)

    print("USERS:\n")
    for user in staff:
        print(f"Name: {user['name']} | ID: {user['id']} | Role: {user['role']}")
    print()

    name = input("Name of User to delete: ")
    user_to_delete = None
    for user in staff:
        if name == user['name']:
            user_to_delete = user
            break

    clear_screen()

    if user_to_delete:
        print(f"Name: {user_to_delete['name']} | ID: {user_to_delete['id']} | Role: {user_to_delete['role']}")
        sure = input("\nAre you sure you want to delete this user? (Y/N): ")
        if sure == "Y":
            staff.remove(user_to_delete)
            save_user(STAFF_FILE, staff)
            print("User deleted")
        else:
            print("Operation canceled.")
    else:
        print("No user found with that name.")
    input("\nPress enter to go back...")

def staff_ui_main():
    while True:
        load_all_users()
        print("=== Employees / Users ===")
        print("\n1. Inspect User\n2. Create User\n3. Delete User\n4. Go Back\n")
        val = int(input("Enter: "))
        if val == 4:
            break
        elif val == 1:
            inspect_user()
        elif val == 2:
            create_user()
        elif val == 3:
            delete_user()