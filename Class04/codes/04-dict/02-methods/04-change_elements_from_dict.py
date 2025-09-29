from collections.abc import Collection

from prettytable import PrettyTable

"""
CHANGE ELEMENTS FROM A DICT
    Syntax: <dict_name>[element_index] = new_value
"""

# 1. STARTING LIST
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) Instantiating a new dict
sample_dict = dict()
sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)

## (b) Add new elements
sample_dict["element_1"] = "new_element"
sample_dict["element_2"] = True
sample_dict["element_3"] = 65.87 - 9.17j
sample_dict["element_4"] = "upGrad"
sample_dict["element_5"] = None
sample_dict["element_6"] = "1"
sample_dict["element_7"] = 5
sample_dict_len = (len(sample_dict)
                   if isinstance(sample_dict, Collection)
                   else None)

## (c) Showing results

### i. Create Table
table = PrettyTable()
### ii. Add header
table.field_names = table_field_names
### iii. Add data to table
table.add_row(["Sample Dict", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id, sample_dict_len])
### iv. Print result
print(table)

# 2. CHANGE ELEMENTS FROM DICT

## (a) Change an element at index 2

### i. Sample dict modified
sample_dict_element_key = "element_3"
sample_dict[sample_dict_element_key] = frozenset({"id": 23})
sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)
sample_dict_len = len(sample_dict)

### ii. Create Table
table2 = PrettyTable()
### iii. Add header
table2.field_names = table_field_names
### iv. Add data to table
table2.add_row(["Sample Dict (index 2 modified)", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id, sample_dict_len])
### v. Print result
print(table2)