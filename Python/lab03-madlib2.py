
user_input = input("Enter three adjectives. \n")

adjectives = user_input.split(' ')
print(adjectives)
print(adjectives[0])
print(adjectives[1])
print(adjectives[2])

user_input2 = input("Enter three nouns. \n")

nouns = user_input2.split(' ')
print(nouns)
print(nouns[0])
print(nouns[1])
print(nouns[2])



def answer():
    user_input3 = input("Would you like to hear our story, type Y or N.>>>")

    if user_input3 == 'Y' or 'y':
        print("Once I had a, " + adjectives[0] + " " + nouns[0] + ", which was my favorite thing ever!\nBut, then I found, " + adjectives[1] + " " +nouns[1]
        + ", and it soon became my new favorite thing ever.\nAnd now I have a, " + adjectives[2] + " " + nouns[2] + ", and it is my absolute favorite!\nFor now....")

    else:
        print("Goodbye!")

answer()