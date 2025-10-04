"""
INSTRUCTIONS:
    Write a program that remains in a loop, reading integer numbers until the number 0 is entered.
    All values entered, except for zero, should be recorded in a file on disk, one per line.
    Use the .write() method

TEST CASES:
    | Case | Number |
    | :--: | :----: |
    | 1    | 10     |
    | 2    | 20     |
    | 3    | 30     |
    | 4    | 40     |
    | 5    | 0      |
"""
from typing import TextIO, Optional, TypeVar

T = TypeVar('T')

# 1. AUXILIARY FUNCTIONS
def input_int_number():
    while True:
        try:
            return int(input('Enter an integer number: '))
        except ValueError:
            print("Error: Invalid input. Please enter an integer number!")

def output_file(file_store: TextIO, format_spec: Optional[T] = ''):
    int_number = input_int_number()
    while int_number != 0:
        file_store.write(f'{int_number:{format_spec}}\n')
        int_number = input_int_number()
    file_store.close()

# 2. MAIN PROGRAM
def main():
    print("Start of the program")
    filename = 'assets/store_file_write_int.txt'
    mode = 'w'
    file_store = open(file=filename, mode=mode)
    output_file(file_store=file_store, format_spec='')
    print('End of the program')

if __name__ == '__main__':
    main()