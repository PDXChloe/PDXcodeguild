# def fibonacci(n):
#     print('fib ' + str(n))
#     if n == 0 or n == 1:
#         print('returning 1')
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# fibonacci(5)
# #recursive fuctiion
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)
#
# def add(*args): #turns it into a list any variable as long as it has an astrix in front of it
#     total = 0
#     for num in args:
#         return total
#
# print(add(5,2,3))

def print_movie_ratings(**ratings): #put in dictionary
    for movie in ratings:
        print(movie+ ": " + str(ratings[movie]))

print_movie_ratings(Sharknado=3, Frozen=2, Fargo=5)

def get_dimensions(): #tuple packing
    return 500, 200
width, height = get_dimensions()

print(width)
print(height)

def swap(nums, i, j):
    t = nums[i]
    nums[i] = t

    nums[i], nums[j] = nums[j], nums[i]