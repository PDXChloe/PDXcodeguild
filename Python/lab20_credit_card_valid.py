# Lab 20: Credit Card Validation
#
# Let's write a function which returns whether a string containing a
# credit card number is valid as a boolean. The steps are as follows:
#
# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# For example, the worked out steps would be:
#
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!



cred_num = input("Enter your credit card number>>>> \n")

new_list = []
def num2list(cred_num):
    for num in cred_num:
        new_list.append(int(num))#put string of numbers into a list of numbers(strings).
    return new_list
num2list(cred_num)
print(new_list)
check_digit = new_list.pop()#takes last item from list and sets to new var to be used later.

print(check_digit)
def rev_list(new_list):
    new_list.reverse()#reverse that list
    return new_list
rev_list(new_list)

print(new_list)

def odd_double(new_list):
    for i in range(0, len(new_list), 2):
        new_list[i] *= 2#find every other index and then double that value within that index.
    return new_list
odd_double(new_list)

print(new_list)

def subtract_nine(new_list):#subtract 9 from numbers over 9.
    for i in range(len(new_list)):
        if new_list[i] > 9:
            new_list[i] -= 9
    return new_list
subtract_nine(new_list)
print(new_list)

two_dig = sum(new_list)
print(two_dig)

if str(two_dig)[1] == str(check_digit):
    print("Valid!")
else:
    print("Not Valid!")