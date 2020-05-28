from style import Style
from board import print_board, empty_cell

DIRECTIVE_UP = "up"
DIRECTIVE_DOWN = "down"
DIRECTIVE_RIGHT = "right"
DIRECTIVE_LEFT = "left"
ANOTHER_CHOICE = "another"


class Player(object):
    """
    The Player object contains the player attributes.
    """

    def __init__(self, color, name, up_or_down):
        """
        :param color: The color of the player.
        :type color: an instance of Style class in style
        :param name: The player's name.
        :type name: str
        :param up_or_down: Used to determine whether the player will go up or down.
                           Should contain one of the two: "up" or "down".
        :type up_or_down: str
        """
        self.color = color
        self.pawn = self.color + "0" + Style.end
        self.queen = self.color + "q" + Style.end
        self.name = self.color + name + Style.end
        self.up_or_down = up_or_down

    def choose_piece(self, board):
        """
        Gets from the player the piece they would like to move.
        :param board: The board that is played.
        :type board: nested list
        :return: tuple(row, column, player.pawn)
            :return row: The row the chosen piece is at.
            :rtype row: int
            :return column: The column the chosen piece is at.
            :rtype column: int
            :return piece_type: The piece type.
            :rtype piece_type: str
        """
        chosen_piece = input(self.name + ", which piece would you like to move?  ")
        writing_error = "Looks like you wrote an invalid place.\n" \
                        "Remember, write the row (in numbers) and then the column (in letters)"
        if len(chosen_piece) > 2:
            print(writing_error)
            return False, False, False

        chosen_piece = chosen_piece.upper()
        try:
            column = chosen_piece[1]
        except IndexError:
            print(writing_error)
            return False, False, False
        columns = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:len(board[0])]
        try:
            column = columns.index(column)
        except ValueError:
            print(writing_error)
            return False, False, False
        column = int(column)
        try:
            row = int(chosen_piece[0])
        except ValueError:
            print("writing_error")
            return False, False, False
        if board[row][column] == self.pawn:
            return row, column, self.pawn
        elif board[row][column] == self.queen:
            return row, column, self.queen
        else:
            print("Oh, oh, looks like you don't have a piece there.\n"
                  "Remember your pieces are", self.pawn, "and", self.queen)
            return False, False, False

    def check_for_another_eat(self, row, column, board, piece_kind):
        ate_up_right = False
        ate_up_left = False
        ate_down_right = False
        ate_down_left = False
        possible = True
        up_right = True
        up_left = True
        down_right = True
        down_left = True
        while possible:
            if self.up_or_down == DIRECTIVE_UP or piece_kind == self.queen:
                if (row - 2) < 0:
                    up_left = False
                    up_right = False
                if (column - 2) >= 0:
                    while up_left:
                        if board[row - 1][column - 1] != self.pawn and board[row - 1][column - 1] != self.queen and \
                                board[row - 1][column - 1] != empty_cell and board[row - 2][column - 2] == empty_cell:
                            board[row][column] = Style.Background.yellow + board[row][column] + Style.end
                            print_board(board)
                            eat_up_left = input("Would you like to eat in a up left diagonal? y/n  ")
                            if eat_up_left == "y":
                                board[row][column] = empty_cell
                                board[row - 1][column - 1] = empty_cell
                                board[row - 2][column - 2] = piece_kind
                                row -= 2
                                column -= 2
                                ate_up_left = True
                                up_right = False
                                up_left = False
                                down_right = False
                                down_left = False
                            elif eat_up_left == "n":
                                board[row][column] = piece_kind
                                up_left = False
                        else:
                            up_left = False
                if (column + 2) < len(board[row]):
                    while up_right:
                        if board[row - 1][column + 1] != self.pawn and board[row - 1][column + 1] != self.queen and \
                             board[row - 1][column + 1] != empty_cell and board[row - 2][column + 2] == empty_cell:
                            board[row][column] = Style.Background.yellow + board[row][column] + Style.end
                            print_board(board)
                            eat_up_right = input("Would you like to eat in a up right diagonal? y/n  ")
                            if eat_up_right == "y":
                                board[row][column] = empty_cell
                                board[row - 1][column + 1] = empty_cell
                                board[row - 2][column + 2] = piece_kind
                                row -= 2
                                column += 2
                                ate_up_right = True
                                up_right = False
                                down_right = False
                                down_left = False
                            elif eat_up_right == "n":
                                board[row][column] = piece_kind
                                up_right = False
                        else:
                            up_right = False

            if self.up_or_down == DIRECTIVE_DOWN or piece_kind == self.queen:
                if (row + 2) >= (len(board)):
                    down_left = False
                    down_right = False
                if (column - 2) >= 0:
                    while down_left:
                        if board[row + 1][column - 1] != self.pawn and board[row + 1][column - 1] != self.queen and \
                             board[row + 1][column - 1] != empty_cell and board[row + 2][column - 2] == empty_cell:
                            board[row][column] = Style.Background.yellow + board[row][column] + Style.end
                            print_board(board)
                            eat_down_left = input("Would you like to eat in a down left diagonal? y/n  ")
                            if eat_down_left == "y":
                                board[row][column] = empty_cell
                                board[row + 1][column - 1] = empty_cell
                                board[row + 2][column - 2] = piece_kind
                                row += 2
                                column -= 2
                                ate_down_left = True
                                down_right = False
                                down_left = False
                            elif eat_down_left == "n":
                                board[row][column] = piece_kind
                                down_left = False
                        else:
                            down_left = False

                if (column + 2) < len(board[row]):
                    while down_right:
                        if board[row + 1][column + 1] != self.pawn and board[row + 1][column + 1] != self.queen and \
                             board[row + 1][column + 1] != empty_cell and board[row + 2][column + 2] == empty_cell:
                            board[row][column] = Style.Background.yellow + board[row][column] + Style.end
                            print_board(board)
                            eat_down_right = input("Would you like to eat in a down right diagonal? y/n  ")
                            if eat_down_right == "y":
                                board[row][column] = empty_cell
                                board[row + 1][column + 1] = empty_cell
                                board[row + 2][column + 2] = piece_kind
                                row += 2
                                column += 2
                                ate_down_right = True
                                down_right = False
                            elif eat_down_right == "n":
                                board[row][column] = piece_kind
                                down_right = False
                        else:
                            down_right = False

            if ate_up_right or ate_up_left or ate_down_right or ate_down_left:
                ate_up_right = False
                ate_up_left = False
                ate_down_right = False
                ate_down_left = False
                up_right = True
                up_left = True
                down_right = True
                down_left = True
            else:
                return board

    def pawn_move(self, horizontal_side, row, column, board):
        vertical_sign = 1
        horizontal_sign = 1
        if horizontal_side == DIRECTIVE_LEFT:
            horizontal_sign *= -1
        if self.up_or_down == DIRECTIVE_UP:
            vertical_sign *= -1

        if 0 <= (row + vertical_sign) < len(board) and 0 <= (column + horizontal_sign) < len(board[row]):
            if board[row + vertical_sign][column + horizontal_sign] == empty_cell:
                board[row][column] = empty_cell
                board[row + vertical_sign][column + horizontal_sign] = self.pawn
                return board
            elif board[row + vertical_sign][column + horizontal_sign] != self.pawn and \
                    board[row + vertical_sign][column + horizontal_sign] != self.queen and \
                    board[row + (2 * vertical_sign)][column + (2 * horizontal_sign)] == empty_cell:
                board[row][column] = empty_cell
                board[row + vertical_sign][column + horizontal_sign] = empty_cell
                board[row + (2 * vertical_sign)][column + (2 * horizontal_sign)] = self.pawn
                current_row = row + (2 * vertical_sign)
                current_column = column + (2 * horizontal_sign)
                if self.up_or_down == DIRECTIVE_DOWN:
                    board = self.check_for_another_eat(current_row, current_column, board, self.pawn)
                elif self.up_or_down == DIRECTIVE_UP:
                    board = self.check_for_another_eat(current_row, current_column, board, self.pawn)
                return board
            else:
                return None
        else:
            return None

    def queen_move(self, horizontal_side, vertical_side, steps_num, row, column, board):
        """
        Moves a queen as the player wishes.
        :param steps_num: The number of steps the player wants to go
        :type steps_num: int
        :param vertical_side: The vertical side the player wants to go.
        :type vertical_side: str
        :param horizontal_side: The horizontal side the player wants to go.
        :type horizontal_side: str
        :param row: The row the queen is at.
        :type row: int
        :param column: The column the queen is at.
        :type column: int
        :param board: The board the queen is at.
        :type board: nested list
        :return: The board after the move.
        :rtype: nested list
        :exception: If the move is illegal, the function will return None.
        """
        squares_in_move = []
        vertical_sign = 1
        horizontal_sign = 1
        if horizontal_side == DIRECTIVE_LEFT:
            horizontal_sign *= -1
        if vertical_side == DIRECTIVE_UP:
            vertical_sign *= -1
        vertical_steps_num = steps_num * vertical_sign
        horizontal_steps_num = steps_num * horizontal_sign
        if 0 <= (row + vertical_steps_num) < len(board) and 0 <= (column + horizontal_steps_num) < len(board[row]):
            for step in range(1, (steps_num + 1)):
                vertical_steps_num = step * vertical_sign
                horizontal_steps_num = step * horizontal_sign
                squares_in_move.append(board[row + vertical_steps_num][column + horizontal_steps_num])
            if self.queen in squares_in_move or self.pawn in squares_in_move:
                return None
            elif squares_in_move[-1] != empty_cell:
                return None
            for num in range(1, len(squares_in_move)):
                if squares_in_move[num] != empty_cell and squares_in_move[num] == squares_in_move[num - 1]:
                    return None
            board[row][column] = empty_cell
            for step in range(1, steps_num):
                vertical_steps_num = step * vertical_sign
                horizontal_steps_num = step * horizontal_sign
                board[row + vertical_steps_num][column + horizontal_steps_num] = empty_cell
            vertical_steps_num = steps_num * vertical_sign
            horizontal_steps_num = steps_num * horizontal_sign
            board[row + vertical_steps_num][column + horizontal_steps_num] = self.queen
            if len(squares_in_move) >= 2:
                if squares_in_move[-2] != empty_cell:
                    row_after = row + vertical_steps_num
                    column_after = column + horizontal_steps_num
                    board = self.check_for_another_eat(row_after, column_after, board, self.queen)
            return board

    def choose_where_to_move_for_pawn(self):
        """
        Gets from the player the move they would like to take with the pawn.
        :return: The chosen move.
        :rtype: str
        """
        while True:
            chosen_move = input(self.name + ", would you like to move left or right?  ")
            chosen_move = chosen_move.lower()
            if chosen_move == "l" or chosen_move == "a" or chosen_move == "left":
                chosen_move = DIRECTIVE_LEFT
            elif chosen_move == "r" or chosen_move == "d" or chosen_move == "right":
                chosen_move = DIRECTIVE_RIGHT
            if chosen_move in [DIRECTIVE_RIGHT, DIRECTIVE_LEFT, ANOTHER_CHOICE]:
                return chosen_move
            else:
                print("This isn't a valid move")

    def choose_where_to_move_for_queen(self):
        """
        Gets from the player the move they would like to take with the queen.
        :return: tuple(horizontal_side, vertical_side, steps_num)
            :return horizontal_side: The horizontal side the queen will move in.
            :rtype horizontal_side: str
            :return vertical_side: The vertical side the queen will move in.
            :rtype vertical_side: str
            :return steps_num: The number of steps the queen will move at.
            :rtype steps_num: int
        """

        horizontal_side, vertical_side, steps_num = None, None, None
        horizontal_valid, vertical_valid, steps_valid = False, False, False

        while not horizontal_valid:
            horizontal_side = input(self.name + ", would you like to move left or right?  ")
            horizontal_side = horizontal_side.lower()
            if horizontal_side == "l" or horizontal_side == "a" or horizontal_side == "left":
                horizontal_side = DIRECTIVE_LEFT
            elif horizontal_side == "r" or horizontal_side == "d" or horizontal_side == "right":
                horizontal_side = DIRECTIVE_RIGHT
            if horizontal_side in [DIRECTIVE_RIGHT, DIRECTIVE_LEFT]:
                horizontal_valid = True
            elif horizontal_side == ANOTHER_CHOICE:
                horizontal_valid = True
                vertical_valid = True
                steps_valid = True
            else:
                print("This isn't a valid move")

        while not vertical_valid:
            vertical_side = input(self.name + ", would you like to move up or down?  ")
            vertical_side = vertical_side.lower()
            if vertical_side == "u" or vertical_side == "w" or vertical_side == "up":
                vertical_side = DIRECTIVE_UP
            elif vertical_side == "d" or vertical_side == "s" or vertical_side == "down":
                vertical_side = DIRECTIVE_DOWN
            if vertical_side in [DIRECTIVE_UP, DIRECTIVE_DOWN]:
                vertical_valid = True
            elif vertical_valid == ANOTHER_CHOICE:
                vertical_valid = True
                steps_valid = True
            else:
                print("This isn't a valid move.")

        while not steps_valid:
            steps_num = input(self.name + ", how many steps would you like to take? ")
            try:
                steps_num = int(steps_num)
                if steps_num > 0:
                    steps_valid = True
            except ValueError:
                if steps_num == ANOTHER_CHOICE:
                    steps_valid = True
                print("Please enter a number bigger than zero.")
        return horizontal_side, vertical_side, steps_num
