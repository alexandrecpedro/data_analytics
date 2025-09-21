from prettytable import PrettyTable

# CONSTANTS
FIELD_NAMES = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)
table2 = PrettyTable(field_names=FIELD_NAMES)

# =========== EXERCISE 1 ===========
VALUE1 = 4
VALUE2 = 5
table.add_row(['EXERCISE 1', ''])
## 1. SUM
sum_values = VALUE1 + VALUE2
table.add_row([f'{VALUE1} + {VALUE2}', sum_values])

## 2. SUBTRACTION
subtract_values = VALUE1 - VALUE2
table.add_row([f'{VALUE1} - {VALUE2}', subtract_values])

## 3. MULTIPLICATION
multiplication_values = VALUE1 * VALUE2
table.add_row([f'{VALUE1} * {VALUE2}', multiplication_values])

## 4. DIVISION
division_values = VALUE1 / VALUE2
table.add_row([f'{VALUE1} / {VALUE2}', division_values])

# =========== EXERCISE 2 ===========
VALUE3 = 25
VALUE4 = 7
int_division = VALUE3 // VALUE4
module_division = VALUE3 % VALUE4
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 2', ''])
table.add_row([f'{VALUE3} // {VALUE4}', int_division])
table.add_row([f'{VALUE3} % {VALUE4}', module_division])

# =========== EXERCISE 3 ===========
VALUE5=5
VALUE6=4
potenciation_value = VALUE5**VALUE6
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 3', ''])
table.add_row([f'{VALUE5} ** {VALUE6}', potenciation_value])

# =========== EXERCISE 4 ===========
VALUE7=10
VALUE8=6
VALUE9=2
expression_value = VALUE7 + VALUE8 * VALUE9
table.add_row(['EXERCISE 4', ''])
table.add_row(['A ordem de predecessão dos operadores', 'potenciação; depois, multipl. ou divisão; depois, soma ou subtração'])
table.add_row([f'{VALUE7} + {VALUE8} * {VALUE9}', expression_value])

print(table)