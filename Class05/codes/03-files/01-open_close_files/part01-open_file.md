# OPEN FILE

## 1. SYNTAX

```shell
file = open(name, mode, buffering, encoding, errors, newline, closefd, opener)
```

Ps1: references [1] and [2]

## 2. PARAMETERS

### a. NAME

Includes path if the file is not at the current directory

### b. MODE

Optional parameter. Showed below

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

### c. BUFFERING

Buffering is an optional integer used to set the buffering policy

### d. ENCODING

- Encoding is the name of the encoding used to decode or encode the file
- This should only be used in text mode

    > 'ANSI', 'UTF-8' (common for latin languages)

Ps2: reference [3]

### e. ERRORS

Errors is an optional string that specifies how encoding errors are to be handled
  > this argument should not be used in binary mode

  ================== ===============================================================
  Error              Description
  ------------------ --------------------------------------------------------------
  'strict'           raise a ValueError exception if there is an encoding error
                     (the default of None has the same effect)
  'ignore'           Ignore the malformed data and continue without further notice
                     (Note that ignoring encoding errors can lead to data loss.)
  'replace'          Replace with a replacement marker
  'backslashreplace' Replace with backslashed escape sequences (\xhh \uxxxx \Uxxxxxxxx)
  'surrogateescape'  On decoding, replace byte with individual surrogate code ranging 
                     from U+DC80 to U+DCFF
  ================== ===============================================================

Ps3: reference [4]

### f. NEWLINE

- Newline controls how universal newlines works (it only applies to text mode)
  > It can be None, '', '\n', '\r', and '\r\n'

### g. CLOSEFD

If closefd is False, the underlying file descriptor will be kept open
when the file is closed. This does not work when a file name is given 
and must be True in that case

### h. OPENER

A custom opener used for low-level I/O operations

## 3. BIBLIOGRAPHICAL REFERENCES

- [1] [Reading and writing files](https://docs.python.org/3/library/pathlib.html#reading-and-writing-files)
- [2] [Python open() Function](https://www.geeksforgeeks.org/python-open-function/)
- [3] [Standard Encodings](https://docs.python.org/3/library/codecs.html#standard-encodings)
- [4] [Codec Base Classes](https://docs.python.org/3/library/codecs.html#codec-base-classes)