#

import random
sock_types = ['ankle', 'crew', 'calf', 'thigh']
list_socks = []

#generate a list of 100 random socks
for i in range(100):
    choose_sock = random.choice(sock_types)
    list_socks.append(choose_sock)
print(list_socks)


#sort out list of socks into like categories
sock_pairs = {}
for sock in list_socks:
    sock_pairs[sock] = sock_pairs.get(sock, 0) + 1
print(sock_pairs)

#find the number of pairs
for sock in sock_pairs:
    #sock_pairs2 =
    amt_pairs = sock_pairs[sock]/2
    print(amt_pairs)


    if amt_pairs%1 == 0:
        print(f'There are {int(amt_pairs)} pairs of socks')
    else:
        print(f'There are {int(amt_pairs)} and there is one loner sock')

#do version 2


#find the number of duplicates and loner socks for each sock type
# amt_crew_sock_pairs = sock_pairs['crew']/2
# amt_calf_sock_pairs = sock_pairs['calf']/2
# amt_thigh_sock_pairs = sock_pairs['thigh']/2
# amt_ankle_sock_pairs = sock_pairs['ankle']/2
# print(amt_ankle_sock_pairs)
# print(amt_calf_sock_pairs)
# print(amt_crew_sock_pairs)
# print(amt_thigh_sock_pairs)

# raven_dic = {}
#     for word in word_pairs:
#         raven_dic[word] = raven_dic.get(word, 0) + 1