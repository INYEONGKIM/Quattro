
def EndOfGame(surrender_flag, winner, player1, player2):
    ending_msg = ""

    if not surrender_flag:
        player1.calculate_total_score()
        player2.calculate_total_score()

        # player1
        if player1.isQuattro():
            ending_msg += f"{player1.user_name} made Quattro!\n"
        else:
            ending_msg += f"{player1.user_name} doesn't make Quattro!\n"

        ending_msg += f"{player1.user_name}'s Total Score is {player1.total_score} and Top Card is {player1.top_card}!\n\n"

        # player2
        if player2.isQuattro():
            ending_msg += f"{player2.user_name} made Quattro!\n"
        else:
            ending_msg += f"{player2.user_name} doesn't make Quattro!\n"

        ending_msg += f"{player2.user_name}'s Total Score is {player2.total_score} and Top Card is {player2.top_card}!\n\n"


        # Winner
        if player1.total_score > player2.total_score:
            winner = player1.user_name

        elif player1.total_score < player2.total_score:
            winner = player2.user_name

        else:
            if player1.top_card > player2.top_card:
                winner = player1.user_name

            elif player1.top_card < player2.top_card:
                winner = player2.user_name

            else:
                ending_msg += "Draw?\n"

                # TODO : Make Draw Case
                winner = "None"

    ending_msg += f"Winner is {winner}"

    print(ending_msg)

