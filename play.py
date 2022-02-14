import Calculus
import random



if __name__ == '__main__':
    # Create deck, shuffle cards, get number of players
    deck = Calculus.FrenchDeck()
    deck.shuffle()

    newGame = Calculus.Game(2)
    newGame.startGame()

    # deal hands
    round1 = Calculus.Round(1,deck, newGame._players)
    round1.deal()
    round1.showHand()
    round1.getBets()

    #player1 = Calculus.Player("Gerald")
    #player2 = Calculus.Player("Ruth")



