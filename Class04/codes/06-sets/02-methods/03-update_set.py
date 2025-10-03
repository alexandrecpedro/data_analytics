from prettytable import PrettyTable

"""
UPDATE SET
    Updates the current set, by adding items from another set (or any other iterable)
    If an item is present in both sets, only one appearance of this item will 
        be present in the updated set
    As a shortcut, you can use the |= operator instead        
"""

table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

# 1. UPDATE METHOD
## (a) Sample Set
sample_set = set()
sample_set.add("new_element")
sample_set.add(None)

sample_set_class = type(sample_set)
sample_set_class_name = sample_set_class.__name__
sample_set_id = id(sample_set)
sample_set_len = len(sample_set)

## (b) New Set
new_set = {"google", "microsoft", "apple"}

new_set_class = type(new_set)
new_set_class_name = new_set_class.__name__
new_set_id = id(new_set)
new_set_len = len(new_set)

## (c) Table
### i. Create Table
table = PrettyTable()
### ii. Add header
table.field_names = table_field_names
### iii. Add data to table
table.add_row(["Sample Set", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])
table.add_row(["New Set", new_set, new_set_class, new_set_class_name, new_set_id, new_set_len])
### iv. Print result
print(f"{table}\n")

# 2. UPDATE METHOD
## (a) Update the sample_set with new_set
### i. Function update
sample_set.update(new_set) # OR sample_set |= new_set

### ii. Sample Set modified
sample_set_class = type(sample_set)
sample_set_class_name = sample_set_class.__name__
sample_set_id = id(sample_set)
sample_set_len = len(sample_set)

## (b) Table
### i. Create Table
table2 = PrettyTable()
### ii. Add header
table2.field_names = table_field_names
### iii. Add data to table
table2.add_row(["Sample Set (update)", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])
### iv. Print result
print(f"{table2}\n")