from prettytable import PrettyTable

FIELD_NAMES = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)

# =========== EXERCISE 1 ===========
table.add_row(['EXERCISE 1', ''])
start = 1
end = 7
while start <= end:
    table.add_row([f'Number {start}', start])
    start += 1

# =========== EXERCISE 2 ===========
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 2', ''])
start = 5
stop = 0
step = -1
number = 1
for start in range(start, stop, step):
    table.add_row([f'Number {number}', start])
    number += 1

# =========== EXERCISE 3 ===========
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 3', ''])
number = int(input('Enter the times table number: '))
start = 1
end = 10
while start <= end:
    result = number * start
    table.add_row([f'{number} x {start:02}', f'{result:02}'])
    start += 1

# =========== EXERCISE 4 ===========
table.add_row(['=========', '========='])
table.add_row(['EXERCISE 4', ''])
sum_numbers = 0
repetition = 1
while True:
    number = int(input('Enter a number: '))
    if number == 0:
        break
    table.add_row([f'Number {repetition}', number])
    repetition += 1
    sum_numbers += number

table.add_row(['Sum of numbers', sum_numbers])
print(table)