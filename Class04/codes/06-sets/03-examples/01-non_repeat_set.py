"""
INSTRUCTION:
    Write a programme that reads an integer Qty and creates a set with random
    integer elements within the closed interval [1,50]
    Display the generated set on the screen.

    Remember that sets cannot contain duplicate elements,
    so generating random numbers may pose a problem. How can this be resolved?

CAUTION: This programme has the potential to enter an infinite loop
    if the value provided for Qty is greater than 50. Avoid it
"""
from random import randint

print("Start of the program")
while True:
    try:
        Qty = int(input('Enter the quantity of elements: '))
        if Qty <= 50:
            break

        print("Invalid input! Please enter an integer number smaller than 51!")
    except ValueError:
        print("Invalid input! Please enter a valid integer!")


set_object = set()
while len(set_object) < Qty:
    set_object.add(randint(1, 50))
print(f'Set => {set_object}')
print('End of the program')