"""
MIN AND MAX NUMBERS:
    | Type    |       Minimum       |       Maximum      |
    | :-----: | :-----------------: | :----------------: |
    | Integer |              -2**31 |          2**31 - 1 |
    | Float   |       float('-inf') |       float('inf') |
    | Float   | -sys.float_info.max | sys.float_info.max |
"""

from random import uniform
from typing import Callable, TypeVar, List

from prettytable import PrettyTable

# 1. GENERIC TYPES
T = TypeVar('T', int, float)

# 2. CONSTANTS
DECIMAL_DIGITS = 0
MIN_INTEGER = -2**31
MAX_INTEGER = 2**31 - 1
TABLE_FIELD_NAMES = ['Initial List', 'After FILTER']
VALUE_NEGATIVE_EXCEPTION = 'Error: Please enter a non-negative value!'
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid value!'

# 3. FUNCTIONS
def get_list_length() -> int:
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

def generate_random_number(
        start: T = MIN_INTEGER,
        end: T = MAX_INTEGER,
        decimal_digits: int = DECIMAL_DIGITS) -> T:
    """
    Generates a random number
    :param start: Minimum value
    :param end: Maximum value
    :param decimal_digits: Number of decimal places to round to
    :return: A random float rounded to the specified decimal places
    """
    number = uniform(start, end)
    if isinstance(start, int) and isinstance(end, int) and decimal_digits == 0:
        return int(round(number))
    return round(number, decimal_digits)

def generate_number_list(
        list_len: int,
        start: T = MIN_INTEGER,
        end: T = MAX_INTEGER) -> List[T]:
    """
    Generates a list of random numbers
    :param list_len: Length of the list to generate
    :param start: Minimum value
    :param end: Maximum value
    :return: A list of unique random numbers
    """
    unique_numbers = set()
    while len(unique_numbers) < list_len:
        unique_numbers.add(generate_random_number(start=start, end=end))
    return list(unique_numbers)


filter_list: Callable[[List[T]], List[T]] = \
    lambda lst: (list(filter(lambda item: item % 3 == 0, lst)))

convert_format: Callable[[List[T], int], List[T]] = \
    lambda value_obj, decimal_digits: [round(item, decimal_digits) for item in value_obj]

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
    table = generate_table(table_field_names=TABLE_FIELD_NAMES)
    case_num = 1

    while True:
        list_length = get_list_length()
        if list_length == 0:
            break
        initial_list = generate_number_list(list_len=list_length, start=MIN_INTEGER, end=MAX_INTEGER)
        list_after_filter = filter_list(lst=initial_list)

        formatted_initial_list = convert_format(value_obj=initial_list, decimal_digits=DECIMAL_DIGITS)
        formatted_list_after_filter = convert_format(
            value_obj=list_after_filter, decimal_digits=DECIMAL_DIGITS)

        table.add_row([formatted_initial_list, formatted_list_after_filter])

        continue_input = input('Do you want more cases?\n0 - No\n1 - Yes\n').strip()
        if continue_input != '1':
            break
        case_num += 1

    print(table)
    print('End of the program')

if __name__ == '__main__':
    main()