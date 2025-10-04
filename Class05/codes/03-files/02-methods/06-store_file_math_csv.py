"""
INSTRUCTIONS:
    Write a programme that reads an input file, loading its data into a dictionary
    and displaying it on the screen at the end. Figure 11.1 shows, on the left,
    the nature of the data to be read and, on the right, the file format

    This format is known as CSV. CSV files are widely used in various fields of
    computing, particularly in Data Analysis. What defines a CSV file is that each line
    contains a set of data that is somehow related and separated by a delimiter character.
    In the file for this exercise, the delimiter is a semicolon, ";"

    In this case, each line contains: a product code (int), the quantity in stock (int),
    and the price (float). Use the product code as the key for the dictionary, and the
    value should be in the form of a tuple
"""

# 1. CONSTANTS
FILENAME = 'assets/store_file_math_csv.txt'
MODE = 'r'
FORMAT_SPEC_5d = '5d'
FORMAT_SPEC_6_2f = '6.2f'
FORMAT_SPEC_8_2f = '8.2f'
SEPARATOR = ';'

# 2. MAIN PROGRAM
def main():
    print("Start of the program")
    Stock = {}
    entry_file = open(file=FILENAME, mode=MODE)
    for line in entry_file:
        lst = line.rstrip().split(SEPARATOR)
        prod_code = int(lst[0])
        stock_qty = int(lst[1])
        unit_price = float(lst[2])
        Stock[prod_code] = (stock_qty, unit_price)
    print('Values loaded into the dictionary')
    print(Stock)
    print('Display of data in table format')
    total_sum = 0
    for prod_code, data in Stock.items():
        total_per_product = data[0] * data[1]
        total_sum += total_per_product
        print(f' {prod_code}: {data[0]:{FORMAT_SPEC_5d}} x {data[1]:{FORMAT_SPEC_6_2f}} '
              f'= {total_per_product:{FORMAT_SPEC_8_2f}}')
    print(' ' * 24, f'{total_sum:{FORMAT_SPEC_8_2f}}')
    print('End of the program')

if __name__ == '__main__':
    main()