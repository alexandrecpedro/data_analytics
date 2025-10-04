"""
INSTRUCTION:
    Write a programme that reads a positive integer N from the keyboard
    and creates a list with N random numbers between -1000 and 1000.
    Then use list comprehension to produce a new list containing only
    the positive values (including zero) and another list for negative values

TIP: Use the randint() function to generate the random numbers
"""
from random import randint
from typing import Callable, List, TypeVar

from prettytable import PrettyTable

# 1. GENERIC TYPES
# F = TypeVar('F') # float
# S = TypeVar('S') # str

# 2. CONSTANTS
TABLE_FIELD_NAMES = ['Case', 'Number N', 'Original List', 'List (positive and zero)', 'List (negative)']
MIN_INTEGER, MAX_INTEGER = -1000, 1000

INVALID_OPTION_EXCEPTION = "Error: Invalid choice. Please enter '0' for No or '1' for Yes!"
INVALID_VALUE_EXCEPTION = "Error: Please enter a valid value!"
NEGATIVE_VALUE_EXCEPTION = "Error: Please enter a non-negative value!"

# 3. FUNCTIONS
def get_integer_input(prompt: str) -> int:
    """
    Requests a positive integer value from the user with exception handling
    :param prompt: Message to prompt the value
    :return: A valid integer number
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0:
                print(NEGATIVE_VALUE_EXCEPTION)
                continue
            return value
        except ValueError:
            print(INVALID_VALUE_EXCEPTION)

def generate_random_integer_list(
        list_len: int,
        start: int = MIN_INTEGER,
        end: int = MAX_INTEGER) -> List[int]:
    """
    Generates a random list of integers within specified bounds
    :param list_len: Length of list
    :param start: Minimum value
    :param end: Maximum value
    :return: A random integer list
    """
    return [randint(start, end) for _ in range(list_len)]

def generate_table(table_field_names: List[str]) -> PrettyTable:
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
    table = PrettyTable(field_names=TABLE_FIELD_NAMES)
    case_num = 1

    while True:
        # Step 1: Get the list length
        list_length = get_integer_input(prompt='Enter a positive integer number for list length: ')

        # Step 2: Generate list of random integer within specified bounds
        int_list = generate_random_integer_list(list_len=list_length)

        # Step 3: Filter positive & zero, and negative values
        positives = [list_item for list_item in int_list if list_item >= 0]
        negatives = [list_item for list_item in int_list if list_item < 0]

        # Step 4: Add result to table
        table.add_row([case_num, list_length, int_list, positives, negatives])

        # Step 5: Ask if the user would like to continue
        while True:
            continue_input = input('Do you want another case?\n0 - No\n1 - Yes\n').strip()
            if continue_input in {'0', '1'}:
                break
            print(INVALID_OPTION_EXCEPTION)

        if continue_input != '1':
            break
        case_num += 1

    # Step 6: Display the table
    print(table)
    print('End of the program')

if __name__ == '__main__':
    main()