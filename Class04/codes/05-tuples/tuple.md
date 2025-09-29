# TUPLE

## 1. METHODS

  | Method        | Example                        | Definition                                                            |
  |---------------|--------------------------------|-----------------------------------------------------------------------|
  | Tuple         | T = tuple()                    | Create an empty tuple                                                 |
  | Access        | element = T[index]             | Access an element by its index                                        |
  | Length        | length = len(T)                | Get the number of elements in the tuple                               |
  | Concatenation | T3 = T1 + T2                   | Combine two tuples into a new tuple                                   |
  | Repetition    | T2 = T * n                     | Repeat a tuple `n` times                                              |
  | Membership    | element in T                   | Check if an element exists in the tuple (returns `True` or `False`)   |
  | Slicing       | T_slice = T[start:end:step]    | Return a new tuple containing a slice of the original tuple           |
  | Count         | count = T.count(element)       | Return the number of times an element appears in the tuple            |
  | Index         | index = T.index(element)       | Return the first index of an element in the tuple                     |
  | Conversion    | T = tuple(iterable)            | Create a tuple from an iterable (e.g., list, set, or dictionary keys) |
  | Unpacking     | a, b, c = T                    | Assign each element of the tuple to corresponding variables           |
  | Nested Tuples | T_nested = (T1, T2)            | Create a tuple containing other tuples as elements                    |
  | Immutable     | T[0] = new_value (not allowed) | Tuples are immutable; elements cannot be modified after creation      |

*Ps1: T, T1, T2, T3, T_nested, T_slice = any tuple*

## 2. APPLICATION EXAMPLES

| Case | Subject                    | Code                                                                   |
|:----:|----------------------------|------------------------------------------------------------------------|
|  1   | New Tuple                  | [New Tuple](methods/01-new_tuple.py)                                   |
|  2   | Access Elements from Tuple | [Access Elements from Tuple](methods/02-access_elements_from_tuple.py) |
|  3   | Zip Tuple                  | [Zip Tuple](methods/03-zip_tuple.py)                                   |

## 3. BIBLIOGRAPHICAL REFERENCES

- [1] [5.3. Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [2] [Tuples in Python](https://www.geeksforgeeks.org/tuples-in-python/)