# EXERCISE - VARIABLES

from typing import Optional

from prettytable import PrettyTable

class Student:
    """Represents a student with grades and average."""
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, grade: float):
        """Add a grade to the student's list."""
        if grade < 0 or grade > 10:
            print("❌ Grade must be between 0 and 10.")
            return
        self.grades.append(grade)

    def remove_grade(self, index: int):
        """Remove a grade from the student's list."""
        if index < 0 or index > len(self.grades):
            print("❌ Invalid grade index.")
            return
        removed = self.grades.pop(index)
        print(f"✅ Removed grade {removed:.2f} from {self.name}.")

    @property
    def average(self) -> float:
        """Calculate and return the student's average grade."""
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

class Gradebook:
    """Manages multiple students and displays results in a table."""
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, name: str):
        student = self.find_student(name=name)
        if not student:
            print(f"❌ Student '{name}' not found.")
            return
        self.students.remove(student)
        print(f"✅ Student {name} removed successfully!")

    def find_student(self, name: str) -> Optional[Student]:
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def display_table(self):
        """Create and print a PrettyTable with all students' results."""
        table = PrettyTable(field_names=['Student', 'Grades', 'Average'])
        for student in self.students:
            table.add_row([
                student.name,
                ", ".join(f"{grade:.2f}" for grade in student.grades),
                f"{student.average:.2f}"
            ])
        print(table)

def get_grade(prompt: str) -> Optional[float]:
    """Capture a non-negative float number with exception handling."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0 or value > 10:
                print("❌ Grade must be between 0 and 10.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a valid number!")

def get_grades_qty(prompt: str) -> Optional[int]:
    """Capture a non-negative integer with exception handling."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("❌ Number must be greater than 0")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a valid number!")

def add_student_flow(gradebook: Gradebook):
    name = input("Enter student name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return

    student = Student(name=name)
    num_grades = get_grades_qty(f"How many grades does {name} have? ")

    for i in range(num_grades):
        grade = get_grade(f"Enter grade {i + 1} for {name}: ")
        student.add_grade(grade=grade)

    gradebook.add_student(student)
    print(f"✅ Student {name} added successfully!")

def remove_student_flow(gradebook: Gradebook):
    name = input("Enter student name to remove: ").strip()
    gradebook.remove_student(name=name)

def remove_grade_flow(gradebook: Gradebook):
    name = input("Enter student name to remove a grade from: ").strip()
    student = gradebook.find_student(name=name)
    if not student:
        print(f"❌ Student '{name}' not found!")
        return

    if not student.grades:
        print(f"❌ {name} has no grades!")
        return

    print(f"Grades for {name}:")
    for i, g in enumerate(student.grades, start=1):
        print(f"{i}. {g:.2f}")

    idx = input("Enter the number of the grade to remove: ").strip()
    if not idx.isdigit() or not (1 <= int(idx) <= len(student.grades)):
        print("❌ Invalid choice, try again!")
        return
    student.remove_grade(index=int(idx) - 1)

def exit_program():
    print("Exiting program... 👋")
    return True

def main():
    gradebook = Gradebook()

    menu_actions = {
        "1": lambda: add_student_flow(gradebook=gradebook),
        "2": lambda: gradebook.display_table(),
        "3": lambda: remove_student_flow(gradebook=gradebook),
        "4": lambda: remove_grade_flow(gradebook=gradebook),
        "5": lambda: exit_program
    }

    while True:
        print("\n--- MENU ---")
        print("1. Add student")
        print("2. Show all results")
        print("3. Remove a student")
        print("4. Remove a grade")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        action = menu_actions.get(choice)
        if not action:
            print("❌ Invalid option! Try again!")
            continue

        should_exit = action()
        if should_exit:
            return

if __name__ == "__main__":
    main()

