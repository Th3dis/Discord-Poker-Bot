from cards import Deck
from cards import Card
from cards import Player

class Poker():
    def __init__(self, numPlayers, players):
        self.numPlayers = numPlayers
        self.players = players
        self.deck = Deck()

    def draw(self):
        for i in range(2):
            for player in players:
                player.hand.append(self.deck.DrawACard())

    def showDeck(self):
        print(self.deck.show())

players = []
numPlayers = int(input('How many players? '))
print('Who is playing?')
for i in range(numPlayers):
    playerName = input()
    players.append(Player(playerName))

game = Poker(1, 'Sam')
game = Poker(numPlayers, players)
game.showDeck()
game.draw()
#players[0].reveal()
