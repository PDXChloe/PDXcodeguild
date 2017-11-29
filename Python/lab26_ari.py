from math import ceil

contents = ''

with open("metamor.txt") as f: #store contents as file_object - will work with later
    contents = f.read() #program to 'read in' the the file into memory. Then edit contents.

c_r = contents.replace("!", ".")
c_r = c_r.replace("?", ".")
sentences = c_r.split(".")

sentence_count = len(sentences)
#for sentence in sentences:
    # print('> '+sentence.replace('\n', ' '))
print("sentence count is: " + str(sentence_count))

c_r = c_r.replace(".", "")
words = c_r.split(" ")
word_count = len(words)
print("word count is: " + str(word_count))

char_count = 0
for char in c_r:
    if char in 'abcdefghijklmnopqrstuvwxyz':
        char_count += 1
print("character count is: " + str(char_count))

def ari_score(c, w, sen):
    s = ((4.71 * (c/w)) + (0.5 * (w/sen))) - 21.43
    # if type(s) == type(float):
    #     s = int(s + 0.9)
    if s > 14:
        return 14
    return ceil(s) #math import to get the ceiling of the float

score = ari_score(char_count, word_count, sentence_count)
#print("ari score is: "+ str(score))

ari_scale = {
    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages': '6-7', 'grade_level': '1st Grade'},
    3: {'ages': '7-8', 'grade_level': '2nd Grade'},
    4: {'ages': '8-9', 'grade_level': '3rd Grade'},
    5: {'ages': '9-10', 'grade_level': '4th Grade'},
    6: {'ages': '10-11', 'grade_level': '5th Grade'},
    7: {'ages': '11-12', 'grade_level': '6th Grade'},
    8: {'ages': '12-13', 'grade_level': '7th Grade'},
    9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}


print("The ARI for gettysburg-address.txt is: " + str(score))
print("This corresponds to a " + ari_scale[score]['grade_level'] + " level of difficulty.")
print("that is suitable for an average person " + ari_scale[score]['ages'] + " years old.")

