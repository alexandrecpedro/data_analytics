"""
INSTRUCTIONS:
    Write a program that remains in a loop, reading float numbers until the number 0 is entered.
    All values entered, except for zero, should be recorded in a file on disk, one per line,
    with 3 decimal places.
    Use the .writelines() method

TEST CASES:
    | Case | Number |
    | :--: | :----: |
    | 1    | 7.32   |
    | 2    | 18.6   |
    | 3    | 0.414  |
    | 4    | 16.379 |
    | 5    | 0      |
"""
from typing import TextIO, Optional, TypeVar

T = TypeVar('T')

# 1. AUXILIARY FUNCTIONS
def input_float_number():
    while True:
        try:
            return float(input('Enter a float number: '))
        except ValueError:
            print("Error: Invalid input. Please enter a float number!")

def output_file(filename: T, mode: T, format_spec: Optional[T] = ''):
    Lst = list()
    float_number = input_float_number()
    while float_number != 0:
        Lst.append(f'{float_number:{format_spec}}\n')
        float_number = input_float_number()
    file_store = open(file=filename, mode=mode)
    file_store.writelines(Lst)
    file_store.close()

# 2. MAIN PROGRAM
print("Start of the program")
filename = 'assets/store_file_writelines_float.txt'
mode = 'w'
format_spec='.3f'
output_file(filename=filename, mode=mode, format_spec=format_spec)
print('End of the program')