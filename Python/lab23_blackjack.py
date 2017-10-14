

c_1 = input("What is your first card?>>> \n")
c_2 = input("What is your second card?>>> \n")
c_3 = input("What is your third card?>>> \n")

card_value ={"A": 1, "2": 2, "3": 3, "4" : 4, "5" : 5, "6" : 6, "7": 7, "8" : 8, "9": 9, "10": 10, "J" : 10, "Q": 10, "K": 10}

#sum up the user card value

user_points = card_value.get(c_1) + card_value.get(c_2) + card_value.get(c_3)
if c_1 == "A" and user_points < 9:
    user_points += 10
elif c_2 == "A" and user_points < 9:
    user_points += 10
elif c_3 == "A" and user_points < 9:
    user_points += 10


if user_points < 17:
    print(str(user_points) + ", you should Hit!")
elif user_points >= 17:
    print(str(user_points) + ", Stay!")
elif user_points == 21:
    print(str(user_points) + ", Blackjack!")
elif user_points > 21:
    print(str(user_points) + ", Already Busted!")

#hmmmm, how to solve the A problem...?