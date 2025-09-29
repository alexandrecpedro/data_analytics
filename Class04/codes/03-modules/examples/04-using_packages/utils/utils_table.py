"""
This is the utils_table module
It contains only functions that creates, modify and returns
a display table for results
"""
from log import setup_logger
from messages import LoggerMessages
from prettytable import PrettyTable
from time import sleep
from typing import List

# 1. SET UP LOGGING
logger = setup_logger()

# 2. FUNCTIONS
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