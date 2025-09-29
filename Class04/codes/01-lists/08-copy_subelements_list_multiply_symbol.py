from prettytable import PrettyTable
from typing import Sized

"""
FUNCTION COPY SUBSEQUENCE FROM LIST WITH MULTIPLY SYMBOL
"""

# ========== PART 1 - NEW LISTS ==========
## (2.1) LIST A
List_A = list()
List_A.extend([1, 2, 3])
List_A_class = type(List_A)
List_A_class_name = List_A_class.__name__
List_A_id = id(List_A)
List_A_len = (len(List_A) if isinstance(List_A, Sized) else None)

## (2.2) LIST B
List_B = list()
List_B.extend([0])
List_B_class = type(List_B)
List_B_class_name = List_B_class.__name__
List_B_id = id(List_B)
List_B_len = (len(List_B) if isinstance(List_B, Sized) else 'N/A')

# ========== PART 2 - MULTIPLY SYMBOL ==========
## (2.1) MULTIPLY SYMBOL LIST A
repetition_times = 3
List_A_multiplied = List_A * repetition_times
List_A_multiplied_class = type(List_A_multiplied)
List_A_multiplied_class_name = List_A_multiplied_class.__name__
List_A_multiplied_id = id(List_A_multiplied)
List_A_multiplied_len = (len(List_A_multiplied) if isinstance(List_A_multiplied, Sized) else 'N/A')

## (2.2) MULTIPLY SYMBOL LIST B
repetition_times = 10
List_B_multiplied = List_B * repetition_times
List_B_multiplied_class = type(List_B_multiplied)
List_B_multiplied_class_name = List_B_multiplied_class.__name__
List_B_multiplied_id = id(List_B_multiplied)
List_B_multiplied_len = (len(List_B_multiplied) if isinstance(List_B_multiplied, Sized) else 'N/A')

# ========== PART 3 - DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', "Object class", "Object class name", "ID (Object)", "Length (Object)"]
table = PrettyTable(field_names=FIELD_NAMES)
table.add_row(['LIST A', List_A, List_A_class, List_A_class_name, List_A_id, List_A_len])
table.add_row(['LIST B', List_B, List_B_class, List_B_class_name, List_B_id, List_B_len])

table.add_row(['=========', '=========', '=========', '=========', '=========', '========='])
table.add_row(['MULTIPLY SYMBOL', '', '', '', '', ''])
table.add_row(['List A multiplied by 3', List_A_multiplied, List_A_multiplied_class, List_A_multiplied_class_name,
               List_A_multiplied_id, List_A_multiplied_len])
table.add_row(['List B multiplied by 10', List_B_multiplied, List_B_multiplied_class, List_B_multiplied_class_name,
               List_B_multiplied_id, List_B_multiplied_len])
print(table)