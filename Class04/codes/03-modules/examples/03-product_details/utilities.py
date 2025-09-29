"""
This is the utilities module
It contains objects and functions that may be useful for our programmes
It is recommended to include a docstring indicating the module's contents
"""
import logging
from prettytable import PrettyTable
from time import sleep
from typing import Callable, List, Optional, TypeVar
from utils.exception_messages import ExceptionMessages
from utils.logger_messages import LoggerMessages

# 1. GENERIC TYPES
T = TypeVar('T', str, float)

# 2. SET UP LOGGING
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()],
    level=logging.INFO)
logger = logging.getLogger()

# 3. FUNCTIONS
def get_product_code(prompt: str) -> str:
    """
    Requests a product code from the user, ensuring it's a string of digits
    :param prompt: The message to prompt the user for input
    :return: A valid product code as a string of digits
    """
    logger.info(LoggerMessages.GET_PRODUCT_CODE_LOGGER.value)
    while True:
        sleep(0.5)
        product_code = input(prompt).strip()
        if product_code.isdigit():
            return product_code
        logger.error(ExceptionMessages.PRODUCT_CODE_EXCEPTION.value)

def get_product_price(prompt: str, allow_negatives: bool = True) -> Optional[T]:
    """
    Requests a price from the user, ensuring it's a valid number (float),
    and optionally checks if negative values are allowed
    :param prompt: The message to prompt the user for input
    :param allow_negatives: Whether to allow negative prices
    :return: A valid price as a float or None if the input is invalid or the user wants to quit
    """
    logger.info(LoggerMessages.GET_PRODUCT_PRICE_LOGGER.value)

    while True:
        sleep(0.5)
        try:
            product_price = float(input(prompt).strip())
            if not allow_negatives and product_price < 0:
                logger.error(ExceptionMessages.NEGATIVE_VALUE_EXCEPTION.value)
                continue
            return product_price
        except ValueError:
            logger.error(ExceptionMessages.INVALID_VALUE_EXCEPTION.value)

def change_margin_percentual(code: str) -> T:
    """
    Adjusts the margin percentage based on the provided code
    :param code: The code defining the adjustment logic
    :return: The updated margin percentage
    """
    return { '8': 12/100, '9': 10/100 }.get(code[0], 16/100)

def sale_price(code: T, cost: T) -> T:
    """
    Calculates the sale price based on code and cost
    :param code: The pricing code or multiplier
    :param cost: The base cost of the item
    :return: The final sale price
    """
    logger.info(LoggerMessages.SALE_PRICE_LOGGER.value)
    margin = change_margin_percentual(code=code)
    return round(number=cost * (1 + margin), ndigits=2)

def generate_table(table_field_names: List[str]) -> PrettyTable:
    """
    Generates a table to display the results
    :param table_field_names: Field names for the table
    :return: A formatted table
    """
    logger.info(LoggerMessages.GENERATE_TABLE_LOGGER.value)
    sleep(0.5)
    return PrettyTable(field_names=table_field_names, border=True, header=True)

# generate_table: Callable[[List[str]], PrettyTable] = \
#     lambda table_field_names: PrettyTable(field_names=table_field_names, border=True, header=True)

def format_value(value_obj: T, decimal_digits: int) -> str:
    """
    Format a numeric value to a string with specified decimal places
    :param value_obj: The numeric value to format
    :param decimal_digits: Number of decimal places to display
    :return: A string representing the formatted value
    """
    logger.info(LoggerMessages.FORMAT_VALUE_LOGGER.value)
    return f'{value_obj:.{decimal_digits}f}'