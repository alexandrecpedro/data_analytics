from prettytable import PrettyTable

# ========== EXERCISE 1 - ALPHABET ==========

## (1.1) ALPHABET LIST
alphabet = list(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
alphabet_class = type(alphabet)
alphabet_class_name = alphabet_class.__name__
alphabet_id = id(alphabet)
alphabet_len = len(alphabet)

## (1.2) GET ALL ITEMS BETWEEN 2 POSITIONS (EXCLUDE END POSITION)
start_position = 2
end_position = 5
alphabet_pos2_pos5 = alphabet[start_position:end_position]
alphabet_pos2_pos5_class = type(alphabet_pos2_pos5)
alphabet_pos2_pos5_class_name = alphabet_pos2_pos5_class.__name__
alphabet_pos2_pos5_id = id(alphabet_pos2_pos5)
alphabet_pos2_pos5_len = len(alphabet_pos2_pos5)

# ========== EXERCISE 2 - ALPHABET ==========

## (2.1) NUMBERS LIST
numbers = list([3,6,9,12,15])
numbers_class = type(numbers)
numbers_class_name = numbers_class.__name__
numbers_id = id(numbers)
numbers_len = len(numbers)

## (2.2) ODD NUMBERS
step = 2
odd_numbers_step2 = numbers[::step]
odd_numbers_step2_class = type(odd_numbers_step2)
odd_numbers_step2_class_name = odd_numbers_step2_class.__name__
odd_numbers_step2_id = id(odd_numbers_step2)
odd_numbers_step2_len = len(odd_numbers_step2)

## (2.3) INVERSE ORDER
step = -1
inverse_list_numbers = numbers[::step]
inverse_list_numbers_class = type(inverse_list_numbers)
inverse_list_numbers_class_name = inverse_list_numbers_class.__name__
inverse_list_numbers_id = id(inverse_list_numbers)
inverse_list_numbers_len = len(inverse_list_numbers)

# ========== DISPLAY THE RESULTS ==========
FIELD_NAMES = ['Description', 'Value', 'Object class', 'Object class name', 'ID (Object)', 'Length (Object)']
table = PrettyTable(field_names=FIELD_NAMES)
table.add_rows([
    ['EXERCISE 1', '', '', '', '', ''],
    ['Alphabet', alphabet, alphabet_class, alphabet_class_name, alphabet_id, alphabet_len],
    ['Sliced Alphabet', alphabet_pos2_pos5, alphabet_pos2_pos5_class, alphabet_pos2_pos5_class_name,
     alphabet_pos2_pos5_id, alphabet_pos2_pos5_len],
    ['========', '========', '========', '========', '========', '========'],
    ['EXERCISE 2', '', '', '', '', ''],
    ['Numbers', numbers, numbers_class, numbers_class_name, numbers_id, numbers_len],
    ['Odd numbers', odd_numbers_step2, odd_numbers_step2_class, odd_numbers_step2_class_name, odd_numbers_step2_id,
     odd_numbers_step2_len],
    ['Inverse list - numbers', inverse_list_numbers, inverse_list_numbers_class, inverse_list_numbers_class_name,
     inverse_list_numbers_id, inverse_list_numbers_len]
])
print(table)