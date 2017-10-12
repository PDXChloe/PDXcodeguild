

#
#
# reverse = "abcdefg"
# print(reverse[::-1])
#
# word = input("Enter a word to check if it is a palindrome...")


def check_palindrome(word):
    if word == word[::-1]:
        print(word + ", is palindrome")
    else:
        print(word + ", is not palindrome")
check_palindrome("racecar")

