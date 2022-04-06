# Hand.py
"""contains bubble sort method & the Hand class. """

from fluentPython.Calculus.CardsUtils import compare_cards


def bubble_sort_cards(cards):
    """returns a bool to indicate if its sorted."""
    swapped = True
    if len(cards) == 0:
        swapped = False
    elif len(cards) == 1:
        swapped = False
    else:
        while swapped == True:
            for i in range(1, len(cards)):
                # check if second card is higher than first
                if compare_cards('hearts', cards[i - 1], cards[i]) == cards[i - 1]:
                    # if second card is higher, then swap
                    tmp = cards[i]
                    cards[i] = cards[i - 1]
                    cards[i - 1] = tmp
                    # cards[i-1], cards[i] = cards[i], cards[i-1]
                    swapped = True
                else:
                    swapped = False
    return not swapped


class Hand():

    def __init__(self):
        self._cards = []
        self._num_of_hearts = 0
        self._num_of_clubs = 0
        self._num_of_diamonds = 0
        self._num_of_spades = 0

    def __len__(self):
        return len(self._cards)

    def takecard(self, card):
        """ append the card to the internally maintained cardlist and increment the count of suits"""
        self._cards.append(card)
        if card[1] == 'hearts':
            self._num_of_hearts += 1
        elif card[1] == 'clubs':
            self._num_of_clubs += 1
        elif card[1] == 'diamonds':
            self._num_of_diamonds += 1
        elif card[1] == 'spades':
            self._num_of_spades += 1
        else:
            raise AttributeError()
            # throw exception

    def __getitem__(self, position):
        return self._cards[position]

    def playcard(self, card):
        """remove the card to the internally maintained cardlist and decrement the count of suits. Returns card."""
        #
        self._cards.remove(card)
        if card[1] == 'hearts':
            self._num_of_hearts -= 1
        elif card[1] == 'clubs':
            self._num_of_clubs -= 1
        elif card[1] == 'diamonds':
            self._num_of_diamonds -= 1
        elif card[1] == 'spades':
            self._num_of_spades -= 1
        else:
            pass
            # throw exception
        return card

    def index(self, card):
        return self.__index__(card)

    def __index__(self, card):
        """returns integer index of first instance of the card"""
        # add checking for if parameter is a Card if type(card)
        index = -1
        if not self.__contains__(card):
            raise ValueError(f'{card} is not in hand')
        else:
            try:
                for i in range(self.__len__()):
                    if self._cards[i] == card:
                        index = i
                        break
            except Exception:
                raise Exception
            else:
                if index == -1:
                    raise Exception
                else:
                    return index

    def indexOf(self, card):
        return self.__index__(card)

    def __str__(self):
        return f'Hand({self._cards})'

    def __contains__(self, item):
        return True if item in self._cards else False

    def sort(self, trumps):
        """takes trumps as a parameter
        sorts the current hand & returns a sorted hand
        """
        unsorted_hand = self._cards.copy()
        sorted_hand = []
        hearts_list = []
        clubs_list = []
        diamonds_list = []
        spades_list = []

        # group the cards into suits
        for card in unsorted_hand:
            if card[1] == 'hearts':
                hearts_list.append(card)
            elif card[1] == 'clubs':
                clubs_list.append(card)
            elif card[1] == 'diamonds':
                diamonds_list.append(card)
            elif card[1] == 'spades':
                spades_list.append(card)
            else:
                pass
                # throw exception

        # sort the cards within the suit-groups
        bubble_sort_cards(hearts_list)
        bubble_sort_cards(clubs_list)
        bubble_sort_cards(diamonds_list)
        bubble_sort_cards(spades_list)

        # sort the suit groups so trumps are on the far right, with R-B pattern for others
        if trumps == 'hearts':  # SDCH
            for card in spades_list:
                sorted_hand.append(card)
            for card in diamonds_list:
                sorted_hand.append(card)
            for card in clubs_list:
                sorted_hand.append(card)
            for card in hearts_list:
                sorted_hand.append(card)
        elif trumps == 'clubs':  # HSDC
            for card in hearts_list:
                sorted_hand.append(card)
            for card in spades_list:
                sorted_hand.append(card)
            for card in diamonds_list:
                sorted_hand.append(card)
            for card in clubs_list:
                sorted_hand.append(card)
        elif trumps == 'diamonds':  # CHSD
            for card in clubs_list:
                sorted_hand.append(card)
            for card in hearts_list:
                sorted_hand.append(card)
            for card in spades_list:
                sorted_hand.append(card)
            for card in diamonds_list:
                sorted_hand.append(card)
        elif trumps == 'spades':  # DCHS
            for card in diamonds_list:
                sorted_hand.append(card)
            for card in clubs_list:
                sorted_hand.append(card)
            for card in hearts_list:
                sorted_hand.append(card)
            for card in spades_list:
                sorted_hand.append(card)
        self._cards = sorted_hand.copy()
        return self._cards
