# SET - METHODS

## 1. METHODS

| Method                      | Example                             | Definition                                                                          |
|-----------------------------|-------------------------------------|-------------------------------------------------------------------------------------|
| Set                         | S = set()                           | Create an empty set                                                                 |
| Add                         | S.add(5)                            | Add element to the set                                                              |
| Clear                       | S.clear()                           | Remove all elements                                                                 |
| Copy                        | NewSet = S.copy()                   | Create a copy from set                                                              |
| Difference                  | S.difference(set2)                  | Return a set containing the difference between two or more sets                     |
| Difference Update           | S.difference_update(set2)           | Updates the set, removing elements found in the specified sets                      |
| Discard                     | S.discard(5)                        | Removes the specified element from the set if present                               |
| Intersection                | S.intersection(set2)                | Returns a new set containing the intersection of two or more sets                   |
| Intersection Update         | S.intersection_update(set2)         | Updates the set with the intersection of its elements and the specified sets        |
| Isdisjoint                  | S.isdisjoint(set2)                  | Returns True if the two sets have no elements in common; False otherwise            |
| Issubset                    | S.issubset(set2)                    | Returns True if the set is contained within the specified set                       |
| Issuperset                  | S.issuperset(set2)                  | Returns True if the set contains all elements of the specified set                  |
| Pop                         | element = S.pop()                   | Removes and returns an arbitrary element from the set                               |
| Remove                      | S.remove(5)                         | Removes the specified element from the set                                          |
| Symmetric Difference        | S.symmetric_difference(set2)        | Returns a new set containing the symmetric difference of two sets                   |
| Symmetric Difference Update | S.symmetric_difference_update(set2) | Updates the set with the symmetric difference of its elements and the specified set |
| Union                       | S.union(set2)                       | Returns a new set with the union of the set and the specified sets                  |
| Update                      | S.update(iterable1, iterable2)      | Update the current set by adding items from another iterable                        |

*Ps1: S = any set*

## 2. APPLICATION EXAMPLES

| Case | Subject                  | Code                                                       |
|:----:|--------------------------|------------------------------------------------------------|
|  1   | New Set                  | [New Set](01-new_set.py)                                   |
|  2   | Add Elements to Set      | [Add Elements to Set](02-add_elements_to_set.py)           |
|  3   | Update Set               | [Update Set](03-update_set.py)                             |
|  4   | Remove Elements from Set | [Remove Elements from Set](04-remove_elements_from_set.py) |
|  5   | Clear Set                | [Clear Set](05-clear_set.py)                               |
|  6   | Union Set                | [Union Set](06-union_set.py)                               |
|  7   | Intersection Set         | [Intersection Set](07-intersection_set.py)                 |
|  8   | Difference Set           | [Difference Set](08-difference_set.py)                     |
|  9   | Symmetric Difference Set | [Symmetric Difference Set](09-symmetric_difference_set.py) |