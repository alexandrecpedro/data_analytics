"""
INSTRUCTIONS:
    Write a programme that reads an input file, knowing that this file contains
    one integer on each line. All numbers read should be displayed on the screen.
    Additionally, display the sum of the values, the count, the arithmetic mean,
    the smallest value, and the largest value
    Use the same input file as in the previous exercise

    Utilise a for iterator with the file as an iterable
"""

print("Start of the program")
filename = 'assets/store_file_readline_math.txt'
mode = 'r'
format_spec='.3f'

Lst = []
entry_file = open(file=filename, mode=mode)
for line in entry_file:
    Lst.append(int(line))
print('File read values')
print(Lst)
sum_values = sum(Lst)
print(f'Sum of values = {sum_values}')
qty_values = len(Lst)
print(f'Quantity = {qty_values}')
print(f'Average of values = {sum_values/qty_values}')
smaller_value = min(Lst)
print(f'Smaller value = {smaller_value}')
largest_value = max(Lst)
print(f'Largest value = {largest_value}')
print('End of the program')