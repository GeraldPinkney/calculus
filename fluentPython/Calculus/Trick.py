from fluentPython.Calculus.CardsUtils import valid_card
from fluentPython.Calculus.CardsUtils import g_trumps_broken
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

    def __init__(self, trumps, *players):
        self.players = players[0]
        self.winner = None
        self._cards_played = []
        #for player in self.players:
        #    self._cards_played.append([player.name, None])
        self._trumps = trumps
        self._completed = False

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
        self._completed = True
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
                  #  if num == 0:
                  #      v_valid_card = valid_card(self._trumps, g_trumps_broken, self.players[num], self.players[num].hand._cards[card_index], [])
                   # else:
                    v_valid_card = valid_card(self._trumps, g_trumps_broken, self.players[num], self.players[num].hand._cards[card_index], self._cards_played)
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