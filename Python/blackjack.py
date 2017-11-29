#blackjack
import random
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        #use for loop to loop suite over the rank
        self.cards = []
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)
        random.shuffle(self.cards)
        random.shuffle(self.cards)

    def cut(self):
        # top_cards = self.cards[0:cut_point]
        # bottom_cards = self.cards[cut_point:]
        # bottom_cards.extend(top_cards)
        # self.cards = bottom_cards


        cut_point = random.randint(4, 46)

        temp = []
        for i in range(cut_point, len(self.cards)):
            temp.append(self.cards[i])
        for i in range(0, cut_point):
            temp.append(self.cards[i])
        self.cards = temp

    def __len__(self):
        return len(self.cards)


deck = Deck()
#deck.shuffle()
deck.cut()
for card in deck.cards:
    print(card)

