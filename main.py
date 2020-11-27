from QuattroComponents.Deck import Deck
from QuattroComponents.Player import Player, Anonymous_player
from QuattroComponents.Input_handler import user_input
from QuattroComponents.View.EndOfGame import EndOfGame
from QuattroComponents.View.MainGameView import MainGameView
from QuattroComponents.View.WelcomeView import WelcomeView


def player_init(player: Player, main_deck: Deck):
    while True:
        print(f"[System] {player.user_name}! Your Deck is \n{player}\n")
        player_input = user_input(now_turn=player, guide_msg="Please Input([o]kay, [m]alligan)")

        if len(player_input) == 1 and (player_input is 'o' or player_input is 'm'):
            # Card Open Case in here
            if player_input is 'o':
                print("\n[System] Select Deck Finished\n")
                break

            # Malligan Case in here
            elif player_input is 'm':
                player.do_malligan(main_deck=main_deck)
                break

            else:
                print("Try Again!(Input Error)")

        else:
            print("Try Again!")

def main():
    ### Show Welcome View
    WelcomeView()

    ### Deck and Players Init!
    main_deck = Deck()
    main_deck.shuffle_deck()

    player1 = Player(user_name="player1", user_deck=main_deck.draw_to_player(player_type="user"))
    player2 = Player(user_name="player2", user_deck=main_deck.draw_to_player(player_type="user"))

    player_init(player=player1, main_deck=main_deck)
    player_init(player=player2, main_deck=main_deck)

    main_deck.shuffle_deck()
    anonymous_player_list = []
    for i in range(1, 7):
        anonymous_player_list.append(Anonymous_player(user_name=f"anonymous{str(i)}",
                                                      user_deck=main_deck.draw_to_player(player_type="anonymous")))

    ### Players Init Fin

    winner = ""
    surrender_flag = False

    ### Play Game
    ### turn rule : p1 -> p2 -> p2 -> p1
    for turn_count in range(8):
        if not surrender_flag:
            if turn_count in (0, 3, 4, 7):
                now_player = player1
            else:
                now_player = player2

            print(f"\n\n[ Round {turn_count + 1}: {now_player.user_name} ]\n")

            MainGameView(player1=player1,
                         player2=player2,
                         anonymous_player_list=anonymous_player_list,
                         now_turn=now_player.user_name)

            while True:
                player_input = user_input(now_turn=now_player, guide_msg="Please Input([o]pen, [c]hange, [s]urrender)")
                if player_input == "o":
                    if (turn_count == 6 and now_player.user_change_quota) or (turn_count == 7 and now_player.user_change_quota):
                        print("You must change card with all anonymous player!")
                        continue

                    else:
                        quit_flag = now_player.open_card()

                        if quit_flag == 0:
                            # only break in open case
                            break
                        else:
                            continue

                elif player_input == "c":
                    now_player.change_card(anonymous_player_list=anonymous_player_list)
                    MainGameView(player1=player1,
                                 player2=player2,
                                 anonymous_player_list=anonymous_player_list,
                                 now_turn=now_player.user_name)

                elif player_input == "s":
                    player_input = user_input(now_turn=now_player, guide_msg="Are you sure? [y]es")

                    if player_input == "y":
                        surrender_flag = True
                        if now_player.user_name == "player1":
                            winner = player2.user_name
                        else:
                            winner = player1.user_name
                        break
                else:
                    print("Try Again!")

            if surrender_flag:
                print(f"{now_player.user_name} Resign!\n")
    ### Play Game

    # Last Print
    MainGameView(player1=player1,
                 player2=player2,
                 anonymous_player_list=anonymous_player_list,
                 now_turn="END")

    ### Fin
    EndOfGame(surrender_flag=surrender_flag, winner=winner, player1=player1, player2=player2)



if __name__ == '__main__':
    main()
