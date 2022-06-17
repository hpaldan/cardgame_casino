
from lib import card
from lib import deck

class player:

    def __init__(self, pile, hand):
        self.hand = hand
        self.pile = pile
        self.spares = 0

    def getHand(self):
        return self.hand

    def getPile(self):
        return self.pile

    def addSpare(self):
        self.spares +=1

    def getSpares(self):
        return self.spares


class casinoEnv:

    def __init__(self,gameDeck):
        self.gameDeck = gameDeck
        self.fieldCards = deck(False)

        player1Hand = deck(False)
        player1Pile = deck(False)

        player2Hand = deck(False)
        player2Pile = deck(False)

        self.p1 = player(player1Pile,player1Hand)
        self.p2 = player(player2Pile, player2Hand)
        self.playerTurn = 0

    def initializeGame(self):
        """Starts the game, meaning that it hands out cards to players and put 4 cards on the table."""
        for i in range(4):
            tempCard1 = self.gameDeck.getCard()
            tempCard2 = self.gameDeck.getCard()
            tempCard3 = self.gameDeck.getCard()

            self.giveCardToPlayer(tempCard1,1)
            self.giveCardToPlayer(tempCard2,2)
            self.addCardOnTable(tempCard3)
        self.playerTurn = 1

    def giveCardToPlayer(self,card,playerNumber):
        """Takes input card and playerNumber and gives card to the player with playerNumber."""
        if(card.getColor() == 'SPADES' and (card.getValue() == 2 or card.getValue() == 15)):
            card.changeValue(15)
        elif (card.getColor() == 'DIAMONDS' and (card.getValue() == 10 or card.getValue() == 16)):
            card.changeValue(16)

        if playerNumber == 1:
            self.p1.hand.addCard(card)
        elif playerNumber == 2:
            self.p2.hand.addCard(card)


    def addCardOnTable(self,card):
        """
        Takes a card object as input and puts it on the table.

        According to the rules of casino when diamonds 10 is on the field it has value 10, when spades 2 is on the field it has value 2
        and when any Ace is on the field it has the value of 1.
        """
        if (card.getColor() == 'SPADES' and (card.getValue() == 2 or card.getValue() == 15)):
            card.changeValue(2)
        elif (card.getColor() == 'DIAMONDS' and (card.getValue() == 10 or card.getValue() == 16)):
            card.changeValue(10)
        elif(card.getValue() == 14):
            card.changeValue(1)

        self.fieldCards.addCard(card)

    def getGameDeckSize(self):
        self.gameDeck.getDeckSize()

    def renderGame(self):
        """
        Prints a string representation of the game in the console.
        """
        print('Player1 cards:')
        self.p1.hand.showDeck('ROW')
        print('Player1 pile:')
        self.p1.pile.showDeck('ROW')
        print()
        print('Field cards')
        self.fieldCards.showDeck('ROW')
        print()
        print('Player2 cards:')
        self.p2.hand.showDeck('ROW')
        print('Player2 pile:')
        self.p2.pile.showDeck('ROW')


    #Function that evaluates a players pile and determines its score.
    def evaluatePile(self,playerNbr):
        """
        Returns all relevant parameters to evaulate how much points the players pile is worth according to the rules of casino.

        Most cards is 1 point.
        Most spade cards is 2 points.
        Spade of 2 is worth 1 point.
        Diamonds of 10 is worth 2 points.
        Each Ace is worth 1 point.
        Each spare is worth 1 point.

        :param playerNbr:
        :return
        """

        nbrOfCards = player.pile.getDeckSize()
        nbrOfSpades = 0
        spadesTwo = 0
        diamondTen = 0
        aces = 0
        spares = player.getSpares()
        for i in range(nbrOfCards):
            currCard = player.pile.getCard()
            if currCard.getColor() == 'SPADES':
                nbrOfSpades +=1
            if currCard.getColor() == 'SPADES' and currCard.getValue() == 2:
                spadesTwo = 1
            if currCard.getColor() == 'DIAMONDS' and currCard.getValue() == 10:
                diamondTen = 1
            if currCard.getValue == 14 or currCard.getValue == 1:
                aces +=1

        return nbrOfCards, nbrOfCards, spadesTwo, diamondTen, aces, spares

    def changePlayer(self):
        if self.playerTurn == 1:
            self.playerTurn = 2
        elif self.playerTurn == 2:
            self.playerTurn == 1

    def getPlayerTurn(self):
        return self.playerTurn

    def subsetOfCards(self):
        """
        This function evaluates all subsets of the fieldCards and returns a List with all possible combinations of cards in the deck.
        """

        fieldSize = self.fieldCards.getDeckSize()

        def recursiveFunction(q,restVec,Q):
            if len(restVec) > 0:
                for j in range(len(restVec)):
                    q_temp = q.copy()
                    q_temp.append(restVec[j])
                    Q.append(q_temp)
                    #print(f'All values: j:{j}, q:{q}, q_temp: {q_temp}, Q: {Q}, restVec[j+1:-1]: {restVec[j + 1:len(restVec)]}')
                    recursiveFunction(q_temp, restVec[j + 1:len(restVec)], Q)
            #else:
                #print('Finished')

        Q = [[el] for el in self.fieldCards]

        for i in range(fieldSize):
            q = Q[i]
            restVec = self.fieldCards[i:fieldSize]
            recursiveFunction(q, restVec, Q)

        return Q



    #Function that performs a move.
    def move(self, playerNbr):
    #Inleder med att ta storleken på handen
        if self.getPlayerTurn() == 1:
            currPlayer = self.p1
        elif self.getPlayerTurn() == 2:
            currPlayer = self.p2

    def playerMoveAddCardOnTable(self,cardNbr):
        if self.getPlayerTurn() == 1:
            currPlayer = self.p1
        elif self.getPlayerTurn() == 2:
            currPlayer = self.p2
        tempHand = currPlayer.getHand()
        tempCard = tempHand.getCard(cardNbr)
        self.addCardOnTable(tempCard)



    def getMoves(self,playerNbr):

        if playerNbr == 1:
            tempHand = self.p1.getHand()
        elif playerNbr == 2:
            tempHand = self.p2.getHand()

        handSize = tempHand.getDeckSize()

        tempField = self.fieldCards
        fieldSize = tempField.getDeckSize()

        moveList = []
        for i in range(handSize):
            moveList.append(tempHand.getCard())

        fieldList = []
        for j in range(fieldSize):
            fieldList.append(tempField.getCard())

        for i in range(0,1):
            tempCard = moveList[i]
            cardValue = tempCard.getValue()
            cardSum = 0
            tempCard.showCardLine()
            for j in range(0,1):
                if fieldList[j].getValue() == cardValue:
                    moveList[i].append(fieldList[j])
                for k in range(j+1,fieldSize):
                    pass








