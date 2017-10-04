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

print("Welcome to the Paper, Rock, Scissors game!")
player = input("Enter your choice either rock, paper, scissors")
