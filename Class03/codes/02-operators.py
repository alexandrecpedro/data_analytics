from prettytable import PrettyTable

# CONSTANTS
VALUE1 = 4
VALUE2 = 5
FIELD_NAMES = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)

# 1. ARITHMETIC OPERATORS
table.add_row(['Arithmetic Operations', ''])
table.add_row(['Potenciação', '**'])
table.add_row(['Multiplication', '*'])
table.add_row(['Division', '/'])
table.add_row(['Sum', '+'])
table.add_row(['Subtraction', '-'])

# 2. NUMERIC OPERATORS
table.add_row(['=========', '========='])
table.add_row(['Numeric Operators', ''])
table.add_row(['Parte inteira da divisão', '//'])
table.add_row(['Resto da divisão', '%'])

print(table)