"""
INSTRUCTIONS:
    Write a programme to display Pascal's Triangle on the screen.
    Use a recursive function to generate its elements.
    As input, this programme should read an integer that represents the number
    of lines of the triangle to be displayed

"""
from typing import TypeVar

# 1. GENERIC TYPES
T = TypeVar('T')

# 2. CONSTANTS
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid number!'
VALUE_NON_NEGATIVE_EXCEPTION = 'Error: Please enter a non-negative number!'

# 3. FUNCTION
def get_number_lines() -> int:
    """
    Reads an integer number of lines from user input and validates it.
    :return: A valid integer representing the number of lines, or 0 to exit
    """
    while True:
        try:
            number_lines = int(input("Enter the number of lines for Pascal's Triangle (or 0 to exit): ")
                               .strip())
            if number_lines < 0:
                print(VALUE_NON_NEGATIVE_EXCEPTION)
                continue

            if number_lines == 0:
                return 0
            return number_lines
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

def binomial_coefficient(n: int, p: int) -> int:
    """
    Computes the binomial coefficient C(n, p) using recursion
    :param n: Total number of items
    :param p: Number of items to choose
    :return: The binomial coefficient C(n, p)
    """
    if p == 0 or p == n:
        return 1
    return binomial_coefficient(n=n-1, p=p-1) + binomial_coefficient(n=n-1, p=p)

def pascal_triangle(lines: int) -> None:
    """
    Prints Pascal's Triangle up to n lines
    :param lines: Number of lines of Pascal's Triangle to display
    """

    for i in range(lines):
        print(" " * (lines - i), end='')

        for j in range(i+1):
            print(binomial_coefficient(n=i, p=j), end=' ')
        print()

# 4. MAIN PROGRAM
def main():
    print("Start of the program")
    while True:
        number_of_lines = get_number_lines()
        if number_of_lines == 0:
            break
        pascal_triangle(lines=number_of_lines)
    print('\nEnd of the program')

if __name__ == '__main__':
    main()