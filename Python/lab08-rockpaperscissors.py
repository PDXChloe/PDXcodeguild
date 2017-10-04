'''Lab 8: Rock Paper Scissors

Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors


rock == rock
rock < paper
rock > scissors

paper > rock
paper == paper
paper < scissors

scissors < rock
scissors > paper
scissors = scissors

'''



'''
user_input = ''
while user_input != 'done':
    user_input = input('enter something, or \'done\' if done: ')
    if user_input != 'done':
        # do something with the input


while True:
    user_input = input('enter something, or \'done\' if done: ')
    if user_input == 'done':
        break
    # do something with the input

'''








import random   #this lets you do random functions
import time

game_pieces = ['rock', 'paper', 'scissors']   #creating a list of choices for game play
com_choice = random.choice(game_pieces)     #computer making a choice but, not showing yet.....

print("")   #I just like white space....
print("")

print("Welcome to the Paper, Rock, Scissors game!\n")  #Welcome message
time.sleep(1)
name = input("What is your name? \n")
player = input(name.title() + ", please enter your choice either rock, paper, scissors.\n")


print(com_choice)

if com_choice == player.lower():
    print("Argh, we both win")

if com_choice == game_pieces[0] and player.lower() == game_pieces[1]:
    print("Paper covers rock, " + name.title() + " wins!")

if com_choice == game_pieces[0] and player.lower() == game_pieces[2]:
    print("Rock crushes scissors, you lose!")

if com_choice == game_pieces[1] and player.lower() == game_pieces[0]:
    print("Paper covers rock, you lose!")

if com_choice == game_pieces[1] and player.lower() == game_pieces[2]:
    print("Scissors cut paper " + name.title() + " wins!")

if com_choice == game_pieces[2] and player.lower() == game_pieces[0]:
    print("Rock crushes scissors " + name.title() + " wins!")

if com_choice == game_pieces[2] and player.lower() == game_pieces[1].lower():
    print("Scissors cut paper, you lose!")


#work on how to make this ask if you want to play again