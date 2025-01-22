import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def getCard(self):
        return self.rank, self.suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    suits = ["H", "D", "C", "S"]
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] 
        self.shuffle()

    def count(self):
        return len(self.cards)
    
    def shuffle(self):
        return random.shuffle(self.cards)
    
    def deal(self):
        if self.cards:
            return self.cards.pop()
        else:
            return 0
        
    def discard(self):
        if self.cards:
            self.cards.pop()
        else:
            return 0
        
    def getDeck(self):
        rank = []
        suit = []
        deck = []
        for card in self.cards:
            r, s = card.getCard()
            rank.append(r)
            suit.append(s)
            deck.append(str(r) + s)
        return rank, suit, deck

        
class Hand:
    def __init__(self):
        self.cards = []
    
    def receive(self, card):
        self.cards.append(card)

    def getHand(self):
        return self.cards
    
    def fold(self):
        self.cards = []
    
class Table:
    def __init__(self):
        self.flop = []
        self.turn = None
        self.river = None
    
    def dealFlop(self, flops):
        for card in flops:
            self.flop.append(card)
    
    def dealTurn(self, turn):
        self.turn = turn

    def dealRiver(self, river):
        self.river = river

    def getTable(self):
        return self.flop, self.turn, self.river
    

class Game:
    def __init__(self, playerNum):
        self.players = playerNum
        self.deck = Deck()
        self.table = Table()
        self.hand = [Hand() for i in range (playerNum)]

    def update(self):
        return self.deck.getDeck()
    
    def dealPlayer(self):
        for i in range (2):
            for j in range (self.players):
                card = self.deck.deal()
                print(card)
                self.hand[j].receive(card)
        



def main():
    #playerNum = int(input("Number of player: "))
    #game = Game(playerNum)
    game = Game(2)
    rank = []
    suit = []
    deck = []
    rank, suit, deck = game.update()
    print(deck)

    game.dealPlayer()
    rank, suit, deck = game.update()
    print(deck)



    print("Done!")

if __name__ == "__main__":
    main()