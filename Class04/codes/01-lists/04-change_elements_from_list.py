from prettytable import PrettyTable

"""
CHANGE ELEMENTS FROM A LIST
    Syntax: <list_name>[element_index] = new_value
"""

# ========== PART 1 - NEW LIST ==========
sample_list = list()
sample_list.extend(["new_element", True, 65.87 - 9.17j, "upGrad", None, "1", 5])
sample_list_class = type(sample_list)
sample_list_class_name = sample_list_class.__name__
sample_list_id = id(sample_list)
sample_list_len = len(sample_list)

# ========== PART 2 - CHANGE ELEMENTS ==========
third_element_index = 2
modified_third_element_sample_list = sample_list.copy()
modified_third_element_sample_list[third_element_index] = {'item_price': 1.45}
modified_third_element_sample_list_class = type(modified_third_element_sample_list)
modified_third_element_sample_list_class_name = modified_third_element_sample_list_class.__name__
modified_third_element_sample_list_id = id(modified_third_element_sample_list)
modified_third_element_sample_list_len = len(modified_third_element_sample_list)

# ========== PART 3 - DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', "Object class", "Object class name", "ID (Object)", "Length (Object)"]
table = PrettyTable(field_names=FIELD_NAMES)
table.add_row(['NEW LIST', sample_list, sample_list_class, sample_list_class_name, sample_list_id, sample_list_len])

table.add_row(['=========', '=========', '=========', '=========', '=========', '========='])
table.add_row(['CHANGING ELEMENTS FROM A LIST', '', '', '', '', ''])
table.add_row(['Index 2 modified', modified_third_element_sample_list, modified_third_element_sample_list_class,
               modified_third_element_sample_list_class_name, modified_third_element_sample_list_id,
               modified_third_element_sample_list_len])
print(table)