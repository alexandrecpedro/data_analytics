"""
INSTRUCTIONS:
    Write a programme that reads an integer N (10 < N < 10,000) and writes a file with
    N lines containing the data listed in the table below. The file should be named
    'Stock.csv' and should use the ';' (semicolon) character as a delimiter.
    The file does not need to be ordered

        | Field               | Description |
        | ------------------- | ----------- |
        | Product Code        | An integer between 10,000 and 50,000. Generate randomly. This code must not be duplicated, and should not be sequential |
        | Quantity in Stock   | An integer between 1 and 3,800. Generate randomly |
        | Unit Purchase Price | A real number between 1.80 and 435.90. Generate randomly |
        | ICMS Rate           | ICMS tax rate. This rate should be 7%, 12%, or 18%. (Do not include the '%' character in the file). Generate randomly |

    Tip (you may follow these or not – it is your choice):
        - To ensure the Product Code is unique, use a dictionary when generating the data
        - Generate the data and store it in the dictionary before writing to the output file
        - The values of the dictionary elements can be in the form of a tuple or a nested dictionary

TEST CASES:
    |    | Header field name   |
    | -- | ------------------- |
    |  1 | Product Code        |
    |  2 | Quantity in Stock   |
    |  3 | Unit Purchase Price |
    |  4 | ICMS Rate           |

"""
import random
from typing import Dict, Optional, Set, Tuple, TypeVar, List

# 1. GENERIC TYPES
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

# 2. CONSTANTS
FILENAME = 'stock.csv'
MODE = 'w'
FORMAT_SPEC_DOT_2f = '.2f'
SEPARATOR = ';'
MIN_VALUE = 10
MAX_VALUE = 10000
PRODUCT_CODE_RANGE = (10000, 50000)
QUANTITY_RANGE = (1, 3800)
PRICE_RANGE = (1.80, 435.90)
ICMS_RATES = [7, 12, 18]

# 3. FUNCTIONS
def get_number_lines(prompt: str, min_value: int, max_value: int) -> int:
    """
    Prompts the user for the number of lines,
    validating that it's between min_value and max_value

    :param prompt: Text prompt for input
    :param min_value: Minimum valid number of lines
    :param max_value: Maximum valid number of lines
    :return: Valid number of lines
    """

    while True:
        try:
            lines = int(input(f'{prompt} (between {min_value} and {max_value}): ').strip())
            if min_value < lines < max_value:
                return lines
            print(f'Error: Please enter a number between {min_value} and {max_value}')
        except ValueError:
            print('Error: Input must be an integer!')

def get_header_fields() -> List[str]:
    """
    Prompts the user to enter header fields for the CSV file

    :return: List of header field names
    """
    header_fields: List[str] = list()
    while True:
        print('Enter the header field name for the CSV file (type "0" when finished):')
        field = input('Header field: ').strip()
        if field == '0':
            break
        if len(field) == 0:
            print('Error: Header field name is mandatory!')
            continue
        header_fields.append(field)
    return header_fields

def generate_unique_code(existing_codes: Set[T], code_range: Tuple[U, V]) -> T:
    """
    Generates a unique code within a specified range, avoiding duplicates

    :param existing_codes: Set of existing codes
    :param code_range: Tuple defining the range for code generation
    :return: A unique code
    """
    while True:
        code = random.randint(*code_range)
        if code not in existing_codes:
            existing_codes.add(code)
            return code

def generate_data_entries(number_of_lines: int) -> Dict[T, Tuple[U, V, U]]:
    """
    Generates data entries with unique keys, each containing quantity, price, and ICMS rate

    :param number_of_lines: Number of data entries to generate
    :return: Dictionary with product codes as keys and tuples of
        (quantity, price, ICMS rate) as values
    """
    data_entries: Dict[T, Tuple[U, V, U]] = {}
    existing_codes: Set[T] = set()

    for _ in range(number_of_lines):
        product_code = generate_unique_code(existing_codes=existing_codes,
                                            code_range=PRODUCT_CODE_RANGE)
        quantity = random.randint(*QUANTITY_RANGE)
        price = round(random.uniform(*PRICE_RANGE), 2)
        icms_rate = random.choice(ICMS_RATES)

        data_entries[product_code] = (quantity, price, icms_rate)

    return data_entries

def write_to_file(
        data: Dict[T, Tuple[U, V, U]],
        filename: str,
        header_fields: List[str],
        mode: str = MODE,
        separator: str = SEPARATOR) -> Optional[None]:
    """
    Writes data entries to a CSV file with custom header

    :param data: Dictionary containing data entries
    :param filename: Name of the CSV file
    :param header_fields: List of header fields to write
    :param mode: File access mode (default is 'w')
    :param separator: CSV file delimiter (default is ';')
    """
    file_record = open(file=filename, mode=mode)
    header = separator.join(header_fields) + '\n'
    file_record.write(header)

    for code, (quantity, price, icms_rate) in data.items():
        line = (f'{code}{separator}'
                f'{quantity}{separator}'
                f'{price:{FORMAT_SPEC_DOT_2f}}{separator}'
                f'{icms_rate}\n')
        file_record.write(line)
    print(f'Data successfully written to {filename}')

# 4. MAIN PROGRAM
def main():
    print("Start of the program")
    header_fields_list = get_header_fields()
    file_number_of_lines = get_number_lines(prompt='Enter the number of lines',
                                            min_value=MIN_VALUE, max_value=MAX_VALUE)
    data_entries = generate_data_entries(number_of_lines=file_number_of_lines)
    write_to_file(data=data_entries, filename=FILENAME, header_fields=header_fields_list)
    print('End of the program')

if __name__ == '__main__':
    main()