from QuattroComponents.Player import Player
from QuattroComponents.Card import Card


def UserPlayerView(line_blocks: list, player1: Player, player2: Player, now_turn: str):
    front_space = 0
    back_space = 0

    # etc data
    etc_space = " " * 9
    etc_back_span = " " * 4
    for i in range(6):
        if i == 0 or i == 1 or i == 4 or i == 5:
            line_blocks[2][i] += etc_space
            line_blocks[3][i] += etc_space
        elif i == 2:
            front_space = 1
            back_space = 1

            line_blocks[2][i] += f"{(' ' * front_space) + player2.user_name + (' ' *  back_space)}"
            line_blocks[3][i] += f"{(' ' * front_space) + player1.user_name + (' ' *  back_space)}"
        elif i == 3:
            line_blocks[2][i] += "Card Open"
            line_blocks[3][i] += "Card Open"

        line_blocks[2][i] += etc_back_span
        line_blocks[3][i] += etc_back_span

    # User Card Data
    for block_num in range(6):
        # Player2 non-opened Card
        if block_num == 0:
            if now_turn == player1.user_name:
                # none modification area
                pass

            elif now_turn == player2.user_name or now_turn == "END":
                for card_idx in range(player2.user_left_card_number):
                    # add card data
                    for i in range(6):
                        if i == 0:
                            line_blocks[block_num][i] += f"┌{'─' * 10}┐ "
                        elif i == 1 or i == 4:
                            line_blocks[block_num][i] += f"│{' ' * 10}│ "
                        elif i == 2:
                            line_blocks[block_num][i] += f"│     {player2.user_deck[4 - player2.user_left_card_number + card_idx].number}    │ "
                        elif i == 3:
                            if player2.user_deck[4 - player2.user_left_card_number + card_idx].color == "blue" or \
                                    player2.user_deck[4 - player2.user_left_card_number + card_idx].color == "zero":
                                front_space = 3
                                back_space = 3
                            elif player2.user_deck[4 - player2.user_left_card_number + card_idx].color == "red":
                                front_space = 4
                                back_space = 3
                            elif player2.user_deck[4 - player2.user_left_card_number + card_idx].color == "green":
                                front_space = 3
                                back_space = 2
                            elif player2.user_deck[4 - player2.user_left_card_number + card_idx].color == "yellow":
                                front_space = 2
                                back_space = 2

                            line_blocks[block_num][i] += f"│{(' ' * front_space) + player2.user_deck[4 - player2.user_left_card_number + card_idx].color + (' ' * back_space)}│ "
                        elif i == 5:
                            line_blocks[block_num][i] += f"└──[No.{card_idx + 1}]──┘ "
            else:
                raise NameError("Wrong now_turn name")

        # Player2 opened Card
        elif block_num == 2:
            for card_idx in range(4 - player2.user_left_card_number):
                # add card data
                for i in range(6):
                    if i == 0:
                        line_blocks[block_num][i] += f"┌{'─' * 10}┐ "
                    elif i == 1 or i == 4:
                        line_blocks[block_num][i] += f"│{' ' * 10}│ "
                    elif i == 2:
                        line_blocks[block_num][i] += f"│     {player2.user_deck[card_idx].number}    │ "
                    elif i == 3:
                        if player2.user_deck[card_idx].color == "blue" or player2.user_deck[card_idx].color == "zero":
                            front_space = 3
                            back_space = 3
                        elif player2.user_deck[card_idx].color == "red":
                            front_space = 4
                            back_space = 3
                        elif player2.user_deck[card_idx].color == "green":
                            front_space = 3
                            back_space = 2
                        elif player2.user_deck[card_idx].color == "yellow":
                            front_space = 2
                            back_space = 2

                        line_blocks[block_num][i] += f"│{(' ' * front_space) + player2.user_deck[card_idx].color + (' ' * back_space)}│ "
                    elif i == 5:
                        line_blocks[block_num][i] += f"└{'─' * 10}┘ "

        # Player1 opened Card
        elif block_num == 3:
            for card_idx in range(4 - player1.user_left_card_number):
                # add card data
                for i in range(6):
                    if i == 0:
                        line_blocks[block_num][i] += f"┌{'─' * 10}┐ "
                    elif i == 1 or i == 4:
                        line_blocks[block_num][i] += f"│{' ' * 10}│ "
                    elif i == 2:
                        line_blocks[block_num][i] += f"│     {player1.user_deck[card_idx].number}    │ "
                    elif i == 3:
                        if player1.user_deck[card_idx].color == "blue" or player1.user_deck[card_idx].color == "zero":
                            front_space = 3
                            back_space = 3
                        elif player1.user_deck[card_idx].color == "red":
                            front_space = 4
                            back_space = 3
                        elif player1.user_deck[card_idx].color == "green":
                            front_space = 3
                            back_space = 2
                        elif player1.user_deck[card_idx].color == "yellow":
                            front_space = 2
                            back_space = 2

                        line_blocks[block_num][i] += f"│{(' ' * front_space) + player1.user_deck[card_idx].color + (' ' * back_space)}│ "
                    elif i == 5:
                        line_blocks[block_num][i] += f"└{'─' * 10}┘ "

        # Player1 non-opened Card
        elif block_num == 5:
            if now_turn == player1.user_name or now_turn == "END":
                for card_idx in range(player1.user_left_card_number):
                    # add card data
                    for i in range(6):
                        if i == 0:
                            line_blocks[block_num][i] += f"┌{'─' * 10}┐ "
                        elif i == 1 or i == 4:
                            line_blocks[block_num][i] += f"│{' ' * 10}│ "
                        elif i == 2:
                            line_blocks[block_num][i] += f"│     {player1.user_deck[4 - player1.user_left_card_number + card_idx].number}    │ "
                        elif i == 3:
                            if player1.user_deck[4 - player1.user_left_card_number + card_idx].color == "blue" or \
                                    player1.user_deck[4 - player1.user_left_card_number + card_idx].color == "zero":
                                front_space = 3
                                back_space = 3
                            elif player1.user_deck[4 - player1.user_left_card_number + card_idx].color == "red":
                                front_space = 4
                                back_space = 3
                            elif player1.user_deck[4 - player1.user_left_card_number + card_idx].color == "green":
                                front_space = 3
                                back_space = 2
                            elif player1.user_deck[4 - player1.user_left_card_number + card_idx].color == "yellow":
                                front_space = 2
                                back_space = 2

                            line_blocks[block_num][i] += f"│{(' ' * front_space) + player1.user_deck[4 - player1.user_left_card_number + card_idx].color + (' ' * back_space)}│ "
                        elif i == 5:
                            line_blocks[block_num][i] += f"└──[No.{card_idx + 1}]──┘ "

            elif now_turn == player2.user_name:
                # none modification area
                pass
            else:
                raise NameError("Wrong now_turn name")

        else:
            # none modification area
            pass
