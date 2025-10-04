from random import uniform
from typing import Callable, TypeVar, List, Dict

from prettytable import PrettyTable

# 1. GENERIC TYPES
T = TypeVar('T', str, float)

# 2. CONSTANTS
DECIMAL_DIGITS = 2
MIN_FLOAT = 10.0
MAX_FLOAT = 100.0
TABLE_FIELD_NAMES = ['Case', 'Initial Dict', 'Ordered by Key', 'Ordered by Value']
VALUE_NEGATIVE_EXCEPTION = 'Error: Please enter a non-negative value!'
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid value!'

# 3. FUNCTIONS
def get_dict_length() -> int:
    """
        Reads a number from user input and validates it as an integer
        :return: A valid integer number entered by the user
        """
    while True:
        try:
            num_entries = int(input("Enter the dictionary length (or 0 to exit): "))
            if num_entries < 0:
                print(VALUE_NEGATIVE_EXCEPTION)
                continue
            return num_entries
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

def generate_product_code() -> str:
    """
    Reads a product code from user input and validates it
    :return: Product code as a string
    """
    while True:
        try:
            product_code = input("Enter the product code (or 0 to exit): ").strip()
            if product_code == '0' or (product_code.isnumeric() and len(product_code) > 0):
                return product_code
            print(VALUE_VALID_EXCEPTION)
            continue
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

def generate_random_price(
        start: T = MIN_FLOAT,
        end: T = MAX_FLOAT,
        decimal_digits: int = DECIMAL_DIGITS) -> T:
    """
    Generates a random price within specified bounds
    :param start: Minimum value
    :param end: Maximum value
    :param decimal_digits: Number of decimal places to round to
    :return: A random float rounded to the specified decimal places
    """
    return round(uniform(start, end), decimal_digits)

def generate_product_dict(
        dict_len: int,
        start: T = MIN_FLOAT,
        end: T = MAX_FLOAT) -> Dict[str, float]:
    """
    Generates a dictionary with product codes and random prices
    :param dict_len: Number of entries in the dictionary
    :param start: Minimum value
    :param end: Maximum value
    :return: A dictionary with product codes as keys and prices as values
    """
    return {generate_product_code():
                generate_random_price(start=start, end=end) for _ in range(dict_len)}

order_by_key: Callable[[Dict[str, T]], Dict[str, T]] = \
    lambda value_obj: dict(sorted(value_obj.items()))

order_by_value: Callable[[Dict[str, T]], Dict[str, T]] = \
    lambda value_obj: dict(sorted(value_obj.items(), key = lambda item: item[1]))

convert_format: Callable[[Dict[str, T], int], Dict[str, T]] = \
    lambda value_obj, decimal_digits: \
        {item_key: round(item_value, decimal_digits)
         for item_key, item_value in value_obj.items()}

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
        dict_length = get_dict_length()
        if dict_length == 0:
            break
        initial_dict = generate_product_dict(dict_len=dict_length, start=MIN_FLOAT, end=MAX_FLOAT)
        dict_ordered_by_key = order_by_key(value_obj=initial_dict)
        dict_ordered_by_value = order_by_value(value_obj=initial_dict)

        # formatted_initial_dict = convert_format(
        #     value_obj=initial_dict, decimal_digits=DECIMAL_DIGITS
        # )
        # formatted_dict_ordered_by_key = convert_format(
        #     value_obj=dict_ordered_by_key, decimal_digits=DECIMAL_DIGITS)
        # formatted_dict_ordered_by_value = convert_format(
        #     value_obj=dict_ordered_by_value, decimal_digits=DECIMAL_DIGITS)

        table.add_row([case_num, initial_dict, dict_ordered_by_key, dict_ordered_by_value])
        # table.add_row([case_num, formatted_initial_dict,
        #                formatted_dict_ordered_by_key, formatted_dict_ordered_by_value])

        continue_input = input('Do you want more cases?\n0 - No\n1 - Yes\n').strip()
        if continue_input != '1':
            break
        case_num += 1

    print(table)
    print('End of the program')

if __name__ == '__main__':
    main()