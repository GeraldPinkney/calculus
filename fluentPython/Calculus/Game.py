
from fluentPython.Calculus.FrenchDeck import FrenchDeck
from fluentPython.Calculus.Player import Player
from fluentPython.Calculus.Round import Round


class Game:
    def __init__(self, deck=FrenchDeck('Y'), numOfPlayers=2, numOfRounds=10):

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
        self._game_state = 0

    def get_game_state(self):
        """returns an int that indicates game state
            0 = awaiting setupGame
            1 = setup complete, actions are getplayers, getcurrentround
        """
        return self._game_state


    def startGame(self):
        self.setupGame()

    def setupGame(self, *names):
        """
        setupGame(*names)
        returns players
        sets up the game by creating players using playernames provided, or if not provided gathers from print calls
        then calls initRounds()
        """

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
        self._game_state = 1
        return self._players

    def initRounds(self):
        self._rounds = [Round((x+1), FrenchDeck('Y'), self._players) for x in range(self.numOfRounds, 0,-1)]

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
