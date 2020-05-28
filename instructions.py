from board import print_board, make_board
from style import Style


def instructions():
    """
    Prints the instructions to the game.
    """
    pawn1 = Style.Foreground.red + "0" + Style.end
    pawn2 = Style.Foreground.blue + "0" + Style.end
    empty_cell = 0
    queen = Style.Foreground.red + "q" + Style.end

    regular_board = make_board(pawn1, pawn2, empty_cell)

    ex_board1 = [[pawn1, empty_cell, empty_cell, empty_cell],
                 [empty_cell, empty_cell, empty_cell, empty_cell],
                 [empty_cell, queen, empty_cell, empty_cell],
                 [empty_cell, empty_cell, empty_cell, pawn2]]

    print("The checkers board is 8 by 8. This is how it looks at the start:")
    print_board(regular_board)
    input("Press Enter to continue.")

    print("\n"
          "Each player has pieces in different color:\n" +
          Style.Foreground.blue + "Blue" + Style.end + " or " + Style.Foreground.red + "Red" + Style.end + ".\n"
          "There are two kinds of pieces: pawn-",
          pawn1, "and queen-", queen + ".\n"
          "A pawn that crosses the board and reaches the other players' side becomes a queen.")
    input("Press Enter to continue.")

    print("\n"
          "The rows in the board are marked in numbers. \n"
          "The columns in the board are marked in capital letters.\n"
          "Each piece is marked first by the row number and then by the column letter. \n"
          "for example:\n" +
          pawn1, "is in" + Style.Foreground.cyan + " 0A" + Style.end + ".\n" +
          queen, "is in" + Style.Foreground.cyan + " 2B" + Style.end + ".\n" +
          pawn2, "is in" + Style.Foreground.cyan + " 3D" + Style.end + ".\n")
    print_board(ex_board1)
    input("Press Enter to continue.")

    print("\n"
          "After choosing a piece you'll need to pick where to move. \n"
          "You can pick to move:", Style.Foreground.cyan + "left \\ right" + Style.end + ". \n"
          "You can also write",
          Style.Foreground.cyan + "l \\ r" + Style.end + " for short. \n"
          "It is also possible to write", Style.Foreground.cyan + "a \\ d" + Style.end + " respectively. \n" +
          Style.Foreground.red + "Clarification:\n" + Style.end +
          "left  is always: <---- \n"
          "right is always: ---->")
    input("Press Enter to continue.")

    print("\n"
          "of course if you choose a queen, you'll need also to choose how to move vertically. \n"
          "You can pick to move:", Style.Foreground.cyan + "up \\ down" + Style.end + ". \n"    
          "You can also write", Style.Foreground.cyan + "u \\ d" + Style.end + " for short. \n"
          "It is also possible to write", Style.Foreground.cyan + "w \\ s" + Style.end + " respectively. \n" +
          Style.Foreground.red + "Clarification: " + Style.end +
          "write the move correctly, otherwise, the computer won't understand your move! \n")
    input("Press Enter to continue.")

    print("\n"
          "Lastly - if you choose a queen - you'll need to chose the number of steps." +
          Style.Foreground.red + "Clarification: " + Style.end +
          "jumping over a pawn counts as two steps!")
    input("Press Enter to continue.")

    print("\n"
          "If you changed your mind and would like to move a different piece, "
          "simply write", Style.Foreground.cyan + "another" + Style.end + ".\n")
    input("Press Enter to continue.")
    print("\n\n\n")


if __name__ == "__main__":
    instructions()
