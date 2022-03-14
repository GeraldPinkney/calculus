from fluentPython.Calculus.FrenchDeck import FrenchDeck


class Round:
    """"""

    def __init__(self, num, deck=FrenchDeck(), *players):
        """"""
        self._tricks = []
        self.round_number = num
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
        self._numOfCards = abs(11 - num)
        self._completed = False

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

    def __str__(self):
        return f'Round Number: {self.round_number}\nNum of Cards: {self._numOfCards}' \
               f'\nplayers: {self.players} ' \
               f'\nactuals: {self.actual}'

    def deal(self):
        """"""
        # deal cards to players
        for player in self.players:
            player.newHand()
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
        self._completed = True

    def playTricks(self):
        #for player in self.players:
       #     player.newHand()
        for each_trick in range(self._numOfCards):
            self._tricks.append(Trick(self._trumps, self.players))
        for num in range(len(self._tricks)):
            print(f'playing trick num: {num+1}\n')
            self._tricks[num].playTrick()
        for num in range(len(self._tricks)):
            self.updateActual(self._tricks[num].getWinner())

        self.internal_score_round()