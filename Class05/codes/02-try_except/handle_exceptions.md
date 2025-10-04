# HANDLE EXCEPTIONS

## 1. SYNTAX

### i. Simple Syntax

```plaintext
try:
    <protected code_bloc>
except:
    <handle_exception_bloc>
```

### ii. Specified exceptions

```plaintext
try:
    <protected code_bloc>
except <except_type_1>:
    <handle_exception_bloc_1>
except <except_type_2>:
    <handle_exception_bloc_2>
...
except:
    <handle_exception_bloc_n>
```

### iii. Complete Mode

```plaintext
try:
    <code_bloc_1>
except <except_type_1>:
    <code_bloc_2>
except <except_type_2>:
    <code_bloc_3>
...
except:
    <code_bloc_n>
else:
    <code_bloc_n+1>
finally:
    <code_bloc_n+2>
```

## 2. APPLICATION EXAMPLES

| Case | Subject                | Title                  | Code                                                   |
|:----:|------------------------|------------------------|--------------------------------------------------------|
|  01  | Simple Try-Except      | Simple Try-Except      | [Simple Try-Except](01-simple_try_except.py)           |
|  02  | Specified Except Types | Specified Except Types | [Specified Except Types](02-specified_except_types.py) |

## 3. BIBLIOGRAPHICAL REFERENCES

- [1] [8. Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [2] [Python Exception Handling](https://www.geeksforgeeks.org/python-exception-handling/)