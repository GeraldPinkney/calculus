import Calculus
import random



if __name__ == '__main__':
    # Create deck, shuffle cards, get number of players
    deck = Calculus.FrenchDeck('Y')

    newGame = Calculus.Game(deck=deck, numOfPlayers=2, numOfRounds=10)
    newGame.startGame()

    newGame.playRounds()


    # deal hands
    #round1 = Calculus.Round(9,deck, newGame._players)
    #round1.deal()
    #round1.showHand()
    #round1.getBets()
    #round1.show_bets()

    #round1.playTricks()
    #round1.show_actual()



    #player1 = Calculus.Player("Gerald")
    #player2 = Calculus.Player("Ruth")



