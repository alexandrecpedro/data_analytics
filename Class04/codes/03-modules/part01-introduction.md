# INTRODUCTION

## 1. GLOSSARY

| Subject   | Definition                                                                                                                                  |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Module    | single file that contains Python code and acts as a self-contained unit of code that can be imported and used in other programs or modules  |
| Package   | collection of modules organized in a directory. Allow us to group multiple related modules together under a common namespace                |
| Namespace | system that has a unique name for each and every object in Python                                                                           |
| Scope     | defines which namespaces will be searched and in what order (namespaces search order: local -> nonlocal -> global -> built-in -> NameError) |

## 2. BENEFITS

|    Advantage    | Explanation                                                                                                                                                                                                                                                         |
|:---------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maintainability | Breaking down code into modules helps us make changes in the independent parts of the overall application without affecting the whole application, since the modules are designed to only deal with one part of the application                                     |
|   Reusability   | This is a key part of software development, where we write code once and we can use it in many different parts of an application as many times as we want. This enables us to write clean and dry code                                                              |
|  Collaboration  | Modular code enhances and enables collaboration. Different teams can work on different parts of the same application at the same time without interfering with each other’s work                                                                                    |
|   Readability   | Breaking down code into modules and packages enhances code readability. We can easily tell what’s going on in a file. We might, for example, have a file named databaseConnection.py: just from the name we can tell that this file deals with database connections |