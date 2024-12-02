import os
root = "C:\\Users\\Lenovo\\Documents\\HR\\3-week\\testing\\storage\\orders"

def clear_screen():
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')


def create_work_order():
    title = input("Title of Order: ")
    desc = input("Description of Order: ")
    for i in range(len(title)):
        if title[i] == " ":
            title[i] == "_"

    file = open(f"{root}/{title.lower()}.txt", 'w')
    file.write(f"Title: {title}\n{desc}")
    file.close()

def open_all_orders():
    for path, _, files in os.walk(root):
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
    with open (f"{root}/{search.lower()}.txt", 'r') as file:
        read = file.readlines()
        for line in read:
            print(line)
    
    input("\nEnter to continue...")