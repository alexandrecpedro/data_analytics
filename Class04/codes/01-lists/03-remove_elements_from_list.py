from prettytable import PrettyTable
from typing import Sized

"""
REMOVE ELEMENTS FROM A LIST
    (a) REMOVE 
        Syntax: <list_name>.remove(item_name)
    (b) DELETE 
        Syntax: del <list_name>(element_index)
    (c) POP 
        Syntax: <list_name>.pop(element_index)
"""

# ========== PART 1 - NEW LIST ==========
sample_list = list()
sample_list.extend([-14.0, 65.87 - 9.17j, 'new element', None, 27.0, ('Node', 'Python', '.NET', 'Java', 'PHP'), False, 98372, {'id': True}])
sample_list_class = type(sample_list)
sample_list_class_name = sample_list_class.__name__
sample_list_id = id(sample_list)
sample_list_len = len(sample_list)

# ========== PART 2 - REMOVE ELEMENTS ==========
## (2.1) FUNCTION REMOVE
removed_element_sample_list = sample_list.copy()
removed_element_sample_list.remove(None)
removed_element_sample_list_class = type(removed_element_sample_list)
removed_element_sample_list_class_name = removed_element_sample_list_class.__name__
removed_element_sample_list_id = id(removed_element_sample_list)
removed_element_sample_list_len = len(removed_element_sample_list)

## (2.2) FUNCTION DELETE
delete_element_sample_list = sample_list.copy()
del delete_element_sample_list[5]

delete_element_sample_list_class = type(delete_element_sample_list)
delete_element_sample_list_class_name = delete_element_sample_list_class.__name__
delete_element_sample_list_id = id(delete_element_sample_list)
delete_element_sample_list_len = len(delete_element_sample_list)

## (2.3) FUNCTION POP
sample_list_element_index = -1
pop_element_sample_list = sample_list.copy()
removed_element = pop_element_sample_list.pop(sample_list_element_index)
removed_element_class = type(removed_element)
removed_element_class_name = removed_element_class.__name__
removed_element_id = id(removed_element)
removed_element_len = len(removed_element) if isinstance(removed_element, Sized) else 'N/A'

pop_element_sample_list_class = type(pop_element_sample_list)
pop_element_sample_list_class_name = pop_element_sample_list_class.__name__
pop_element_sample_list_id = id(pop_element_sample_list)
pop_element_sample_list_len = len(pop_element_sample_list)

# ========== PART 3 - DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', "Object class", "Object class name", "ID (Object)", "Length (Object)"]
table = PrettyTable(field_names=FIELD_NAMES)
table.add_row(['NEW LIST', sample_list, sample_list_class, sample_list_class_name, sample_list_id, sample_list_len])

table.add_row(['=========', '=========', '=========', '=========', '=========', '========='])
table.add_row(['REMOVE ELEMENTS FROM LIST', '', '', '', '', ''])
table.add_row(['Function Remove', removed_element_sample_list, removed_element_sample_list_class,
               removed_element_sample_list_class_name, removed_element_sample_list_id, removed_element_sample_list_len])
table.add_row(['Function Delete', delete_element_sample_list, delete_element_sample_list_class,
               delete_element_sample_list_class_name, delete_element_sample_list_id, delete_element_sample_list_len])
table.add_row(['Function Pop (list)', pop_element_sample_list, pop_element_sample_list_class,
               pop_element_sample_list_class_name, pop_element_sample_list_id, pop_element_sample_list_len])
table.add_row(['Function Pop (element)', removed_element, removed_element_class, removed_element_class_name,
               removed_element_id, removed_element_len])

print(table)