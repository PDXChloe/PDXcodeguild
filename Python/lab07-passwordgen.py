'''Lab 7: Password Generator

Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Concepts Covered

input, print
looping
random.choice
the 'sting builder pattern'
Version 2

Allow the user to enter the value of n, remember to convert its type, as input returns a string.'''

import random

password_selection = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?><"
password_length = 10
my_password = ""

for i in range(password_length):
    pwd_metric = random.randrange(len(password_selection))
    my_password = my_password + password_selection[pwd_metric]

print(my_password)