import unittest
from QuattroComponents.Player import Anonymous_player
from QuattroComponents.Card import Card
from TestModule.GetMethodName import get_method_name_decorator
from collections import deque


def reset_player_attributes(anonymous: Anonymous_player):
    anonymous.player1_changed = False
    anonymous.player2_changed = False


class AnonymousPlayerTest(unittest.TestCase):
    # this card doesn't care
    origin_card = Card(number=1, color="green", isOpen=False)

    method_names = set()

    @get_method_name_decorator
    def test_correct_zero_card_change(self):
        # Zero idx 0
        anonymous = Anonymous_player(user_name="anonymous", user_deck=[
            Card(number=0, color="zero", isOpen=False),
            Card(number=1, color="red", isOpen=False),
            Card(number=2, color="red", isOpen=False)
        ])
        opened_deck = deque([])
        return_card = anonymous.handle_card_change(user_name='player2', origin_card=self.origin_card, opened_deck=opened_deck)
        self.assertEqual(return_card.number, 0)
        self.assertEqual(return_card.color, 'zero')
        self.assertTrue(anonymous.player2_changed)

        # Zero idx 1
        reset_player_attributes(anonymous=anonymous)
        self.origin_card.isOpen = False

        anonymous = Anonymous_player(user_name="anonymous", user_deck=[
            Card(number=1, color="red", isOpen=False),
            Card(number=0, color="zero", isOpen=False),
            Card(number=2, color="red", isOpen=False)
        ])
        opened_deck = deque([])
        return_card = anonymous.handle_card_change(user_name='player2', origin_card=self.origin_card, opened_deck=opened_deck)
        self.assertEqual(return_card.number, 0)
        self.assertEqual(return_card.color, 'zero')
        self.assertTrue(anonymous.player2_changed)

        # Zero idx 2
        reset_player_attributes(anonymous=anonymous)
        self.origin_card.isOpen = False

        anonymous = Anonymous_player(user_name="anonymous", user_deck=[
            Card(number=1, color="red", isOpen=False),
            Card(number=2, color="red", isOpen=False),
            Card(number=0, color="zero", isOpen=False)
        ])
        opened_deck = deque([])
        return_card = anonymous.handle_card_change(user_name='player2', origin_card=self.origin_card,
                                                   opened_deck=opened_deck)
        self.assertEqual(return_card.number, 0)
        self.assertEqual(return_card.color, 'zero')
        self.assertTrue(anonymous.player2_changed)

        # with opened_deck
        reset_player_attributes(anonymous=anonymous)
        self.origin_card.isOpen = False

        anonymous = Anonymous_player(user_name="anonymous", user_deck=[
            Card(number=1, color="red", isOpen=False),
            Card(number=2, color="red", isOpen=False),
            Card(number=0, color="zero", isOpen=False)
        ])
        opened_deck = deque([Card(number=3, color="blue", isOpen=False)])
        return_card = anonymous.handle_card_change(user_name='player2', origin_card=self.origin_card,
                                                   opened_deck=opened_deck)
        self.assertEqual(return_card.number, 0)
        self.assertEqual(return_card.color, 'zero')
        self.assertTrue(anonymous.player2_changed)

    @get_method_name_decorator
    def test_made_quattro_card_change(self):
        anonymous = Anonymous_player(user_name="anonymous", user_deck=[
            Card(number=1, color="blue", isOpen=False),
            Card(number=1, color="yellow", isOpen=False),
            Card(number=1, color="red", isOpen=False)
        ])
        opened_deck = deque([
            Card(number=6, color="blue", isOpen=True),
            Card(number=6, color="red", isOpen=True),
            Card(number=6, color="green", isOpen=True)
        ])
        return_card = anonymous.handle_card_change(user_name='player2', origin_card=self.origin_card,
                                                   opened_deck=opened_deck)
        self.assertEqual(return_card.number, 1)
        self.assertEqual(return_card.color, 'yellow')
        self.assertTrue(anonymous.player2_changed)

    @get_method_name_decorator
    def test_top_card_change(self):
        anonymous = Anonymous_player(user_name="anonymous", user_deck=[
            Card(number=1, color="blue", isOpen=False),
            Card(number=2, color="red", isOpen=False),
            Card(number=1, color="red", isOpen=False)
        ])
        opened_deck = deque([
            Card(number=6, color="blue", isOpen=True),
            Card(number=6, color="red", isOpen=True),
            Card(number=6, color="green", isOpen=True)
        ])
        return_card = anonymous.handle_card_change(user_name='player2', origin_card=self.origin_card,
                                                   opened_deck=opened_deck)
        self.assertEqual(return_card.number, 2)
        self.assertEqual(return_card.color, 'red')
        self.assertTrue(anonymous.player2_changed)

        reset_player_attributes(anonymous=anonymous)
        self.origin_card.isOpen = False

        anonymous.user_deck = [
            Card(number=2, color="blue", isOpen=False),
            Card(number=2, color="red", isOpen=False),
            Card(number=1, color="red", isOpen=False)
        ]
        opened_deck = deque([
            Card(number=6, color="blue", isOpen=True),
            Card(number=6, color="red", isOpen=True),
            Card(number=6, color="green", isOpen=True)
        ])
        return_card = anonymous.handle_card_change(user_name='player2', origin_card=self.origin_card,
                                                   opened_deck=opened_deck)
        self.assertEqual(return_card.number, 2)
        self.assertEqual(return_card.color, 'red')
        self.assertTrue(anonymous.player2_changed)
