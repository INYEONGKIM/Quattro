import unittest
from QuattroComponents.Deck import Deck
from QuattroComponents.Player import Player, Anonymous_player
from collections import deque
from TestModule.GetMethodName import get_method_name_decorator


class DeckTest(unittest.TestCase):

    d = Deck()
    method_names = set()

    @get_method_name_decorator
    def test_deck_len(self):
        self.assertEqual(len(self.d.deck), 26)

    @get_method_name_decorator
    def test_zero_count(self):
        zero_cnt = 0
        for card in self.d.deck:
            if card.color == 'zero' and card.number == 0:
                zero_cnt += 1

        self.assertEqual(zero_cnt, 2)

    @get_method_name_decorator
    def test_deck_random_shuffle(self):
        last_card = self.d.deck[-1]

        for _ in range(10):
            self.d.shuffle_deck()
            self.assertNotEqual(last_card, self.d.deck[-1])
            last_card = self.d.deck[-1]

    @get_method_name_decorator
    def test_is_original_deck(self):
        test_deck = set()
        zero_cnt = 0

        for card in self.d.deck:
            if card.number == 0 and card.color == 'zero':
                zero_cnt += 1
            self.assertTrue(0 <= card.number <= 6)
            self.assertTrue(card.color == 'zero' or card.color == 'red' or card.color == 'blue'
                            or card.color == 'green' or card.color == 'yellow')
            test_deck.add((card.number, card.color))

        self.assertEqual(zero_cnt, 2)
        self.assertEqual(len(test_deck) + zero_cnt - 1, 26)

    @get_method_name_decorator
    def test_handling_malligan(self):
        mall_deck = Deck()
        mall_deck.shuffle_deck()

        first_card_deck = [mall_deck.deck.popleft() for _ in range(4)]

        last_card_deck = [mall_deck.deck[-i] for i in range(1, 5)]

        after_malligan_deck = mall_deck.handle_malligan(origin_deck=deque(first_card_deck))

        self.assertEqual(len(after_malligan_deck), 4)
        for i in range(4):
            self.assertEqual(first_card_deck[i], mall_deck.deck[3 - i])
            self.assertEqual(after_malligan_deck[i], last_card_deck[i])

    @get_method_name_decorator
    def test_deck_distribution(self):
        main_deck = Deck()
        main_deck.shuffle_deck()

        player1 = Player(user_name="player1", user_deck=main_deck.draw_to_player(player_type="user"))
        player2 = Player(user_name="player2", user_deck=main_deck.draw_to_player(player_type="user"))

        for i in range(4):
            if not (player1.user_deck[i].color == 'zero' and player2.user_deck[i].color):
                self.assertNotEqual(player1.user_deck[i], player2.user_deck[i])

        anonymous_player_list = [Anonymous_player(user_name=f"anonymous{str(i)}",
                                                  user_deck=main_deck.draw_to_player(player_type="anonymous")) for i in range(1, 7)]
        for i in range(3):
            two_zeros = 0
            now_set = set()

            for cnt in range(6):
                if anonymous_player_list[cnt].user_deck[i].color == 'zero':
                    two_zeros += 1
                now_set.add((anonymous_player_list[cnt].user_deck[i].color, anonymous_player_list[cnt].user_deck[i].number))

            self.assertTrue(two_zeros < 3)

            if two_zeros < 2:
                self.assertEquals(len(now_set), 6)
            else:
                self.assertEquals(len(now_set), 5)

