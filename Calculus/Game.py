from fluentPython import Calculus
from fluentPython.Calculus import *



class Game:
    def __init__(self, deck=Calculus.FrenchDeck('Y'), numOfPlayers=2, numOfRounds=10):

        self._deck = deck
        self._deck.shuffle()
        self._players = []
        self.numOfRounds = numOfRounds
        if numOfPlayers > 4:
            self._numOfPlayers = 4
        else:
            self._numOfPlayers = numOfPlayers
        # set 10 rounds
        self._rounds = []
        self.trumps_broken = False


    def startGame(self):
        self.setupGame()
        self.initRounds()

    def setupGame(self, *names):
        """get player names."""

        # if player names are not passed into the setupGame method then get them from UI
        if len(names) != self._numOfPlayers:
            for x in range(self._numOfPlayers):
                playername = input("player name: ")
                self._players.append(Player(playername))
        # if player names are  passed into the setupGame method then get them *names
        else:
            for x in range(self._numOfPlayers):
                playername = names[x]
                self._players.append(Player(playername))
        self.initRounds()
        return self._players

    def initRounds(self):
        self._rounds = [Round((x+1), FrenchDeck('Y'), self._players) for x in range(self.numOfRounds)]

    def getPlayers(self):
        return self._players

    def playRounds(self):
        for round in self._rounds:
            round.deal()


    def getCurrentRound(self):
        currentRound = None
        for nextround in self._rounds:
            currentRound = nextround
            if not nextround._completed: break
        return currentRound
