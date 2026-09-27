files = {}
next_block = 0


def create_file(name, data):
    global next_block

    if name in files:
        print("File already exists.")
        return

    files[name] = {
        "data": data,
        "block": next_block
    }

    next_block += 1

    print("File created successfully.")


def read_file(name):
    if name in files:
        print("File Data:", files[name]["data"])
        print("Block:", files[name]["block"])
    else:
        print("File not found.")


def delete_file(name):
    if name in files:
        del files[name]
        print("File deleted successfully.")
    else:
        print("File not found.")


def show_directory():
    if len(files) == 0:
        print("Directory is empty.")
        return

    print("\nDirectory")
    print("----------------")

    for name in files:
        print("File:", name)
        print("Block:", files[name]["block"])
        print()


# Program starts here

while True:

    print("\n----- SIMPLE FILE SYSTEM -----")
    print("1. Create File")
    print("2. Read File")
    print("3. Delete File")
    print("4. Show Directory")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        name = input("Enter file name: ")
        data = input("Enter file data: ")

        create_file(name, data)

    elif choice == 2:

        name = input("Enter file name: ")

        read_file(name)

    elif choice == 3:

        name = input("Enter file name: ")

        delete_file(name)

    elif choice == 4:

        show_directory()

    elif choice == 5:

        print("Program ended.")
        break

    else:

        print("Invalid choice.")