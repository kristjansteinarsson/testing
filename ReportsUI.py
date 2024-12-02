import os
from MainUI import *

STORAGE_ROOT = "storage/reports"

def clear_screen():
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

def create_maintenance_report():
    title = input("Title of Report: ")
    desc = input("Description of Report: ")
    for i in range(len(title)):
        if title[i] == " ":
            title[i] == "_"

    file = open(f"{STORAGE_ROOT}/{title.lower()}.txt", 'w')
    file.write(f"Title: {title}\n{desc}")
    file.close()

def open_all_reports():
    for path, _, files in os.walk(STORAGE_ROOT):
        for name in files:
            fileName = os.path.join(path, name)
            with open(fileName, 'r') as files:
                print(files.readline())

def open_maintenance_report():
    open_all_reports()
    search = input("Report to open: ")
    clear_screen()
    for i in range(len(search)):
        if search[i] == " ":
            search[i] == "_"
    with open (f"{STORAGE_ROOT}/{search.lower()}.txt", 'r') as file:
        read = file.readlines()
        for line in read:
            print(line)
    
    input("\nEnter to continue...")

def maintenance_reports_main():
    while True:
        clear_screen()
        print("=== Maintenance reports ===\n")
        print("1. Create Maintenance Report\n2. Print all Reports\n3. Open Maintenance Report\n4. Go Back")
        val = int(input("Enter: "))
        if val == 4:
            break
        elif val == 1:
            clear_screen()
            create_maintenance_report()
            clear_screen()
        elif val == 2:
            clear_screen()
            open_all_reports()
            input("Press enter to go back...")
            clear_screen()

        elif val == 3:
            clear_screen()
            open_maintenance_report()
            clear_screen()