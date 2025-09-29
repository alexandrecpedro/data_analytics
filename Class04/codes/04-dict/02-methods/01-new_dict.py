from collections.abc import Collection

from prettytable import PrettyTable

"""
NEW DICTIONARY - Instantiating a new dictionary
    (a) DICT - empty dictionary
        Syntax: dict()

    (b) FROMKEYS - returns the dictionary with key mapped and specific value
        Syntax: dict.fromkeys(seq, val)
            - seq: the sequence to be transformed into a dictionary
            - val: initial values that need to be assigned to the generated keys. Defaults to None
"""

table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]
seq = ('a', 'b', 'c')
val = (-14.56, True, {'id': 'Manos'})

# 1. DICTIONARIES
## (a) Empty Dict
empty_dict = dict()
empty_dict_class = type(empty_dict)
empty_dict_class_name = empty_dict_class.__name__
empty_dict_id = id(empty_dict)
empty_dict_len = (len(empty_dict)
                  if isinstance(empty_dict, Collection)
                  else None)

## (b) New Dict with None Values
none_value_dict = dict.fromkeys(seq, None)  # OR dict.fromkeys(seq)
none_value_dict_class = type(none_value_dict)
none_value_dict_class_name = none_value_dict_class.__name__
none_value_dict_id = id(none_value_dict)
none_value_dict_len = (len(none_value_dict)
                       if isinstance(none_value_dict, Collection)
                       else None)

## (c) New Dict with non-null Values
sample_dict = dict(zip(seq, val))
sample_dict_class = type(sample_dict)
sample_dict_class_name = sample_dict_class.__name__
sample_dict_id = id(sample_dict)
sample_dict_len = (len(sample_dict)
                   if isinstance(sample_dict, Collection)
                   else None)

# 2. TABLE
## (a) Create Table
table = PrettyTable()

## (b) Add header
table.field_names = table_field_names

## (c) Add data to table
table.add_row(["New Dict", empty_dict, empty_dict_class, empty_dict_class_name, empty_dict_id, empty_dict_len])
table.add_row(
    ["Sample Dict (None value)", none_value_dict, none_value_dict_class, none_value_dict_class_name, none_value_dict_id,
     none_value_dict_len])
table.add_row(["Sample Dict (Non-null value)", sample_dict, sample_dict_class, sample_dict_class_name, sample_dict_id,
               sample_dict_len])

## (d) Print result
print(table)