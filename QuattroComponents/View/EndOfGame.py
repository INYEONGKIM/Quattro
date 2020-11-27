from QuattroComponents.Player import Player
from pyfiglet import Figlet

def EndOfGame(surrender_flag: bool, winner: str, player1: Player, player2: Player):
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
                p1_top_color = -1
                p2_top_color = -1

                ## Rating
                ## Red: 4, Blue: 3, Yellow: 2, Green: 1

                print(player1.top_card)

                for p1_card in player1.user_deck:
                    if p1_card.number == player1.top_card:
                        if p1_card.color == "red":
                            p1_top_color = 4

                        elif p1_card.color == "blue" and p1_top_color < 4:
                            p1_top_color = 3

                        elif p1_card.color == "yellow" and p1_top_color < 3:
                            p1_top_color = 2

                        elif p1_card.color == "green" and p1_top_color < 2:
                            p1_top_color = 1

                for p2_card in player2.user_deck:
                    if p2_card.number == player2.top_card:
                        if p2_card.color == "red":
                            p2_top_color = 4

                        elif p2_card.color == "blue" and p2_top_color < 4:
                            p2_top_color = 3

                        elif p2_card.color == "yellow" and p2_top_color < 3:
                            p2_top_color = 2

                        elif p2_card.color == "green" and p2_top_color < 2:
                            p2_top_color = 1

                if p1_top_color > p2_top_color:
                    winner = player1.user_name

                elif p1_top_color < p2_top_color:
                    winner = player2.user_name
                else:
                    winner = "None"

    ending_msg += f"Winner is {winner}"

    f = Figlet(font="small").renderText("Game Over!")
    print(f, ending_msg, sep='\n')

