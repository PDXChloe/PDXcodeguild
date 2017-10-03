'''Lab 5: Magic 8-Ball

Let's write a program to simulate the classic "Magic Eight Ball"

Instructions

Print a welcome screen to the user.
Use the random module's random.choice() to choose a prediction.
Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
Display the result of the 8-ball.
Below are some example 'predictions':

It is certain
It is decidedly so
Without a doubt
Yes definitely
You may rely on it
As I see it, yes
Most likely
Outlook good
Yes
Signs point to yes
Reply hazy try again
Ask again later
Better not tell you now
Cannot predict now
Concentrate and ask again
Don't count on it
My reply is no
My sources say no
Outlook not so good
Very doubtful
Version 2

Using a while loop, keep asking the user for a question, if they enter 'done', exit

Concepts Covered

input, print
import
random.choice
'''

import random
import time

answers = ["Mission Impossible", "I don't think so!", "Yeah, Not gonna happen", "In your dreams", "Nope", "Nada", "I wish I knew the answer",
           "In another life, this could be a possibility for you", "I just don't see it happening for you, maybe for your friend",
           "One day but, not today", "Could you look up the possibility?", "Google it, cuz I don't have a flippin clue!"]

print("Welcome to Magic 8 Ball, where all your answers to all your life questions are!\n")
time.sleep(1)
print("Think really hard about your life.....\n")
time.sleep(1)
print("Your dreams, your hopes, your desires.....\n")
time.sleep(2)
print("Now\n")
time.sleep(2)
print("This is your chance to ask a true mystic your deepest darkest questions about your future.\n")



question = input("Ask me any question about your future, and I will give you my most honest answer...\n")
print("Now let me dig deep into my energy and...")
time.sleep(1)
print("the answer is.....")
time.sleep(2)
print(random.choice(answers))





