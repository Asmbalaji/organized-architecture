def get_input():
    value = input("Enter a value: ").strip()

    while not value:
        print("Input cannot be empty!")
        value = input("Enter a value: ").strip()

    return value


def get_menu_choice():
    choice = input("Enter your choice: ").strip()

    while choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        choice = input("Enter your choice: ").strip()

    return choice