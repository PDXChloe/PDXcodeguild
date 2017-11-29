

#problem 2 Print out every other element of a list, first using a while loop, then using a for loop.

nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[::2]) #we could do it like this with this built in function


#while loop example


#for loop example
other_nums = []

for num in nums:
    if num%2 == 0:
        other_nums.append(num)
print(other_nums)



# while i in range(len(nums)):
#     if i%2 == 0:
#         other_nums.append(num)
# print(other_nums)