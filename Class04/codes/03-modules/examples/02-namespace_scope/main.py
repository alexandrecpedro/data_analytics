"""
TEST CASES:
    | Case | Number 1 | Number 2 | Sum | Difference |
    | ---- | -------- | -------- | --- | ---------- |
    |   1  |    26    |    15    |  41 |     11     |
    |   2  |    37    |    18    |  55 |     19     |
"""

import arithmetic
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
TABLE_FIELD_NAMES = ['Case', 'Number 1', 'Number 2', 'Sum', 'Difference']

# 3. SET UP LOGGING
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=logging.StreamHandler(),
    level=logging.INFO)
logger = logging.getLogger()

# 4. MAIN PROGRAM
def main():
    logger.info(MAIN_PROGRAM_START_LOGGER)
    sleep(0.5)
    print('Built-in namespace')
    print(dir())

    table = arithmetic.generate_table(table_field_names=TABLE_FIELD_NAMES)
    case_num = 1
    while True:
        print('Programme global namespace - except element with "__"')
        print(', '.join(string for string in dir() if '__' not in string))
        # for string in dir():
        #     if '__' not in string:
        #         print(string, end=', ')
        print()

        sleep(0.5)
        number_1 = arithmetic.get_number_input(prompt='Enter a number: ')
        number_2 = arithmetic.get_number_input(prompt='Enter a number: ')

        sum_numbers = arithmetic.add_numbers(number_1=number_1, number_2=number_2)
        sleep(0.5)
        difference_number1_number2 = arithmetic.subtract_numbers(
            number_1=number_1,
            number_2=number_2)

        table.add_row([case_num, number_1, number_2, sum_numbers, difference_number1_number2])

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