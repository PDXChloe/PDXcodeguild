import random

print("")
print("")

print("Welcome to Guess the Number!\n")
print("I am thinking of a number between 1 and 10.")
computer_number = random.randint(1,10)
guess_count = 0

while True:
    user_guess = int(input("Guess a number...."))
    guess_count += 1

    if user_guess == computer_number:
        print("Congrats, that is the number I was thinking of. You guessed it in " + str(guess_count) + " tries!")
        break

    if user_guess != computer_number:
        print("Try again, thats " + str(guess_count) + " tries so far!")