# Anagram
#
# Two words are anagrams of eachother if the letters of one can be rearranged
# to fit the other. e.g. anagram and nag a ram.
#
# Write another function check_anagram that takes two strings as parameters
# and returns True if they're anagrams of eachother, False if they're not.
# The procedure for comparing the two strings is as follow:
#
# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal
# >>> enter the first word: anagram
# >>> enter the second word: nag a ram
# >>> 'anagram' and 'nag a ram' are anagrams
#

first_word = input("\nEnter a word...\n")
second_word = input("\nEnter a second word....\n")

new_word1 = sorted(first_word.lower().replace(" ", ""), key=str.lower)
new_word2 = sorted(second_word.lower().replace(" ", ""), key=str.lower)

if new_word1 == new_word2:
    print("is anagram")
else:
    print("is not anagram")


# sorted("This is a test string from Andrew".split(), key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
