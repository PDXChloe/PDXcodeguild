# '''
# Return the number of letter occorrances in a string.
#
# >>>count_letter("i", "Antidisestablishmentterianism")
#
# >>>count_letter("p", "Pneumonoultramicroscopicsilicovolcanoconiosis")
# '''

# def count_letter(char, word):
#     for letter in word:


def count_letter(char, word):
    letter_count = 0
    for letter in word:
        if letter == char:
            letter_count += 1
    print("The letter " + char + " occurs " + str(letter_count) + " times.")

char = "q"
word = "asdfkjhaewiufhilusdbfviuqqqqhsfuyiahweku"

count_letter(char, word)



#
# def count_letter(char_to_find, text):
#     count = 0
#     for char in text:
#         if char == char_to_find
#             count += 1
#         return count
#