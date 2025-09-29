"""
INSTRUCTIONS:
    Write a programme that displays on the screen the code, cost price, and sale
    price of products, knowing that the company's gross profit margin is 16%
    for most products. Some products may have a reduced margin, and in such cases,
    the product code's first digit is changed. When the first digit is '8',
    the margin is 12%, and when this digit is '9', the margin is 10%

TEST CASES:
    | Code | Cost Price | Sale Price |
    | :--: | :--------: | :--------: |
    | 1280 |   100.00   |   116.00   |
    | 8280 |   100.00   |   112.00   |
    | 9280 |   100.00   |   110.00   |
"""
import locale
import utilities
from logger import setup_logger
from time import sleep
from utils.exception_messages import ExceptionMessages
from utils.logger_messages import LoggerMessages

# 1. CONSTANTS
## (a) Currency
locale.setlocale(locale.LC_ALL, '')
INTL_CURRENCY_SYMBOL = locale.localeconv().get('int_curr_symbol')
LOCAL_CURRENCY_SYMBOL = locale.localeconv().get('currency_symbol')
DECIMAL_DIGITS = 2

## (b) Table
TABLE_FIELD_NAMES = ['Product Code', f'Cost Price ({INTL_CURRENCY_SYMBOL})', f'Sale Price ({INTL_CURRENCY_SYMBOL})']

# 2. SET UP LOGGING
logger = setup_logger()

# 3. MAIN PROGRAM
def main():
    logger.info(LoggerMessages.MAIN_PROGRAM_START_LOGGER.value)
    table = utilities.generate_table(table_field_names=TABLE_FIELD_NAMES)

    while True:
        # Step 1: Request the product code (string with digits only)
        product_code = utilities.get_product_code(prompt='Enter a product code (digits only): ')
        if product_code == -1:
            logger.info(LoggerMessages.EXIT_PROGRAM_LOGGER.value)
            break

        try:
            # Step 2: Request the cost price (float)
            cost_price = utilities.get_product_price(
                prompt=f'Enter the cost price for the product {product_code}: ',
                allow_negatives=False
            )
            if cost_price is None:
                continue

            # Step 3: Calculate sale price
            sale_price = utilities.sale_price(code=product_code, cost=cost_price)
            table.add_row([
                product_code,
                utilities.format_value(value_obj=cost_price, decimal_digits=DECIMAL_DIGITS),
                utilities.format_value(value_obj=sale_price, decimal_digits=DECIMAL_DIGITS)])
        except ValueError:
            logger.error(ExceptionMessages.INVALID_COST_INPUT_EXCEPTION.value)

        while True:
            sleep(0.5)
            continue_input = input('Do you want another case?\n0 - No\n1 - Yes\n').strip()
            if continue_input in {'0', '1'}:
                break
            logger.warning(f'{ExceptionMessages.INVALID_OPTION_EXCEPTION.value}: {continue_input}')

        if continue_input == '0':
            logger.info(LoggerMessages.EXIT_PROGRAM_LOGGER.value)
            break

    sleep(0.5)
    print(table)
    logger.info(LoggerMessages.MAIN_PROGRAM_END_LOGGER.value)

if __name__ == '__main__':
    main()