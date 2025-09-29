from prettytable import PrettyTable
from typing import Sized

"""
FUNCTION CONCAT LISTS WITH PLUS SYMBOL: 
    Join the elements from two lists.
"""

# ========== PART 1 - NEW LISTS ==========
## (2.1) LIST A
List_A = list()
List_A.extend([10, 12, 14, 16])
List_A_class = type(List_A)
List_A_class_name = List_A_class.__name__
List_A_id = id(List_A)
List_A_len = (len(List_A) if isinstance(List_A, Sized) else 'N/A')

## (2.2) LIST B
List_B = list()
List_B.extend([8, 20, 22, 24])
List_B_class = type(List_B)
List_B_class_name = List_B_class.__name__
List_B_id = id(List_B)
List_B_len = (len(List_B) if isinstance(List_B, Sized) else 'N/A')

# ========== PART 2 - JOIN LISTS ==========
List_R = List_A + List_B
List_R_class = type(List_R)
List_R_class_name = List_R_class.__name__
List_R_id = id(List_R)
List_R_len = (len(List_R) if isinstance(List_R, Sized) else 'N/A')

# ========== PART 3 - DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', "Object class", "Object class name", "ID (Object)", "Length (Object)"]
table = PrettyTable(field_names=FIELD_NAMES)
table.add_row(['LIST A', List_A, List_A_class, List_A_class_name, List_A_id, List_A_len])
table.add_row(['LIST B', List_B, List_B_class, List_B_class_name, List_B_id, List_B_len])

table.add_row(['=========', '=========', '=========', '=========', '=========', '========='])
table.add_row(['JOIN LISTS', 'List_A + List_B', '', '', '', ''])
table.add_row(['LIST R', List_R, List_R_class, List_R_class_name, List_R_id, List_R_len])
print(table)