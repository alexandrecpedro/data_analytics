from prettytable import PrettyTable

FIELD_NAMES = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)

number = int(input('Enter the times table number: '))
start = 10
end = 1
while start <= end:
    result = number * start
    table.add_row([f'{number} x {start:02}', result])
    start -= 1
print(table)