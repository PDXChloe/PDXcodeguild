'''Problem 6

print out the powers of 2 from 2^0 to 2^20

1, 2, 4, 8, 16, 32, ...

'''

#need to use range. 0 - 20
#need to use 2.
#print() in a loop

def powers():

    for i in range (0, 20):
        print(2**i)

powers()