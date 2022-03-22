from fluentPython.Calculus.Hand import Hand


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
        # f'Player: {self.name}, Score: {self._score}, Hand: {self.hand}'
        return f'Player: {self.name}'

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.name == other.name:
            return False
        else:
            return True

    def __lt__(self, other):
        if self._score < other._score:
            return True
        else:
            return False

    def __le__(self, other):
        if self._score <= other._score:
            return True
        else:
            return False

    def __gt__(self, other):
        if self._score > other._score:
            return True
        else:
            return False

    def __le__(self, other):
        if self._score >= other._score:
            return True
        else:
            return False
