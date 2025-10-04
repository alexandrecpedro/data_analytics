"""
INSTRUCTIONS:
    Write a programme that implements a binary search using a recursive function.
    The main programme should remain in a loop, reading integer values to be searched in the list

TEST CASE:

(a) Ordered value list (ASC)
| Number   | 14 | 17 | 20 | 22 | 23 | 25 | 28 | 29 | 31 | 35 | 40 | 45 | 50 | 53 | 56 | 59 | 62 | 65 |
| Position |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |

(b) 1st verification:
    - central position = 8
    - value = 31 (smaller than 40)
    ::: Therefore, goes the upper part of list (positions: 9 - 17)
                                             | Number   | 35 | 40 | 45 | 50 | 53 | 56 | 59 | 62 | 65 |
                                             | Position |  9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |

(c) 2nd verification:
    - central position = 13
    - value = 53 (greater than 40)
    ::: Therefore, goes the upper part of list (positions: 9 - 12)
                                             | Number   | 35 | 40 | 45 | 50 |
                                             | Position |  9 | 10 | 11 | 12 |

(d) 3rd verification:
    - central position = 10
    - value = 40 (stop the search)
"""
from typing import Optional, List

from prettytable import PrettyTable

# 1. CONSTANTS
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid value!'
TABLE_FIELD_NAMES = ['Case', 'Search Value', 'List contains this value?', 'Index of search value']

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

def binary_search(value: int, lst: List[int], start: int, end: int) -> bool:
    """
    Recursively searches for a value in a sorted list.
    :param value: The integer value to search for
    :param lst: The sorted list of integers
    :param start: Starting index for the search
    :param end: Ending index for the search
    :return: True if the value is found; False otherwise
    """
    if start > end:
        return False

    mid = (start + end) // 2
    if value == lst[mid]:
        return True

    return binary_search(value=value, lst=lst, start=start, end=mid-1) if value < lst[mid] \
        else binary_search(value=value, lst=lst, start=mid+1, end=end)


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
    List = [14, 17, 20, 22, 23, 25, 28, 29, 31, 35, 40, 45, 50, 53, 56, 59, 62, 65]

    while (X := get_number('Enter a value to search in the list (or 0 to stop): ')) != 0:
        found = binary_search(value=X, lst=List, start=0, end=len(List) - 1)
        position = List.index(X) if found else 'N/A'
        table.add_row([case_num, X, found, position])
        case_num += 1

    print('\nResults')
    print(table)
    print('End of the program')

if __name__ == '__main__':
    main()