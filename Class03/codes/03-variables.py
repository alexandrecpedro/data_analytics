from prettytable import PrettyTable

# CONSTANTS
FIELD_NAMES = ['Description', 'Value', 'Object_Type']
table = PrettyTable(field_names=FIELD_NAMES)

table.add_row(['Variable Types', 'Dynamically typed', ''])
## 1. INTEGER
int_number = 3
int_number_type = type(int_number)
table.add_row(['Integer', int_number, int_number_type])

## 2. FLOAT
float_number = 985.17
float_number_type = type(float_number)
table.add_row(['Float', float_number, float_number_type])

## 3. BOOLEAN
boolean_var = True
boolean_var_type = type(boolean_var)
table.add_row(['Boolean', boolean_var, boolean_var_type])

## 4. STRING
str_var = 'My text'
str_var_type = type(str_var)
table.add_row(['String', str_var, str_var_type])
print(table)

### CHALLENGE
print('\nCalculate the square root of an input number')
number = int(input('Number to get the square root of: '))
square_root_number = number ** (1/2)
print(f'Square Root of {number}: {square_root_number}')

