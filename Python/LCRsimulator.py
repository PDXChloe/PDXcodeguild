

import random

player_names = ['Matthew', 'Jean', 'Caroline', 'Adrienne', 'Ron', 'Dot', 'Roger', 'Gary', 'Julissa']

while True:
    num_players = int(input('How many players? '))
    if num_players < 3 or num_players > 9:
        print('Fool! You can only play with 3 to 9 players')
    else:
        break

def pick_players():

    players = []

    for player in range(num_players):
        player_name = random.choice(player_names)
        player_names.remove(player_name)#will remove duplicates names in one game
        num_chips = 3
        players.append({'name': player_name, 'chips': num_chips})

    return players

# print(pick_players())

def roll_bones():
    faces = ["L", 'C', 'R', '.', '.', '.']
    roll = random.choice(faces)
    return roll

#print(roll_bones())
def find_winner():
    winner = None
    for player in players:  # player is the dictionary
        if player['chips'] >= 1:
            if winner is None:
                winner = player
            else:
                return None
    return winner

pot = 0
player_id = 0
players = pick_players()

while True:
    player = players[player_id]
    num_chips = player['chips']
    player_lt_id = player_id - 1
    player_rt_id = player_id + 1
    if player_rt_id == len(players):
        player_rt_id = 0
    if num_chips >= 3:
        num_rolls = 3
    else:
        num_rolls = num_chips

    for roll in range(num_rolls): #if '.' happens, nothing happens
        outcome = roll_bones()
        if outcome == 'C':
            pot += 1
            num_chips -= 1
        if outcome == 'R':
            players[player_rt_id]['chips'] += 1
            #chips of player_id_rt += 1
            num_chips -= 1
        if outcome == 'L':
            players[player_lt_id]['chips'] += 1
            num_chips -= 1
    player['chips'] = num_chips
    winner = find_winner()

    if winner is not None:
        winner['chips'] += pot
        print(winner)
        break

    for player in players:
        print(player['chips'], end=' ')
    print()
