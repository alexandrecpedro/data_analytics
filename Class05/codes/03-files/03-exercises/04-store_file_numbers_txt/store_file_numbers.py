"""
INSTRUCTIONS:
    Write a programme that creates a file named NUMBERS.TXT with 2,000 numbers,
    one on each line, generated using the randint() function from the random module
    in the range [1, 5,000]

   Variation: Modify this programme by replacing the fixed size of 2,000 with
   a quantity input to be read from the keyboard

"""
import random
from typing import List, Optional, Tuple, TypeVar

# 1. GENERIC TYPES
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

# 2. CONSTANTS
FILENAME = 'NUMBERS.TXT'
MODE = 'w'
SEPARATOR = '\n'
NUMBER_RANGE = (1, 5000)

# 3. FUNCTIONS
def get_number_lines(prompt: str) -> int:
    """
    Prompts the user for the number of lines

    :param prompt: Text prompt for input
    :return: Valid number of lines
    """

    while True:
        try:
            return int(input(f'{prompt}: ').strip())
        except ValueError:
            print('Error: Input must be an integer!')

def generate_list_of_numbers(number_of_lines: int, number_range: Tuple[U, V]) -> List[T]:
    """
    Generates a list of random numbers within a specified range

    :param number_of_lines: Number of lines in file
    :param number_range: Tuple defining the range for number generation
    :return: A list of random numbers
    """
    # number_list: List[T] = list()
    # for line in range(lines):
    #     generated_number = random.randint(*number_range)
    #     number_list.append(generated_number)
    # return number_list
    return [random.randint(*number_range) for _ in range(number_of_lines)]

def write_to_file(
        data: List[T],
        filename: str,
        mode: str = MODE,
        separator: str = SEPARATOR) -> Optional[None]:
    """
    Writes a list of numbers to a file, one number per line

    :param data: List containing data entries
    :param filename: Name of the file
    :param mode: File access mode (default is 'w')
    :param separator: File delimiter (default is '\n')
    """
    file_record = open(file=filename, mode=mode)

    for item in data:
        file_record.write(f'{item}{separator}')
    print(f'Data successfully written to {filename}')

# 4. MAIN PROGRAM
def main():
    print("Start of the program")
    file_number_of_lines = get_number_lines(prompt='Enter the number of lines')
    list_of_numbers = generate_list_of_numbers(number_of_lines=file_number_of_lines, number_range=NUMBER_RANGE)
    write_to_file(data=list_of_numbers, filename=FILENAME)
    print('End of the program')

if __name__ == '__main__':
    main()