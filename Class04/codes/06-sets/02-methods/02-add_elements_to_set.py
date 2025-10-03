from prettytable import PrettyTable

"""
ADD ELEMENTS TO SET
    Add single item to the set    
"""

table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

# 1. ADD METHOD
## (a) New Set

### i. Instantiate new set
sample_set = set()
sample_set_class = type(sample_set)
sample_set_class_name = sample_set_class.__name__
sample_set_id = id(sample_set)
sample_set_len = len(sample_set)

### ii. Create Table
table = PrettyTable()
### iii. Add header
table.field_names = table_field_names
### iv. Add data to table
table.add_row(["Sample Set", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])
### v. Print result
print(f"{table}\n")

## (b) Add new element

### i. Sample set modified
sample_set.add("new_element")
sample_set.add(None)

sample_set_class = type(sample_set)
sample_set_class_name = sample_set_class.__name__
sample_set_id = id(sample_set)
sample_set_len = len(sample_set)

### ii. Create Table
table2 = PrettyTable()
### iii. Add header
table2.field_names = table_field_names
### iv. Add data to table
table2.add_row(["Sample Set (add)", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])
### v. Print result
print(f"{table2}\n")