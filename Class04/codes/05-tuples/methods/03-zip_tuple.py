from collections.abc import Collection

from prettytable import PrettyTable

"""
ZIP METHOD - Returns a zip object, which is an iterator of tuples 
    where the first item in each passed iterator is paired together, 
    and then the second item in each passed iterator are paired together
    If the passed iterables have different lengths, 
    the iterable with the least items decides the length of the new iterator

    Syntax: zip(iterator1, iterator2, ...)

Ps: Tuple cannot be modified after instantiated
"""

# 1. NEW TUPLE
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) Initial Tuples
### i. Sequence (seq)
seq_tuple = ('a', 'b', 'c')
seq_tuple_class = type(seq_tuple)
seq_tuple_class_name = seq_tuple_class.__name__
seq_tuple_id = id(seq_tuple)
seq_tuple_len = (len(seq_tuple)
                 if isinstance(seq_tuple, Collection)
                 else None)

### ii. Value (val)
val_tuple = (-14.56, True, {'id': 'Manos'})
val_tuple_class = type(val_tuple)
val_tuple_class_name = val_tuple_class.__name__
val_tuple_id = id(val_tuple)
val_tuple_len = (len(val_tuple)
                 if isinstance(val_tuple, Collection)
                 else None)

## (b) Zip method
zip_tuple = zip(seq_tuple, val_tuple)
zip_tuple_class = type(zip_tuple)
zip_tuple_class_name = zip_tuple_class.__name__
zip_tuple_id = id(zip_tuple)
zip_tuple_len = (len(zip_tuple)
                 if isinstance(zip_tuple, Collection)
                 else None)

# 2. TABLE
## (a) Create Table
table = PrettyTable()

## (b) Add header
table.field_names = table_field_names

## (c) Add data to table
table.add_row(["Seq tuple", seq_tuple, seq_tuple_class, seq_tuple_class_name, seq_tuple_id, seq_tuple_len])
table.add_row(["Val tuple", val_tuple, val_tuple_class, val_tuple_class_name, val_tuple_id, val_tuple_len])
table.add_row(["ZIP object", zip_tuple, zip_tuple_class, zip_tuple_class_name, zip_tuple_id, zip_tuple_len])

## (d) Print result
print(table)