from collections.abc import Collection

from prettytable import PrettyTable

"""
FUNCTION INTERSECTION 
    Returns a new set with elements that are common to all sets
    If the argument is not passed to intersection(), it returns a shallow copy of the first set

    Syntax: <set_1>.intersection(*other_sets)
    Other syntax: <set_1> & <set_2> & ...

    Ps: * means that the method can take 0 or more arguments
"""

# 1. SETS
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) Sets
### i. Soccer Teams
soccer_teams = {'Corinthians', 'Real Madrid', 'Manchester City', 'Flamengo', 'Inter Miami', 'Palmeiras',
                'Atlético-MG', 'Barcelona', 'Vasco', 'Borussia Dortmund', 'Cruzeiro'}
soccer_teams_class = type(soccer_teams)
soccer_teams_class_name = soccer_teams_class.__name__
soccer_teams_id = id(soccer_teams)
soccer_teams_len = (len(soccer_teams)
                    if isinstance(soccer_teams, Collection)
                    else None)

### ii. Brazilian Cup
brazilian_cup = {'Flamengo', 'Atlético-MG', 'Corinthians', 'Vasco'}
brazilian_cup_class = type(brazilian_cup)
brazilian_cup_class_name = brazilian_cup_class.__name__
brazilian_cup_id = id(brazilian_cup)
brazilian_cup_len = (len(brazilian_cup)
                     if isinstance(brazilian_cup, Collection)
                     else None)

### iii. FIFA Teams World Cup
fifa_teams_cup = {'Real Madrid', 'Manchester City', 'Flamengo', 'Inter Miami', 'Palmeiras',
                  'Barcelona'}
fifa_teams_cup_class = type(fifa_teams_cup)
fifa_teams_cup_class_name = fifa_teams_cup_class.__name__
fifa_teams_cup_id = id(fifa_teams_cup)
fifa_teams_cup_len = (len(fifa_teams_cup)
                      if isinstance(fifa_teams_cup, Collection)
                      # if fifa_teams_cup is not None and
                      #    not isinstance(fifa_teams_cup, (int, float, complex, bool))
                      else None)

# 2. SET - INTERSECTION
## (a) Union Of Sets
### i. Individual
result_soccer_brazilian = soccer_teams.intersection(brazilian_cup)  # OR soccer_teams & brazilian_cup
result_soccer_brazilian_class = type(result_soccer_brazilian)
result_soccer_brazilian_class_name = result_soccer_brazilian_class.__name__
result_soccer_brazilian_id = id(result_soccer_brazilian)
result_soccer_brazilian_len = (len(result_soccer_brazilian)
                               if isinstance(result_soccer_brazilian, Collection)
                               else None)

result_soccer_fifa_teams_cup = soccer_teams & fifa_teams_cup  # OR soccer_teams.intersection(fifa_teams_cup)

### ii. Intersection of many
# intersection_result = soccer_teams.intersection(brazilian_cup, fifa_teams_cup)
intersection_result = soccer_teams & brazilian_cup & fifa_teams_cup
intersection_result_class = type(intersection_result)
intersection_result_class_name = intersection_result_class.__name__
intersection_result_id = id(intersection_result)
intersection_result_len = (len(intersection_result)
                           if isinstance(intersection_result, Collection)
                           # if intersection_result is not None and
                           #    not isinstance(intersection_result, (int, float, complex, bool))
                           else None)

# 3. TABLE
## (a) Create Table
table = PrettyTable()
## (b) Add header
table.field_names = table_field_names
## (c) Add data to table
table.add_row(
    ["Soccer Teams", soccer_teams, soccer_teams_class, soccer_teams_class_name, soccer_teams_id, soccer_teams_len])
table.add_row(["Brazilian Cup", brazilian_cup, brazilian_cup_class, brazilian_cup_class_name, brazilian_cup_id,
               brazilian_cup_len])
table.add_row(["FIFA Teams Cup", fifa_teams_cup, fifa_teams_cup_class, fifa_teams_cup_class_name, fifa_teams_cup_id,
               fifa_teams_cup_len])
table.add_row(["Intersection (Soccer and Brazilian Cup)", result_soccer_brazilian, result_soccer_brazilian_class,
               result_soccer_brazilian_class_name, result_soccer_brazilian_id, result_soccer_brazilian_len])
table.add_row(
    ["Intersection Result (all)", intersection_result, intersection_result_class, intersection_result_class_name,
     intersection_result_id, intersection_result_len])
## (d) Print result
print(table)