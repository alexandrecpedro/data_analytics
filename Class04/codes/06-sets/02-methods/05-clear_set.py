from prettytable import PrettyTable

"""
CLEAR ELEMENTS FROM A SET
    removes all the elements without warning if the set is empty
    It does not return any value
"""

# 1. STARTING SET
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) Instantiating a new set
sample_set = set()
sample_set_class = type(sample_set)
sample_set_class_name = sample_set_class.__name__
sample_set_id = id(sample_set)

## (b) Add new elements
sample_set.add("new_element")
sample_set.add(True)
sample_set.add(65.87 - 9.17j)
sample_set.add("upGrad")
sample_set.add(None)
sample_set.add("1")
sample_set.add(5)
sample_set_len = len(sample_set)

## (c) Showing results

### i. Create Table
table = PrettyTable()
### ii. Add header
table.field_names = table_field_names
### iii. Add data to table
table.add_row(["Sample Set (new)", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])
### iv. Print result
print(table)

# 2. CLEAR ALL ELEMENTS FROM NON-EMPTY SET
## (a) Clear function
sample_set.clear()
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
table2.add_row(["Sample Set (clear)", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])
### iv. Print result
print(table2)

# 3. CLEAR ALL ELEMENTS FROM EMPTY SET
## (a) Empty Set

### i. Instantiate
empty_set = set()
empty_set_class = type(empty_set)
empty_set_class_name = empty_set_class.__name__
empty_set_id = id(empty_set)
empty_set_len = len(empty_set)

### ii. Create Table
table3 = PrettyTable()
### iii. Add header
table3.field_names = table_field_names
### iv. Add data to table
table3.add_row(["Empty Set (new)", empty_set, empty_set_class, empty_set_class_name, empty_set_id, empty_set_len])
### v. Print result
print(table3)

## (b) Clear Empty Set
## i. Function to clear
empty_set.clear()

## ii. Empty Set details after clear
empty_set_class = type(empty_set)
empty_set_class_name = empty_set_class.__name__
empty_set_id = id(empty_set)
empty_set_len = len(empty_set)

### iii. Create Table
table4 = PrettyTable()
### iv. Add header
table4.field_names = table_field_names
### v. Add data to table
table4.add_row(["Empty Set (after clear)", empty_set, empty_set_class, empty_set_class_name, empty_set_id, empty_set_len])
### vi. Print result
print(table4)