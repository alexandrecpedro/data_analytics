from prettytable import PrettyTable
from typing import Sized

# ========== EXERCISE 1 - COUNTRY REGISTER ==========

## (1.1) COUNTRY REGISTER
country_register = "Brasil,Argentina,Chile,Uruguai,Paraguai"
country_register_class = type(country_register)
country_register_class_name = country_register_class.__name__
country_register_id = id(country_register)
country_register_len = len(country_register)

## (1.2) COUNTRY REGISTER LIST
country_register_list = country_register.split(',')
country_register_list_class = type(country_register_list)
country_register_list_class_name = country_register_list_class.__name__
country_register_list_id = id(country_register_list)
country_register_list_len = len(country_register_list)

# ========== EXERCISE 2 - EMPLOYEE DATA ==========

## (2.1) EMPLOYEE REGISTER
employee_register = "ID005;Maria Silva;12500.75;Contabilidade"
employee_register_class = type(employee_register)
employee_register_class_name = employee_register_class.__name__
employee_register_id = id(employee_register)
employee_register_len = len(employee_register)

## (2.2) EMPLOYEE REGISTER LIST
employee_register_list = employee_register.split(';')
employee_register_list_class = type(employee_register_list)
employee_register_list_class_name = employee_register_list_class.__name__
employee_register_list_id = id(employee_register_list)
employee_register_list_len = len(employee_register_list)

## (2.3) EMPLOYEE SALARY
salary_comparison = 50000
employee_salary = float(employee_register_list[2])
is_employee_salary_greater_50000 = employee_salary > salary_comparison

is_employee_salary_greater_50000_class = type(is_employee_salary_greater_50000)
is_employee_salary_greater_50000_class_name = is_employee_salary_greater_50000_class.__name__
is_employee_salary_greater_50000_id = id(is_employee_salary_greater_50000)
is_employee_salary_greater_50000_len = (len(is_employee_salary_greater_50000)
    if isinstance(is_employee_salary_greater_50000, Sized)
        else 'N/A')

# ========== DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', 'Object class', 'Object class name', 'ID (Object)', 'Length (Object)']
table = PrettyTable(field_names=FIELD_NAMES)
table.add_rows([
    ['EXERCISE 1', '', '', '', '', ''],
    ['Country Register', country_register, country_register_class, country_register_class_name, country_register_id,
     country_register_len],
    ['Country Register List', country_register_list, country_register_list_class, country_register_list_class_name,
     country_register_list_id, country_register_list_len],
    ['========', '========', '========', '========', '========', '========'],
    ['EXERCISE 2', '', '', '', '', ''],
    ['Employee Register', employee_register, employee_register_class, employee_register_class_name,
     employee_register_id, employee_register_len],
    ['Employee Register List', employee_register_list, employee_register_list_class, employee_register_list_class_name,
     employee_register_list_id, employee_register_list_len],
    ['Employee Salary > 50000 ?', is_employee_salary_greater_50000, is_employee_salary_greater_50000_class,
     is_employee_salary_greater_50000_class_name, is_employee_salary_greater_50000_id,
     is_employee_salary_greater_50000_len]
])
print(table)