"""
INSTRUCTIONS:
    Write a programme that uses a recursive function to perform a countdown.
    This programme should read an integer from the keyboard representing
    the number of counts in this countdown. When the countdown reaches zero,
    the programme should display the message "ON AIR!!!" on the screen
"""
# from prettytable import PrettyTable
from time import sleep

# 1. CONSTANTS
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid value!'
# TABLE_FIELD_NAMES = ['Number', 'Factorial']

# 2. FUNCTION
def get_number() -> int:
    """
    Reads a number from user input and validates it as an integer
    :return: A valid integer number entered by the user
    """
    while True:
        try:
            return int(input('Enter the number of countdown counts: '))
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

def countdown(count: int) -> None:
    """
    Recursively performs a countdown
    :param count: Integer representing countdown starting value
    """
    if count == 0:
        print('ON AIR!!!')
        return

    print(count)
    sleep(1) # in seconds
    countdown(count=count-1)

# def generate_table(table_field_names: list[str]) -> PrettyTable:
#     """
#     Generates a table to display the results
#     :param table_field_names: Field names for the table
#     :return: A formatted table
#     """
#     table = PrettyTable()
#     table.field_names = table_field_names
#     return table

# 3. MAIN PROGRAM
def main():
    print("Start of the program")
    # table = generate_table(table_field_names=TABLE_FIELD_NAMES)
    counts = get_number()
    print(f'Attention for the {counts} second count...')
    countdown(count=counts)
    # table.add_row([number, result])
    # print(table)
    print('End of the program')

if __name__ == '__main__':
    main()