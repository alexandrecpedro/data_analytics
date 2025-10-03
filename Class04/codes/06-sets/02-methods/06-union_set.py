from collections.abc import Collection

from prettytable import PrettyTable

"""
FUNCTION UNION 
    Returns a new set with distinct elements from all the sets
    If the argument is not passed to union(), it returns a shallow copy of the first set

    Syntax: <set_1>.union(*other_sets)
    Other syntax: <set_1> | <set_2> | ...

    Ps: * means that the method can take 0 or more arguments
"""

# 1. SETS
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) Sets
### i. Soccer Teams
soccer_teams = {'Corinthians', 'Real Madrid', 'Manchester City', 'Inter Miami'}
soccer_teams_class = type(soccer_teams)
soccer_teams_class_name = soccer_teams_class.__name__
soccer_teams_id = id(soccer_teams)
soccer_teams_len = (len(soccer_teams)
                    if isinstance(soccer_teams, Collection)
                    else None)

### ii. Airplane Manufacturers
airplanes_manufacturers = {'Boeing', 'Airbus', 'Embraer', 'Bombardier'}
airplanes_manufacturers_class = type(airplanes_manufacturers)
airplanes_manufacturers_class_name = airplanes_manufacturers_class.__name__
airplanes_manufacturers_id = id(airplanes_manufacturers)
airplanes_manufacturers_len = (len(airplanes_manufacturers)
                               if isinstance(airplanes_manufacturers, Collection)
                               else None)

### iii. Numbers
numbers = {-1.12, 9.23, 8.76, -65.26}
numbers_class = type(numbers)
numbers_class_name = numbers_class.__name__
numbers_id = id(numbers)
numbers_len = (len(numbers)
               if isinstance(numbers, Collection)
               else None)

### iv. Object Types
object_types = {True, None, (2 + 7j), frozenset({1: ('er', True, 3)})}
object_types_class = type(object_types)
object_types_class_name = object_types_class.__name__
object_types_id = id(object_types)
object_types_len = (len(object_types)
                    if isinstance(object_types, Collection)
                    # if object_types is not None and
                    #    not isinstance(object_types, (int, float, complex, bool))
                    else None)

# 2. SET - FUNCTION UNION
## (a) Union Of Sets
### i. Individual
result_soccer_airplanes = soccer_teams.union(airplanes_manufacturers)  # OR soccer_teams | airplanes_manufacturers
result_soccer_airplanes_class = type(result_soccer_airplanes)
result_soccer_airplanes_class_name = result_soccer_airplanes_class.__name__
result_soccer_airplanes_id = id(result_soccer_airplanes)
result_soccer_airplanes_len = (len(result_soccer_airplanes)
                               if isinstance(result_soccer_airplanes, Collection)
                               else None)

result_soccer_numbers = soccer_teams | numbers  # OR soccer_teams.union(numbers)
result_soccer_object_types = soccer_teams | object_types  # OR soccer_teams.union(object_types)

### ii. Union of many
# union_result = soccer_teams.union(airplanes_manufacturers, numbers, object_types)
union_result = soccer_teams | airplanes_manufacturers | numbers | object_types
union_result_class = type(union_result)
union_result_class_name = union_result_class.__name__
union_result_id = id(union_result)
union_result_len = (len(union_result)
                    if isinstance(union_result, Collection)
                    # if union_result is not None and
                    #    not isinstance(union_result, (int, float, complex, bool))
                    else None)

# 3. TABLE
## (a) Create Table
table = PrettyTable()
## (b) Add header
table.field_names = table_field_names
## (c) Add data to table
table.add_row(
    ["Soccer Teams", soccer_teams, soccer_teams_class, soccer_teams_class_name, soccer_teams_id, soccer_teams_len])
table.add_row(["Airplanes Manufacturers", airplanes_manufacturers, airplanes_manufacturers_class,
               airplanes_manufacturers_class_name, airplanes_manufacturers_id, airplanes_manufacturers_len])
table.add_row(["Numbers", numbers, numbers_class, numbers_class_name, numbers_id, numbers_len])
table.add_row(
    ["Object Types", object_types, object_types_class, object_types_class_name, object_types_id, object_types_len])
table.add_row(["Union (Soccer and Airplanes)", result_soccer_airplanes, result_soccer_airplanes_class,
               result_soccer_airplanes_class_name, result_soccer_airplanes_id, result_soccer_airplanes_len])
table.add_row(["Union Result (all)", union_result, union_result_class, union_result_class_name, union_result_id,
               union_result_len])
## (d) Print result
print(table)