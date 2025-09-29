from prettytable import PrettyTable

"""
ADD ELEMENTS TO LIST
    (a) APPEND - add item to the end of the list
    (b) INSERT - insert an item at a given position
    (c) EXTEND - extend an array of items to the end of the list
"""

# ========== PART 1 - NEW LIST ==========
sample_list = list()
sample_list_class = type(sample_list)
sample_list_class_name = sample_list_class.__name__
sample_list_id = id(sample_list)
sample_list_len = len(sample_list)

# ========== PART 2 - INSERT ELEMENTS INTO LIST ==========
## (2.1) FUNCTION APPEND
appended_list = sample_list.copy()
appended_list.append("new element")
appended_list.append(None)
appended_list_class = type(appended_list)
appended_list_class_name = appended_list_class.__name__
appended_list_id = id(appended_list)
appended_list_len = len(appended_list)

## (2.2) FUNCTION INSERT
insert_list = appended_list.copy()
insert_list.insert(2, 54 / 2)
insert_list.insert(0, -(196 ** 0.5))
insert_list.insert(1, True)
insert_list_class = type(insert_list)
insert_list_class_name = insert_list_class.__name__
insert_list_id = id(insert_list)
insert_list_len = len(insert_list)

## (2.3) FUNCTION EXTENDS
extends_list = insert_list.copy()
extends_list.extend([('Node', 'Python', '.NET', 'Java', 'PHP'), False, 98372, { "id": None }])

extends_list_class = type(extends_list)
extends_list_class_name = extends_list_class.__name__
extends_list_id = id(extends_list)
extends_list_len = len(extends_list)

# ========== PART 3 - DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', "Object class", "Object class name", "ID (Object)", "Length (Object)"]
table = PrettyTable(field_names=FIELD_NAMES)
table.add_row(['NEW LIST', sample_list, sample_list_class, sample_list_class_name, sample_list_id, sample_list_len])

table.add_row(['=========', '=========', '=========', '=========', '=========', '========='])
table.add_row(['INSERT ELEMENTS TO LIST', '', '', '', '', ''])
table.add_row(['Function Append', appended_list, appended_list_class, appended_list_class_name, appended_list_id, appended_list_len])
table.add_row(['Function Insert', insert_list, insert_list_class, insert_list_class_name, insert_list_id, insert_list_len])
table.add_row(['Function Extends', extends_list, extends_list_class, extends_list_class_name, extends_list_id, extends_list_len])

print(table)