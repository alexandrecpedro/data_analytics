from random import randint, seed
from prettytable import PrettyTable
from typing import Sized

# ========== EXERCISE - RANDOM NUMBERS ==========
lower_limit = 1
upper_limit = 100
quantity_numbers = 5

seed_value = 45
seed(seed_value)

numbers_list = [randint(a=lower_limit, b=upper_limit) for _ in range(quantity_numbers)]

numbers_list_class = type(numbers_list)
numbers_list_class_name = numbers_list_class.__name__
numbers_list_id = id(numbers_list)
numbers_list_len = len(numbers_list) if isinstance(numbers_list, Sized) else 'N/A'

# ========== DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', 'Object class', 'Object class name', 'ID (Object)', 'Length (Object)']
table = PrettyTable(field_names=FIELD_NAMES)
table.add_row(['Numbers List', numbers_list, numbers_list_class, numbers_list_class_name, numbers_list_id, numbers_list_len])
print(table)