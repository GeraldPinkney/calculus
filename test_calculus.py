import unittest
import Calculus

class CompareTestCase(unittest.TestCase):
    def test_compare0(self):
        # first card is trumps.
        result = Calculus.compare_cards('hearts', Calculus.Card(rank='9', suit='hearts'),Calculus.Card(rank='8', suit='spades'))
        self.assertEqual(Calculus.Card(rank='9', suit='hearts'),result)

    def test_compare1(self):
        # second card is trumps.
        result = Calculus.compare_cards('hearts', Calculus.Card(rank='9', suit='spades'),Calculus.Card(rank='8', suit='hearts'))
        self.assertEqual(Calculus.Card(rank='8', suit='hearts'),result)

    def test_compare2(self):
        # both cards trumps. first higher.
        result = Calculus.compare_cards('hearts', Calculus.Card(rank='9', suit='hearts'),Calculus.Card(rank='8', suit='hearts'))
        self.assertEqual(Calculus.Card(rank='9', suit='hearts'),result)

    def test_compare3(self):
        # both cards trumps. second higher.
        result = Calculus.compare_cards('hearts', Calculus.Card(rank='9', suit='hearts'),Calculus.Card(rank='10', suit='hearts'))
        self.assertEqual(Calculus.Card(rank='10', suit='hearts'),result)

    def test_compare4(self):
        # both cards non-trumps. first higher.
        result = Calculus.compare_cards('hearts', Calculus.Card(rank='A', suit='spades'),Calculus.Card(rank='10', suit='spades'))
        self.assertEqual(Calculus.Card(rank='A', suit='spades'),result)

    def test_compare5(self):
        # both cards non-trumps. second higher.
        result = Calculus.compare_cards('hearts', Calculus.Card(rank='K', suit='spades'),Calculus.Card(rank='A', suit='spades'))
        self.assertEqual(Calculus.Card(rank='A', suit='spades'),result)

    def test_compare6(self):
        # both cards non-trumps, but different. second higher.
        result = Calculus.compare_cards('hearts', Calculus.Card(rank='K', suit='spades'),Calculus.Card(rank='A', suit='diamonds'))
        self.assertEqual(Calculus.Card(rank='K', suit='spades'),result)

    def test_compare7(self):
        # both cards non-trumps, but different. first higher.
        result = Calculus.compare_cards('hearts', Calculus.Card(rank='A', suit='spades'),Calculus.Card(rank='K', suit='diamonds'))
        self.assertEqual(Calculus.Card(rank='A', suit='spades'),result)


class TrickTestCase(unittest.TestCase):
    deck = Calculus.FrenchDeck()
    players = [Calculus.Player('Gerald'), Calculus.Player('Ruth'),Calculus.Player('Patrick')]
    for player in players:
        player.hand.takecard(Calculus.Card(rank='A', suit='spades'))

    def testTrick1(self):
        testTrick = Calculus.Trick('hearts',self.players)
        testTrick.playTrick()

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
