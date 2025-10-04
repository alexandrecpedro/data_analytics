"""
INSTRUCTION:
    Write a program that prompts the user to enter two integer numbers, A and B.
    The program should attempt to divide A by B and display the result of the
    division formatted to two decimal places

    However, the program must handle potential errors that may occur during input
    and division. Specifically, it should:

        (a) Convert the user inputs to integers
        (b) Perform the division of A by B
        (c) If an error occurs (such as entering a non-integer value or attempting
            to divide by zero), the program should catch the error and display a
            user-friendly message: "It is not possible to divide A per B!"

TEST CONDITIONS:
    | Attempt | A    | B  |
    |:-------:|------|----|
    |    1    | 20   | 0  |
    |    2    | 5o   | == |
    |    3    | text | == |
    |    4    | 18   | 4  |
"""

def main():
    print("Start of the program")
    try:
        A = int(input("Enter an integer number: "))
        B = int(input("Enter an integer number: "))
        R = A / B
        print(f"Division {A}/{B} = {R:.2f}")
    except ZeroDivisionError:
        print("Error: B cannot be zero!")
    except ValueError:
        print("Error: Please provide integer numbers for A and B!")
    except:
        print("Unknown error: It is not possible to divide A per B!")
    print("End of the program")

if __name__ == '__main__':
    main()