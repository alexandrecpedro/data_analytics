from random import random, randint
from typing import TypeVar

from prettytable import PrettyTable

# 1. GENERIC TYPES
T = TypeVar('T')

# 2. CONSTANTS
# DECIMAL_DIGITS = 2
# FORMAT_SPEC_DOT_2f = '.2f'
TABLE_FIELD_NAMES = ['Case', 'List 1', 'List 2', 'MAP List Result']
VALUE_NEGATIVE_EXCEPTION = 'Error: Please enter a non-negative value!'
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid value!'

# 3. FUNCTIONS
def get_list_length() -> int | None:
    """
        Reads a number from user input and validates it as an integer
        :return: A valid integer number entered by the user
        """
    while True:
        try:
            num_grades = int(input("Enter the list length (or 0 to exit): "))
            if num_grades < 0:
                print(VALUE_NEGATIVE_EXCEPTION)
                continue
            return num_grades
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

def generate_random_number(start: int, end: int) -> T:
    """
    Generates a random number
    :param start: Minimum value
    :param end: Maximum value
    :return: A random int
    """
    return randint(a=start, b=end)

def generate_number_list(list_len: int, start: T, end: T) -> list[T]:
    """
    Generates a list of random numbers
    :param list_len: Length of the list to generate
    :param start: Minimum value
    :param end: Maximum value
    :return: A list of random numbers
    """
    return [generate_random_number(start=start, end=end) for _ in range(list_len)]

# def map_with_list(lst: list[T]) -> list[T]:
#     """
#     Maps a list to a new list where each element is multiplied by 10
#     :param lst: The list to be mapped
#     :return: A new list with each element multiplied by 10
#     """
#     return list(map(lambda item: item * 10, lst))
"""
Maps two lists to a new list where each element is the sum of elements at the corresponding 
index in both lists
:param list1: The first list to be mapped
:param list2: The second list to be mapped
:return: A new list where each element is the sum of elements from list1 and list2 at each index
"""
map_with_lists = lambda list1, list2: list(
    map(lambda number_1, number_2: number_1 + number_2, list1, list2))

def generate_table(table_field_names: list[str]) -> PrettyTable:
    """
    Generates a table to display the results
    :param table_field_names: Field names for the table
    :return: A formatted table
    """
    table = PrettyTable()
    table.field_names = table_field_names
    return table

# 4. MAIN PROGRAM
def main():
    print("Start of the program")
    table = generate_table(table_field_names=TABLE_FIELD_NAMES)
    case_num = 1

    while True:
        list_length = get_list_length()
        if list_length == 0:
            break
        initial_list = generate_number_list(list_len=list_length, start=2, end=7)
        additional_list = generate_number_list(list_len=list_length, start=100, end=501)
        list_after_map = map_with_lists(list1=initial_list, list2=additional_list)

        table.add_row([case_num, initial_list, additional_list, list_after_map])

        continue_input = input('Do you want more cases?\n0 - No\n1 - Yes\n').strip()
        if continue_input != '1':
            break
        case_num += 1

    print(table)
    print('End of the program')

if __name__ == '__main__':
    main()