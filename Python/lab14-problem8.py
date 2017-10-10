
# Problem 8
#
# Write a function that returns the reverse of a list.
#
# def reverse(nums):
#

def reverse(nums):
    rev_list = nums[::-1]
    print(rev_list)

reverse([1,2,3,4,5,6])

def reverse(nums):
    rev_nums = []

def reverse_v2(nums):
    for i in range(len(nums) // 2):
        j = len(nums) - i - 1
