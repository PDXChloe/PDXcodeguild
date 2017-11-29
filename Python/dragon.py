import random
import time


def displayIntro():
    print()
    print("\nYou have magically arrived in a land full of intelligent dragons.\n")
    time.sleep(1)
    print("\nLook to the front of you and you will see two caves.\n")
    time.sleep(1)
    print("\nIn one of the caves the dragon is inviting and will share his treasure with you.\n")
    time.sleep(1)
    print("\nBut....\n")
    time.sleep(2)
    print("\nBeware, in the other cave the dragon is greedy and hungry and will eat you on sight.\n")
    print()


# displayIntro()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave


# chooseCave()

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and....')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")


displayIntro()
caveNumber = chooseCave()
checkCave(caveNumber)  # may 29th, there is an issue here with calling this function.

'''
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you want to play again? (yes or no)")
    playAgain = input()

closing_question = input("Would you like to ask the Wise One another question? Y/N: ").lower()
while closing_question == str("y"):
    answerQuery()
    closing_question = input("Would you like to ask the Wise One another question? Y/N: ").lower()
else:
    print(input("Thanks for playing... Use your fortune wisely..."))
'''

closing_question = input("Would you like to try again? Y/N >>>   ").lower()
while closing_question == str("y"):
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    closing_question = input("Would you like to try again? Y/N >>>   ").lower()
else:
    print("Thanks for playing... make wise choices...")
