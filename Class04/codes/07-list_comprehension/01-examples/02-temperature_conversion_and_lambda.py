"""
INSTRUCTIONS:
    Write a programme that converts a list of temperatures from Fahrenheit to Celsius or
    from Celsius to Fahrenheit based on user input. Display the resulting
    values with one decimal place.

    The conversion is done using the following formula:
        Celsius = (Fahrenheit - 32) * (5/9)
        Fahrenheit = Celsius * (9/5) + 32

TEST CASE:
    | Case | Fahrenheit (ºF) | Celsius (ºC) |
    | :--: | :-------------: | :----------: |
    |   1  |      83.0       |     28.3     |
    |   2  |      91.0       |     32.8     |
    |   3  |      79.0       |     26.1     |
    |   4  |      95.0       |     35.0     |
    |   5  |      104.0      |     40.0     |
    |   6  |      100.0      |     37.8     |
    |   7  |      98.0       |     36.7     |
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
TABLE_FIELD_NAMES = ['Case', 'Fahrenheit (degF)', 'Celsius (degC)']

INVALID_OPTION_EXCEPTION = "Error: Invalid choice. Please enter '1' or '2'!"
INVALID_VALUE_EXCEPTION = "Error: Please enter a valid value!"

# 3. FUNCTION
def get_float_input(prompt: str) -> float:
    """
    Requests a float value from the user with exception handling
    :param prompt: Message to prompt the value
    :return: A valid float number
    """
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print(INVALID_VALUE_EXCEPTION)

def set_conversion_type() -> Callable[[float], float]:
    """
    Prompts the user to select a conversion type (Fahrenheit to Celsius or Celsius to Fahrenheit)
    :return: A function for the chosen conversion
    """
    print("Choose the conversion type:")
    print("1 - Fahrenheit to Celsius")
    print("2 - Celsius to Fahrenheit")

    conversion_options = {
        '1': (lambda temp: (temp - 32) * (5 / 9), 'degF', 'degC'),
        '2': (lambda temp: temp * (9 / 5) + 32, 'degC', 'degF')
    }

    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice in conversion_options:
            return conversion_options[choice]
        print(INVALID_OPTION_EXCEPTION)

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
    # (a) Step 1: Select conversion type
    conversion_func, original_scale, target_scale = set_conversion_type()

    while True:
        # (b) Step 2: Get temperature in the original scale
        original_temp = get_float_input(f"Enter temperature in {original_scale} (or 0 to exit): ")

        if original_temp == 0:
            break

        original_temp = round(original_temp, DECIMAL_DIGITS)

        # (c) Step 3: Convert the temperature
        converted_temp = round(conversion_func(original_temp), DECIMAL_DIGITS)

        # (d) Step 4: Add the result to the table and display it
        table.add_row([
            case_num,
            original_temp if original_scale == 'degF' else converted_temp,
            original_temp if original_scale == 'degC' else converted_temp,
        ])

        case_num += 1

    # (e) Step 5: Ask the user if they would like to add more cases
    continue_input = input('Do you want to convert more temperatures?\n0 - No\n1 - Yes\n').strip()
    if continue_input != '1':
        break
    case_num += 1

# (f) Step 6: Display the table
print(table)
print('End of the program')