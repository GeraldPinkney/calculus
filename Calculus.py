import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # creates 52 card deck with suits
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

        self._burnt_cards = []

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def dealCard(self, num=1):
        # returns single card & burns it. DO NOT USE IF NOT SHUFFILED FIRST
        returned = self[-num:]
        self._burnt_cards.append(self[-num:])
        del self._cards[-num]
        return returned

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


class Hand:

    def __init__(self):
        self._cards = []

    def __len__(self):
        return len(self._cards)

    def takecard(self, card):
        self._cards.append(card)

    def __getitem__(self, position):
        return self._cards[position]

    def __str__(self):
        return f'Hand({self._cards})'


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


class Game:
    def __init__(self, numOfPlayers):
        self._players = []
        self._numOfPlayers = numOfPlayers
        # set 10 rounds
        self._rounds = [x for x in range(9)]


    def startGame(self):
        self.setupGame()

    def setupGame(self):
        # get player names.
        for x in range(self._numOfPlayers):
            playername = input("player name: ")
            self._players.append(Player(playername))

        #for player in self._players:
        #    print(player)


class Round:

    def __init__(self, num, deck, *players):
        self.players = players[0]

        self.deck = deck
        # set number of cards in this round
        self._numOfCards = 11 - num

        # set trumps
        if self._numOfCards % 4 == 0:
            self._trumps = 'hearts'
        if self._numOfCards % 4 == 1:
            self._trumps = 'clubs'
        if self._numOfCards % 4 == 2:
            self._trumps = 'diamonds'
        if self._numOfCards % 4 == 3:
            self._trumps = 'spades'

        # TODO set who starts

        # TODO set predicted and actual for each player
        self.predicted = []
        for player in range(len(self.players)):
            self.predicted.append(0)


    def deal(self):
        # TODO deal hand
        for player in self.players:
            for x in range(self._numOfCards):
                player.hand.takecard(self.deck.dealCard())


    def showHand(self):
        for player in self.players:
            print(player)


    def getBets(self):
        iterator = 0
        total = 0
        for player in self.players:
            print(f'Playername: {player.name}')
            print(f'Hand: {player.hand}')
            self.predicted[iterator] = int(input('Bet: '))
            iterator += 1



