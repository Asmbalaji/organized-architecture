
from inputs.input_handler import get_input
from outputs.output_handler import display_output
from menus.menu import show_menu

from operations.list_operations import (
    add_element,
    display_list,
    remove_element
)

my_list = []

while True:

    choice = show_menu()

    if choice == "1":

        value = get_input()
        add_element(my_list, value)

        print("Element added successfully!")

    elif choice == "2":

        data = display_list(my_list)
        display_output(data)

    elif choice == "3":

        value = get_input()

        if remove_element(my_list, value):
            print("Element removed successfully!")
        else:
            print("Element not found!")

    elif choice == "4":

        print("Thank you!")
        break

    else:

        print("Invalid choice!")




