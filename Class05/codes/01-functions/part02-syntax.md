# FUNCTIONS - SYNTAX

## 1. SIMPLE FUNCTION

```shell
def <function_name>():
  <code_bloc>
```

## 2. RECURSIVE

```shell
def <function_name>(pA, pB):
  if <condition>:
    return something
    
  <code_bloc_1 - define x>
  <code_bloc_2 - define y>
  R = recursive_function(x, y)
  return R
```

## 3. LAMBDA FUNCTION

### a. BASIC

```shell
lambda <args>: <expression>
```

### b. With MAP

```shell
map(<function>, <iterable>, <*iterables>)
```

### c. With FILTER

```shell
filter(<function>, <iterable>)
```