from prettytable import PrettyTable

FIELD_NAMES = ['Description', 'Value']
table = PrettyTable(field_names=FIELD_NAMES)

# 1. IF
grade_1 = float(input("Grade 1: "))
grade_2 = float(input("Grade 2: "))
table.add_row(['Grade 1', grade_1])
table.add_row(['Grade 2', grade_2])

average = (grade_1 + grade_2)/2
table.add_row(['Average', average])

## 1.1. SIMPLE IF
situation_simple_if = ''
if average >= 7:
    situation_simple_if = 'Approved'
table.add_row(['==========', '=========='])
table.add_row(['SIMPLE IF', ''])
table.add_row(['Situation', situation_simple_if])

## 1.2. IF-ELSE
situation_if_else = 'Approved' if average >= 7 else 'Failed'
table.add_row(['==========', '=========='])
table.add_row(['IF-ELSE', ''])
table.add_row(['Situation', situation_if_else])

## 1.3. IF-ELSE-IF
situation_if_else_if = 'Failed'
if average >= 7:
    situation_if_else_if = 'Approved'
    study_year = int(input("Study Year: "))
    if study_year == 3:
        situation_simple_if = 'Diplomado'

table.add_row(['==========', '=========='])
table.add_row(['IF-ELSE-IF', ''])
table.add_row(['Situation', situation_if_else_if])

print(table)
