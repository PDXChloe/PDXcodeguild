
"""Search the interwebs for an example Mad Lib
Create a new file and save it as lab03-madlib.py
Ask the user for each word you'll put in your Mad Lib
Use string concatenation to put each word into the Mad Lib
"""

username = input("Hello, what is your name? >>> \n")


reply = "Hello, " + username + ", we are going to do a madlib together. I need your help, please answer the following few questions.>>>\n"
print(reply)

one = input("Give me a Place. >>>>\n")
print(one)

two = input("Give me an object you could buy. >>>>>\n")
print(two)
three = input("Give me another object you could buy. >>>>.\n")
print(three)
four = input("I need a verb. >>>>>>\n")
print(four)

conclusion = """{}, thank you! We have completed our Madlib, here it is: 
A long time ago we went to {} .
There, we found {} and we also happened to, luckily, find {}.
Once we came home we decided to {} it.""".format(username, one, two, three, four)

print(conclusion)
