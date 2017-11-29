import random
import time

width = 30  # the width of the board
height = 10  # the height of the board
player_points = 0
# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# add obstacles in random locations
for i in range(4):
    fairy_i = random.randint(0, height - 1)
    fairy_j = random.randint(0, width - 1)
    board[fairy_i][fairy_j] = '§'

for i in range(5):
    heart_i = random.randint(0, height - 1)
    heart_j = random.randint(0, width - 1)
    board[heart_i][heart_j] = '❤'

# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left' or command == 'l':
        # only move them left if they're not on the left side
        player_j -= 1  # move left
    elif command == 'right' or command == 'r':
        player_j += 1  # move right
    elif command == 'up' or command == 'u':
        player_i -= 1  # move up
    elif command == 'down' or command == 'd':
        player_i += 1  # move down


    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        treasure_door = random.randint(1, 2)
        print(''' 
                            _______
                            |     |
                            |     |  Welcome to fairyland!
                            |   . |    Our brains are bigger than yours!              
                            |     |        And we are twice as attractive.....
                            |     |            pick a door, bitches!
        ''')
        print('You\'ve encountered a trickster fairy, you also see two fairy doors,')
        print('"Pick a door" says the fairy, "One will lead to fortune, and one will lead to your doom"')
        print('')
        chosen_door = input('Which door will you choose, 1 or 2.')
        if chosen_door == str(treasure_door):
            print('You open the door and find a beautiful fairy man, he says to you')
            print('You\'re soul is pure, here is 20points!')
            player_points += 20
            print()
            print('Your points are now at:' + str(player_points))
            board[player_i][player_j] = ' '  # remove the obstacle from the board
        else:
            time.sleep(2)
            print('GRRRRRRrrrrr, an angry twisted evil fairy attacks you with her jagged teeth.')
            print('She takes out a chunk of your leg, and takes away 20 points.')
            player_points -= 20
            print()
            print('Your points are now at:' + str(player_points))
            board[player_i][player_j] = ' '

    if board[player_i][player_j] == '❤':
        print('You can earn some points, if your soul is pure and you answer this question right....')
        player_answer = input('Fill in the blank. "Donald Trump is a _________."\n "joke", "asshole", "genius".' ).lower()
        if player_answer == 'joke':
            print('Your soul is True! 30points')
            player_points += 30
            board[player_i][player_j] = ' '
            print('Your score is: ' + str(player_points))

        if player_answer == 'asshole':
            print('One of Us! 40points')
            player_points += 40
            board[player_i][player_j] = ' '
            print('Your score is: ' + str(player_points))

        if player_answer == 'genius':
            print('How about -50points GENIUS???')
            player_points -= 50
            board[player_i][player_j] = ' '
            print('Your genius score is: ' + str(player_points))
            print('Hey, you are in my world, son!')



            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()

#  ❤♞﹘⍂⌞⌟⌜⌝⌈⌉⌊⌋