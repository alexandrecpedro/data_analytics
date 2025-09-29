from prettytable import PrettyTable

# ========== PART 1 - NEW LIST ==========
sample_list = list()
sample_list_class = type(sample_list)
sample_list_class_name = sample_list_class.__name__
sample_list_id = id(sample_list)
sample_list_len = len(sample_list)

# ========== PART 2 - DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', "Object class", "Object class name", "ID (Object)", "Length (Object)"]
table = PrettyTable(field_names=FIELD_NAMES)
table.add_row(['NEW LIST', sample_list, sample_list_class, sample_list_class_name, sample_list_id, sample_list_len])
print(table)