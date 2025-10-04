"""
INSTRUCTION:
    Use list comprehension to produce a list of all positive integers that
    are divisible by N and less than Limit. The integer values N and Limit
    should be read from the keyboard

TIP: Use range class
"""

import locale
from locale import localeconv, setlocale
from typing import Callable, Dict, List, TypeVar

from prettytable import PrettyTable

# 1. GENERIC TYPES
# F = TypeVar('F') # float
# S = TypeVar('S') # str

# 2. CONSTANTS
DECIMAL_DIGITS = 1
TABLE_FIELD_NAMES = ['Case', 'Number N', 'Limit', 'Divisible Numbers']

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

"""
Generates a list of positive integers divisible by a given number up to a specified limit
:param number: The integer divisor for generating divisible numbers
:param limit_number: The upper limit, non-inclusive, for the generated numbers
:return: A list of integers divisible by 'number' and less than 'limit_number'
"""
positive_int_divisible_list: Callable[[int, int], List[int]] = \
    lambda number, limit_number: [item for item in range(number, limit_number, number)]

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
    table = PrettyTable()
    table.field_names = TABLE_FIELD_NAMES
    case_num = 1

    while True:
        # Step 1: Get input values
        prompt_int_number = 'Enter a positive integer number for'
        N = get_integer_input(prompt=f'{prompt_int_number} N (divisor): ')
        Limit = get_integer_input(prompt=f'{prompt_int_number} Limit: ')

        # Step 2: Generate list of divisible numbers
        divisible_numbers = positive_int_divisible_list(number=N, limit_number=Limit)

        # Step 3: Add result to table
        table.add_row([case_num, N, Limit, divisible_numbers])

        # Step 4: Ask if the user would like to continue
        while True:
            continue_input = input('Do you want another case?\n0 - No\n1 - Yes\n').strip()
            if continue_input in {'0', '1'}:
                break
            print(INVALID_OPTION_EXCEPTION)

        if continue_input != '1':
            break
        case_num += 1

    # Step 5: Display the table
    print(table)
    print('End of the program')

if __name__ == '__main__':
    main()