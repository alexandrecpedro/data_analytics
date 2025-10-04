"""
INSTRUCTIONS:
    Write a programme that reads an input CSV file containing two integers on each line.
    The first is a product code, and the second is the quantity sold.
    The programme should total the number of items sold for each product

    Tip: use a dictionary with the product code as the key and the quantity as the value.
    For each code read from the file, check if it already exists in the dictionary
    using the in operator. If it does not exist, add it; if it does exist, add the new quantity
    from the file to the existing quantity
"""
from prettytable import PrettyTable
from typing import Dict, IO, Optional, TypeVar

# 1. GENERIC TYPES
T = TypeVar('T')
U = TypeVar('U')

# 2. CONSTANTS
FILENAME = 'product_code_sales_quantity.csv'
MODE = 'r'
FORMAT_SPEC_5d = '5d'
SEPARATOR = ';'
TABLE_FIELD_NAMES = ['Product Code', 'Quantity Sold (items)']

# 3. FUNCTIONS
def display_table(dictionary_obj: Dict[T, U]) -> Optional[None]:
    """
    Displays the sales dictionary in a table, sorted by product code

    :param dictionary_obj: Dictionary with product codes as keys and quantities as values
    """
    table = PrettyTable()
    table.field_names = TABLE_FIELD_NAMES

    for code, items_quantity in sorted(dictionary_obj.items()):
        table.add_row([code, items_quantity])

    print(table)

def total_sales(file: IO[str], separator: str = SEPARATOR) -> Optional[None]:
    """
    Reads a CSV file with product code and quantity sold, totalling the sales for each product.

    :param file: Path to the CSV file
    :param separator: CSV file delimiter (default is ';')
    """
    sales = {}
    for line in file:
        lst = line.rstrip().split(separator)
        prod_code = int(lst[0])
        quantity_sold = int(lst[1])
        sales[prod_code] = sales[prod_code] + quantity_sold if (prod_code in sales) else quantity_sold

    # print("Total items sold per product:")
    # for code, items_quantity in sales.items():
    #     print(f'Product {code}:\t{items_quantity} units sold')
    display_table(dictionary_obj=sales)

# 4. MAIN PROGRAM
def main():
    print("Start of the program")
    entry_file = open(file=FILENAME, mode=MODE)
    total_sales(file=entry_file)
    print('End of the program')

if __name__ == '__main__':
    main()