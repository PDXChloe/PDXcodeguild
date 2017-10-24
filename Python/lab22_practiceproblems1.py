#problem 1 write a REPL which asks users for a list of numbers, which they enter, until they say 'done.
#then print out the list
num_list = []
while True:

    user_data = input('Enter a number or "done"')
    if user_data == 'done' or user_data == 'd':
        print(f'Goodbye, here is your number list: {num_list}')
        break


    num_list.append(user_data)

