"""
This is the utils_bool module
It contains only functions that returns a boolean
"""
from log import setup_logger
from messages import LoggerMessages
from time import sleep
from typing import TypeVar

# 1. GENERIC TYPES
T = TypeVar('T', int, float)

# 2. SET UP LOGGING
logger = setup_logger()

# 3. FUNCTIONS
def is_even(value: T) -> bool:
    """
    Determines if a given number is even

    :param value: Integer to evaluate.
    :return: True if the number is even, False if the number is odd
    """
    logger.info(LoggerMessages.PARITY_LOGGER.value)
    sleep(0.5)
    return value % 2 == 0

def is_prime(value: T) -> bool:
    """
    Determines if a given number is prime

    :param value: Integer to evaluate
    :return: True if the number is prime, False otherwise
    """
    logger.info(LoggerMessages.IS_PRIME_LOGGER.value)
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