"""
INSTRUCTION:
    Write a programme that reads an integer Qty and creates a list with random
    integer elements within the closed interval [1,50]
    Display the generated list on the screen.

    Then, remove any values that are repeated, leaving only one occurrence of each.
    Display the new list without duplicates and its size
"""
from collections.abc import Sized
from prettytable import PrettyTable
from random import randint

table = PrettyTable()
table.field_names = ['Description', 'Value', 'Length']

print("Start of the program")
while True:
    try:
        Qty = int(input('Enter the quantity of elements: '))
        if Qty <= 50:
            break

        print("Invalid input! Please enter an integer number smaller than 51!")
    except ValueError:
        print("Invalid input! Please enter a valid integer!")

List = list()
for value in range(Qty):
    List.append(randint(1, 50))
List_len = len(List) if isinstance(List, Sized) else None
table.add_row(['Generated List', List, List_len])

List_sort = List[:]
List_sort = sorted(List_sort)
List_sort_len = len(List_sort) if isinstance(List_sort, Sized) else None
table.add_row(['Generated List (sort)', List_sort, List_sort_len])

new_set = set(List)
new_list = list()
new_list.extend(new_set)
new_list_len = len(new_list)
table.add_row(['Non repeat List', new_list, new_list_len])

new_list_sort = new_list[:]
new_list_sort = sorted(new_list_sort)
new_list_sort_len = len(new_list_sort) if isinstance(new_list_sort, Sized) else None
table.add_row(['Non repeat List (sort)', new_list_sort, new_list_sort_len])

print(table)
print('\nEnd of the program')