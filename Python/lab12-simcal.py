'''
Lab 12: Simple Calculator

Write a program that asks the user for an operator and each operand.
Don't forget that input returns a string, which you can convert to a
float using float(user_input) where user_input is the string you got from input.
Below is some sample input/output.

> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17
Version 2

Allow the user to keep performing operations until they say 'done'.
Use while True and break. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!
'''




operation = input("What is the operation you would like to perform?  \n")
first_num = input("What is the first number?  \n")
second_num = input("What is the second number?  \n")


user_input = first_num + operation + second_num
print(eval(user_input)) #eval takes the string of user_input and EVAL's it so it can perform the math.


#version 2

#????