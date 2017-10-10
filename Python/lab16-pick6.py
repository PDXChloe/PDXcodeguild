# Lab 16: Pick6

# Have the computer play pick6 many times and determine net balance.
#
# Initially the program will pick 6 random numbers as the 'winner'.
# Then try playing powerball 100,000 times, with the ticket cost and payoff below.
#
# A ticket contains 6 numbers, 1 to 99, and the number of matches between the
# ticket and the winning numbers determines the payoff. Calculate your net
# winnings (the sum of all expenses and earnings).
#
# the price of a ticket is $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win #1,000,000
# if 6 numbers match, you win #25,000,000
# Steps
#
# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 1000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
# Version 2
#
# The ROI (return on investment) is defined as (earnings - expenses)/expenses.
# Calculate your ROI, print it out along with your earnings and expenses.
import random


def pick6(): # return a list of 6 random numbers
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1,99))
    return ticket

winning_numbers = pick6()
#print("winning numbers: " + str(winning_numbers))
balance = 0
for i in range(100):
    user_ticket = pick6()
    balance -= 2
    #print(balance)
    common_nums = 0
    for i in range(len(winning_numbers)):
        if winning_numbers[i] == user_ticket[i]:
            common_nums += 1
    print(common_nums)

    prizes = [0, 4, 7, 100, 50000, 1000000, 25000000]

    # for i in common_nums:
    #     if common_nums == prizes[i]:
    #         balance += i
    #         print(balance)

    # compare ticket and winning numbers

# def player_tx():
#     tickets = []
#     for i in range(1000):
#         ticket_nums = []
#         for nums in range(0,6):
#             ticket_nums.append(random.randint(1, 99))
#         tickets.append(ticket_nums)
#     return tickets
#
# print(player_tx())
#
# def winning_nums():
#     win_nums = []
#     for number in range(0,6):
#         win_nums.append(random.randint(1, 99))
#
#     print("Here is the winning ticket number: \n"+ str(win_nums))
#     return win_nums
#
# winning_nums()
#
#
# def common_nums():
#     pass

