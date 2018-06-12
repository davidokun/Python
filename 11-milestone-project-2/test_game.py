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
        self.assertEqual(test_player.cards[0].suit, pulled_card.suit)

    def test_take_bet_invalid_integer(self):
        test_chips = game.Chips()
        response = game.take_bet(test_chips, "wrong_int")
        self.assertEqual(response, "Sorry, please provide a valid integer")

    def test_take_bet_not_enough_chips(self):
        test_chips = game.Chips()
        response = game.take_bet(test_chips, 250)
        self.assertEqual(response, "Sorry, you do not have enough chips!. You have 100")

    def test_hit_card(self):
        test_deck = game.Deck()
        test_hand = game.Hand()
        game.hit(test_deck, test_hand)

        self.assertEqual(len(test_hand.cards), 1)

    def test_hit_or_stand_player_hit(self):
        test_deck = game.Deck()
        test_hand = game.Hand()
        test_selection = 'h'

        game.hit_or_stand(test_deck, test_hand, test_selection)

        self.assertEqual(len(test_hand.cards), 1)

    def test_hit_or_stand_player_stands(self):
        test_deck = game.Deck()
        test_hand = game.Hand()
        test_selection = 's'

        game.hit_or_stand(test_deck, test_hand, test_selection)

        self.assertEqual(game.playing, False)
