from random import uniform
from sys import float_info
from typing import Callable, List, TypeVar

from prettytable import PrettyTable

# 1. GENERIC TYPES
T = TypeVar('T')

# 2. CONSTANTS
DECIMAL_DIGITS = 2
# FORMAT_SPEC_DOT_2f = '.2f'
MIN_FLOAT = -1000
MAX_FLOAT = 1000
TABLE_FIELD_NAMES = ['Case', 'Initial List', 'After MAP']
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
        start: T = MIN_FLOAT,
        end: T = MAX_FLOAT,
        decimal_digits: int = DECIMAL_DIGITS) -> T:
    """
    Generates a random number within specified bounds
    :param start: Minimum value
    :param end: Maximum value
    :param decimal_digits: Decimal digits format
    :return: A random float
    """
    return round(uniform(start, end), decimal_digits)

def generate_number_list(
        list_len: int,
        start: T = MIN_FLOAT,
        end: T = MAX_FLOAT) -> list[T]:
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
Maps a list to a new list where each element is multiplied by 10
:param lst: The list to be mapped
:return: A new list with each element multiplied by 10
"""
map_with_list: Callable[[List[T]], List[T]] = \
    lambda lst: list(map(lambda item: item * 10, lst))

convert_format: Callable[[List[T], int], List[T]] = \
    lambda value_obj, decimal_digits: [round(item, decimal_digits) for item in value_obj]

# def convert_format(value_obj: T, format_spec: str) -> str:
#     """
#     Formats the given value_obj to a string with the specified format
#     :param value_obj: The value to format
#     :param format_spec: The formatting string (e.g., '.2f')
#     :return: A string representing the formatted value
#     """
#     return f'{value_obj:{format_spec}}'

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
print("Start of the program")
table = generate_table(table_field_names=TABLE_FIELD_NAMES)
case_num = 1

while True:
    list_length = get_list_length()
    if list_length == 0:
        break
    initial_list = generate_number_list(list_len=list_length, start=MIN_FLOAT, end=MAX_FLOAT)
    list_after_map = map_with_list(lst=initial_list)

    formatted_initial_list = convert_format(value_obj=initial_list, decimal_digits=DECIMAL_DIGITS)
    formatted_list_after_map = convert_format(value_obj=list_after_map, decimal_digits=DECIMAL_DIGITS)

    table.add_row([case_num, formatted_initial_list, formatted_list_after_map])

    continue_input = input('Do you want more cases?\n0 - No\n1 - Yes\n').strip()
    if continue_input != '1':
        break
    case_num += 1

print(table)
print('End of the program')