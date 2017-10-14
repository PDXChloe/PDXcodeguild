

c_1 = input("What is your first card?>>> \n")
c_2 = input("What is your second card?>>> \n")
c_3 = input("What is your third card?>>> \n")

card_value ={"A": 1, "2": 2, "3": 3, "4" : 4, "5" : 5, "6" : 6, "7": 7, "8" : 8, "9": 9, "10": 10, "J" : 10, "Q": 10, "K": 10}

#sum up the user card value

user_points = card_value.get(c_1) + card_value.get(c_2) + card_value.get(c_3)
if c_1 == "A" and user_points <= 11: #already added the A value as 1, so instead of the total being <= 11, it's 1 less
    user_points += 10
elif c_2 == "A" and user_points <= 11: #you would never have two A = 11 because that would bust you with two cards.
    user_points += 10
elif c_3 == "A" and user_points <= 11: #so the code only needs to check for at least one A, and that the total of all three cards (with A = 1) being <=11
    user_points += 10 #add 10 points to total because you already have 1 added for the Ace. 10+1 = 11 yay!


if user_points < 17:
    print(str(user_points) + ", you should Hit!")
elif user_points >= 17:
    print(str(user_points) + ", Stay!")
elif user_points == 21:
    print(str(user_points) + ", Blackjack!")
elif user_points > 21:
    print(str(user_points) + ", Already Busted!")

#hmmmm, how to solve the A problem...?