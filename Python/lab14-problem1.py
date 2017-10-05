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

cksdflkj = "q"
asdjkh = "asdfkjhaewiufhilusdbfviuqqqqhsfuyiahweku"

count_letter(cksdflkj, asdjkh)


