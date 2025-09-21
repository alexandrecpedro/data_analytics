from prettytable import PrettyTable

FIELD_NAMES = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)

# =========== EXERCISE 1 ===========
number = float(input("Enter a number: ").strip())
result = 'Positive number!' if number > 0 else ''
table.add_row(['EXERCISE 1', ''])
table.add_row(['Number', number])
table.add_row(['Is this number positive?', result])

# =========== EXERCISE 2 ===========
study_schedule = input("Enter a study schedule\nM - morning\nN - night\n").strip().upper()
greetings = 'Good morning!' if study_schedule == 'M' else 'Good evening!'
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 2', ''])
table.add_row(['Study Schedule', study_schedule])
table.add_row(['Greetings', greetings])

# =========== EXERCISE 3 ===========
temperature_celsius = float(input('Temperature (deg C): ').strip())
conditions = {
    "It's very hot!": lambda t: t > 30,
    "It's very cold!": lambda t: t < 10,
    "Pleasant temperature!": lambda t: 10 <= t <= 30,
}
temperature_celsius_message = next(msg for msg, cond in conditions.items() if cond(temperature_celsius))
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 3', ''])
table.add_row(['Temperature (deg C)', temperature_celsius])
table.add_row(['Message', temperature_celsius_message])

# =========== EXERCISE 4 ===========
even_odd_number = int(input('Enter an integer number: ').strip())
conditions = {
    'Even and large number!': lambda n: n % 2 == 0 and n > 10,
    'Even and small number!': lambda n: n % 2 == 0 and n <= 10,
    'Odd number!': lambda n: n % 2 != 0,
}
even_odd_message = next(msg for msg, cond in conditions.items() if cond(even_odd_number))
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 4', ''])
table.add_row(['Integer number', even_odd_number])
table.add_row(['Message', even_odd_message])

print(table)