from prettytable import PrettyTable

"""
FUNCTION COUNT: Return the number of times a given element appears in the list.
"""

# ========== PART 1 - NEW LIST ==========
sample_list = list()
sample_list.extend(['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana'])
sample_list_class = type(sample_list)
sample_list_class_name = sample_list_class.__name__
sample_list_id = id(sample_list)
sample_list_len = len(sample_list)

# ========== PART 2 - COUNT ELEMENTS ==========
number_of_apples = sample_list.count('apple')
number_of_bananas = sample_list.count('banana')
number_of_kiwi = sample_list.count('kiwi')
number_of_orange = sample_list.count('orange')
number_of_pear = sample_list.count('pear')

# ========== PART 3 - DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)
table.add_row(['NEW LIST', sample_list])
table.add_row(['=========', '========='])
table.add_row(['FRUIT', 'QUANTITY'])
table.add_row(["Apple", number_of_apples])
table.add_row(["Banana", number_of_bananas])
table.add_row(["Kiwi", number_of_kiwi])
table.add_row(["Orange", number_of_orange])
table.add_row(["Pear", number_of_pear])
print(table)