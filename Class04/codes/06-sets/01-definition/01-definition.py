from prettytable import PrettyTable

# 1. SET OBJECT
## (a) Homogeneous Set
homogeneous_set = {"google", "microsoft", "apple"}
homogeneous_set_class = type(homogeneous_set)
homogeneous_set_class_name = homogeneous_set_class.__name__
homogeneous_set_id = id(homogeneous_set)
homogeneous_set_len = len(homogeneous_set)

## (b) Heterogeneous Set
heterogeneous_set = {"upGrad", True, "Python", frozenset({None: "sun"}) , "ML", 23432}
heterogeneous_set_class = type(heterogeneous_set)
heterogeneous_set_class_name = heterogeneous_set_class.__name__
heterogeneous_set_id = id(heterogeneous_set)
heterogeneous_set_len = len(heterogeneous_set)

# 2. TABLE
## (a) Create Table
table = PrettyTable()

## (b) Add header
table.field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]

## (c) Add data to table
table.add_row(["Homogeneous Set", homogeneous_set, homogeneous_set_class, homogeneous_set_class_name, homogeneous_set_id, homogeneous_set_len])
table.add_row(["Heterogeneous Set", heterogeneous_set, heterogeneous_set_class, heterogeneous_set_class_name, heterogeneous_set_id, heterogeneous_set_len])

## (d) Print result
print(table)