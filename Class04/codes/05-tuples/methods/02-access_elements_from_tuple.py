from collections.abc import Sized

from prettytable import PrettyTable

"""
ACCESS ELEMENTS FROM TUPLE
"""

# 1. ACCESS ELEMENTS FROM TUPLE
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) Instantiating a new tuple
sample_tuple = ("upGrad", -9.18+76.98j,  True, "Python", None, 23432)
sample_tuple_class = type(sample_tuple)
sample_tuple_class_name = sample_tuple_class.__name__
sample_tuple_id = id(sample_tuple)
sample_tuple_len = len(sample_tuple)

## (b) Access an element

### i. Element at index 1
sample_tuple_element_index = 1
sample_tuple_element_index_1 = sample_tuple[sample_tuple_element_index]
sample_tuple_element_index_1_class = type(sample_tuple_element_index_1)
sample_tuple_element_index_1_class_name = sample_tuple_element_index_1_class.__name__
sample_tuple_element_index_1_id = id(sample_tuple_element_index_1)
sample_tuple_element_index_1_len = (len(sample_tuple_element_index_1)
                       if isinstance(sample_tuple_element_index_1, Sized)
                       else None)

### ii. Element index 3
sample_tuple_element_index = 3
sample_tuple_element_index_3 = sample_tuple[sample_tuple_element_index]
sample_tuple_element_index_3_class = type(sample_tuple_element_index_3)
sample_tuple_element_index_3_class_name = sample_tuple_element_index_3_class.__name__
sample_tuple_element_index_3_id = id(sample_tuple_element_index_3)
sample_tuple_element_index_3_len = (len(sample_tuple_element_index_3)
                       if isinstance(sample_tuple_element_index_3, Sized)
                       else None)

### iii. Element index 4
sample_tuple_element_index = 4
sample_tuple_element_index_4 = sample_tuple[sample_tuple_element_index]
sample_tuple_element_index_4_class = type(sample_tuple_element_index_4)
sample_tuple_element_index_4_class_name = sample_tuple_element_index_4_class.__name__
sample_tuple_element_index_4_id = id(sample_tuple_element_index_4)
sample_tuple_element_index_4_len = (len(sample_tuple_element_index_4)
                       if isinstance(sample_tuple_element_index_4, Sized)
                       else None)

## (c) Showing results

### i. Create Table
table = PrettyTable()
### ii. Add header
table.field_names = table_field_names
### iii. Add data to table
table.add_row(["New Tuple", sample_tuple, sample_tuple_class, sample_tuple_class_name, sample_tuple_id, sample_tuple_len])
table.add_row(["Tuple element (index 1)", sample_tuple_element_index_1, sample_tuple_element_index_1_class, sample_tuple_element_index_1_class_name, sample_tuple_element_index_1_id, sample_tuple_element_index_1_len])
table.add_row(["Tuple element (index 3)", sample_tuple_element_index_3, sample_tuple_element_index_3_class, sample_tuple_element_index_3_class_name, sample_tuple_element_index_3_id, sample_tuple_element_index_3_len])
table.add_row(["Tuple element (index 4)", sample_tuple_element_index_4, sample_tuple_element_index_4_class, sample_tuple_element_index_4_class_name, sample_tuple_element_index_4_id, sample_tuple_element_index_4_len])
### iv. Print result
print(table)