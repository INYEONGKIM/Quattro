
def CardInitView(user_deck: list):
    card_info = [["" for _ in range(6)] for _ in range(4)]
    front_space = 0
    back_space = 0

    for card_idx in range(4):
        for i in range(6):
            if i == 0:
                card_info[card_idx][i] += f"┌{'─' * 10}┐ "
            if i == 1 or i == 4:
                card_info[card_idx][i] += f"│{' ' * 10}│ "
            elif i == 2:
                card_info[card_idx][i] += f"│     {user_deck[card_idx].number}    │ "
            elif i == 3:
                if user_deck[card_idx].color == "blue" or user_deck[card_idx].color == "zero":
                    front_space = 3
                    back_space = 3
                elif user_deck[card_idx].color == "red":
                    front_space = 4
                    back_space = 3
                elif user_deck[card_idx].color == "green":
                    front_space = 3
                    back_space = 2
                elif user_deck[card_idx].color == "yellow":
                    front_space = 2
                    back_space = 2

                card_info[card_idx][i] += f"│{(' ' * front_space) + user_deck[card_idx].color + (' ' * back_space)}│ "
            elif i == 5:
                card_info[card_idx][i] += f"└{'─' * 10}┘ "

    s = ""
    for i in range(6):
        for j in range(4):
            s += card_info[j][i]
        s += '\n'
    return s

