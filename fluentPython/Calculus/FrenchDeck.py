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

    def __init__(self, shuffled='Y'):
        """
        # creates 52 card deck with suits
        :param shuffled:
        """
        self._state = 0  # 0 = new deck, 1 means its been used (less than 52 cards)
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
        self._state = 1
        return returned[0]

    def shuffle(self):
        if self._state == 1:  # check to see if its a new deck
            raise Exception("needs full deck to shuffle")
            return -1
        else:
            for num in range(len(self._cards)):
                r = num + (random.randint(0, 55) % (len(self._cards) - num))
                tmp = self._cards[num]
                self._cards[num] = self._cards[r]
                self._cards[r] = tmp
            return 0

    def __str__(self):
        return f'Deck: ({self._cards})'
