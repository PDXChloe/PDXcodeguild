'''Lab 9: Make Change

Let's convert a dollar amount into a number of coins.
The input will be the total amount, the output will be the number of
quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first,
resulting in the fewest amount of coins. For this, you'll have to use floor division //,
which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered

conditionals, comparisons
arithmetic
Version 1

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Version 2

Have the user enter a dollar amount (1.36), convert this to the total in pennies.

'''
import time

print("Let's play a game called 'How Much Money Do You Have?' \n")
time.sleep(1)
print("We are gonna break down your pocket money into quarters, dimes, nickles and pennies.\n")
time.sleep(1)
print("You know, into the change that gets left in the car console and turns your purse into a personal shaker weight....\n")
time.sleep(1)
print("Super useful, right?.....\n")

money = input("How much money you got? \nPlease break it down into pennies, e.g. you have $2.36, so you enter into the computer 236.\n")

quarters = 25
dimes = 10
nickles = 5
pennies = 1

money_quarters = int(money) // int(quarters)    #finds how many quarters are in the total amount
print("You currently have in your pocket, " + str(money_quarters) + " quarters!\n")

quarter_modulus = int(money) % int(quarters)    #finds the remainder after the quarters
money_dimes = int(quarter_modulus) // int(dimes)    #finds how many dimes are in the remainder after the quarters
print("And you have, " + str(money_dimes) + " dimes!\n")

dime_modulus = int(quarter_modulus) % int(dimes)    #finds the remainder after the quarters and dimes
money_nickles = int(dime_modulus) // int(nickles)   #finds how many nickles are in the remainder after the quarters and dimes
print("As well as, " + str(money_nickles) + " nickles!\n")

nickle_modulus = int(dime_modulus) % int(nickles)   #finds the remainder after the quarters, dimes and nickles
money_pennies = int(nickle_modulus) // int(pennies) #finds how many pennies are in the rest
print("with, " + str(money_pennies) + " pennies!\n")
