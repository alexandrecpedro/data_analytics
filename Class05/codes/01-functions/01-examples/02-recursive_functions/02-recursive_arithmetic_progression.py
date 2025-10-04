"""
INSTRUCTIONS:
    Write a recursive function to calculate the summation of the terms of an Arithmetic Progression
    defined by the parameters First (first term), Ratio and Qty (number of elements). These parameters
    should be read from the keyboard. Write the main programme to test the function, which should
    display the value of this sum on the screen. Test your programme with the following test cases:

    | Case | First | Ratio | Qty |  Sum |
    | :--: | ----- | ----- | --- | ---- |
    |    1 |     7 |     4 |   7 |  133 |
    |    2 |    12 |     8 |  15 | 1020 |
    |    3 |     2 |     3 |   6 |   57 |
"""
from typing import Optional

from prettytable import PrettyTable

# 1. CONSTANTS
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid value!'
TABLE_FIELD_NAMES = ['Case', 'First Term', 'Ratio', 'Quantity', 'Sum']

# 2. FUNCTION
def get_number(prompt: str) -> int:
    """
    Reads a number from user input and validates it as an integer
    :param prompt: Prompt message for the user
    :return: A valid integer entered by the user
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

def sum_of_terms(a1: int, d: int, n: int) -> Optional[any]:
    """
    Recursively calculates the sum of an arithmetic progression
    :param a1: First term
    :param d: Common difference (ratio)
    :param n: Number of terms
    :return: Sum of the progression
    """
    if n == 0:
        return 0

    if d > 0:
        return a1 + sum_of_terms(a1=a1 + d, d=d, n=n - 1)
    return 0


def generate_table(table_field_names: list[str]) -> PrettyTable:
    """
    Generates a table to display the results
    :param table_field_names: List of column names for the table
    :return: A formatted table
    """
    table = PrettyTable()
    table.field_names = table_field_names
    return table

# 3. MAIN PROGRAM
def main():
    print("Start of the program")
    table = generate_table(table_field_names=TABLE_FIELD_NAMES)
    case_num = 1

    while True:
        first_term = get_number('Enter the first term: ')
        ratio = get_number('Enter the ratio: ')
        quantity = get_number('Enter the number of terms: ')

        result = sum_of_terms(a1=first_term, d=ratio, n=quantity)
        table.add_row([case_num, first_term, ratio, quantity, result])

        another_test = input('Do you want to add another test case?\n0 - No\n1 - Yes\n').strip()
        if another_test != '1':
            break
        case_num += 1

    print('\nResults')
    print(table)
    print('End of the program')

if __name__ == '__main__':
    main()