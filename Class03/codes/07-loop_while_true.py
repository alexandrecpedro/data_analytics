import locale
from prettytable import PrettyTable

locale.setlocale(category=locale.LC_ALL, locale='pt_BR.UTF-8')

FIELD_NAMES = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)

bank_slip_sum = 0
bank_slip_number = 0

while True:
    bank_slip = float(input('Bank slip value: '))
    if bank_slip == 0:
        break
    bank_slip_number += 1

    bank_slip_str = locale.currency(val=bank_slip, grouping=True)
    table.add_row([f'Bank Slip {bank_slip_number}', bank_slip_str])
    bank_slip_sum += bank_slip

bank_slip_sum_str = locale.currency(val=bank_slip_sum, grouping=True)
table.add_row(['=========', '========='])
table.add_row(['Expenses', bank_slip_sum_str])
print(table)