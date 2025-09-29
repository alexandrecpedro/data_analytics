"""
TEST CASES:
    | Case | Number | Parity | Is Prime? |
    | :--: | :----: | :----: | :-------: |
    |   1  |   317  |   ODD  |    True   |
    |   2  |   225  |   ODD  |   False   |
    |   3  |    86  |  EVEN  |   False   |
    |   4  |     0  | ====== | ========= |
"""
from log import setup_logger
from messages import ExceptionMessages, LoggerMessages
from utils import is_prime, generate_table, get_number_input, parity
from time import sleep

# 1. CONSTANTS
TABLE_FIELD_NAMES = ['Case', 'Number', 'Parity', 'Is Prime?']

# 2. SET UP LOGGING
logger = setup_logger()

# 3. MAIN PROGRAM
def main():
    logger.info(LoggerMessages.MAIN_PROGRAM_START_LOGGER.value)
    table = generate_table(table_field_names=TABLE_FIELD_NAMES)
    case_num = 1

    while True:
        number = get_number_input(prompt='Enter an integer number (or -1 to quit): ')
        if number == -1:
            logger.info(LoggerMessages.EXIT_PROGRAM_LOGGER.value)
            break

        number_parity = parity(value=number)
        number_is_prime = is_prime(value=number)
        table.add_row([case_num, number, number_parity, number_is_prime])

        while True:
            continue_input = input('Do you want another case?\n0 - No\n1 - Yes\n').strip()
            if continue_input in {'0', '1'}:
                break
            logger.warning(f'{ExceptionMessages.INVALID_OPTION_EXCEPTION.value}: {continue_input}')

        if continue_input == '0':
            logger.info(LoggerMessages.EXIT_PROGRAM_LOGGER.value)
            break
        case_num += 1

    sleep(0.5)
    print(table)
    logger.info(LoggerMessages.MAIN_PROGRAM_END_LOGGER.value)

if __name__ == '__main__':
    main()