from prettytable import PrettyTable
from typing import Sized

# ========== EXERCISE - COMPANY DATA ==========
## (1.1) COMPANY DATA
company_data = ('Matriz 01',2023,['Alice', 'Roberto', 'Carla'])
company_data_class = type(company_data)
company_data_class_name = company_data_class.__name__
company_data_id = id(company_data)
company_data_len = len(company_data) if isinstance(company_data, Sized) else 'N/A'

## (1.2) FIRST NAME OF LIST
company_data_1st_name = company_data[-1][0]
company_data_1st_name_class = type(company_data_1st_name)
company_data_1st_name_class_name = company_data_1st_name_class.__name__
company_data_1st_name_id = id(company_data_1st_name)
company_data_1st_name_len = len(company_data_1st_name) if isinstance(company_data_1st_name, Sized) else 'N/A'

## (1.3) NEW NAME FOR LIST
new_name = 'Felipe'
employee_list_copy = company_data[-1][:]
employee_list_copy.append(new_name)

company_data_new = company_data[:-1] + (employee_list_copy,)

company_data_new_class = type(company_data_new)
company_data_new_class_name = company_data_new_class.__name__
company_data_new_id = id(company_data_new)
company_data_new_len = len(company_data_new) if isinstance(company_data_new, Sized) else 'N/A'

# ========== DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', 'Object class', 'Object class name', 'ID (Object)', 'Length (Object)']
table = PrettyTable(field_names=FIELD_NAMES)
table.add_rows([
    ['EXERCISE 1', '', '', '', '', ''],
    ['Company Data', company_data, company_data_class, company_data_class_name, company_data_id, company_data_len],
    ['First Name', company_data_1st_name, company_data_1st_name_class, company_data_1st_name_class_name,
     company_data_1st_name_id, company_data_1st_name_len],
    ['Company Data New', company_data_new, company_data_new_class, company_data_new_class_name,
     company_data_new_id, company_data_new_len],
])
print(table)