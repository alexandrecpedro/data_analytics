from enum import Enum

class LoggerMessages(Enum):
    EXIT_PROGRAM_LOGGER = 'Exiting program...'
    GENERATE_TABLE_LOGGER = 'Generating results display table...'
    GET_NUMBER_LOGGER = 'Requesting an user input...'
    INVALID_INPUT_LOGGER = 'Invalid input detected'
    IS_PRIME_LOGGER = 'Verifying if number is prime...'
    MAIN_PROGRAM_END_LOGGER = 'End of the program'
    MAIN_PROGRAM_START_LOGGER = 'Start of the program'
    PARITY_LOGGER = 'Verifying number parity...'