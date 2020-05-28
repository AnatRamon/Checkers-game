from board import print_board
from players import DIRECTIVE_DOWN, DIRECTIVE_UP, ANOTHER_CHOICE


def player_move(player, board_state):
    """
    Make a move according to the players
    :param player: The player that is playing now.
    :type player: an instance of the class Player in players
    :param board_state: The board that is played.
    :type board_state: nested list
    :return: the board after a move has been made.
    :rtype: nested list
    """
    move = True
    piece_kind = False
    piece_row, piece_column = 0, 0
    move_valid = False
    times_tried_to_make_a_move = 0
    final_board = None
    impossible_move_message = "You can't move like that :(\n" + \
                              "Please pick a different move, or choose to move a different piece."
    choose_another = False
    while move:

        while not piece_kind:
            move_valid = False
            piece_row, piece_column, piece_kind = player.choose_piece(board_state)

        while not move_valid:
            if piece_kind == player.pawn:
                the_chosen_move = player.choose_where_to_move_for_pawn()
                if the_chosen_move == ANOTHER_CHOICE:
                    move_valid = True
                    piece_kind = False
                    choose_another = True
                else:
                    final_board = player.pawn_move(the_chosen_move, piece_row, piece_column, board_state)

            elif piece_kind == player.queen:
                horizontal_side, vertical_side, steps_num = player.choose_where_to_move_for_queen()
                if horizontal_side == ANOTHER_CHOICE or vertical_side == ANOTHER_CHOICE or steps_num == ANOTHER_CHOICE:
                    move_valid = True
                    piece_kind = False
                    choose_another = True
                else:
                    final_board = player.queen_move(horizontal_side, vertical_side, steps_num,
                                                    piece_row, piece_column, board_state)

            if final_board is not None:
                return final_board
            elif choose_another:
                pass
            elif times_tried_to_make_a_move > 0:
                print(impossible_move_message)
                print_board(board_state)
                move_valid = False
            else:
                print(impossible_move_message)
                times_tried_to_make_a_move += 1
                move_valid = False


def check_if_player_won(player1, player2, board):
    """
    Make a move according to the players
    :param player1: The first player that is playing.
    :type player1: an instance of the class Player in players
    :param player2: The second player that is playing now.
    :type player2: an instance of the class Player in players
    :param board: The board that is played.
    :type board: nested list
    :return: the player that won.
    :rtype: an instance of the class Player in players
    :exception: if no player won yet, returns False.
    """
    player1_pieces = False
    player2_pieces = False
    for row in board:
        if player1.pawn in row:
            player1_pieces = True
            break
        if player1.queen in row:
            player1_pieces = True
            break
    for row in board:
        if player2.pawn in row:
            player2_pieces = True
            break
        if player2.queen in row:
            player2_pieces = True
            break
    if not player1_pieces:
        return player2
    if not player2_pieces:
        return player1
    else:
        return False


def check_if_player_has_a_queen(player, board):
    """
    Make a move according to the players
    :param player: The player that has just made a move.
    :type player: an instance of the class Player in players
    :param board: The board that is played.
    :type board: nested list
    :return: the board after the needed pawns became queens.
    :rtype: nested list
    """
    if player.up_or_down == DIRECTIVE_UP:
        row = 0
    elif player.up_or_down == DIRECTIVE_DOWN:
        row = -1
    else:
        row = None

    for square in range(0, len(board[row])):
        if board[row][square] == player.pawn:
            board[row][square] = player.queen
    return board
