import Hand

class Player:
    def __init__(self, name):
        self._score = 100
        self.name = name
        self.hand = Hand()

    def UpdateScore(self, roundEffect):
        self._score += roundEffect

    def newHand(self):
        self.hand = Hand()

    def __str__(self):
        return f'Player: {self.name}, Score: {self._score}, Hand: {self.hand}'

    def __repr__(self):
        return f'Player: {self.name}, Score: {self._score}, Hand: {self.hand}'
