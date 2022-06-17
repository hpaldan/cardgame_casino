
from casinoEnv import casinoEnv

from lib import deck, card




def main():




    #Testcase:
    mainDeck = deck(True)
    mainDeck.shuffleDeck()
    env = casinoEnv(mainDeck)
    card1 = card('SPADES',8)
    card2 = card('SPADES', 4)
    #card3 = card('SPADES', 6)
    #card4 = card('HEARTS', 6)
    #card5 = card('HEARTS', 2)
    #card6 = card('SPADES', 2)

    #env.giveCardToPlayer(playerCard,1)

    env.addCardOnTable(card1)
    env.addCardOnTable(card2)
    #env.addCardOnTable(card3)
    #env.addCardOnTable(card4)
    #env.addCardOnTable(card5)
    #env.addCardOnTable(card6)

    env.renderGame()







if __name__ == "__main__":
    main()


