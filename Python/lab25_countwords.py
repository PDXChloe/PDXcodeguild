

with open("theraven.txt") as f: #store contents as file_object - will work with later
    contents = f.read() #program to 'read in' the the file into memory. Then edit contents.
    # print(contents)
    c_l = contents.lower()

    for char in ",;:/\[]-_=()\"\'|#$%^&*+<>“”—":
        c_l = c_l.replace(char, "") #strips the unwanted characters.
    c_l = c_l.replace("!", ".")
    c_l = c_l.replace("?", ".")

    # c_l = c_l.split(".")
    # for sentence in c_l:
    #     #print('> '+sentence.replace('\n', ' '))
    #     c_l = c_l.split(" ")
    c_l = c_l.replace('\n', ' ')
    c_l = c_l.replace('.', '')
    words = c_l.split(' ')
    #print(words)

    raven_dic = {}
    for word in words:
        raven_dic[word] = raven_dic.get(word, 0) + 1
        #this tricks the get() func to put the word in dict. even if it is not currently there
        #you put it in at 0value, but then immediately add 1 to the value count

    # for word in words:
    #     if word in raven_dic:
    #         raven_dic[word] += 1
    #     else:
    #         raven_dic[word] = 1

    print(raven_dic)


    words = list(raven_dic.items()) # list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(11, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])


# # loop through c_s
#
# catelog each unique word into Key in Dictionary using dict()????
#
#
# same Loop?: find same word? it gets added to the count as the Value
