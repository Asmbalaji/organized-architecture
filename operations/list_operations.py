def add_element(my_list: list, value: str) -> None:
    my_list.append(value)


def display_list(my_list: list) -> list:
    return my_list


def remove_element(my_list: list, value: str) -> bool:

    if value in my_list:
        my_list.remove(value)
        return True

    return False