"""
This is the utils_number module
It contains only functions that returns a number
"""
from log import setup_logger
from messages import ExceptionMessages, LoggerMessages
from time import sleep
from typing import TypeVar

# 1. GENERIC TYPES
T = TypeVar('T', int, float)

# 2. SET UP LOGGING
logger = setup_logger()

# 3. FUNCTIONS:
def get_number_input(prompt: str) -> T:
    """
    Requests a value from the user with exception handling
    :param prompt: Message to prompt the value
    :return: A valid integer number
    """
    logger.info(LoggerMessages.GET_NUMBER_LOGGER.value)
    while True:
        sleep(0.5)
        try:
            value = int(input(prompt).strip())
            if value < -1:
                logger.error(ExceptionMessages.NEGATIVE_VALUE_EXCEPTION.value)
                continue
            return value
        except ValueError:
            logger.error(ExceptionMessages.INVALID_VALUE_EXCEPTION.value)