from style import Style

empty_cell = "0"


def make_board(pawn1, pawn2, empty):
    """"
    Creates a board for two given players.
    :param pawn1: an instance from the class Player in players. This player will be at the top of the board.
    :param pawn2: an instance from the class Player in players. This player will be at the bottom of the board.
    :param empty: defines how an empty call will look.
    :return: a board with the players pieces organized like in Checkers.
    :rtype: nested list.
    """
    row_0 = [empty, pawn1] * 4
    row_1 = [pawn1, empty] * 4
    row_2 = [empty, pawn1] * 4
    row_3 = [empty] * 8
    row_4 = [empty] * 8
    row_5 = [pawn2, empty] * 4
    row_6 = [empty, pawn2] * 4
    row_7 = [pawn2, empty] * 4
    board = [row_0] + [row_1] + [row_2] + [row_3] + [row_4] + [row_5] + [row_6] + [row_7]
    return board


def print_board(board):
    """
    Prints nicely a given board.
    :param board: a given board.
    :type board: nested lists
    """
    possible_columns_names = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    columns = ""
    columns_names = possible_columns_names[:len(board[0])]
    for column in columns_names:
        columns += " " + column
    styled_columns = Style.Background.light_grey + Style.Foreground.dark_grey + "   " + columns + " " + Style.end
    print(styled_columns)
    row_num = 0
    if len(board) > 10:
        for row in range(len(board)):
            if row_num < 10:
                styled_row_num = Style.Background.light_grey + Style.Foreground.dark_grey + "  " + str(row_num) \
                                 + " " + Style.end
            else:
                styled_row_num = Style.Background.light_grey + Style.Foreground.dark_grey + " " + str(row_num) \
                                 + " " + Style.end
            print(styled_row_num, *board[row])
            row_num += 1
    else:
        for row in range(len(board)):
            styled_row_num = Style.Background.light_grey + Style.Foreground.dark_grey + " " + str(
                row_num) + " " + Style.end
            print(styled_row_num, *board[row])
            row_num += 1


if __name__ == "__main__":
    ex_board = make_board(Style.Foreground.red + "0" + Style.end, Style.Foreground.blue + "0" + Style.end, "0")
    print_board(ex_board)
