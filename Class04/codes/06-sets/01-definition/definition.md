# SET - DEFINITION

## 1. CONCEPT

Sets are used to store multiple items in a single variable

### (a) Set Items

Set items are unordered, unchangeable, and do not allow duplicate values

#### i. Unordered

Unordered means that the items in a set do not have a defined order
Set items can appear in a different order every time you use them, 
    and cannot be referred to by index or key

#### ii. Unchangeable

Set items are unchangeable, meaning that we cannot change the items after the set has been created

*Ps: Once a set is created, you cannot change its items, but you can remove items and add new items*

#### iii. Duplicates Not Allowed

Sets cannot have two items with the same value

Duplicate values will be ignored:
    thisset = set({"apple", "banana", "cherry", "apple"})
    print(thisset) -> {"apple", "banana", "cherry"}

*Ps1: The values True and 1 are considered the same value*
*Ps2: The values False and 0 are considered the same value*

## 2. APPLICATION EXAMPLES

| Case | Subject    | Code                           |
|:----:|------------|--------------------------------|
|  1   | Definition | [Definition](01-definition.py) |