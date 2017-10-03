"""
Lab 4: Grading

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Concepts Covered

input, print
type conversion (str to int)
comparisons (< <= > >=)
if, elif, else
Instructions

Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
Numeric Ranges

90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
"""


grade = input("What is your number grade?")
print(input(grade + "is, this correct?"))

if int(grade) >= 90:
    print("You got an A!")

elif int(grade) <= 89 and int(grade) >= 80:
    print("You got a B!")

elif int(grade) <= 79 and int(grade) >= 70:
    print("You got a C.")

elif int(grade) <= 69 and int(grade) >= 60:
    print("You got a D.")

else:
    print("Ummm yeah, you flunked...")






