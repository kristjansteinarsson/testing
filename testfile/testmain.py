from work_orders import *
import os

def clear_screen():
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

while True:
    print("1. Create Work Report\n2. Print all Reports\n3. Open Work Order\n4. Quit")
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
