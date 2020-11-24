
def AnonymousPlayerView(line_blocks: list, anonymous_player_list: list, now_turn: str):
    # In Box normal len = 4 + [ + name + ] + 4
    term_space = "        "

    for block_num in range(6):
        for i in range(6):
            if i == 0:
                line = f"┌────[ {anonymous_player_list[block_num].user_name} ]────┐{term_space}"

            elif i == 4:
                if (now_turn == "player1" and anonymous_player_list[block_num].player1_changed) or \
                        now_turn == "player2" and anonymous_player_list[block_num].player2_changed:
                    line = f"│ You already changed! │{term_space}"

                else:
                    line = f"│                      │{term_space}"

            elif i == 5:
                line = f"└────{'─' * (len(anonymous_player_list[block_num].user_name) + 4)}────┘{term_space}"

            else:
                if anonymous_player_list[block_num].user_deck[i - 1].isOpen or now_turn == "END":
                    front_space = 5
                    back_space = 4
                    if anonymous_player_list[block_num].user_deck[i - 1].color != "yellow":
                        front_space += 1

                        if anonymous_player_list[block_num].user_deck[i - 1].color == "blue" or \
                                anonymous_player_list[block_num].user_deck[i - 1].color == "zero":
                            back_space += 1
                        elif anonymous_player_list[block_num].user_deck[i - 1].color == "red":
                            back_space += 2

                    line = f"│{(' ' * front_space) + anonymous_player_list[block_num].user_deck[i - 1].color + (' ' * back_space)}" \
                        f"{str(anonymous_player_list[block_num].user_deck[i - 1].number) + (' ' * 6)}│{term_space}"
                else:
                    tot_space = len(anonymous_player_list[block_num].user_name) + 12
                    line = f"│{' ' * 10 + '?' + ' ' * (tot_space - 11)}│{term_space}"

            line_blocks[block_num][i] = line

