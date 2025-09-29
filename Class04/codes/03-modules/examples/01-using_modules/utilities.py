"""
This is the utilities module
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
TEXT = 'This is the module arithmetic.py'
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'ago', 'sep', 'oct', 'nov', 'dec']

INVALID_VALUE_EXCEPTION = "Error: Please enter a valid value!"
NEGATIVE_VALUE_EXCEPTION = "Error: Please enter a non-negative value!"

GENERATE_TABLE_LOGGER = 'Generating results display table...'
GET_NUMBER_LOGGER = 'Requesting an user input...'
INVALID_INPUT_LOGGER = 'Invalid input detected'
IS_PRIME_LOGGER = 'Verifying if number is prime...'
PARITY_LOGGER = 'Verifying number parity...'

# 3. SET UP LOGGING
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()],
    level=logging.INFO)
logger = logging.getLogger()

# 4. FUNCTIONS:
def parity(value: T) -> str:
    """
    Determines the parity (even or odd) of a given number.

    :param value: Integer to evaluate.
    :return: "EVEN" if the number is even, "ODD" if the number is odd.
    :raises Invalid
    """
    logger.info(PARITY_LOGGER)
    sleep(0.5)
    return 'EVEN' if value % 2 == 0 else 'ODD'

def is_prime(value: T) -> bool:
    """
    Determines if a given number is prime

    :param value: Integer to evaluate
    :return: True if the number is prime, False otherwise
    """
    logger.info(IS_PRIME_LOGGER)
    sleep(0.5)
    if value == 2:
        return True
    if value % 2 == 0:
        return False

    square_root = pow(base=value, exp=0.5)
    divisor = 3
    while divisor <= square_root:
        if value % divisor == 0:
            return False
        divisor += 2
    return True

def get_number_input(prompt: str) -> T:
    """
    Requests a value from the user with exception handling
    :param prompt: Message to prompt the value
    :return: A valid integer number
    """
    logger.info(GET_NUMBER_LOGGER)
    while True:
        sleep(0.5)
        try:
            value = int(input(prompt).strip())
            if value < -1:
                logger.error(NEGATIVE_VALUE_EXCEPTION)
                continue
            return value
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
    return PrettyTable(field_names=table_field_names, border=True, header=True)

# generate_table: Callable[[List[str]], PrettyTable] = \
#     lambda table_field_names: PrettyTable(field_names=table_field_names, border=True, header=True)