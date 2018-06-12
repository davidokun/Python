import unittest
import game


class TestGame(unittest.TestCase):

    def test_deck_creation(self):
        test_deck = game.Deck()
        self.assertEqual(len(test_deck.deck), 52)

