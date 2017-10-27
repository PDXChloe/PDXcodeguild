# Problem 6
#
# Write a function that takes two ints, a and b,
# and returns True if one is positive and the other is negative.
#
# opposite(10, -1) → True
# opposite(2, 3) → False
# opposite(-1, -1) → False

def opposite(a, b):
    if a < 0 and b > 0:
        print("true")


    elif a > 0 and b < 0:
        print("true")

    else:
        print("false")


opposite(-1,-1)