import locale
from enum import Enum
from prettytable import PrettyTable
from typing import Sized

# ========== EXERCISE 1 - STUDENT ==========

## (1.1) STUDENT DICT
student = {
    'name': 'Joe Doe',
    'age': 22,
    'course': 'Data Analytics',
}
student_class = type(student)
student_class_name = student_class.__name__
student_id = id(student)
student_len = len(student)

## (1.2) STUDENT NAME
property_name = 'name'
student_name = student.get(property_name)
student_name_class = type(student_name)
student_name_class_name = student_name_class.__name__
student_name_id = id(student_name)
student_name_len = len(student_name) if isinstance(student_name, Sized) else 'N/A'

# ========== EXERCISE 2 - EMPLOYEE DATA ==========

## (2.1) STOCK DICT
stock = {
    'TV': 1500,
    'Radio': 200,
    'Microwave-oven': 900
}
stock_class = type(stock)
stock_class_name = stock_class.__name__
stock_id = id(stock)
stock_len = len(stock)

## (2.2) GET PRICE BY PRODUCT NAME INPUT
class ErrorMessage(Enum):
    INVALID_TYPE = 'Invalid item type!'
    NOT_FOUND = 'Item not found!'

class Color(Enum):
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    MAGENTA = "\033[35m"
    RED = "\033[31m"
    RESET = "\033[0m"
    YELLOW = "\033[33m"

locale.setlocale(category=locale.LC_ALL, locale='pt_BR.UTF-8')

stock_lower = {key.lower(): value for key, value in stock.items()}
product_name = input('Enter product name (or type "all" to list all): ').strip().lower()
item_value = stock_lower.get(product_name, ErrorMessage.NOT_FOUND.value)
if isinstance(item_value, (int, float)):
    item_value = locale.currency(val=item_value, grouping=True)

item_value_class = type(item_value)
item_value_class_name = item_value_class.__name__
item_value_id = id(item_value)
item_value_len = len(item_value)

# ========== DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', 'Object class', 'Object class name', 'ID (Object)', 'Length (Object)']
table = PrettyTable(field_names=FIELD_NAMES)
table.add_rows([
    ['EXERCISE 1', '', '', '', '', ''],
    ['Student', student, student_class, student_class_name, student_id, student_len],
    ['Student Name', student_name, student_name_class, student_name_class_name, student_name_id, student_name_len],
    ['========', '========', '========', '========', '========', '========'],
    ['EXERCISE 2', '', '', '', '', ''],
    ['Stock', stock, stock_class, stock_class_name, stock_id, stock_len],
    [product_name.capitalize(), item_value, item_value_class, item_value_class_name, item_value_id, item_value_len],
])
print(table)