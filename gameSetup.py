from random import shuffle

class Card:

    def __init__(self, value, house):
        self.value = value
        self.house = house


class Deck:

    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    houses = ["S", "C", "D", "H"]

    def __init__(self):
        self.deck = []

        for house in self.houses:
            for value in self.values:
                self.deck.append(Card(value, house))

    
    def showDeck(self):
        cardDeck = [f"{card.value}{card.house}" for card in self.deck]
        print(f"{cardDeck}\nCard deck length: {len(cardDeck)}")

    
    def shuffleDeck(self):
        shuffle(self.deck)
    

    def dealCard(self):
        return self.deck.pop()
    

    def deckLength(self):
        return len(self.deck)
