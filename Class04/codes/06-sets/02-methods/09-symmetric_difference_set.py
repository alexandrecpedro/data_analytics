from collections.abc import Collection

from prettytable import PrettyTable

"""
FUNCTION SYMMETRIC DIFFERENCE 
    Returns all the items present in given sets, except the items in their intersections

    Syntax: <set_1>.symmetric_difference(<set_2>).symmetric_difference(<set_3>) ...
    Other syntax: <set_1> ^ <set_2> ^ <set_3> ^ ...

    Ps: * means that the method can take 0 or more arguments
"""

# 1. SETS
table_field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (a) Sets
### i. Soccer Teams
soccer_teams = {'Corinthians', 'Real Madrid', 'Manchester City', 'Inter Miami', 'Palmeiras',
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

# 2. SET - SYMMETRIC DIFFERENCE
## (a) Symmetric Difference Of Sets
### i. Soccer Teams - FIFA Teams Cup
result_soccer_fifa_teams_symm = soccer_teams.symmetric_difference(fifa_teams_cup)
# OR soccer_teams ^ fifa_teams_cup
result_soccer_fifa_teams_symm_class = type(result_soccer_fifa_teams_symm)
result_soccer_fifa_teams_symm_class_name = result_soccer_fifa_teams_symm_class.__name__
result_soccer_fifa_teams_symm_id = id(result_soccer_fifa_teams_symm)
result_soccer_fifa_teams_symm_len = (len(result_soccer_fifa_teams_symm)
                                     if isinstance(result_soccer_fifa_teams_symm, Collection)
                                     else None)

### ii. FIFA Teams symm - Soccer Teams
result_fifa_brazilian_symm = fifa_teams_cup ^ brazilian_cup
# OR fifa_teams_cup.symmetric_difference(brazilian_cup)
result_fifa_brazilian_symm_class = type(result_fifa_brazilian_symm)
result_fifa_brazilian_symm_class_name = result_fifa_brazilian_symm_class.__name__
result_fifa_brazilian_symm_id = id(result_fifa_brazilian_symm)
result_fifa_brazilian_symm_len = (len(result_fifa_brazilian_symm)
                                  if isinstance(result_fifa_brazilian_symm, Collection)
                                  # if result_fifa_brazilian_symm is not None and
                                  #    not isinstance(result_fifa_brazilian_symm, (int, float, complex, bool))
                                  else None)

## (b) Symmetric diff of many sets
result_all_symm = soccer_teams ^ brazilian_cup ^ fifa_teams_cup
# OR soccer_teams.symmetric_difference(brazilian_cup).symmetric_difference(fifa_teams_cup)
result_all_symm_class = type(result_all_symm)
result_all_symm_class_name = result_all_symm_class.__name__
result_all_symm_id = id(result_all_symm)
result_all_symm_len = (len(result_all_symm)
                       if isinstance(result_all_symm, Collection)
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
table.add_row(
    ["Symmetric Diff (Soccer and FIFA Teams Cup)", result_soccer_fifa_teams_symm, result_soccer_fifa_teams_symm_class,
     result_soccer_fifa_teams_symm_class_name, result_soccer_fifa_teams_symm_id, result_soccer_fifa_teams_symm_len])
table.add_row(
    ["Symmetric Diff (FIFA Teams Cup and Soccer)", result_fifa_brazilian_symm, result_fifa_brazilian_symm_class,
     result_fifa_brazilian_symm_class_name, result_fifa_brazilian_symm_id, result_fifa_brazilian_symm_len])
table.add_row(
    ["Symmetric Diff (all)", result_all_symm, result_all_symm_class, result_all_symm_class_name, result_all_symm_id,
     result_all_symm_len])
## (d) Print result
print(table)