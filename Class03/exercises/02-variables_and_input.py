from prettytable import PrettyTable

# CONSTANTS
FIELD_NAMES = ['Description', 'Value', 'Type']
FIELD_NAMES_2 = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)
table2 = PrettyTable(field_names=FIELD_NAMES_2)
table3 = PrettyTable(field_names=FIELD_NAMES_2)
table4 = PrettyTable(field_names=FIELD_NAMES_2)

# =========== EXERCISE 1 ===========

# 1. VARIABLES
nome_cidade = "São Paulo"
temperatura = 23.5
table.add_row(['EXERCISE 1', '', ''])
table.add_row(['City Name', nome_cidade, type(nome_cidade)])
table.add_row(['Temperatura', temperatura, type(temperatura)])
print(table)

# =========== EXERCISE 2 ===========
number_students = int(input('Number of students: '))
table2.add_row(['EXERCISE 2', ''])
table2.add_row(['Number of students', number_students])
print(table2)

# =========== EXERCISE 3 ===========
item_value = float(input('Item value: '))
table3.add_row(['EXERCISE 3', ''])
table3.add_row(['Item value', item_value])
print(table3)

# =========== EXERCISE 4 ===========
number = float(input('Enter a number: '))
square_root_number = number ** (1 / 2)
table4.add_row(['EXERCISE 4', ''])
table4.add_row(['Number', number])
table4.add_row([f'Square root of {number}', square_root_number])
print(table4)



