#Version 2 Hundreds final, does both two digit and three digit.


ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
hundreds = ["one-hundred", "two-hundred", "three-hundred", "four-hundred", "five-hundred", "six-hundred", "seven-hundred", "eight-hundred", "nine-hundred"]

user_num = int(input("Give me an one, two or three digit number...>>>\n")) #get user input, put in variable.

def num2phrase(num):

    tens_digit = num // 10 #finding the tens digit

    ones_digit = num % 10 #finding the ones digit

    if num < 10: #uses the list
        return(ones[num])
    elif num < 20 and num > 10: #uses the list
        return(teens[ones_digit])
    elif ones_digit == 0:  #uses the list
        return(tens[tens_digit-2])
    else:                                                           #uses the dictionary
        return(tens[tens_digit-2] + "-" + ones[ones_digit])





if user_num > 99:
    h_digit = (user_num // 10) // 10  # or user_num//100
    last_two = user_num - (h_digit * 100) #just need the last two-digit to feed back into the num2phrase function.

    print(hundreds[h_digit - 1] + "-" + num2phrase(last_two))
else:
    print(num2phrase(user_num))





# tens_of_hun = (user_num // 10) - (h_digit * 10)
# ones_of_hun = user_num % 10