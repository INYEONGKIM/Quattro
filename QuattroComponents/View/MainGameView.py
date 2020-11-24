from QuattroComponents.View.AnonymousPlayerView import AnonymousPlayerView
from QuattroComponents.View.UserPlayerView import UserPlayerView
from QuattroComponents.Player import Player


def MainGameView(player1: Player, player2: Player, anonymous_player_list: list, now_turn: str):
    line_blocks = [["" for _ in range(6)] for _ in range(6)]

    # Print Anonymous Fist
    AnonymousPlayerView(line_blocks=line_blocks, anonymous_player_list=anonymous_player_list, now_turn=now_turn)

    # Update User Data
    UserPlayerView(line_blocks=line_blocks, player1=player1, player2=player2, now_turn=now_turn)

    for block in line_blocks:
        print('\n'.join(block))
