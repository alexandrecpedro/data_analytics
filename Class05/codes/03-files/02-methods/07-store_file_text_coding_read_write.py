"""
INSTRUCTIONS:
    In this exercise, we will examine how text file encoding functions in Python.
    Write a programme that writes the two lines of text below into a file.
    Then read this file and display its contents on the screen. The encodings
    we will test are ANSI and UTF-8, and they should be input from the keyboard

    Text to be written to the file
        > File Writing
        > accents: á, é, í, Á, É, Í, ç, Ç

TEXT CASES:
    | Case | Writing Code | Reading Code |
    | :--: | :----------: | :----------: |
    | 1    | ANSI         | ANSI         |
    | 2    | UTF-8        | UTF-8        |
    | 3    | UTF-8        | ANSI         |
    | 4    | ANSI         | UTF-8        |

Ps: the cases 3 and 4 can result in problems
    => pay attention to the encoding types
        - should be the same for reading and writing
"""

def writing_file_step(file: str, mode: str, encoding: str):
    print('Writing file step')
    store_file = open(file=file, mode=mode, encoding=encoding)
    store_file.write('File Writing\n')
    store_file.write('accents: á, é, í, Á, É, Í, ç, Ç')
    store_file.close()

def reading_file_step(file: str, mode: str, encoding: str):
    print('\nReading file step')
    store_file = open(file=file, mode=mode, encoding=encoding)
    for line in store_file:
        print(line.rstrip())

def main():
    print("Start of the program")
    filename = 'assets/store_file_text_coding_read_write.txt'
    reading_mode = 'r'
    writing_mode = 'w'

    writing_encoding = input('Enter the writing coding: ')
    reading_encoding = input('Enter the reading coding: ')

    writing_file_step(file=filename, mode=writing_mode, encoding=writing_encoding)
    reading_file_step(file=filename, mode=reading_mode, encoding=reading_encoding)

    print('End of the program')

if __name__ == '__main__':
    main()