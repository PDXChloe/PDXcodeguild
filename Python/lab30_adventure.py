import random

width = 10  # the width of the board
height = 10  # the height of the board

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
player_score = 0

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

for i in range(6):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '@'


# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'quit':
        break  # exit the game
    elif command == 'left' or command == 'l':
        player_j -= 1  # move left
    elif command == 'right' or command == 'r':
        player_j += 1  # move right
    elif command == 'up' or command == 'u':
        player_i -= 1  # move up
    elif command == 'down' or command == 'd':
        player_i += 1  # move down


    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('You\'ve encountered a trickster fairy, you also see three fairy doors,')
        print('"Pick a door" says the fairy, "One will lead to fortune, and two will lead to your doom"')
        print('')
        action = input('what will you do? Will you pick door 1, 2 or 3?')
        if action == '1':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hesitated and were slain')
            break


    def choose_door():
        door = ''
        while door != '1' and door != '2' and door != '3':
            print('Which door will you go choose? (1 or 2 or 3)')
            door = input()

        return door


    def check_door(choose_door):
        print('You have choosen door ' + door + '.')
        time.sleep(1)
        print('and........')
        time.sleep(2)


        treasure_door = random.randint(1, 2)

        if choose_door == str(treasure_door):
            player_score += 20
            print("You have chosen wisely and you will be rewarded, 20points")
            print("You now have: " + player_score)
        else:
            time.sleep(2)
            print("Grrrr behind the door is a hungry zombie and he takes a big chunk of your arm, you lose 20 points!")
            print("You now have: " + player_score)


    if board[player_i][player_j] == '@':
        print("You found a magic sea shell, it adds 10 points!")
        player_score += 10
    print(player_score)

            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')

            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()


        #❤♞﹘⍂⌞⌟⌜⌝⌈⌉⌊⌋