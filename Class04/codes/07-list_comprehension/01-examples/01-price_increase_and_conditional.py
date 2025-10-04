"""
INSTRUCTIONS:
    Consider that you need to apply a percentage increase to all prices in a list.
    Write a programme that reads this list from the keyboard. The values should be
    read until zero is entered. Then, read the percentage increase. Next, using
    list comprehension, apply this increase to values that match a chosen condition
    and display the result on the screen

TEST CASE:
    | Case |     Original Prices     | Increase (%) |          Prices with Increase          |
    | :--: | ----------------------- | :----------: | -------------------------------------- |
    |   1  | [50, 120, 20, 100, 200] |    10.00     | [55.00, 132.00, 22.00, 110.00, 220.00] |
    |   2  | [50, 120, 20, 100, 200] |    10.00     |             [55.00, 22.00]             |
"""
import locale
from locale import localeconv, setlocale
from typing import Callable, Dict, List, TypeVar

from prettytable import PrettyTable

# 1. GENERIC TYPES
# F = TypeVar('F') # float
# S = TypeVar('S') # str

# 2. CONSTANTS
LOCALE = setlocale(locale.LC_ALL, '')
LOCAL_CURRENCY_SYMBOL = localeconv().get('currency_symbol').strip()
LOCAL_INT_CURRENCY_SYMBOL = localeconv().get('int_curr_symbol').strip()

DECIMAL_DIGITS = 2
TABLE_FIELD_NAMES = ['Case', 'Original Prices', 'Increase (%)', 'Prices with Increase']

INVALID_OPTION_EXCEPTION = "Error: Invalid choice. Please enter '1' or '2'!"
INVALID_VALUE_EXCEPTION = "Error: Please enter a valid value!"
NEGATIVE_VALUE_EXCEPTION = "Error: Please enter a non-negative value!"

# 3. FUNCTION
def get_float_input(prompt: str) -> float | None:
    """
    Requests a float value from the user with exception handling
    :param prompt: Message to prompt the value
    :return: A valid float number
    """
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                print(NEGATIVE_VALUE_EXCEPTION)
                continue
            return value
        except ValueError:
            print(INVALID_VALUE_EXCEPTION)

def get_price_list() -> List[float]:
    """
    Collects a list of prices from the user until they enter 0
    :return: List of prices provided by the user
    """
    print('Please provide prices for the list (or 0 to exit)')
    return [price_item for price_item in iter(
        lambda: get_float_input(prompt=f'Enter a price ({LOCAL_INT_CURRENCY_SYMBOL}): '), 0)]

def set_condition_type() -> Callable[[float], bool]:
    """
    Prompts the user to select a condition type for applying the increase
    :return: The appropriate condition function
    """
    global condition
    print("Choose the condition for applying the increase:")
    print("0 - Apply increase to all prices")
    print("1 - Apply increase only to prices less than 100")

    condition_options: Dict[str, Callable[[float], bool]] = {
        '0': lambda price: True,
        '1': lambda price: price < 100
    }

    while True:
        condition_choice = input("Enter your choice (0 or 1): ").strip()
        if condition_choice in condition_options:
            return condition_options[condition_choice]
        print(INVALID_OPTION_EXCEPTION)

def apply_increase(
        price_list: List[float],
        increase_percentage: float,
        condition: Callable[[float], bool]) -> List[float]:
    """
    Applies a percentage increase to each price that fields the condition in the list
    :param price_list: Original list of prices
    :param increase_percentage: Percentage increase
    :param condition: A callable condition to filter prices
    :return: New list of prices with the increase applied
    """
    return [round(price_item * (1 + increase_percentage / 100), DECIMAL_DIGITS)
            if condition(price_item) else price_item for price_item in price_list]

currency_format_list: Callable[[List[float]], List[str]] = \
    lambda value_obj: [locale.currency(item, symbol=True, grouping=True)
                       for item in value_obj]

convert_format: Callable[[float, int], float] = \
    lambda value, format_spec = DECIMAL_DIGITS: round(value, format_spec)

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
print("Start of the program")
table = generate_table(table_field_names=TABLE_FIELD_NAMES)
case_num = 1

while True:
    # (a) Step 1: Collect prices from the user
    price_list = get_price_list()
    if not price_list:
        print('The price list is empty. Terminating the programme...')
        break

    # (b) Step 2: Request percentage increase
    percentage_increase = get_float_input(
        prompt='Enter the percentage increase (without the %): ')

    # (c) Step 3: Select condition type
    condition = set_condition_type()

    # (d) Step 4: Apply the increase
    price_list_increase = apply_increase(
        price_list=price_list, increase_percentage=percentage_increase,
        condition=condition
    )

    # (e) Step 5: Convert list to currency format and add to the table in one step
    table.add_row([
        case_num,
        currency_format_list(value_obj=price_list),
        convert_format(value=percentage_increase, format_spec=DECIMAL_DIGITS),
        currency_format_list(value_obj=price_list_increase)
    ])

    # (f) Step 6: Ask the user if they would like to add more cases
    continue_input = input('Do you want more cases?\n0 - No\n1 - Yes\n').strip()
    if continue_input != '1':
        break
    case_num += 1

# (g) Step 7: Display the table
print(table)
print('End of the program')