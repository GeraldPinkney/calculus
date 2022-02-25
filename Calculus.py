# Calculus.py

""""""

import collections
import random
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)

Card = collections.namedtuple('Card', ['rank', 'suit'])
g_trumps_broken = False


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


def valid_card(trumps, trumps_broken, player, card, *played):
    """
    you cannot lead with a trump unless trumps are broken
    you have to follow suit if you can
    if you cannot follow suit, you can play any card

    :param trumps:
    :param trumps_broken:
    :param played:
    :return allowed:
    """
    allowed = False
    cards_played = played[0]

    card_rank, card_suit = card
    # you cannot lead with a trump unless trumps are broken or you only have trumps left
    if len(cards_played) == 0: # this means that you are leading
        if trumps_broken==False: # this means you cannot play a trump
            if card_suit != trumps: # if don't play trumps, its fine
                allowed = True
            else: # if do play trumps, that must be all you have
                for card in player.hand:
                    v_card_rank, v_card_suit = card
                    if v_card_suit != trumps:
                        allowed = False
                        break
                    else:
                        allowed = True
        else:
            allowed = True
    else:
        # you have to follow suit if you can
        first_card = cards_played[0]
        first_card_rank, first_card_suit = first_card
        if first_card_suit == card_suit:
            allowed = True
        else:
            # check if the player has any of the first card's suit in their hand
            for card in player.hand:
                v_card_rank, v_card_suit = card
                if v_card_suit == first_card_suit:
                    allowed = False
                    break
                else:
                    # if you cannot follow suit, you can play any card
                    allowed = True

    return allowed


class FrenchDeck:
    """

    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self,shuffled='Y'):
        """
        # creates 52 card deck with suits
        :param shuffled:
        """

        self._cards = [Card(rank, suit) for suit in self.suits
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
        del self._cards[-num]
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
    def __init__(self, deck=FrenchDeck(), numOfPlayers=2, numOfRounds=10):

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


    def startGame(self):
        self.setupGame()
        self.initRounds()

    def setupGame(self, *names):
        """get player names."""

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
        return self._players

    def initRounds(self):
        self._rounds = [Round((x+1), self._deck, self._players) for x in range(self.numOfRounds)]

    def getPlayers(self):
        return self._players

    def playRounds(self):
        for round in self._rounds:
            round.deal()


class Round:
    """"""

    def __init__(self, num, deck=FrenchDeck(), *players):
        """"""
        self._tricks = []
        self.players = players[0]
        #self.predicted = []
        self.actual = []
        for player in self.players:
            self.actual.append([player.name, 0])
        self.deck = deck
        self.deck.shuffle()
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
        #print(f'Trumps are: {self._trumps}')
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

    def getBets(self, *bets):
        iterator = 0
        total = 0
        # TODO add rules to disallow bet that exceeds total number of cards. disallow bet if this is the last bet and total equals total num of cards
        if len(bets) == 0:
            # if getBets is called without bets passed into it, we must get via input()
            for player in self.players:
                print(f'Playername: {player.name}')
                print(f'Hand: {player.hand}')
                placeholder = int(input('Bet: '))
                self.bets.append((player.name, placeholder))
                total = total + placeholder
                print(f'Num of Cards: {self._numOfCards}, current bet: {placeholder}, running total: {total}')
                iterator += 1
        else:
            temp_bets = bets[0]

            for each_bet in temp_bets:
                self.bets.append(each_bet)
        return self.bets

    def show_bets(self):
        print(self.bets)
        for bet in self.bets:
            print(f'playername: {bet[0]}. bet: {bet[1]}')

    def show_trumps(self):
        return self._trumps

    def updateActual(self, playername):
        new_actual = -1
        for record in self.actual:

            if record[0] == playername:
                record[1] += 1
                #print(f'playername: {record[0]}, current actual: {record[1]}')
                new_actual = record[1]

        return (new_actual, playername)

    def show_actual(self):
        #print(self.actual)
        for record in self.actual:
            print(f'playername: {record[0]}, current actual: {record[1]}')
        return self.actual

    def internal_compare_bet_and_actual(self, playername):
        # if actual != bet, return the difference between actual and bet as a negative.
        # if actual == bet, return abs(actual)
        result = -1000
        tmp_actual = -1
        tmp_bet = -1
        for record in self.actual:
            if record[0] == playername:
                tmp_actual = record[1]

        for record in self.bets:
            if record[0] == playername:
                tmp_bet = record[1]

        if tmp_actual == tmp_bet:
            # if actual == bet, return abs(actual)
            result = abs(tmp_actual)+10
        else:
            # if actual != bet, return the difference between actual and bet as a negative.
            result = (abs(tmp_bet - tmp_actual))*-1
        return result

    def internal_score_round(self):
        #for num in range(len(self.players)):
        for player in self.players:
            # compare the players bet against their actual. if they are the same, update score
            player.UpdateScore(self.internal_compare_bet_and_actual(player.name))

    def playTricks(self):
        for each_trick in range(self._numOfCards):
            self._tricks.append(Trick(self._trumps, self.players))
        for num in range(len(self._tricks)):
            print(f'playing trick num: {num+1}\n')
            self._tricks[num].playTrick()
        for num in range(len(self._tricks)):
            self.updateActual(self._tricks[num].getWinner())

        self.internal_score_round()


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
        #for player in self.players:
        #    self._cards_played.append([player.name, None])
        self._trumps = trumps

    def playCard(self, playername, card):
        """"""
        global g_trumps_broken
        input_card = card[0]
        self._cards_played.append([playername, *input_card])
        for record in self._cards_played:
            if record[0] == playername:
                record[1] = card
                print(f'playername: {record[0]}, card: {record[1]}')
                card_rank, card_suit = card
                if card_suit == self._trumps:
                    g_trumps_broken = True

        return (playername, card)

    def calcWinner(self):
        # set the temp winner as the card play by lead
        tempwinner1 = self._cards_played[0]
        tempwinner = tempwinner1[1]

        for card in self._cards_played:
            # sort through cards. sort order is by suit, then by number. owner of highest card wins
            # compare 2 cards and swap positions of smaller
            played_card = card[1]
            if tempwinner == compare_cards(self._trumps, tempwinner, played_card):
                pass
            else:
                tempwinner = card[1]
        for record in self._cards_played:
            if record[1] == tempwinner:
                self.winner = record[0]
        #self.winner = self.players[0]
        return (self.winner)

    def playTrick(self, *played):
        global g_trumps_broken
        if len(played) == 0:
            for num in range(len(self.players)):
                card_index = -1
                v_valid_card = False
                print(f'{self.players[num].name}\'s turn.\n {self.players[num].hand}')

                while (card_index < 0 or card_index > len(self.players[num].hand) and not v_valid_card) :
                    card_index = int(input(f'provide index of card, 0 to {len(self.players[num].hand) - 1}: '))
                    # check if choice is valid
                    v_valid_card = valid_card(trumps=self._trumps[0], trumps_broken=g_trumps_broken, player=self.players[num],
                                       card=self.players[num].hand._cards[card_index], *self._cards_played)
                # print(f'player {self.players[num].name}. card played: {self.players[num].hand._cards[card_index]}')

                # play card
                self.playCard(self.players[num].name,self.players[num].hand.playcard(self.players[num].hand._cards[card_index]))


        else:
            temp_played = played
            for played in temp_played:
                name, index = played
                self.playCard(name, index)
        winner = self.calcWinner()
        #print(f'winner: {winner}')
        return winner

    def getWinner(self):
        return(self.winner)


class InterfaceLayer:
    def __init__(self):
        current_menu = 'Main'