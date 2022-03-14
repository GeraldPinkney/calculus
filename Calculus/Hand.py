

class Hand:

    def __init__(self):
        self._cards = []

    def __len__(self):
        return len(self._cards)

    def takecard(self, card):
        self._cards.append(card)

    def __getitem__(self, position):
        return self._cards[position]

    def playcard(self, card):
        self._cards.remove(card)
        return card

    def __str__(self):
        return f'Hand({self._cards})'


    def __contains__(self, item):
        return True if item in self._cards else False
