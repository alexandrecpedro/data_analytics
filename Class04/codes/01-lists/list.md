# LIST

## 1. DEFINITION

Lists are used to store multiple items in a single variable

### (a) List Items

List items are ordered, changeable, and allow duplicate values
List items are indexed, the first item has index [0], the second item has index [1] etc

### (b) Ordered

When we say that lists are ordered, it means that the items have a defined order, and that order will not change
If you add new items to a list, the new items will be placed at the end of the list

### (c) Changeable

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created

### (d) Allow Duplicates

Since lists are indexed, lists can have items with the same value

Lists allow duplicate values:
    this_list = ["apple", "banana", "cherry", "apple", "cherry"]

## 2. METHODS

    | Method  | Example               | Definition                                                                    |
    |---------|-----------------------|-------------------------------------------------------------------------------|
    | List    | L = [] or L = list()  | Create an empty list                                                          |
    | Append  | L.append(5)           | Add element to in the end                                                     |
    | Clear   | L.clear()             | Remove all elements                                                           |
    | Copy*   | NewList = L.copy()    | Create a copy from list                                                       |
    | Count   | Qty = L.count(5)      | Return the number of times a given object appears in the list                 |
    | Extend  | L.extend(OtherList)   | Add objects from other list to current one                                    |
    | Index   | position = L.index(5) | Return the first index of a given object in the list                          |
    | Insert  | L.insert(2, 30)       | Insert an object at a given position                                          |
    | Pop     | L.pop(0)              | Return an item at a given position and remove it                              |
    | Remove  | L.remove(5)           | Remove from the list the fist object with the given value                     |
    | Reverse | L.reverse()           | Invert the object positions in the list                                       |
    | Slice   | Dest = Origin[1:5:2]  | Create a copy from list, from start (1), stop(5, without include) and step(2) |
    | Sort    | L.sort(reverse=False) | Order the objects in the list (ASC order)                                     |
    | Sort    | L.sort(reverse=True)  | Order the objects in the list (DESC order)                                    |

*Ps1: L = any list*
*Ps2: slice is an alternative from copy*

## 3. APPLICATION EXAMPLES

| Case | Subject                                       | Code                                                                                         |
|:----:|-----------------------------------------------|----------------------------------------------------------------------------------------------|
|  1   | New List                                      | [New List](01-new_list.py)                                                                   |
|  2   | Add Elements to List                          | [Add Elements to List](02-add_elements_to_list.py)                                           |
|  3   | Remove Elements from List                     | [Remove Elements from List](03-remove_elements_from_list.py)                                 |
|  4   | Change Elements from List                     | [Change Elements from List](04-change_elements_from_list.py)                                 |
|  5   | Slicing List                                  | [Slicing List](05-slicing_list.py)                                                           |
|  6   | Count List                                    | [Count List](06-count.py)                                                                    |
|  7   | Concat List (Plus Symbol)                     | [Concat List (Plus Symbol)](07-concat_list_plus_symbol.py)                                   |
|  8   | Copy Sub-elements from List (Multiply Symbol) | [Copy Sub-elements from List (Multiply Symbol)](08-copy_subelements_list_multiply_symbol.py) |

## 4. BIBLIOGRAPHICAL REFERENCES

- [1] [5. Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [2] [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [3] [Python Lists](https://www.geeksforgeeks.org/python-lists/)