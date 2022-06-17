
import random

"""Class that represents a card in the carddeck."""
class card:
    def __init__(self,color,value):
        self.value = value
        self.color = color

    """Returns color of card"""
    def getColor(self):
        return self.color

    """Returns value of card"""
    def getValue(self):
        return self.value

    """Change value of card to newVal"""
    def changeValue(self,newVal):
        self.value = newVal

    """Change color of card to newColor"""
    def changeColor(self,newColor):
        self.color = newColor

    """stringrepresentation of the card in the console"""
    def showCardRow(self):
        print(str(self.color) +' ' +str(self.value), end="")

    """Stringrepresentation of the card but on a single line"""
    def showCardLine(self):
        print(str(self.color) + ' ' + str(self.value))

class deck:
    """
    Class that represents an entire deck with some functions to it. A deck is an arbitrary amount of cards,
    example the cards in the hand, cards on the table etc.
    """

    def __init__(self, full):
        self.deckList = []
        self.deckSize = 0
        if full:
            for j in range(4):
                for i in range(13):
                    if j == 0:
                        color = 'HEARTS'
                    elif j == 1:
                        color = 'DIAMONDS'
                    elif j == 2:
                        color = 'SPADES'
                    else:
                        color = 'CLUBS'

                    value = i+2

                    currCard = card(color,value)
                    self.addCard(currCard)


    def addCard(self,newCard):
        """Add card to the deck"""
        self.deckList.append(newCard)
        self.deckSize = self.deckSize +1


    def getCard(self, cardNbr = -1):
        "Returns the top card in the deck if there is any cards in it."
        if self.deckSize >0:
            self.deckSize = self.deckSize - 1
        else:
            print('Cant get card, deck is empty')
            return False
        if cardNbr == -1:
            return self.deckList.pop()
        else:
            return self.deckList.pop(cardNbr)



    def getDeckSize(self):
        """Returns size of the deck"""
        return self.deckSize


    def shuffleDeck(self):
        """Shuffles the deck"""
        random.shuffle(self.deckList)


    def showTopCard(self):
        """
        Shows the top card
        """
        if self.deckSize >0:
            self.deckList[self.deckSize-1].showCard()
        else:
            print('Deck is empty')

    def showDeck(self, inp='LINE'):
        """
        Prints a stringrepresentation of the deck in the console
        """

        if inp == 'LINE':

            if self.deckSize >0:
                for i in range(self.deckSize):
                    self.deckList[i].showCardLine()
            else:
                print('Deck is empty')
        elif inp == 'ROW':
            if self.deckSize >0:
                for i in range(self.deckSize):
                    if i < self.deckSize-1:
                        self.deckList[i].showCardRow()
                        print(', ',end='')
                self.deckList[i].showCardRow()
                print()
            else:
                print('Deck is empty')