from collections.abc import Collection

from prettytable import PrettyTable

"""
CLEAR ELEMENTS FROM A DICT
    removes all the elements without warning if the dict is empty
    It does not return any value
"""

# 1. STARTING DICT
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) Instantiating a New Dictionary
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
table.add_row(["Sample Dict (new)", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id, sample_dict_len])

# 2. CLEAR ALL ELEMENTS FROM NON-EMPTY DICT
## (a) Clear function
clear_dict = sample_dict.copy()
clear_dict.clear()
clear_dict_class = type(clear_dict)
clear_dict_class_name = clear_dict_class.__name__
clear_dict_id = id(clear_dict)
clear_dict_len = len(clear_dict)

## (b) Table
### i. Add data to table
table.add_row(["============", "============", "============", "============", "============", "============"])
table.add_row(["Sample Dict (after clear)", clear_dict, clear_dict_class, clear_dict_class_name, clear_dict_id, clear_dict_len])

# 3. CLEAR ALL ELEMENTS FROM EMPTY DICT
## (a) Empty Dict
### i. Instantiate
empty_dict = dict()
empty_dict_class = type(empty_dict)
empty_dict_class_name = empty_dict_class.__name__
empty_dict_id = id(empty_dict)
empty_dict_len = len(empty_dict)

### iI. Add data to table
table.add_row(["============", "============", "============", "============", "============", "============"])
table.add_row(["Empty Dict (new)", empty_dict, empty_dict_class, empty_dict_class_name, empty_dict_id, empty_dict_len])

## (b) Clear Empty dict
## i. Function to clear
empty_dict.clear()

## ii. Empty dict details after clear
empty_dict_class = type(empty_dict)
empty_dict_class_name = empty_dict_class.__name__
empty_dict_id = id(empty_dict)
empty_dict_len = len(empty_dict)

### iii. Add data to table
table.add_row(["============", "============", "============", "============", "============", "============"])
table.add_row(["Empty Dict (after clear)", empty_dict, empty_dict_class, empty_dict_class_name, empty_dict_id, empty_dict_len])
### vi. Print result
print(table)