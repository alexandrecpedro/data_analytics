from prettytable import PrettyTable

"""
NEW TUPLE - Instantiating a new tuple
    (a) TUPLE - creates an empty tuple
        Syntax: tuple()

    (b) ZIP - returns a zip object, which is an iterator of tuples 
        where the first item in each passed iterator is paired together, 
        and then the second item in each passed iterator are paired together
        If the passed iterables have different lengths, 
        the iterable with the least items decides the length of the new iterator

        Syntax: zip(iterator1, iterator2, ...)

Ps: Tuple cannot be modified after instantiated
"""

# 1. NEW TUPLE
## (a) New Tuple
### i. Empty Tuple
empty_tuple = tuple()
empty_tuple_class = type(empty_tuple)
empty_tuple_class_name = empty_tuple_class.__name__
empty_tuple_id = id(empty_tuple)
empty_tuple_len = len(empty_tuple)

### ii. Sample Tuple
sample_tuple = ("upGrad", "Python", "ML", 23432)
sample_tuple_class = type(sample_tuple)
sample_tuple_class_name = sample_tuple_class.__name__
sample_tuple_id = id(sample_tuple)
sample_tuple_len = len(sample_tuple)

## (b) Table

### i. Create Table
table = PrettyTable()

### ii. Add header
table.field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

### iii. Add data to table
table.add_row(["Empty tuple", empty_tuple, empty_tuple_class, empty_tuple_class_name, empty_tuple_id, empty_tuple_len])
table.add_row(
    ["Sample tuple", sample_tuple, sample_tuple_class, sample_tuple_class_name, sample_tuple_id, sample_tuple_len])

### iv. Print result
print(table)