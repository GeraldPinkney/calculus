# Trick.py
"""contains the Trick class"""

from fluentPython.Calculus.CardsUtils import valid_card
from fluentPython.Calculus.CardsUtils import compare_cards


class Trick:
    """an individual trick within a round.
    # variables:
    #  what cards each player plays
    #  who wins tricks
    # methods
    #  get cards
    #  calc winner
    """

    def __init__(self, trumps, players, trumps_broken=False):
        self.players = players
        self.winner = None
        self._cards_played = []
        # for player in self.players:
        #    self._cards_played.append([player.name, None])
        self._trumps = trumps
        self._completed = False
        self._trumps_broken = trumps_broken

    def __str__(self):
        return f'Trick:   ' \
               f'\nCards Played: {self._cards_played}' \
               f'\nplayers:      {self.players} ' \
               f'\nTrumps:       {self._trumps}' \
               f'\nTrumps Broken:{self._trumps_broken}'

    def playCard(self, playername, card):
        """
        play a card, parameters PlayerName, Card
        returns playername, Card

        """
        input_card = card[0]
        self._cards_played.append([playername, *input_card])
        for record in self._cards_played:
            if record[0] == playername:
                record[1] = card
                print(f'playername: {record[0]}, card: {record[1]}')
                card_rank, card_suit = card
                if card_suit == self._trumps:
                    self.set_trumps_broken(True)

        return (playername, card)

    def reorder_players(self, newLead):
        if len(self.players) == 2:
            if self.players[0] != newLead:
                tmp = self.players[0]
                self.players[0] = self.players[1]
                self.players[1] = tmp

        elif len(self.players) == 3:
            if self.players[0] != newLead:
                if self.players[1] == newLead:
                    tmp = self.players[0]
                    self.players[0] = self.players[1]
                    self.players[1] = self.players[2]
                    self.players[2] = tmp
                elif self.players[2] == newLead:
                    tmp = self.players[0]
                    self.players[0] = self.players[2]
                    self.players[2] = self.players[1]
                    self.players[1] = tmp

        elif len(self.players) == 4:
            pass
            #ToDo will need to implement this later.
        else:
            pass

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
        # self.winner = self.players[0]
        self._completed = True

        # now reorder the players to set the new lead based off the winner of the last one
        self.reorder_players(self.get_player_from_name(self.winner))
        return self.winner

    def get_player_from_name(self, player_name):
        returned = None
        for player in self.players:
            if player_name == player.name:
                returned = player
        return returned

    def playTrick(self, *played):

        if len(played) == 0:
            for num in range(len(self.players)):
                card_index = -1
                v_valid_card = False
                print(f'{self.players[num].name}\'s turn.\n {self.players[num].hand}')
                # ToDo change how this works so it throws an exception if invalid card, but catches it and handles it
                #while (card_index < 0 or card_index > len(self.players[num].hand) and not v_valid_card):
                while not v_valid_card:
                    card_index = int(input(f'provide index of card, 0 to {len(self.players[num].hand) - 1}: '))
                    # check if choice is valid
                    v_valid_card = valid_card(self._trumps, self.get_trumps_broken(), self.players[num],
                                              self.players[num].hand._cards[card_index], self._cards_played)
                # play card
                self.playCard(self.players[num].name,
                              self.players[num].hand.playcard(self.players[num].hand._cards[card_index]))
        else:
            temp_played = played
            for played in temp_played:
                name, index = played
                self.playCard(name, index)
        winner = self.calcWinner()
        # print(f'winner: {winner}')
        return winner

    def getWinner(self):
        return (self.winner)

    def set_trumps_broken(self, value):
        self._trumps_broken = value

    def get_trumps_broken(self):
        return self._trumps_broken

    def get_trick_state(self):
        """"""
        if self._completed:
            return 1
        else:
            return 0
