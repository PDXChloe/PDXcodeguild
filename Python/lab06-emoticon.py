'''Lab 6: Random Emoticon Generator


Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
import random

fruits = ['apple', 'banana', 'pineapple']
fruit = random.choice(fruits)
print(fruit)
Example output:

:-P
Version 2

Use a while loop to generate 5 emoticons.'''

import random

eyes = [";", ":", "="]
noses = ["<", ">", "*"]
mouths = ["|", ")", "O", "o", "P"]

name = input("hello, what is your name?\n")

print(input(name.title() + ", welcome to Emoticon Generator, where I can generate a personal emoticon based on your name. Please press Enter:\n"))

print(random.choice(eyes)+random.choice(noses)+random.choice(mouths))