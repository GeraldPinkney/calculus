import unittest
from fluentPython.Calculus import FrenchDeck, CardsUtils, Player, Round, Trick, Game


class CompareTestCase(unittest.TestCase):
    def test_compare0(self):
        # first card is trumps.
        result = CardsUtils.compare_cards('hearts', CardsUtils.Card(rank='9', suit='hearts'),
                                        CardsUtils.Card(rank='8', suit='spades'))
        self.assertEqual(CardsUtils.Card(rank='9', suit='hearts'), result)

    def test_compare1(self):
        # second card is trumps.
        result = CardsUtils.compare_cards('hearts', CardsUtils.Card(rank='9', suit='spades'),
                                        CardsUtils.Card(rank='8', suit='hearts'))
        self.assertEqual(CardsUtils.Card(rank='8', suit='hearts'), result)

    def test_compare2(self):
        # both cards trumps. first higher.
        result = CardsUtils.compare_cards('hearts', CardsUtils.Card(rank='9', suit='hearts'),
                                        CardsUtils.Card(rank='8', suit='hearts'))
        self.assertEqual(CardsUtils.Card(rank='9', suit='hearts'), result)

    def test_compare3(self):
        # both cards trumps. second higher.
        result = CardsUtils.compare_cards('hearts', CardsUtils.Card(rank='9', suit='hearts'),
                                        CardsUtils.Card(rank='10', suit='hearts'))
        self.assertEqual(CardsUtils.Card(rank='10', suit='hearts'), result)

    def test_compare4(self):
        # both cards non-trumps. first higher.
        result = CardsUtils.compare_cards('hearts', CardsUtils.Card(rank='A', suit='spades'),
                                        CardsUtils.Card(rank='10', suit='spades'))
        self.assertEqual(CardsUtils.Card(rank='A', suit='spades'), result)

    def test_compare5(self):
        # both cards non-trumps. second higher.
        result = CardsUtils.compare_cards('hearts', CardsUtils.Card(rank='K', suit='spades'),
                                        CardsUtils.Card(rank='A', suit='spades'))
        self.assertEqual(CardsUtils.Card(rank='A', suit='spades'), result)

    def test_compare6(self):
        # both cards non-trumps, but different. second higher.
        result = CardsUtils.compare_cards('hearts', CardsUtils.Card(rank='K', suit='spades'),
                                        CardsUtils.Card(rank='A', suit='diamonds'))
        self.assertEqual(CardsUtils.Card(rank='K', suit='spades'), result)

    def test_compare7(self):
        # both cards non-trumps, but different. first higher.
        result = CardsUtils.compare_cards('hearts', CardsUtils.Card(rank='A', suit='spades'),
                                        CardsUtils.Card(rank='K', suit='diamonds'))
        self.assertEqual(CardsUtils.Card(rank='A', suit='spades'), result)

    def test_compare8(self):
        # both cards non-trumps, but different. first higher.
        result = CardsUtils.compare_cards('hearts', CardsUtils.Card(rank='A', suit='spades'),
                                        CardsUtils.Card(rank='3', suit='spades'))
        self.assertEqual(CardsUtils.Card(rank='A', suit='spades'), result)

class HandSortingTestCase(unittest.TestCase):
    deck = FrenchDeck()
    players = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    for player in players:
        if player.name == 'Gerald':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='spades'))
        if player.name == 'Ruth':
            player.hand.takecard(CardsUtils.Card(rank='4', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='5', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='A', suit='diamonds'))
        if player.name == 'Patrick':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='hearts'))

    def testSortHand0(self):
        self.players[0].hand.sort_hand('spades')
        print(self.players[0])


class PlayCardTestCase(unittest.TestCase):
    deck = FrenchDeck()
    players = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    for player in players:
        if player.name == 'Gerald':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='spades'))
        if player.name == 'Ruth':
            player.hand.takecard(CardsUtils.Card(rank='4', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='5', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='A', suit='diamonds'))
        if player.name == 'Patrick':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='hearts'))

    def testPlayCard0(self):
        testTrick = Trick('hearts', self.players)
        for player in self.players:
            if player.name == 'Gerald':
                testTrick.playCard(player.name, player.hand.playcard(player.hand._cards[1]))
            elif player.name == 'Ruth':
                testTrick.playCard(player.name, player.hand.playcard(player.hand._cards[1]))
            elif player.name == 'Patrick':
                testTrick.playCard(player.name, player.hand.playcard(player.hand._cards[2]))
        self.assertEqual(testTrick._cards_played, [['Gerald', CardsUtils.Card(rank='2', suit='hearts')], ['Ruth', CardsUtils.Card(rank='5', suit='spades')], ['Patrick', CardsUtils.Card(rank='3', suit='hearts')]])


class PlayTrickTestCase(unittest.TestCase):
    deck = FrenchDeck()
    players = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    for player in players:
        if player.name == 'Gerald':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='spades'))
        if player.name == 'Ruth':
            player.hand.takecard(CardsUtils.Card(rank='4', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='5', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='A', suit='diamonds'))
        if player.name == 'Patrick':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='hearts'))

    def testTakeCard0(self):
        self.assertEqual(1, self.players[0].hand._num_of_hearts)
        self.assertEqual(2, self.players[0].hand._num_of_spades)

    def testPlayTrick1(self):
        # g plays 1, R plays 1, P plays 2
        testTrick = Trick('hearts', self.players)
        print('g plays 1, R plays 1, P plays 2')
        testTrick.playTrick()
        print(testTrick._cards_played)
        self.assertEqual(testTrick.winner, 'Patrick')


class PlayTrickTestCase1(unittest.TestCase):
    deck = FrenchDeck()
    players = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    for player in players:
        if player.name == 'Gerald':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='spades'))
        if player.name == 'Ruth':
            player.hand.takecard(CardsUtils.Card(rank='4', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='5', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='A', suit='diamonds'))
        if player.name == 'Patrick':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='hearts'))

    def testPlayTrick(self):
        # test without UI
        testTrick = Trick('hearts', self.players)

        testTrick.playTrick((self.players[0].name, self.players[0].hand._cards[1]), (self.players[1].name, self.players[1].hand._cards[1]), (self.players[2].name, self.players[2].hand._cards[2]))
        print(testTrick._cards_played)
        self.assertEqual(testTrick.winner, 'Patrick')


class PlayTrickTestCase2(unittest.TestCase):
    deck = FrenchDeck()
    players = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    for player in players:
        if player.name == 'Gerald':
            player.hand.takecard(deck.dealCard())
            player.hand.takecard(deck.dealCard())
            player.hand.takecard(deck.dealCard())
        if player.name == 'Ruth':
            player.hand.takecard(deck.dealCard())
            player.hand.takecard(deck.dealCard())
            player.hand.takecard(deck.dealCard())
        if player.name == 'Patrick':
            player.hand.takecard(deck.dealCard())
            player.hand.takecard(deck.dealCard())
            player.hand.takecard(deck.dealCard())

    def testPlayedCards(self):
        self.assertEqual(3,len(self.players[0].hand))


class CalcWinnerTestCase(unittest.TestCase):
    deck = FrenchDeck()
    players = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    for player in players:
        if player.name == 'Gerald':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='spades'))
        if player.name == 'Ruth':
            player.hand.takecard(CardsUtils.Card(rank='4', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='5', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='A', suit='diamonds'))
        if player.name == 'Patrick':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='hearts'))

    def testCalcWinnerTrick2(self):
        # test calcWinner. win with trump
        testTrick = Trick('hearts', self.players)
        testTrick._cards_played.append(['Gerald', CardsUtils.Card(rank='2', suit='hearts')])
        testTrick._cards_played.append(['Ruth', CardsUtils.Card(rank='4', suit='hearts')])
        testTrick._cards_played.append(['Patrick', CardsUtils.Card(rank='3', suit='hearts')])
        #print(testTrick._cards_played)
        winner = testTrick.calcWinner()
        self.assertEqual(winner, 'Ruth')

    def testCalcWinnerTrick3(self):
        # test calcWinner. win with high card
        testTrick = Trick('hearts', self.players)
        testTrick._cards_played.append(['Gerald', CardsUtils.Card(rank='3', suit='spades')])
        testTrick._cards_played.append(['Ruth', CardsUtils.Card(rank='A', suit='clubs')])
        testTrick._cards_played.append(['Patrick', CardsUtils.Card(rank='A', suit='spades')])
        #print(testTrick._cards_played)
        winner = testTrick.calcWinner()
        self.assertEqual(winner, 'Patrick')


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here


class RoundTestCase(unittest.TestCase):
    deck = FrenchDeck()
    players = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    for player in players:
        if player.name == 'Gerald':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='spades'))
        if player.name == 'Ruth':
            player.hand.takecard(CardsUtils.Card(rank='4', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='5', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='A', suit='diamonds'))
        if player.name == 'Patrick':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='hearts'))

    def testgetBets1(self):
        # test passing in bets into the getBets method
        round1 = Round(9, FrenchDeck(), self.players)
        input_bets = [('Gerald', 1), ('Ruth', 2), ('Patrick', 3)]
        round1.getBets(input_bets)
        self.assertEqual([('Gerald', 1), ('Ruth', 2), ('Patrick', 3)],round1.bets)

    def testgetBets2(self):
        # test not passing in bets. then use UI to enter
        round1 = Round(9, FrenchDeck(), self.players)
        print('Gerald-1, Ruth-2, Patrick-3')
        round1.getBets()
        self.assertEqual([('Gerald', 1), ('Ruth', 2), ('Patrick', 3)], round1.bets)

    def testRoundDeal0(self):
        round1 = Round(1, FrenchDeck(), self.players)
        for player in self.players:
            player.newHand()
            self.assertEqual(0, len(player.hand))
        round1.deal()
        for player in self.players:
            self.assertEqual(10, len(player.hand))
            print(player.hand)

    deck1 = FrenchDeck()
    players1 = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    def testPlayRound(self):
        round2 = Round(1, self.deck, self.players1)
        round2.deal()
        for player in self.players1:
            self.assertEqual(10, len(player.hand))

    def testcompare_bet_and_actual0(self):
        # test if bet matches actual
        round1 = Round(9, FrenchDeck(), self.players)
        input_bets = [('Gerald', 1), ('Ruth', 2), ('Patrick', 0)]
        round1.getBets(input_bets)
        round1.updateActual('Gerald')
        round1.updateActual('Ruth')
        round1.updateActual('Ruth')
        self.assertEqual(11, round1.internal_compare_bet_and_actual('Gerald'))
        self.assertEqual(12, round1.internal_compare_bet_and_actual('Ruth'))
        self.assertEqual(10, round1.internal_compare_bet_and_actual('Patrick'))

    def testcompare_bet_and_actual1(self):
        # test if bet does not match actual
        round1 = Round(9, FrenchDeck(), self.players)
        input_bets = [('Gerald', 1), ('Ruth', 2), ('Patrick', 0)]
        round1.getBets(input_bets)
        round1.updateActual('Patrick')
        round1.updateActual('Patrick')
        round1.updateActual('Patrick')
        self.assertEqual(-1, round1.internal_compare_bet_and_actual('Gerald'))
        self.assertEqual(-2, round1.internal_compare_bet_and_actual('Ruth'))
        self.assertEqual(-3, round1.internal_compare_bet_and_actual('Patrick'))


class ActualsTestCase(unittest.TestCase):
    deck = FrenchDeck()
    players = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    for player in players:
        if player.name == 'Gerald':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='spades'))
        if player.name == 'Ruth':
            player.hand.takecard(CardsUtils.Card(rank='4', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='5', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='A', suit='diamonds'))
        if player.name == 'Patrick':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='hearts'))

    def test_initialised_actuals(self):
        round1 = Round(9, self.deck, self.players)
        self.assertEqual([['Gerald', 0], ['Ruth', 0], ['Patrick', 0]], round1.actual)

    def test_init_and_updated_actuals(self):
        round1 = Round(9, self.deck, self.players)
        self.assertEqual([['Gerald', 0], ['Ruth', 0], ['Patrick', 0]], round1.actual)
        round1.updateActual('Gerald')
        self.assertEqual([['Gerald', 1], ['Ruth', 0], ['Patrick', 0]], round1.actual)
        round1.updateActual('Ruth')
        self.assertEqual([['Gerald', 1], ['Ruth', 1], ['Patrick', 0]], round1.actual)


class GameTestCase(unittest.TestCase):
    def testInitGame0(self):
        deck = FrenchDeck()
        newGame = Game.Game(deck=deck, numOfPlayers=2, numOfRounds=10)
        newGame.setupGame('Gerald', 'Ruth')

        players = newGame.getPlayers()
        self.assertEqual(players[0].name, 'Gerald')
        self.assertEqual(players[1].name, 'Ruth')
        #newGame.initRounds()

    def testInitGame1(self):
        deck = FrenchDeck()
        newGame = Game.Game(deck=deck, numOfPlayers=2, numOfRounds=10)
        newGame.setupGame('Gerald', 'Ruth')

        players = newGame.getPlayers()
        newGame.initRounds()
        self.assertEqual(1, newGame.getCurrentRound().round_number)
        for rounds in newGame._rounds:
            print(rounds)


class FrenchDeckTestCase(unittest.TestCase):
    # test create non-shuffled deck
    def testDeck0(self):
        deck = FrenchDeck('N')
        self.assertEqual(len(deck._cards),52)
        self.assertEqual(CardsUtils.Card(rank='2', suit='spades'), deck.__getitem__(0))
        self.assertEqual(0,len(deck._burnt_cards))

    # test create shuffled deck
    def testDeck1(self):
        deck = FrenchDeck('Y')
        self.assertEqual(len(deck),52)
        self.assertNotEqual(CardsUtils.Card(rank='2', suit='spades'), deck.__getitem__(0))

    # test dealing a card
    def testDeck2(self):
        deck = FrenchDeck()
        self.assertEqual(len(deck), 52)
        card1 = deck.dealCard()
        print(card1)
        self.assertEqual(1, len(deck._burnt_cards))
        card2 = deck.dealCard()
        self.assertEqual(2, len(deck._burnt_cards))
        self.assertEqual(50,len(deck))


class ValidCardTestCase(unittest.TestCase):
    #valid_card(trumps, trumps_broken, player, card, *played)
    # you cannot lead with a trump unless trumps are broken
    # you have to follow suit if you can
    # if you cannot follow suit, you can play any card
    deck = FrenchDeck()
    players = [Player('Gerald'), Player('Ruth'), Player('Patrick')]
    for player in players:
        if player.name == 'Gerald':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='3', suit='spades'))
        if player.name == 'Ruth':
            player.hand.takecard(CardsUtils.Card(rank='4', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='5', suit='spades'))
            player.hand.takecard(CardsUtils.Card(rank='A', suit='diamonds'))
        if player.name == 'Patrick':
            player.hand.takecard(CardsUtils.Card(rank='A', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='2', suit='hearts'))
            player.hand.takecard(CardsUtils.Card(rank='5', suit='hearts'))

    def testValidCard0(self):
        # trumps broken, can lead with non-trump
        response = CardsUtils.valid_card('hearts', True, self.players[0], CardsUtils.Card(rank='3', suit='spades'), [])
        self.assertEqual(True, response)

    def testValidCard1(self):
        # trumps not broken, cannot lead with trump
        response = CardsUtils.valid_card('hearts', False, self.players[0], CardsUtils.Card(rank='2', suit='hearts'), [])
        self.assertEqual(False, response)

    def testValidCard3(self):
        # trumps broken, can lead with trump
        response = CardsUtils.valid_card('hearts', True, self.players[0], CardsUtils.Card(rank='2', suit='hearts'), [])
        self.assertEqual(True, response)

    def testValidCard4(self):
        # trumps not broken, can lead with trump as only trumps in hand
        response = CardsUtils.valid_card('hearts', False, self.players[2], CardsUtils.Card(rank='2', suit='hearts'), [])
        self.assertEqual(True, response)

    def testValidCard5(self):
        # test following suit. player1 cannot play diamonds as they have a spade in hand
        response = CardsUtils.valid_card('hearts', False, self.players[1], CardsUtils.Card(rank='A', suit='diamonds'), [['Gerald', CardsUtils.Card(rank='3', suit='spades')]])
        self.assertEqual(False, response)

    def testValidCard6(self):
        # test following suit. player1 can play diamonds as they do not have a heart in hand
        response = CardsUtils.valid_card('hearts', False, self.players[1], CardsUtils.Card(rank='A', suit='diamonds'), [['Gerald', CardsUtils.Card(rank='2', suit='hearts')]])
        self.assertEqual(True, response)

    def testValidCard7(self):
        # test following suit. player1 follows suit
        response = CardsUtils.valid_card('hearts', False, self.players[1], CardsUtils.Card(rank='4', suit='spades'), [['Gerald', CardsUtils.Card(rank='A', suit='spades')]])
        self.assertEqual(True, response)

    def testValidCard8(self):
        # test following suit. player2 can play hearts
        response = CardsUtils.valid_card('hearts', True, self.players[2], CardsUtils.Card(rank='A', suit='hearts'), [['Gerald', CardsUtils.Card(rank='2', suit='hearts')], ['Ruth', CardsUtils.Card(rank='4', suit='spades')]])
        self.assertEqual(True, response)

if __name__ == '__main__':
    unittest.main()
