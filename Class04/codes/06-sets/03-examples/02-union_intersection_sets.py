"""
INSTRUCTION:
    Write a programme that reads two sets of integers entered by the user from the keyboard.
    Display the union and intersection of these sets on the screen

TEST CASES:
    | Set | Value |
    | --- | ----- |
    | 1   | 16    |
    | 1   | 8     |
    | 1   | 44    |
    | 1   | 0     |
    | === | ===== |
    | 2   | 12    |
    | 2   | 14    |
    | 2   | 16    |
    | 2   | 10    |
    | 2   | 8     |
    | 2   | 0     |
"""
from prettytable import PrettyTable

MESSAGE = 'Enter an integer number: '

# 1. FUNCTIONS
def input_int_number():
    while True:
        try:
            return int(input(MESSAGE))
        except ValueError:
            print("Invalid input! Please enter a valid integer!")

def create_new_set():
    new_set = set()
    number = input_int_number()

    while number != 0:
        new_set.add(number)
        number = input_int_number()

    return new_set

# 2. MAIN PROGRAM
print("Start of the program")
print('Data from the first set')
set_1 = create_new_set()
print('Data from the second set')
set_2 = create_new_set()

# 3. TABLE
table = PrettyTable()
table.field_names = ['Description', 'Value']
table.add_row(['Set 1', set_1])
table.add_row(['Set 2', set_2])
table.add_row(['Union set 1 and set 2', set_1 | set_2])
table.add_row(['Intersection set 1 and set 2', set_1 & set_2])
print(table)

print('\nEnd of the program')