from QuattroComponents.Input_handler import user_input, select_number
from collections import deque


class Player:
    def __init__(self, user_name, user_deck):
        self.user_type = "user"
        self.user_name = user_name
        self.user_deck = user_deck # list
        self.user_left_card_number = 4
        self.user_malligan_fin_flag = False

        self.user_change_quota = [1, 2, 3, 4, 5, 6]
        self.top_card = -1
        self.total_score = 0

    def __str__(self):
        card_info = f"[{self.user_name}]\n"
        for card in self.user_deck:
            card_info += card.__str__() + "\n"
        return card_info.strip()

    def open_card(self):
        opened_color = set()
        for card in self.user_deck:
            if card.isOpen:
                opened_color.add(card.color)

        while True:
            card_idx = select_number(start=1, end=self.user_left_card_number)

            if 1 <= card_idx <= self.user_left_card_number:
                if (self.user_left_card_number == 1 and self.user_change_quota == []) \
                        or (self.user_deck[4 - self.user_left_card_number + card_idx - 1].color not in opened_color):

                    self.user_deck[4 - self.user_left_card_number + card_idx - 1].isOpen = True
                    self.user_deck.insert(4 - self.user_left_card_number, self.user_deck.pop(4 - self.user_left_card_number + card_idx - 1))
                    self.user_left_card_number -= 1

                    break
                else:
                    print(f"Try Again! color {self.user_deck[4 - self.user_left_card_number + card_idx - 1].color} "
                          f"is already opened!")
                    return -1

            else:
                print("Try Again! Wrong number!")

        return 0

    def change_card(self, anonymous_player_list):
        if len(self.user_change_quota) > 0:
            # Select Card Number
            while True:
                card_idx = select_number(start=1, end=self.user_left_card_number)

                if 1 <= card_idx <= self.user_left_card_number:
                    # Selcet Anonymous_player
                    while True:
                        anonymous_player_idx = select_number(start=1, end=6)
                        if 1 <= anonymous_player_idx <= 6 and anonymous_player_idx in self.user_change_quota:

                            opened_deck = deque()
                            for card in self.user_deck:
                                if card.isOpen:
                                    opened_deck.append(card)

                            # Call Anonymous_player's change def
                            new_card = anonymous_player_list[anonymous_player_idx - 1].handle_card_change(user_name=self.user_name,
                                                                                                          origin_card=self.user_deck[4 - self.user_left_card_number + card_idx - 1],
                                                                                                          opened_deck=opened_deck)

                            self.user_change_quota.remove(anonymous_player_idx)
                            self.user_deck.pop(4 - self.user_left_card_number + card_idx - 1)
                            self.user_deck.insert(4 - self.user_left_card_number + card_idx - 1, new_card)

                            break # anonymous_player_idx and change Loop
                        else:
                            print(f"Try Again! You already change card with Anonymous player {anonymous_player_idx}")

                    break # card_idx Loop

                else:
                    print("Try Again!")
        else:
            print("[System] You have no chance to change!")

    def do_malligan(self, main_deck):
        if not self.user_malligan_fin_flag:

            # Do Malligan
            self.user_deck = main_deck.handle_malligan(origin_deck=self.user_deck)
            print(f"\n[System] Now Your Deck is \n{self}\n")

            player_yn = user_input(now_turn=self,
                                   guide_msg=f"Do you want malligan again?"
                                   f" You have 1 malligan chance (y, n)")

            # Do One more Malligan
            while True:
                if player_yn == "y":
                    self.user_deck = main_deck.handle_malligan(origin_deck=self.user_deck)
                    print(f"\n[System] Now Your Deck is \n{self}\n")
                    break

                elif player_yn == "n":
                    print("\n[System] Select Deck Finished\n")
                    break
                else:
                    player_yn = user_input(now_turn=self, guide_msg="Input must be y or n !")
        else:
            print("Try Again!")

    def isQuattro(self):
        my_color = set()
        for col in self.user_deck:
            my_color.add(col.color)

        if len(my_color) == 4:
            return True
        else:
            return False

    def calculate_total_score(self):
        for card in self.user_deck:
            if self.top_card < card.number:
                self.top_card = card.number

            if self.isQuattro():
                self.total_score += card.number



class Anonymous_player:
    def __init__(self, user_name, user_deck):
        self.user_type = "anonymous"
        self.user_name = user_name
        self.user_deck = user_deck  # list

        self.player1_changed = False
        self.player2_changed = False

    def __str__(self):
        card_info = f"[{self.user_name}]\n"
        for card in self.user_deck:
            card_info += card.__str__() + "\n"
        return card_info.strip()

    def handle_card_change(self, user_name, origin_card, opened_deck):

        change_idx = -1

        # TODO : change_idx Implementation
        # Rule 0: zero first!
        for i in range(3):
            if self.user_deck[i].color == 'zero':
                change_idx = i
                # print(f"Zero Found!, i: {i}, change_idx: {change_idx}")

        # Zero doesn't in here
        if change_idx == -1:
            idx_candidate = [0, 1, 2]
            max_no, max_idx = -1, []

            for od in opened_deck:
                for i in range(3):
                    if od.color == self.user_deck[i].color and i in idx_candidate:
                        idx_candidate.remove(i)

            # Rule 2: Impossible to make
            if not idx_candidate:
                idx_candidate = [0, 1, 2]

            # find max idx
            for i in idx_candidate:
                if max_no == self.user_deck[i].number:
                    max_idx.append(i)
                elif max_no < self.user_deck[i].number:
                    max_no = self.user_deck[i].number
                    max_idx = [i]

            # Rule 3: Red, Blue, Yellow, Green
            if len(max_idx) > 1:
                for i in range(len(max_idx)):
                    if self.user_deck[max_idx[i]].color == "red":
                        max_idx[i] = (max_idx[i], 1)
                    elif self.user_deck[max_idx[i]].color == "blue":
                        max_idx[i] = (max_idx[i], 2)
                    elif self.user_deck[max_idx[i]].color == "yellow":
                        max_idx[i] = (max_idx[i], 3)
                    elif self.user_deck[max_idx[i]].color == "green":
                        max_idx[i] = (max_idx[i], 4)
                    else:
                        raise TypeError("zero error!")

                max_idx = sorted(max_idx, key=lambda x: x[1])
                change_idx = max_idx[0][0]

            else:
                change_idx = max_idx[0]
        else:
            # if Zero in here, just pass
            pass

        ###########

        # card change
        return_card = self.user_deck.pop(change_idx)
        return_card.isOpen = False

        origin_card.isOpen = True
        self.user_deck.insert(change_idx, origin_card)

        if user_name == "player1":
            self.player1_changed = True
        else:
            self.player2_changed = True

        return return_card


