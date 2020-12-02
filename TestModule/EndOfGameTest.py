import unittest
from TestModule.GetMethodName import get_method_name_decorator
from QuattroComponents.Player import Player
from QuattroComponents.Card import Card
from QuattroComponents.View.EndOfGame import EndOfGame


def reset_players_attributes(player1: Player, player2: Player):
    player1.total_score = 0
    player2.total_score = 0

    player1.top_card = -1
    player2.top_card = -1


class EndOfGameTest(unittest.TestCase):
    method_names = set()

    @get_method_name_decorator
    def test_get_winner(self):
        surrender_flag = False

        ###### Made Quattro Case

        # Both Made Quattro (sum)
        player1 = Player(user_name="player1", user_deck=[
            Card(number=6, color="red", isOpen=True),
            Card(number=6, color="blue", isOpen=True),
            Card(number=6, color="yellow", isOpen=True),
            Card(number=6, color="green", isOpen=True)
        ])

        player2 = Player(user_name="player2", user_deck=[
            Card(number=5, color="red", isOpen=True),
            Card(number=5, color="blue", isOpen=True),
            Card(number=5, color="yellow", isOpen=True),
            Card(number=5, color="green", isOpen=True)
        ])

        self.assertEqual(EndOfGame(surrender_flag=surrender_flag,
                                   winner="", player1=player1, player2=player2),
                         "player1", msg="Normal Test Case Fail!")

        # Both Made Quattro (Top number)
        reset_players_attributes(player1=player1, player2=player2)

        player1.user_deck = [
            Card(number=3, color="red", isOpen=True),
            Card(number=3, color="blue", isOpen=True),
            Card(number=3, color="yellow", isOpen=True),
            Card(number=3, color="green", isOpen=True)
        ]

        player2.user_deck = [
            Card(number=2, color="red", isOpen=True),
            Card(number=4, color="blue", isOpen=True),
            Card(number=2, color="yellow", isOpen=True),
            Card(number=4, color="green", isOpen=True)
        ]
        self.assertEqual(EndOfGame(surrender_flag=surrender_flag,
                                   winner="", player1=player1, player2=player2),
                         "player2", msg="Both Quattro Top number Test Case Fail!")

        # Both Made Quattro (Top color)
        reset_players_attributes(player1=player1, player2=player2)
        player1.user_deck = [
            Card(number=2, color="red", isOpen=True),
            Card(number=4, color="blue", isOpen=True),
            Card(number=5, color="yellow", isOpen=True),
            Card(number=6, color="green", isOpen=True)
        ]

        player2.user_deck = [
            Card(number=6, color="red", isOpen=True),
            Card(number=5, color="blue", isOpen=True),
            Card(number=4, color="yellow", isOpen=True),
            Card(number=2, color="green", isOpen=True)
        ]
        self.assertEqual(EndOfGame(surrender_flag=surrender_flag,
                                   winner="", player1=player1, player2=player2),
                         "player2", msg="Normal Test Case Fail!")

        ###### Made Quattro Case

        # Both Didn't Made Quattro (Top number)
        reset_players_attributes(player1=player1, player2=player2)
        player1.user_deck = [
            Card(number=6, color="red", isOpen=True),
            Card(number=5, color="red", isOpen=True),
            Card(number=6, color="yellow", isOpen=True),
            Card(number=6, color="green", isOpen=True)
        ]

        player2.user_deck = [
            Card(number=5, color="red", isOpen=True),
            Card(number=5, color="blue", isOpen=True),
            Card(number=4, color="blue", isOpen=True),
            Card(number=5, color="green", isOpen=True)
        ]

        self.assertEqual(EndOfGame(surrender_flag=surrender_flag,
                                   winner="", player1=player1, player2=player2),
                         "player1", msg="Number Top Case Fail!")

        # Both Didn't Made Quattro (color)
        reset_players_attributes(player1=player1, player2=player2)
        player1.user_deck = [
            Card(number=6, color="red", isOpen=True),
            Card(number=5, color="red", isOpen=True),
            Card(number=6, color="yellow", isOpen=True),
            Card(number=6, color="green", isOpen=True)
        ]

        player2.user_deck = [
            Card(number=5, color="red", isOpen=True),
            Card(number=5, color="blue", isOpen=True),
            Card(number=6, color="blue", isOpen=True),
            Card(number=5, color="green", isOpen=True)
        ]

        self.assertEqual(EndOfGame(surrender_flag=surrender_flag,
                                   winner="", player1=player1, player2=player2),
                         "player1", msg="color Top Case Fail!")

