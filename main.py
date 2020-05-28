from players import Player, DIRECTIVE_DOWN, DIRECTIVE_UP
from style import Style
from board import make_board, print_board, empty_cell
from moves import player_move, check_if_player_won, check_if_player_has_a_queen
from instructions import instructions


def main(player1, player2):
    game_winner = False
    start_text = Style.Foreground.violet + "Let's get started!" + Style.end
    board_at_start = make_board(player1.pawn, player2.pawn, empty_cell)
    move = 1

    print("Hello players!")
    if_instructions = input("Would you like to see the instructions?\n"
                            "y/n\n")
    if if_instructions == "n":
        pass
    else:
        instructions()
    print(start_text)
    board = board_at_start
    while not game_winner:
        if (move % 2) == 0:
            playing_player = player2
        else:
            playing_player = player1
        print_board(board)
        board = player_move(playing_player, board)
        board = check_if_player_has_a_queen(playing_player, board)
        game_winner = check_if_player_won(player1, player2, board)
        move += 1
    print("Congratulations, " + game_winner.name + ", you won!!!! ")
    print(game_winner.color + """          o 
       o^/|\\^o
    o_^|\\/*\\/|^_o
   o\\*`'.\\|/.'`*/o
    \\\\\\\\\\\\|//////
     {><><@><><}
     `\"\"\"\"\"\"\"\"\"`""" + Style.end)


if __name__ == "__main__":
    red_player = Player(Style.Foreground.red, "Red", DIRECTIVE_DOWN)
    blue_player = Player(Style.Foreground.blue, "Blue", DIRECTIVE_UP)
    main(red_player, blue_player)

