import unittest
import game


class TestGame(unittest.TestCase):

    def test_deck_creation(self):
        test_deck = game.Deck()
        self.assertEqual(len(test_deck.deck), 52)

    def test_deal_to_player(self):
        test_deck = game.Deck()
        test_deck.shuffle()

        test_player = game.Hand()
        pulled_card = test_deck.deal()
        test_player.add_card(pulled_card)

        self.assertIsNotNone(test_player.value)
        self.assertEquals(test_player.cards[0].suit, pulled_card.suit)


