# Calculus.py

""""""

import collections
import random
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)

Card = collections.namedtuple('Card', ['rank', 'suit'])

def convert_rank_to_number(rank):
    number = 0
    if rank == '1':
        number = 1
    elif rank == '2':
        number = 2
    elif rank == '3':
        number = 3
    elif rank == '4':
        number = 4
    elif rank == '5':
        number = 5
    elif rank == '6':
        number = 6
    elif rank == '7':
        number = 7
    elif rank == '8':
        number = 8
    elif rank == '9':
        number = 9
    elif rank == '10':
        number = 10
    elif rank == 'J':
        number = 11
    elif rank == 'Q':
        number = 12
    elif rank == 'K':
        number = 13
    elif rank == 'A':
        number = 14
    return number


def compare_cards(trumps, card1, card2):
    """compare card1 with card2 and return the higher card. card1 gets precedence."""
    higher_card = Card(rank=0, suit='joker')

    card1_rank, card1_suit = card1
    card2_rank, card2_suit = card2
    if card2_suit == trumps and card1_suit != trumps:
        # if the second card is a trump then it takes precedence
        higher_card = card2
    elif card2_suit == card1_suit:
        # if they are the same suit, then higher card wins
        if convert_rank_to_number(card1_rank) > convert_rank_to_number(card2_rank):
            higher_card = card1
        else:
            higher_card = card2
    else:
        # if suits are mismatched, and card2 is not a trump, then card1 wins
        higher_card = card1
    return higher_card


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

    def playcard(self, card):
        self._cards.remove(card)
        return card

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
    def __init__(self, numOfPlayers=2):
        self._players = []
        if numOfPlayers >4:
            self._numOfPlayers = 4
        else:
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

        # for player in self._players:
        #    print(player)


class Round:
    """"""

    def __init__(self, num, deck, *players):
        """"""
        self._tricks = []
        self.players = players[0]
        self.predicted = []
        self.actual = []
        for player in self.players:
            self.actual.append([player.name, 0])
        self.deck = deck
        # store bets as a list of tuples as they don't change.
        self.bets = []
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
        print(f'Trumps are: {self._trumps}')
        # TODO set who starts

    def deal(self):
        """"""
        # deal cards to players
        for player in self.players:
            for x in range(self._numOfCards):
                player.hand.takecard(self.deck.dealCard())
        return 0

    def showHand(self):
        # TODO change method to take player as param and only return hand of that player(s).
        for player in self.players:
            print(player.hand)

    def show_actual(self):
        for record in self.actual:
            print(f'playername: {record[0]}, current actual: {record[1]}')

    def getBets(self):
        iterator = 0
        total = 0
        for player in self.players:
            print(f'Playername: {player.name}')
            print(f'Hand: {player.hand}')
            print(f'Num of Cards: {self._numOfCards}, current bet: {self.predicted[iterator]}, running total: {total}')

            self.predicted[iterator] = int(input('Bet: '))
            while ((self.predicted[iterator] + total == self._numOfCards) and iterator == len(self.players)) and not (
                    self.predicted[iterator] > self._numOfCards):
                # show conditional error messages
                if ((self.predicted[iterator] + total == self._numOfCards) and iterator == len(self.players)):
                    print('\nRules disallow bet that equals total num of cards if you are last to place bet')
                elif not (self.predicted[iterator] > self._numOfCards):
                    print('\nRules disallow bet that exceed total num of cards')
                # then show current state of bets and get a new bet
                print(
                    f'Num of Cards: {self._numOfCards}, current bet: {self.predicted[iterator]}, running total: {total}')
                self.predicted[iterator] = int(input('Bet: '))
            total = total + self.predicted[iterator]
            iterator += 1
        return self.predicted

    def getBets2(self):
        iterator = 0
        total = 0
        for player in self.players:
            print(f'Playername: {player.name}')
            print(f'Hand: {player.hand}')
            print(f'Num of Cards: {self._numOfCards}, current bet: {self.predicted[iterator]}, running total: {total}')

            self.predicted[iterator] = int(input('Bet: '))
            self.bets.append((player.name, self.predicted[iterator]))
            total = total + self.predicted[iterator]
            iterator += 1
        return self.bets

    def show_bets(self):
        print(self.bets)

    def updateActual(self, playername):
        new_actual = -1
        for record in self.actual:
            print(record)
            if record[0] == playername:
                record[1] += 1
                #print(f'playername: {record[0]}, current actual: {record[1]}')
                new_actual = record[1]
        return (new_actual, playername)

    def playTricks(self):
        for each_trick in range(self._numOfCards):
            self._tricks.append(Trick(self._trumps, self.players))
        for num in range(len(self._tricks)):
            print(f'playing trick num: {num}\n')
            self._tricks[num].playTrick()
        for num in range(len(self._tricks)):
            self.updateActual(self._tricks[num].getWinner())


class Trick:
    """an individual trick within a round.
    # variables:
    #  what cards each player plays
    #  who wins tricks
    # methods
    #  get cards
    #  calc winner
    """

    def __init__(self, trumps, *players):
        self.players = players[0]
        self.winner = None
        self._cards_played = []
        for player in self.players:
            self._cards_played.append([player.name, None])
        self._trumps = trumps

    def playCard(self, playername, card):
        for record in self._cards_played:
            if record[0] == playername:
                record[1] = card
                print(f'playername: {record[0]}, card: {record[1]}')
        return (playername, card)

    def calcWinner(self):
        tempwinner1 = self._cards_played[0]
        tempwinner0 = tempwinner1[1]
        tempwinner = tempwinner0[0]

        for card in self._cards_played:
            # sort through cards. sort order is by suit, then by number. owner of highest card wins
            # compare 2 cards and swap positions of smaller
            input_card = card[1]
            if tempwinner == compare_cards(self._trumps, tempwinner, input_card[0]):
                pass
            else:
                tempwinner = card
        for record in self._cards_played:
            if record[1] == tempwinner:
                self.winner = record[0]
        self.winner = self.players[0]
        return (self.winner)

    def playTrick(self):
        for num in range(len(self.players)):
            card_index = -1
            print(f'{self.players[num].name}\'s turn.\n {self.players[num].hand}')

            while card_index < 0 or card_index > len(self.players[num].hand):
                card_index = int(input(f'provide index of card, 0 to {len(self.players[num].hand) - 1}: '))
            # print(f'player {self.players[num].name}. card played: {self.players[num].hand._cards[card_index]}')
            self.playCard(self.players[num].name,
                          self.players[num].hand.playcard(self.players[num].hand._cards[card_index]))

        winner = self.calcWinner()
        print(f'winner: {winner.name}')
        return winner

    def getWinner(self):
        return(self.winner)