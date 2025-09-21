import locale
from prettytable import PrettyTable

FIELD_NAMES = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)

locale.setlocale(category=locale.LC_ALL, locale='pt_BR.UTF-8')

# =========== EXERCISE 1 ===========

value_a = 15
value_b = 15
result = value_a < value_b
table.add_row(['EXERCISE 1', ''])
table.add_row([f'{value_a} < {value_b}', result])

# =========== EXERCISE 2 ===========
word_1 = "Olá"
word_2 = "olá"
word_1_equals_word_2 = (word_1 == word_2)
word_1_differs_word_2 = (word_1 != word_2)
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 2', ''])
table.add_row([f'{word_1} = {word_2}', word_1_equals_word_2])
table.add_row([f'{word_1} != {word_2}', word_1_differs_word_2])

# =========== EXERCISE 3 ===========
registered_client = True
purchase_amount = float(input('Purchase amount (R$): '))
purchase_amount_str = locale.currency(val=purchase_amount, grouping=True)
free_shipping = (purchase_amount > 200) and registered_client
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 3', ''])
table.add_row(['Registered Client', registered_client])
table.add_row(['Purchase Amount', purchase_amount_str])
table.add_row(['Free Shipping', free_shipping])

print(table)
