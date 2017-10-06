# Problem 11
#
# Write a function to combine two lists of equal length into one, alternating elements.
#
# def combine(nums1, nums2):
#
# combine(['a','b','c'],[1,2,3]) returns ['a', 1, 'b', 2, 'c', 3]






new = []
def combine(list_a, list_b):
    for i in range(len(list_a)): #can use RANGE to compare multiple index within multiple lists
        new.append(list_a[i])   #take index from list_a and put it on a new list
        new.append(list_b[i])   #then take the index from list_b and put it next on the same list
                                #then it loops and does it all over again but, with the next incremental index

    print(new)

combine(['a', 'b', 'c', 'd'],[1,2,3,4] )