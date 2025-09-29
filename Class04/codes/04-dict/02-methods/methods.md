# DICTIONARY - METHODS

## 1. METHODS

| Method       | Example                            | Definition                                                                              |
|--------------|------------------------------------|-----------------------------------------------------------------------------------------|
| Dictionary   | D = dict()                         | Create an empty dictionary                                                              |
| Add / Update | D[key] = value                     | Add or update a key-value pair in the dictionary                                        |
| Clear        | D.clear()                          | Remove all key-value pairs from the dictionary                                          |
| Copy         | NewDict = D.copy()                 | Create a shallow copy of the dictionary                                                 |
| Get          | value = D.get(key, default)        | Get the value associated with a key, or return a default value if key doesn’t exist     |
| Keys         | keys = D.keys()                    | Return a view object containing all the keys in the dictionary                          |
| Values       | values = D.values()                | Return a view object containing all the values in the dictionary                        |
| Items        | items = D.items()                  | Return a view object containing key-value pairs as tuples                               |
| Pop          | value = D.pop(key, default)        | Remove the key and return its value, or return the default if the key doesn’t exist     |
| Popitem      | key, value = D.popitem()           | Remove and return the last inserted key-value pair as a tuple                           |
| Update       | D.update(other_dict)               | Update the dictionary with key-value pairs from another dictionary or iterable of pairs |
| Setdefault   | value = D.setdefault(key, default) | Get the value of a key. If the key doesn’t exist, insert it with the default value      |
| Fromkeys     | D = dict.fromkeys(iterable, value) | Create a dictionary with keys from an iterable and all values set to a specified value  |
| Del          | del D[key]                         | Remove a key-value pair from the dictionary                                             |
| Contains     | key in D                           | Check if a key exists in the dictionary (returns `True` or `False`)                     |


*Ps1: D = any dict*

## 2. APPLICATION EXAMPLES

| Case | Subject                   | Code                                                         |
|:----:|---------------------------|--------------------------------------------------------------|
|  1   | New Dict                  | [New Dict](01-new_dict.py)                                   |
|  2   | Add Elements to Dict      | [Add Elements to Dict](02-add_elements_to_dict.py)           |
|  3   | Remove Elements from Dict | [Remove Elements from Dict](03-remove_elements_from_dict.py) |
|  4   | Change Elements from Dict | [Change Elements from Dict](04-change_elements_from_dict.py) |
|  5   | Clear Dict                | [Clear Dict](05-clear_dict.py)                               |
|  6   | Update Dict               | [Update Dict](06-update_dict.py)                             |

## 3. BIBLIOGRAPHICAL REFERENCES

- [1] [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [2] [Dictionaries in Python](https://www.geeksforgeeks.org/python-dictionary/)