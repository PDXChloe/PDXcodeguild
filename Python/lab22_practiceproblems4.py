# Problem 4
#
# Get a string from the user, print out another string, doubling every letter.
#
# >>> Enter some text: hello
# hheelloo


user_word = input("Enter a word.>>> \n")
double_letter = []


for i in range(len(user_word)):
    double_letter.append(user_word[i]*2)


#print(double_letter)

s_double = ''
for x in double_letter:
    s_double = s_double + x

print(s_double)


