# FrenchDeck.py
"""contains the FrenchDeck class"""
import random

from fluentPython.Calculus import CardsUtils

class FrenchDeck:
    """
    methods: dealCard(), shuffle()

    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self,shuffled='Y'):
        """
        # creates 52 card deck with suits
        :param shuffled:
        """

        self._cards = [CardsUtils.Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

        self._burnt_cards = []

        if shuffled == 'Y':
            self.shuffle()


    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def dealCard(self, num=1):
        # returns single card & burns it. DO NOT USE IF NOT SHUFFILED FIRST
        returned = self[-num:]
        self._burnt_cards.append(self[-num:])
        del self._cards[-num:]
        return returned[0]

    def shuffle(self):
        if len(self._cards) != 52:
            raise Exception("needs full deck to shuffle")
            return -1
        else:
            for num in range(len(self._cards)):
                r = num + (random.randint(0, 55) % (52 - num))
                tmp = self._cards[num]
                self._cards[num] = self._cards[r]
                self._cards[r] = tmp
            return 0

    def __str__(self):
        return f'Deck: ({self._cards})'
