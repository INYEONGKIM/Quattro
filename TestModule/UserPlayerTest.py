import unittest
from QuattroComponents.Player import Player
from QuattroComponents.Card import Card
from TestModule.GetMethodName import get_method_name_decorator


class UserPlayerTest(unittest.TestCase):
    player = Player(user_name="player", user_deck=[])
    method_names = set()

    @get_method_name_decorator
    def test_is_quattro(self):
        self.player.user_deck = [
            Card(number=1, color='green', isOpen=False),
            Card(number=1, color='blue', isOpen=False),
            Card(number=5, color='yellow', isOpen=False),
            Card(number=2, color='red', isOpen=False)
        ]
        self.assertTrue(self.player.isQuattro(), msg="Normal Quattro-Case Test Fail!")

        self.player.user_deck = [
            Card(number=0, color='zero', isOpen=False),
            Card(number=1, color='blue', isOpen=False),
            Card(number=5, color='yellow', isOpen=False),
            Card(number=2, color='red', isOpen=False)
        ]
        self.assertTrue(self.player.isQuattro(), msg="Zero-include Quattro-Case Test Fail!")

        self.player.user_deck = [
            Card(number=0, color='zero', isOpen=False),
            Card(number=0, color='zero', isOpen=False),
            Card(number=1, color='blue', isOpen=False),
            Card(number=2, color='red', isOpen=False)
        ]
        self.assertFalse(self.player.isQuattro(), msg="Two Zeros False Test Fail!")

        self.player.user_deck = [
            Card(number=3, color='blue', isOpen=False),
            Card(number=1, color='blue', isOpen=False),
            Card(number=5, color='yellow', isOpen=False),
            Card(number=2, color='red', isOpen=False)
        ]
        self.assertFalse(self.player.isQuattro(), msg="Duplicate Color Test Fail!")

    @get_method_name_decorator
    def test_calculate_score_and_top(self):
        self.player.user_deck = [
            Card(number=1, color='green', isOpen=False),
            Card(number=1, color='blue', isOpen=False),
            Card(number=1, color='yellow', isOpen=False),
            Card(number=1, color='red', isOpen=False)
        ]
        self.player.calculate_total_score()
        self.assertEqual(self.player.total_score, 4, msg="Normal Quattro-Case Calculate Test Fail!")
        self.assertEqual(self.player.top_card, 1, msg="Normal Quattro-Case Top-Card Test Fail!")

        self.player.total_score = 0
        self.top_card = -1
        self.player.user_deck = [
            Card(number=0, color='zero', isOpen=False),
            Card(number=1, color='blue', isOpen=False),
            Card(number=1, color='yellow', isOpen=False),
            Card(number=1, color='red', isOpen=False)
        ]
        self.player.calculate_total_score()
        self.assertEqual(self.player.total_score, 3, msg="Zero-include Quattro-Case Calculate Test Fail!")
        self.assertEqual(self.player.top_card, 1, msg="Zero-include Quattro-Case Top-Card Test Fail!")

        self.player.total_score = 0
        self.top_card = -1
        self.player.user_deck = [
            Card(number=0, color='zero', isOpen=False),
            Card(number=0, color='zero', isOpen=False),
            Card(number=1, color='yellow', isOpen=False),
            Card(number=1, color='red', isOpen=False)
        ]
        self.player.calculate_total_score()
        self.assertEqual(self.player.total_score, 0, msg="Two Zeros Calculate Test Fail!")
        self.assertEqual(self.player.top_card, 1, msg="Two Zeros Top-Card Test Fail!")

        self.player.total_score = 0
        self.top_card = -1
        self.player.user_deck = [
            Card(number=0, color='zero', isOpen=False),
            Card(number=2, color='yellow', isOpen=False),
            Card(number=1, color='yellow', isOpen=False),
            Card(number=1, color='red', isOpen=False)
        ]
        self.player.calculate_total_score()
        self.assertEqual(self.player.total_score, 0, msg="Non-Quattro Case Calculate Test Fail!")
        self.assertEqual(self.player.top_card, 2, msg="Non-Quattro Case Top-Card Test Fail!")

        self.player.total_score = 0
        self.top_card = -1
        self.player.user_deck = [
            Card(number=1, color='blue', isOpen=False),
            Card(number=2, color='yellow', isOpen=False),
            Card(number=2, color='green', isOpen=False),
            Card(number=1, color='red', isOpen=False)
        ]
        self.player.calculate_total_score()
        self.assertEqual(self.player.total_score, 6, msg="Duplicate Color Top Case Calculate Test Fail!")
        self.assertEqual(self.player.top_card, 2, msg="Duplicate Color Top Case Top-Card Test Fail!")

        self.player.total_score = 0
        self.top_card = -1
        self.player.user_deck = [
            Card(number=6, color='blue', isOpen=False),
            Card(number=5, color='yellow', isOpen=False),
            Card(number=4, color='green', isOpen=False),
            Card(number=3, color='red', isOpen=False)
        ]
        self.player.calculate_total_score()
        self.assertEqual(self.player.total_score, 18, msg="Normal Top Case Calculate Test Fail!")
        self.assertEqual(self.player.top_card, 6, msg="Normal Top Case Top-Card Test Fail!")
