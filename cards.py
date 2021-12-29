from random import shuffle


class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f'{self.value} of {self.suit}')

class Deck():
    def __init__(self):
        self.cards = []
        self.build()


    def build(self):
        s = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        v = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        for suit in s:
            for value in v:
                self.cards.append(Card(suit, value))
        shuffle(self.cards)

    def show(self):
        for c in self.cards:
            c.show()

    def DrawACard(self):
        return self.cards.pop()


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self):
        self.hand.append(self.deck.draw())

    def reveal(self):
        for card in self.hand:
            card.show()


