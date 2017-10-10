# Lab 17: Number to Phrase
#
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
#
# Hint: you can use modulus to extract the ones and tens digit.
#
# x = 67
# tens_digit = x//10
# ones_digit = x%10
# Hint2: use the digit as an index to look up a string in a list.
#
# Version 2
#
# Handle numbers from 100-999.

dic_tens = {1: "ten" , 2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety" }
dic_ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine" }
ones = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["ten","ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["n/a","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


user_num = int(input("Give me an one or two-digit number...>>>\n"))

tens_digit = user_num//10

ones_digit = user_num%10

if user_num < 10:
    print(ones[user_num])
elif user_num < 20 and user_num > 10:
    print(teens[user_num%10])
elif user_num%10 == 0:
    print(tens[user_num//10])
else:
    print(dic_tens[tens_digit] + "-" + dic_ones[ones_digit])




