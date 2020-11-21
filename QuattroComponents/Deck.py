from collections import deque
import random
from QuattroComponents import Card as c


class Deck:
    def __init__(self):
        # 2 Zero + (1 ~ 6) x 4
        self.deck = deque([c.Card(color='zero', number=0, isOpen=False),
                           c.Card(color='zero', number=0, isOpen=False)])

        for col in ['red', 'blue', 'yellow', 'green']:
            for n in range(1, 7):
                self.deck.append(c.Card(color=col, number=n, isOpen=False))

    def __str__(self):
        s = "***** Print Now Deck *****\n"
        for x in self.deck:
            s += f'{x.color} {x.number} {x.isOpen}\n'
        s += f"Total left {len(self.deck)}\n"

        return s

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_to_player(self, player_type):
        if len(self.deck) > 0:
            player_deck = []
            if player_type == "user":
                for _ in range(4):
                    player_deck.append(self.deck.pop())
            elif player_type == "anonymous":
                for _ in range(3):
                    player_deck.append(self.deck.pop())
            else:
                raise TypeError("Wrong User Input Type")

            return player_deck
        else:
            raise IndexError("QuattroComponents is Empty")

    def handle_malligan(self, origin_deck):
        for od in origin_deck:
            self.deck.appendleft(od)

        return [self.deck.pop(), self.deck.pop(), self.deck.pop(), self.deck.pop()]


