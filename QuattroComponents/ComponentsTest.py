from collections import deque
from QuattroComponents.Player import Player
from QuattroComponents.Card import Card
from QuattroComponents.View.EndOfGame import EndOfGame


def deck_distribution_test(player1, player2, anonymous_player_list):
    zero_count = 0
    test_deck = set()
    for p1_card in player1.user_deck:
        test_deck.add((p1_card.color, p1_card.number))
        if p1_card.color == 'zero' and p1_card.number == 0:
            zero_count += 1

    for p2_card in player2.user_deck:
        test_deck.add((p2_card.color, p2_card.number))
        if p2_card.color == 'zero' and p2_card.number == 0:
            zero_count += 1

    for an in anonymous_player_list:
        for an_card in an.user_deck:
            test_deck.add((an_card.color, an_card.number))
            if an_card.color == 'zero' and an_card.number == 0:
                zero_count += 1

    if zero_count == 2 and len(test_deck) == 25:
        print("[TEST CODE] Deck Origin Test Passed!")
    else:
        raise RuntimeError(f"Deck Error!\n{test_deck}\nlen : {len(test_deck)}")


def change_card_test(player_deck, an_deck):
    # opened_deck SET
    opened_deck = deque()
    for card in player_deck:
        if card.isOpen:
            opened_deck.append(card)
    # opened_deck SET

    idx_candidate = [0, 1, 2]
    max_no, max_idx = -1, []

    # Rule 1: Remove Duplicate Color
    for od in opened_deck:
        for i in range(3):
            if od.color == an_deck[i].color and i in idx_candidate:
                idx_candidate.remove(i)

    # Rule 2: Impossible to make
    if not idx_candidate:
        idx_candidate = [0, 1, 2]

    # find max idx
    for i in idx_candidate:
        if max_no == an_deck[i].number:
            max_idx.append(i)
        elif max_no < an_deck[i].number:
            max_no = an_deck[i].number
            max_idx = [i]

    # Rule 3: Red, Blue, Yellow, Green
    if len(max_idx) > 1:
        for i in range(len(max_idx)):
            if an_deck[max_idx[i]].color == "red":
                max_idx[i] = (max_idx[i], 1)
            elif an_deck[max_idx[i]].color == "blue":
                max_idx[i] = (max_idx[i], 2)
            elif an_deck[max_idx[i]].color == "yellow":
                max_idx[i] = (max_idx[i], 3)
            elif an_deck[max_idx[i]].color == "green":
                max_idx[i] = (max_idx[i], 4)
            else:
                raise TypeError("zero error!")

        max_idx = sorted(max_idx, key=lambda x: x[1])

    print(f"change card is : {an_deck[max_idx[0]]}")


def non_quattro_test():
    player1 = Player(user_name="player1",
                     user_deck=[
                         Card(color="yellow", number=5, isOpen=False),
                         Card(color="red", number=4, isOpen=False),
                         Card(color="red", number=3, isOpen=False),
                         Card(color="green", number=5, isOpen=False)
                     ])

    player2 = Player(user_name="player2",
                     user_deck=[
                         Card(color="blue", number=5, isOpen=False),
                         Card(color="blue", number=4, isOpen=False),
                         Card(color="blue", number=3, isOpen=False),
                         Card(color="red", number=5, isOpen=False),
                     ])

    EndOfGame(surrender_flag=False, winner="", player1=player1, player2=player2)

