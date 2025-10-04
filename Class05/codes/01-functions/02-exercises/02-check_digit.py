"""
INSTRUCTIONS:
    Write a function that receives as input a five-digit integer in the range [10,000, 99,999],
    representing product codes sold in a store. The function should calculate and return the
    check digit using the calculation rule explained below. Write the main programme to test
    the function

RULE:
    Consider the code 31483, where each digit is multiplied by a weight starting at 2 and
    ending at 6. The resulting values are summed, and the remainder of their division by 7
    is calculated

    | Digit          | 3 | 1 |  4 |  8 |  3 |            |
    | Weight         | 2 | 3 |  4 |  5 |  6 |            |
    | Multiplication | 6 | 3 | 16 | 40 | 18 |   Sum = 83 |
    |                |   |   |    |    |    | 83 % 7 = 6 |

TEST CASE:
    | Code  | Digit |
    | ----- | ----: |
    | 31483 |     6 |
    | 11000 |     5 |
    | 12350 |     3 |
    | 12500 |     0 |
    | 12600 |     4 |
    | 12750 |     5 |
    |     0 | ===== |

"""
from typing import TypeVar

from prettytable import PrettyTable

# 1. GENERIC TYPES
T = TypeVar('T')

# 2. CONSTANTS
# FORMAT_SPEC_DOT_5d = '5d'
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid 5-digit code!'
MIN_VALUE = 10000
MAX_VALUE = 99999
TABLE_FIELD_NAMES = ['Code', 'Check Digit']

# 3. FUNCTION
def get_five_digit_code() -> int:
    """
    Reads a five-digit product code from user input and validates it
    :return: A valid integer in the range [10000, 99999] or 0 to stop
    """
    while True:
        try:
            code = int(input('Enter a 5-digit product code (or 0 to stop): ').strip())
            if code == 0 or MIN_VALUE <= code <= MAX_VALUE:
                return code
            print(VALUE_VALID_EXCEPTION)
        except ValueError:
            print(VALUE_VALID_EXCEPTION)


def calculate_check_digit(code: int) -> int:
    """
    Calculates the check digit for a five-digit product code
    :param code: A five-digit product code
    :return: The check digit
    """
    digits = [int(digit) for digit in str(code)]
    weights = range(2, 7)
    weighted_sum = sum(digit * weight for digit, weight in zip(digits, weights))
    return weighted_sum % 7

def generate_table(table_field_names: list[str]) -> PrettyTable:
    """
    Generates a table to display the results
    :param table_field_names: Field names for the table
    :return: A formatted table
    """
    table = PrettyTable()
    table.field_names = table_field_names
    return table

# def display_results_table(code: int, check_digit: int, table: T) -> None:
#     """
#     Displays a formatted table of code and check digit
#     :param code: Product code (5-digit)
#     :param check_digit: Calculated check digit
#     :param table: Table to display the results
#     :return: None
#     """
#     table.add_row([code, check_digit])
#     print(table)

# 4. MAIN PROGRAM
def main():
    print("Start of the program")
    results_table = generate_table(table_field_names=TABLE_FIELD_NAMES)

    while True:
        product_code = get_five_digit_code()
        if product_code == 0:
            break
        product_check_digit = calculate_check_digit(code=product_code)
        results_table.add_row([product_code, product_check_digit])
    print('Results')
    print(results_table)
    print('\nEnd of the program')

if __name__ == '__main__':
    main()