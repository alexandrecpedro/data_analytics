from collections.abc import Collection

from prettytable import PrettyTable

"""
FUNCTION DIFFERENCE 
    Computes the difference of two sets and returns items that are unique to the first set

    Syntax: <set_1>.difference(<set_2>)
    Other syntax: <set_1> - <set_2>

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

### ii. FIFA Teams World Cup
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

# 2. SET - DIFFERENCE
## (a) Difference Of Sets
### i. Soccer Teams - FIFA Teams Cup
result_soccer_fifa_teams_cup = soccer_teams.difference(fifa_teams_cup)
# OR soccer_teams - fifa_teams_cup
result_soccer_fifa_teams_cup_class = type(result_soccer_fifa_teams_cup)
result_soccer_fifa_teams_cup_class_name = result_soccer_fifa_teams_cup_class.__name__
result_soccer_fifa_teams_cup_id = id(result_soccer_fifa_teams_cup)
result_soccer_fifa_teams_cup_len = (len(result_soccer_fifa_teams_cup)
                                    if isinstance(result_soccer_fifa_teams_cup, Collection)
                                    else None)

### ii. FIFA Teams Cup - Soccer Teams
result_fifa_teams_cup_soccer = fifa_teams_cup - soccer_teams
# OR fifa_teams_cup.difference(soccer_teams)
result_fifa_teams_cup_soccer_class = type(result_fifa_teams_cup_soccer)
result_fifa_teams_cup_soccer_class_name = result_fifa_teams_cup_soccer_class.__name__
result_fifa_teams_cup_soccer_id = id(result_fifa_teams_cup_soccer)
result_fifa_teams_cup_soccer_len = (len(result_fifa_teams_cup_soccer)
                                    if isinstance(result_fifa_teams_cup_soccer, Collection)
                                    # if result_fifa_teams_cup_soccer is not None and
                                    #    not isinstance(result_fifa_teams_cup_soccer, (int, float, complex, bool))
                                    else None)

# 3. TABLE
## (a) Create Table
table = PrettyTable()
## (b) Add header
table.field_names = table_field_names
## (c) Add data to table
table.add_row(
    ["Soccer Teams", soccer_teams, soccer_teams_class, soccer_teams_class_name, soccer_teams_id, soccer_teams_len])
table.add_row(["FIFA Teams Cup", fifa_teams_cup, fifa_teams_cup_class, fifa_teams_cup_class_name, fifa_teams_cup_id,
               fifa_teams_cup_len])
table.add_row(
    ["Differences (Soccer and FIFA Teams Cup)", result_soccer_fifa_teams_cup, result_soccer_fifa_teams_cup_class,
     result_soccer_fifa_teams_cup_class_name, result_soccer_fifa_teams_cup_id, result_soccer_fifa_teams_cup_len])
table.add_row(
    ["Differences (FIFA Teams Cup and Soccer)", result_fifa_teams_cup_soccer, result_fifa_teams_cup_soccer_class,
     result_fifa_teams_cup_soccer_class_name, result_fifa_teams_cup_soccer_id, result_fifa_teams_cup_soccer_len])
## (d) Print result
print(table)