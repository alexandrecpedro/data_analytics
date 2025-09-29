# DICTIONARY - DEFINITION

## 1. CONCEPT

Dictionaries are used to store data values in key:value pairs

### (a) Dictionary Items

Dictionary items are ordered, changeable, and do not allow duplicates
Dictionary items are presented in key:value pairs, and can be referred to by using the key name

#### i. Ordered

When we say that dictionaries are ordered, it means that the items have a defined order, 
and that order will not change

#### ii. Changeable

Dictionaries are changeable, meaning that we can change, add or remove items 
after the dictionary has been created

#### iii. Duplicates Not Allowed

Dictionaries cannot have two items with the same key

E.g.:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) # result: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
```

## 2. APPLICATION EXAMPLES

| Case | Subject    | Code                                  |
|:----:|------------|---------------------------------------|
|  1   | Definition | [Definition](01-dictionary_object.py) |