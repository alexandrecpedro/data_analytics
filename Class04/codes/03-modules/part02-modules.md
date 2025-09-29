# MODULES

## 1. TYPES

| Type                                   | Description                                                             |
|----------------------------------------|-------------------------------------------------------------------------|
| *Built-in module*                      | contained within the interpreter                                        |
| Modules written in the C language      | can be dynamically loaded into Python at runtime within the interpreter |
| Modules written in the Python language | focus on this course                                                    |

## 2. MODULE FOLDERS RELATED WITH A PROGRAM

```python
import sys

# Get and display all
for item in sys.path:
  print(item)

# Add a path to all related modules from interpreter:
sys.path.append('C:/myModulePath')
```