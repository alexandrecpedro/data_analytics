"""
INSTRUCTIONS:
    Write a programme that reads two real numbers and calculates
    the four arithmetic operations between them using a function.
    Display the result with two decimal places

TEST CASE:
    | Value 1 | Value 2 |   Sum | Difference | Multiplication | Division |
    | ------- | ------- | ----- | ---------- | -------------- | -------- |
    |    12.6 |     4.4 | 17.00 |       8.20 |          55.44 |     2.86 |
"""
from typing import TypeVar

from prettytable import PrettyTable

# 1. GENERIC TYPES
T = TypeVar('T')
U = TypeVar('U')

# 2. CONSTANTS
FORMAT_SPEC_DOT_2f = '.2f'
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid value!'
TABLE_FIELD_NAMES = ['Field', 'Value']

# 3. FUNCTION
def get_number() -> float:
    """
    Reads a number from user input and validates it as a float
    :return: A valid floating-point number entered by the user
    """
    while True:
        try:
            return float(input('Enter the number: '))
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

def convert_format(value_obj: T, format_spec: str) -> str:
    """
    Formats the given value_obj to a string with the specified format
    :param value_obj: The value to format
    :param format_spec: The formatting string (e.g., '.2f')
    :return: A string representing the formatted value
    """
    return f'{value_obj:{format_spec}}'

def arithmetic_operations(value_1: T, value_2: U, format_spec: str) -> dict[str, str]:
    """
    Calculates and formats the results of basic arithmetic operations
    :param value_1: First operand
    :param value_2: Second operand
    :param format_spec: The formatting string for output
    :return: A dictionary with formatted results for each operation
    """
    sum_obj = value_1 + value_2
    difference_obj = value_1 - value_2
    multiplication_obj = value_1 * value_2
    division_obj = value_1 / value_2

    return {
        "sum": convert_format(value_obj=sum_obj, format_spec=format_spec),
        "difference": convert_format(value_obj=difference_obj, format_spec=format_spec),
        "multiplication": convert_format(value_obj=multiplication_obj, format_spec=format_spec),
        "division": convert_format(value_obj=division_obj, format_spec=format_spec)
    }

def display_results_table(
        dict_operations: dict[str, str],
        table_field_names: list[str]) -> None:
    """
    Displays a formatted table of arithmetic operations and their results
    :param dict_operations: Dictionary with operation results
    :param table_field_names: Field names for the table
    :return: None
    """
    table = PrettyTable()
    table.field_names = table_field_names

    for key, value in dict_operations.items():
        table.add_row([key, value])

    print(table)

# 4. MAIN PROGRAM
def main():
    print("Start of the program")
    number_1 = get_number()
    number_2 = get_number()
    results = arithmetic_operations(value_1=number_1, value_2=number_2, format_spec=FORMAT_SPEC_DOT_2f)
    print('Results')
    display_results_table(dict_operations=results, table_field_names=TABLE_FIELD_NAMES)
    # for operation, result in results.items():
    #     print(f'\t{operation}\t= {result}')
    print('End of the program')

if __name__ == '__main__':
    main()