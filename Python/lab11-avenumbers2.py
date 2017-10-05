#Version 2

nums = []
print("Welcome to Average Numbers")



while True:
    user_input = input("Enter a number or 'done'.")
    if user_input == "done":
        break
    nums.append(user_input)


print(nums)
total = 0

for num in nums:
    total += int(num)

average = total/len(nums)

print(str(nums) + "\nThis is your list of numbers.")
print(str(average) + "\nThis is the average of your list of numbers.")
