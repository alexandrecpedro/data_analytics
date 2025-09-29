from enum import Enum

class LoggerMessages(Enum):
    EXIT_PROGRAM_LOGGER = 'Exiting program...'
    FORMAT_VALUE_LOGGER = 'Formatting the numeric value to the specified decimal places...'
    GENERATE_TABLE_LOGGER = 'Creating a display table for results...'
    GET_PRODUCT_CODE_LOGGER = 'Requesting user input for a product code...'
    GET_PRODUCT_PRICE_LOGGER = 'Requesting user input for a product price...'
    MAIN_PROGRAM_END_LOGGER = 'End of the program'
    MAIN_PROGRAM_START_LOGGER = 'Start of the program'
    SALE_PRICE_LOGGER = 'Calculating product sale price...'