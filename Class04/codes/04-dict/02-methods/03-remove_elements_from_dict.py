from collections.abc import Collection

from prettytable import PrettyTable

"""
REMOVE ELEMENTS FROM A DICT
    (a) DELETE - delete the key that is present in the dictionary
        (raises an exception if the key is not found and 
        hence non-existence of the key has to be handled)

        Syntax: del <dict_name>[key]

    (b) POP - removes the specified item from the dictionary
        and returns the value of the removed item
        (raises an exception if default value is not specified and
        no item with the specified key is found)

        Syntax: <dict_name>.pop(key, Optional<default_value>**)

    Ps: default_value is returned if the specified key does not exist 

    (c) POPITEM - removes the item that was last inserted into the dictionary
        and return its value

        Syntax: <dict_name>.popitem()
"""

# 1. STARTING LIST
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) Instantiating a new dict
sample_dict = dict()
sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)

## (b) Add new elements
sample_dict["key_1"] = "new_element"
sample_dict["key_2"] = True
sample_dict["key_3"] = 65.87 - 9.17j
sample_dict["key_4"] = "upGrad"
sample_dict["key_5"] = None
sample_dict["key_6"] = "1"
sample_dict["key_7"] = 5
sample_dict_len = (len(sample_dict)
                   if isinstance(sample_dict, Collection)
                   else None)

## (c) Showing results

### i. Create Table
table = PrettyTable()
### ii. Add header
table.field_names = table_field_names
### iii. Add data to table
table.add_row(["New Dict", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id, sample_dict_len])
### iv. Print result
print(table)

# 2. REMOVE ELEMENTS FROM DICT
## (a) Remove an element by its key using 'DEL'
element_to_be_removed_key = "key_2"
del sample_dict[element_to_be_removed_key]

### i. Sample Dict after removed element
sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)
sample_dict_len = len(sample_dict)

### ii. Create Table
table2 = PrettyTable()
### iii. Add header
table2.field_names = table_field_names
### iv. Add data to table
table2.add_row(["Sample Dict (del function)", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id,
                sample_dict_len])
### v. Print result
print(table2)

## (b) Remove an element by its key using 'POP'
### i. Removed element
sample_dict_element_key = "key_3"
removed_element = sample_dict.pop(sample_dict_element_key)
removed_element_class = type(removed_element)
removed_element_class_name = removed_element_class.__name__
removed_element_id = id(removed_element)
# removed_element_len = len(removed_element) if hasattr(removed_element, '__len__') else None
removed_element_len = (len(removed_element)
                       if isinstance(removed_element, Collection)
                       # if removed_element is not None and
                       #    not isinstance(removed_element, (int, float, complex, bool))
                       else None)

### ii. Sample Dict status after modified
sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)
sample_dict_len = len(sample_dict)

### iii. Create Table
table3 = PrettyTable()
### iv. Add header
table3.field_names = table_field_names
### v. Add data to table
table3.add_row(["Sample Dict (pop function)", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id,
                sample_dict_len])
table3.add_row(
    ["Removed element", removed_element, removed_element_class, removed_element_class_name, removed_element_id,
     removed_element_len])
### vi. Print result
print(table3)

## (c) Remove the last inserted element using 'POPITEM()'
### i. Removed last inserted element
removed_last_item = sample_dict.popitem()
removed_last_item_key, removed_last_item_value = removed_last_item
removed_last_item_class = type(removed_last_item_value)
removed_last_item_class_name = removed_last_item_class.__name__
removed_last_item_id = id(removed_last_item_value)
# removed_last_item_len = len(removed_last_item) if hasattr(removed_last_item, '__len__') else None
removed_last_item_len = (len(removed_last_item_value)
                         if isinstance(removed_last_item_value, Collection)
                         # if removed_last_item_value is not None and
                         #    not isinstance(removed_last_item_value, (int, float, complex, bool))
                         else None)

### ii. Sample Dict status after modified
sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)
sample_dict_len = len(sample_dict)

### iii. Create Table
table4 = PrettyTable()
### iv. Add header
table4.field_names = table_field_names
### v. Add data to table
table4.add_row(
    ["Sample Dict (popitem function)", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id,
     sample_dict_len])
table4.add_row([f"Removed element (key={removed_last_item_key})", removed_last_item, removed_last_item_class,
                removed_last_item_class_name, removed_last_item_id, removed_last_item_len])
### vi. Print result
print(table4)