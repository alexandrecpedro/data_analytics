from prettytable import PrettyTable

"""
NEW SET - Instantiating a new set
"""

# 1. NEW SET
## (a) Instantiation
sample_set = set()
sample_set_class = type(sample_set)
sample_set_class_name = sample_set_class.__name__
sample_set_id = id(sample_set)
sample_set_len = len(sample_set)

## (b) Table

### i. Create Table
table = PrettyTable()

### ii. Add header
table.field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

### iii. Add data to table
table.add_row(["New Set", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])

### iv. Print result
print(table)