"""
This is the utils_text module
It contains only functions that returns a text
"""
from log import setup_logger
from messages import LoggerMessages
from time import sleep
from typing import TypeVar

# 1. GENERIC TYPES
T = TypeVar('T', int, float)

# 2. CONSTANTS
TEXT = 'This is the module utils.text.py'
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'ago', 'sep', 'oct', 'nov', 'dec']

# 3. SET UP LOGGING
logger = setup_logger()

# 4. FUNCTIONS:
def parity(value: T) -> str:
    """
    Determines the parity (even or odd) of a given number

    :param value: Integer to evaluate
    :return: "EVEN" if the number is even, "ODD" if the number is odd
    """
    logger.info(LoggerMessages.PARITY_LOGGER.value)
    sleep(0.5)
    return 'EVEN' if value % 2 == 0 else 'ODD'