from prettytable import PrettyTable

"""
REMOVE ELEMENTS FROM A SET
    (a) REMOVE - removes the specified element from the set 
        (raise an error if the specified item does not exist)
    (b) DISCARD - removes element without warning if element not present 
    (c) POP - removes a random item from the set and updates it 
        returns the removed item
        (raise an exception if the set is empty)
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

# 2. REMOVE ELEMENTS FROM SET
## (a) Remove an element by its name
element_to_be_removed = True
sample_set.remove(element_to_be_removed)
sample_set_class = type(sample_set)
sample_set_class_name = sample_set_class.__name__
sample_set_id = id(sample_set)
sample_set_len = len(sample_set)

### i. Create Table
table2 = PrettyTable()
### ii. Add header
table2.field_names = table_field_names
### iii. Add data to table
table2.add_row(["Sample Set (remove function)", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])
### iv. Print result
print(table2)

## (b) Discard an element by its name
element_to_be_discarded_1 = "Hello World"
element_to_be_discarded_2 = 65.87-9.17j
sample_set.discard(element_to_be_discarded_1)
sample_set.discard(element_to_be_discarded_2)

### i. Sample set after discarded element
sample_set_class = type(sample_set)
sample_set_class_name = sample_set_class.__name__
sample_set_id = id(sample_set)
sample_set_len = len(sample_set)

### ii. Create Table
table3 = PrettyTable()
### iii. Add header
table3.field_names = table_field_names
### iv. Add data to table
table3.add_row(["Sample Set (discard function)", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])
### v. Print result
print(table3)

## (c) Remove an element by index and returns the removed element

### i. Removed element 1
removed_element_1 = sample_set.pop()
removed_element_1_class = type(removed_element_1)
removed_element_1_class_name = removed_element_1_class.__name__
removed_element_1_id = id(removed_element_1)
# removed_element_1_len = len(removed_element_1) if hasattr(removed_element_1, '__len__') else None
removed_element_1_len = (len(removed_element_1)
                       if removed_element_1 is not None and
                          not isinstance(removed_element_1, (int, float, complex, bool))
                       else None)

### ii. Removed element 2
removed_element_2 = sample_set.pop()
removed_element_2_class = type(removed_element_2)
removed_element_2_class_name = removed_element_2_class.__name__
removed_element_2_id = id(removed_element_2)
# removed_element_2_len = len(removed_element_2) if hasattr(removed_element_2, '__len__') else None
removed_element_2_len = (len(removed_element_2)
                       if removed_element_2 is not None and
                          not isinstance(removed_element_2, (int, float, complex, bool))
                       else None)

### iii. Sample set status after modified
sample_set_class = type(sample_set)
sample_set_class_name = sample_set_class.__name__
sample_set_id = id(sample_set)
sample_set_len = len(sample_set)

### iv. Create Table
table4 = PrettyTable()
### v. Add header
table4.field_names = table_field_names
### vi. Add data to table
table4.add_row(["Sample Set (pop function)", sample_set, sample_set_class, sample_set_class_name, sample_set_id, sample_set_len])
table4.add_row(["Removed element 1", removed_element_1, removed_element_1_class, removed_element_1_class_name, removed_element_1_id, removed_element_1_len])
table4.add_row(["Removed element 2", removed_element_2, removed_element_2_class, removed_element_2_class_name, removed_element_2_id, removed_element_2_len])
### vii. Print result
print(table4)