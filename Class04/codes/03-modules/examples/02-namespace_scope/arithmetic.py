"""
This is the arithmetic module
It contains objects and functions that may be useful for our programmes
It is recommended to include a docstring indicating the module's contents
"""
import logging
from time import sleep
from typing import TypeVar, Callable, List

from prettytable import PrettyTable

# 1. GENERIC TYPES
T = TypeVar('T', int, float)

# 2. CONSTANTS
INVALID_VALUE_EXCEPTION = "Error: Please enter a valid value!"

ADD_NUMBERS_LOGGER = 'Adding the numbers...'
GENERATE_TABLE_LOGGER = 'Generating results display table...'
GET_NUMBER_LOGGER = 'Requesting an user input...'
LOCAL_SCOPE_LOGGER = 'Local Scope -'
INVALID_INPUT_LOGGER = 'Invalid input detected'
SUBTRACT_NUMBERS_LOGGER = 'Subtracting the numbers...'

# 3. SET UP LOGGING
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()],
    level=logging.INFO)
logger = logging.getLogger()

# 4. FUNCTIONS:
def add_numbers(number_1: T, number_2: T) -> T:
    logger.info(ADD_NUMBERS_LOGGER)
    sleep(0.5)
    print(f'{LOCAL_SCOPE_LOGGER} add_numbers function')
    print(dir())
    return number_1 + number_2

def subtract_numbers(number_1: T, number_2: T) -> T:
    logger.info(SUBTRACT_NUMBERS_LOGGER)
    sleep(0.5)
    print(f'{LOCAL_SCOPE_LOGGER} subtract_numbers function')
    print(dir())
    return number_1 - number_2

def get_number_input(prompt: str) -> T:
    """
    Requests a value from the user with exception handling
    :param prompt: Message to prompt the value
    :return: A valid number
    """
    logger.info(GET_NUMBER_LOGGER)
    print(f'{LOCAL_SCOPE_LOGGER} get_number_input function')
    print(dir())
    while True:
        sleep(0.5)
        try:
            return float(input(prompt).strip())
        except ValueError:
            logger.error(INVALID_VALUE_EXCEPTION)

def generate_table(table_field_names: List[str]) -> PrettyTable:
    """
    Generates a table to display the results
    :param table_field_names: Field names for the table
    :return: A formatted table
    """
    logger.info(GENERATE_TABLE_LOGGER)
    sleep(0.5)
    print(f'{LOCAL_SCOPE_LOGGER} generate_table function')
    print(dir())
    return PrettyTable(field_names=table_field_names, border=True, header=True)

# generate_table: Callable[[List[str]], PrettyTable] = \
#     lambda table_field_names: PrettyTable(field_names=table_field_names, border=True, header=True)