from collections.abc import Collection

from prettytable import PrettyTable

"""
ADD ELEMENTS TO DICTIONARY
"""

# 1. STARTING DICTIONARY
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) New Dict

### i. Instantiate new dictionary
sample_dict = dict()
sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)
sample_dict_len = (len(sample_dict)
                   if isinstance(sample_dict, Collection)
                   else None)

### ii. Create Table
table = PrettyTable()
### iii. Add header
table.field_names = table_field_names
### iv. Add data to table
table.add_row(["Sample List", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id, sample_dict_len])
### v. Print result
print(f"{table}\n")

## (b) Add new elements

### i. Sample dict modified
sample_dict["element_1"] = "new_element"
sample_dict["element_2"] = True
sample_dict["element_3"] = 65.87 - 9.17j
sample_dict["element_4"] = "upGrad"
sample_dict["element_5"] = None
sample_dict["element_6"] = "1"
sample_dict["element_7"] = 5

sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)
sample_dict_len = (len(sample_dict)
                   if isinstance(sample_dict, Collection)
                   else None)

### ii. Create Table
table2 = PrettyTable()
### iii. Add header
table2.field_names = table_field_names
### iv. Add data to table
table2.add_row(["Sample Dict (after add)", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id, sample_dict_len])
### v. Print result
print(f"{table2}\n")