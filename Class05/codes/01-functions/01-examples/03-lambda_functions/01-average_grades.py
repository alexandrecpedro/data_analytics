from prettytable import PrettyTable

# 1. CONSTANTS
FORMAT_SPEC_DOT_2f = '.2f'
TABLE_FIELD_NAMES = ['Case', 'Grades', 'Average']
VALUE_NEGATIVE_EXCEPTION = 'Error: Please enter a non-negative value!'
VALUE_VALID_EXCEPTION = 'Error: Please enter a valid value!'

# 2. FUNCTION
def get_number_grades() -> int | None:
    """
    Reads a number from user input and validates it as an integer
    :return: A valid integer number entered by the user
    """
    while True:
        try:
            num_grades = int(input("Enter the number of grades (or 0 to exit): "))
            if num_grades < 0:
                print(VALUE_NEGATIVE_EXCEPTION)
                continue
            return num_grades
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

def get_grade() -> float | None:
    """
    Reads a number from user input and validates it as a float
    :return: A valid floating-point number entered by the user
    """
    while True:
        try:
            grade = float(input("Enter the student's grade: "))
            if grade < 0:
                print(VALUE_NEGATIVE_EXCEPTION)
                continue
            return grade
        except ValueError:
            print(VALUE_VALID_EXCEPTION)

average = lambda grades: sum(grades)/len(grades) if grades else 0.0
convert_format = lambda number, format_spec: f'{number:{format_spec}}'

def generate_table(table_field_names: list[str]) -> PrettyTable:
    """
    Generates a table to display the results
    :param table_field_names: Field names for the table
    :return: A formatted table
    """
    table = PrettyTable()
    table.field_names = table_field_names
    return table

# 3. MAIN PROGRAM
print("Start of the program")
table = generate_table(table_field_names=TABLE_FIELD_NAMES)
case_num = 1

while True:
    number_grades = get_number_grades()
    if number_grades == 0:
        break

    grades_list = list()
    for _ in range(number_grades):
        grade = get_grade()
        grades_list.append(grade)

    average_grade = average(grades=grades_list)
    average_grade_display = convert_format(number=average_grade, format_spec=FORMAT_SPEC_DOT_2f)
    grades_display = ', '.join(
        convert_format(number=grade, format_spec=FORMAT_SPEC_DOT_2f)
        for grade in grades_list)

    table.add_row([case_num, grades_display, average_grade])

    continue_input = input('Do you want to continue entering grades?\n0 - No\n1 - Yes\n').strip()
    if continue_input != '1':
        break
    case_num += 1

print(table)
print('End of the program')