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
        
    def burn(self):
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

    def __str__(self):
        for card in self.cards:
            print(card)


def getbestSets(hand):
    bestSets = []
    setPoints = []
    suits = [card.getSuit() for card in hand]
    ranks = [card.getRank() for card in hand]
    for card in hand:
        if card.getRank() in {1, 10, 11, 12, 13}: # Royal Flush
            s = card.getSuit()
            set = [Card(1, s), Card(10, s), Card(11, s), Card(12, s), Card(13, s)]
            if set in bestSets:
                continue
            bestSets.append(set)
            setPoints.append(10)

        



            
            




def calculateOuts(hand, table, deck):
    out = 0



    
class Table:
    def __init__(self):
        self.flop = []
        self.turn = None
        self.river = None
    
    def getFlop(self, flops):
        for card in flops:
            self.flop.append(card)
    
    def getTurn(self, turn):
        self.turn = turn

    def getRiver(self, river):
        self.river = river

    def getTable(self):
        return self.flop, self.turn, self.river
    

class Game:
    def __init__(self, playerNum, random):
        self.players = playerNum
        self.random = random
        if not self.random:
            self.deck = Deck()
            self.table = Table()
            self.hand = [Hand() for i in range (playerNum)]
        else:
            self.deck = None
            self.table = None
            self.hand = None
        
    def updateDeck(self):
        return self.deck.getDeck()
    
    def dealPlayer(self):
        for i in range (2):
            for j in range (self.players):
                card = self.deck.deal()
                print(card)
                self.hand[j].receive(card)

    def dealFlop(self):
        flop = []
        self.deck.burn()
        for i in range (3):
            card = self.deck.deal()
            flop.append(card)
        self.table.getFlop(flop)
    
    def dealTurn(self):
        self.deck.burn()
        card = self.deck.deal()
        self.table.getTurn(card)

    def dealRiver(self):
        self.deck.burn()
        card = self.deck.deal()
        self.table.getRiver(card)

    def getTable(self):
        return self.table.getTable()
    



def main():
    #playerNum = int(input("Number of player: "))
    #game = Game(playerNum)
    game = Game(2, True)
    rank = []
    suit = []
    deck = []
    rank, suit, deck = game.updateDeck()
    print(deck)

    game.dealPlayer()
    rank, suit, deck = game.updateDeck()
    print(deck)


if __name__ == "__main__":
    main()