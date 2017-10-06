#lab 15 Rot Cipher



english = "abcdefghijklmnopqrstuvwxyz"
rot_13 = "nopqrstuvwxyzabcdefghijklm"

user_word = "puybr" #chloe...ummm...



#I wanna take the first element on the user_word,
#compare it to the rot_13 alpha
#find the coordinating rot_13 index
#use that index to find the coordinating english element
#loop back to find the next user_word element......



english_word = ""

for letter in user_word:         #for every element in the user_word provided (in rot_13code)
                                          #if that element is in the rot_13 cipher
    i = rot_13.find(letter)
    english_word += english[i]

print(english_word)




# english_word = ""
#
# i = rot_13.find(user_word[0])
# english_word += english[i]
#
# i = rot_13.find(user_word[1])
# english_word += english[i]
#
# i = rot_13.find(user_word[2])
# english_word += english[i]
#
# i = rot_13.find(user_word[3])
# english_word += english[i]
#
# i = rot_13.find(user_word[4])
# english_word += english[i]
#
# print(english_word)







