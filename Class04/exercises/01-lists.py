from prettytable import PrettyTable
from typing import Sized

# ========== PART 1 - NEW LIST ==========

sales = list([1, 2, 3, 6])
sales_class = type(sales)
sales_class_name = sales_class.__name__
sales_id = id(sales)
sales_len = len(sales)

# ========== PART 2 - FUNCTIONS ==========

## (2.1) SUM
sum_elements_sales = sum(sales)
sum_elements_sales_class = type(sum_elements_sales)
sum_elements_sales_class_name = sum_elements_sales_class.__name__
sum_elements_sales_id = id(sum_elements_sales)
sum_elements_sales_len = len(sum_elements_sales) if isinstance(sum_elements_sales, Sized) else 'N/A'

## (2.2) MAX
max_element_sales = max(sales)
max_element_sales_class = type(max_element_sales)
max_element_sales_class_name = max_element_sales_class.__name__
max_element_sales_id = id(max_element_sales)
max_element_sales_len = len(max_element_sales) if isinstance(max_element_sales, Sized) else 'N/A'

## (2.3) MIN
min_element_sales = min(sales)
min_element_sales_class = type(min_element_sales)
min_element_sales_class_name = min_element_sales_class.__name__
min_element_sales_id = id(min_element_sales)
min_element_sales_len = len(min_element_sales) if isinstance(min_element_sales, Sized) else 'N/A'

# ========== PART 3 - INSERT ELEMENTS TO LIST ==========
new_sales = sales.copy()
new_sales.append(500)
new_sales.insert(1, 999)
new_sales_class = type(new_sales)
new_sales_class_name = new_sales_class.__name__
new_sales_id = id(new_sales)
new_sales_len = len(new_sales) if isinstance(new_sales, Sized) else 'N/A'

# ========== PART 4 - DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', 'Object class', 'Object class name', 'ID (Object)', 'Length (Object)']
table = PrettyTable(field_names=FIELD_NAMES)
table.add_rows([
    ['Sales List', sales, sales_class, sales_class_name, sales_id, sales_len],
    ['========', '========', '========', '========', '========', '========'],
    ['Sum', sum_elements_sales, sum_elements_sales_class, sum_elements_sales_class_name, sum_elements_sales_id,
     sum_elements_sales_len],
    ['Max', max_element_sales, max_element_sales_class, max_element_sales_class_name, max_element_sales_id,
     max_element_sales_len],
    ['Min', min_element_sales, min_element_sales_class, min_element_sales_class_name, min_element_sales_id,
     min_element_sales_len],
    ['========', '========', '========', '========', '========', '========'],
    ['New Sales List', new_sales, new_sales_class, new_sales_class_name, new_sales_id, new_sales_len],
])
print(table)