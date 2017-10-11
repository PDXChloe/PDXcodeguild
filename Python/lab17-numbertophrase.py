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

#This version is my first, I used a combo of dictionary and lists - is a no no.. lol but, interesting? No?

dic_tens = {1: "ten" , 2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety" }
dic_ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine" }
ones = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["ten","ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


user_num = int(input("Give me an one or two-digit number...>>>\n")) #get user input, put in variable.

tens_digit = user_num//10 #finding the tens digit

ones_digit = user_num%10 #finding the ones digit

if user_num < 10: #uses the list
    print(ones[user_num])
elif user_num < 20 and user_num > 10: #uses the list
    print(teens[user_num%10])
elif user_num%10 == 0:  #uses the list
    print(tens[user_num//10])
else:                                                           #uses the dictionary
    print(dic_tens[tens_digit] + "-" + dic_ones[ones_digit])




