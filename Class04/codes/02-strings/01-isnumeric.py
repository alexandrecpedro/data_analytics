"""
FUNCTION ISNUMERIC:
    Check if an entered string contains only numeric digits

TEST CASES:
    | Case | Entry  |
    | :--: | ------ |
    | 1    | 188    |
    | 2    | 13abc9 |
"""

input_str = input('Enter an integer number: ')
if input_str.isnumeric():
    int_number = int(input_str)
    print(f'\tEntered number was {int_number}')
else:
    print(f'\tError: Please enter only numbers')