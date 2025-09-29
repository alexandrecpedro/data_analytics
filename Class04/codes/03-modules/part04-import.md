# IMPORT COMMAND

## 1. MODULES IN THE SAME PACKAGE

| Form                      | Syntax                                                      |
|---------------------------|-------------------------------------------------------------|
| Single                    | import <module_name>                                        |
| Many                      | import <module1>, <module2> ... <moduleN>                   |
| Using alias               | import <module> as <alias_name>                             |
| Some elements inside it   | from <module> import <element1>, <element2>, ... <elementN> |
| Include all elements      | from <module> import *                                      |
| Import element with alias | from <module> import <element> as <alias_name>              |

## 2. MODULES IN DIFFERENT PACKAGES

| Form                      | Syntax                                                                |
|---------------------------|-----------------------------------------------------------------------|
| Single                    | import <package>.<module>                                             |
| Using alias               | import <package>.<module> as <alias_name>                             |
| Some elements inside it   | from <package>.<module> import <element1>, <element2>, ... <elementN> |
| Include all elements      | from <package>.<module> import *                                      |
| Import element with alias | from <package>.<module> import <element> as <alias_name>              |