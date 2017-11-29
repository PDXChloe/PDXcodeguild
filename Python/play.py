

import copy
import keyword
import random
import time

class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color


harry = Animal('hippogriff', 6, 'pink')
harriet = copy.copy(harry)
#print(harry.species)
#print(harriet.species)

carrie = Animal('chimea', 4, 'green polka dots')
billy = Animal('bogill', 0, 'paisley')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[2].species)

my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(more_animals[0].species) #the copy function makes a shallow copy it will be changed when the oi

sally = Animal('sphinx', 4, 'sand')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))

more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'wyrm'
print(my_animals[0].species)
print(more_animals[0].species)


print(keyword.iskeyword('if'))
print(keyword.iskeyword('ozwald'))
print(keyword.kwlist)

print(random.randint(1, 100))
print(random.randint(100, 1000))
print(random.randint(1000, 5000))

# num = random.randint(1, 10)
# while True:
#     guess = input('Guess a number between 1 and 10')
#     i = int(guess)
#     if i == num:
#         print('You guessed right')
#         break
#     elif i < num:
#         print('Try higher')
#     elif i > num:
#         print('Try lower')

desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
print(random.choice(desserts))
random.shuffle(desserts) #could use for card game
print(desserts)

print(time.time()) #will print the number of seconds since January 1, 1970

def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print('it took {} seconds'.format(t2-t1))
lots_of_numbers(10000)

print(time.asctime())

t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))

print(time.localtime())
time.struct_time(tm_year=2020, tm_mon=2, tm_mday=23, tm_hour=22, tm_min=18, tm_sec=39, tm_wday=0, tm_yday=73, tm_isdst=0)
