import Calculus
import random



if __name__ == '__main__':
    # Create deck, shuffle cards, get number of players
    deck = Calculus.FrenchDeck('Y')

    newGame = Calculus.Game(deck=deck, numOfPlayers=2, numOfRounds=10)
    newGame.startGame()

    current_round = newGame.getCurrentRound()
    current_round.deal()
    current_round.showHand()
    current_round.show_trumps()
    current_round.getBets()
    current_round.playTricks()
    current_round.show_actual()
    #newGame.playRounds()
    #for round in newGame._rounds:
    #    round.deal()
    #    round.showHand()
    #    round.show_trumps()
    #    round.getBets()
    #    round.playTricks()
    #    round.show_actual()

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



