from prettytable import PrettyTable

# 1. CONSTANTS
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid value!'
TABLE_FIELD_NAMES = ['Number', 'Factorial']

# 2. FUNCTION
def get_number() -> int:
    """
    Reads a number from user input and validates it as an integer
    :return: A valid integer number entered by the user
    """
    while True:
        try:
            return int(input('Enter the number: '))
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

def factorial(number: int) -> int:
    """
    Calculates the factorial of an integer number
    :param number: An integer number
    :return:
    """
    if number <= 1:
        return 1
    return number * factorial(number=number-1)

def generate_table(table_field_names: list[str]) -> PrettyTable:
    """
    Generates a table to display the results
    :param table_field_names: Field names for the table
    :return: A formatted table
    """
    table = PrettyTable()
    table.field_names = table_field_names
    return table

# 3. MAIN PROGRAM
def main():
    print("Start of the program")
    table = generate_table(table_field_names=TABLE_FIELD_NAMES)
    number = get_number()
    result = factorial(number=number)
    table.add_row([number, result])
    print(table)
    print('End of the program')

if __name__ == '__main__':
    main()