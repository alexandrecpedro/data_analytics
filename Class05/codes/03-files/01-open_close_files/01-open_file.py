"""
OPEN FILE

(a) Syntax
file = open(name, mode, buffering, encoding, errors, newline, closefd, opener)

where:
    -> name: file name
    -> mode: optional parameter; showed below

    | Group | Character | Meaning                                                                  |
    | :---: | :-------: | :----------------------------------------------------------------------: |
    | G1    | r         | Open for reading (default)                                               |
    | G1    | w         | Open for writing, removing all content (no confirm action)               |
    | G1    | x         | Open for exclusive generation. If file already exists, throw an error    |
    | G1    | a         | Open for writing. If something already exists, insert content at the end |
    | ===== | ========= | ======================================================================== |
    | G2    | b         | Open file in binary mode                                                 |
    | G2    | t         | Open file in text mode (default)                                         |
    | ===== | ========= | ======================================================================== |
    | ===== | +         | Open for updating. Allows simultaneous reading and writing               |

    -> encoding: 'ANSI', 'UTF-8' (common for latin languages)

(b) Documentation
Link: https://docs.python.org/3/library/pathlib.html#reading-and-writing-files
"""