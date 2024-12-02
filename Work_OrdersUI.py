import os
from MainUI import *


STORAGE_ROOT = "storage/orders"

def clear_screen():
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

def create_work_order():
    title = input("Title of Order: ")
    desc = input("Description of Order: ")
    for i in range(len(title)):
        if title[i] == " ":
            title[i] == "_"

    file = open(f"{STORAGE_ROOT}/{title.lower()}.txt", 'w')
    file.write(f"Title: {title}\n{desc}")
    file.close()

def open_all_orders():
    for path, _, files in os.walk(STORAGE_ROOT):
        for name in files:
            fileName = os.path.join(path, name)
            with open(fileName, 'r') as files:
                print(files.readline())

def open_work_order():
    open_all_orders()
    search = input("Order to open: ")
    clear_screen()
    for i in range(len(search)):
        if search[i] == " ":
            search[i] == "_"
    with open (f"{STORAGE_ROOT}/{search.lower()}.txt", 'r') as file:
        read = file.readlines()
        for line in read:
            print(line)
    
    input("\nEnter to continue...")

def work_orders_main():
    while True:
        clear_screen()
        print("=== Work Orders ===\n")
        print("1. Create Work Report\n2. Print all Reports\n3. Open Work Order\n4. Go Back")
        val = int(input("Enter: "))
        if val == 4:
            break
        elif val == 1:
            clear_screen()
            create_work_order()
            clear_screen()
        elif val == 2:
            clear_screen()
            open_all_orders()
            input("Press enter to go back...")
            clear_screen()

        elif val == 3:
            clear_screen()
            open_work_order()
            clear_screen()