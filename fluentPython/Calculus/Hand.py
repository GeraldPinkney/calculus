

class Hand:

    def __init__(self):
        self._cards = []
        self._num_of_hearts = 0
        self._num_of_clubs = 0
        self._num_of_diamonds = 0
        self._num_of_spades = 0

    def __len__(self):
        return len(self._cards)

    def takecard(self, card):
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
            pass
            # throw exception


    def __getitem__(self, position):
        return self._cards[position]

    def playcard(self, card):
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

    def __str__(self):
        return f'Hand({self._cards})'

    def __contains__(self, item):
        return True if item in self._cards else False

    # TODO add sort hand method
    def sort_hand(self, trumps):
        pass
        unsorted_hand = self._cards.copy()
        sorted_hand = []
        hearts_list = []
        hearts_sorted = False
        clubs_list = []
        clubs_sorted = False
        diamonds_list = []
        diamonds_sorted = False
        spades_list = []
        spades_sorted = False

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
        for index in range(len(hearts_list)):
            pass

        # sort the suit groups so trumps are on the far right, with R-B pattern for others
        if trumps == 'hearts':
            sorted_hand.append(spades_list, diamonds_list, clubs_list, hearts_list)
        elif trumps == 'clubs':
            sorted_hand.append(hearts_list, spades_list, diamonds_list, clubs_list)
        elif trumps == 'diamonds':
            sorted_hand.append(clubs_list, hearts_list, spades_list, diamonds_list)
        elif trumps == 'spades':
            sorted_hand.append(diamonds_list, clubs_list, hearts_list, spades_list)

        self._cards = sorted_hand.copy()
        return self._cards
