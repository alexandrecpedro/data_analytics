"""
TEST CASES:
    | Case | Number | Parity | Is Prime? |
    | :--: | :----: | :----: | :-------: |
    |   1  |   317  |   ODD  |    True   |
    |   2  |   225  |   ODD  |   False   |
    |   3  |    86  |  EVEN  |   False   |
    |   4  |     0  | ====== | ========= |
"""
import utilities
import logging
from time import sleep
from typing import TypeVar

# 1. GENERIC TYPES
T = TypeVar('T', int, float)

# 2. CONSTANTS
## (a) Exceptions
INVALID_OPTION_EXCEPTION = "Error: Invalid choice. Please enter '0' for No or '1' for Yes!"

## (b) Logging's
EXIT_PROGRAM_LOGGER = 'Exiting program...'
MAIN_PROGRAM_END_LOGGER = 'End of the program'
MAIN_PROGRAM_START_LOGGER = 'Start of the program'

## (c) Table
TABLE_FIELD_NAMES = ['Case', 'Number', 'Parity', 'Is Prime?']

# 3. SET UP LOGGING
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=logging.StreamHandler(),
    level=logging.INFO)
logger = logging.getLogger()

# 4. MAIN PROGRAM
def main():
    logger.info(MAIN_PROGRAM_START_LOGGER)
    table = utilities.generate_table(table_field_names=TABLE_FIELD_NAMES)
    case_num = 1

    while True:
        number = utilities.get_number_input(prompt='Enter an integer number (or -1 to quit): ')
        if number == -1:
            logger.info(EXIT_PROGRAM_LOGGER)
            break

        number_parity = utilities.parity(value=number)
        number_is_prime = utilities.is_prime(value=number)
        table.add_row([case_num, number, number_parity, number_is_prime])

        while True:
            continue_input = input('Do you want another case?\n0 - No\n1 - Yes\n').strip()
            if continue_input in {'0', '1'}:
                break
            logger.warning(f'{INVALID_OPTION_EXCEPTION}: {continue_input}')

        if continue_input == '0':
            logger.info(EXIT_PROGRAM_LOGGER)
            break
        case_num += 1

    sleep(0.5)
    print(table)
    logger.info(MAIN_PROGRAM_END_LOGGER)

if __name__ == '__main__':
    main()