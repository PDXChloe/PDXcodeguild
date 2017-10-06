# Problem 10
#
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.
#
# def extract_less_than_ten(nums):
#





def extract_less_than_ten(list_numbers):
    new_list = []
    for number in list_numbers:
        if number < 10:
            new_list.append(number)
    print(new_list)

extract_less_than_ten([2,3,4,5,6,10,12,34,56,78,99])