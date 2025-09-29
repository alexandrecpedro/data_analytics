from collections.abc import Collection

from prettytable import PrettyTable

"""
UPDATE ELEMENTS FROM A DICT
    (a) Definition
        updates the dictionary with the elements from another dictionary object 
        or from an iterable of key/value pairs
        It does not return any value

    (b) Syntax
        dict.update([obj])
            where obj = dict or tuple or list of tuples
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
table.add_row(
    ["Sample Dict (new)", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id, sample_dict_len])
### iv. Print result
print(table)

# 2. UPDATE ELEMENTS FROM NON-EMPTY DICT
## (a) Update function
tuple_update = ((177, 'Onion'), (217, 'Apple'), (185, 'Avocado'))

sample_dict.update(tuple_update)
sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)
sample_dict_len = len(sample_dict)

## (b) Table
### i. Create Table
table2 = PrettyTable()
### ii. Add header
table2.field_names = table_field_names
### iii. Add data to table
table2.add_row(["Sample Dict (after update)", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id,
                sample_dict_len])
### iv. Print result
print(table2)