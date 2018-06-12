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

    def test_take_bet_invalid_integer(self):
        test_chips = game.Chips()
        response = game.take_bet(test_chips, "wrong_int")
        self.assertEquals(response, "Sorry, please provide a valid integer")

    def test_take_bet_not_enough_chips(self):
        test_chips = game.Chips()
        response = game.take_bet(test_chips, 250)
        self.assertEquals(response, "Sorry, you do not have enough chips!. You have 100")

