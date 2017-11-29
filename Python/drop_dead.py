'''
drop dead - dice game
'''

import random

#create dice class

class Die:

    def __init__(self):
        self.alive = True


    def roll(self):
        return random.randint(1, 6)


dice = []

for i in range(5):
    dice.append(Die())
print(dice)



num_player = 4

player_score = []
player_dice = []

for i in range(num_player):
    print(f'player {i} turn')
    player_dice.extend(dice)
    player_score.append(0)
    while len(player_dice) > 0:
        for j in range(len(player_dice)):
            if j >= len(player_dice):
                continue# iterating over the dice
            die_value = player_dice[j].roll()  # each dice gets one roll with the roll function module
            if die_value in (2, 5):
                player_dice.pop(j)

            print(len(player_dice))

