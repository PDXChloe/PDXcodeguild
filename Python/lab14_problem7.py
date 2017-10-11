'''Problem 7

Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.

def minimum(nums):

def maxmimum(nums):

def mean(nums):

(OPTIONAL) def mode(nums):

'''

# need a list of values, (from a end user?)
# create the list
# run it through mins, max, mean and mode - all separate functions
# output value to end user,
#

def min_nums(nums_list):
    the_mini = min(nums_list)
    print(the_mini)


def max_nums(nums_list):
    the_big = max(nums_list)
    print(the_big)


def mean_nums(nums_list):
    the_av = sum(nums_list)/(len(nums_list))
    return the_av


if __name__ == 'main':

    nums_list = []
    user_reply = ""

    while True:        #creating a user list of values to be put through the different functions
        user_reply = input("Enter a number, or 'done'\n")
        if user_reply == 'done':
            print(nums_list)
            break
        nums_list.append(int(user_reply))
        print(nums_list)

    print("Here is the mean of all your numbers:")
    mean_nums(nums_list)
    print("Here is the maximum of yor list of numbers:")
    max_nums(nums_list)
    print("Here is the minumum of your list of numbers:")
    min_nums(nums_list)


#Nick gift
#look at this closer!
#Can generate a dictionary which can keep taps on occurances of same keys/keep score/ and creates a dynamic variables
#Also, use (Command ? ) to comment out whole sections of code!

# def mode(list):
#     dictionary = {}
#     for num in list:
#         if num in dictionary:
#             dictionary[num] += 1
#         else:
#             dictionary[num] = 1
#
#     max_key = 0
#     max_value = 0
#     for key in dictionary:
#         if dictionary[key] > max_value:
#             max_value = dictionary[key]
#             max_key = key
#
#     print(f"{max_key}: {max_value}")
#
#
#
# mode([1, 4, 4, 4, 1, 7, 1, 4, 7, 4, 4])