from game import *

def startup_game() :
    print ("Enter the board size")
    board_size = int(input().strip())
    new_game = TicTacToe(board_size)

    new_game.print_board()

    game_over = False
    while game_over != True:
        print("Enter the row and column number to place -1 or 1")
        player, row, col = input().strip().split()

        player = int(player)
        row = int(row)
        col = int(col)

        game_over = new_game.move(row, col, player)

        if game_over == -3:
            print("Invalid move")
        elif game_over == -2:
            new_game.print_board()
            continue
        elif game_over == 0:
            new_game.print_board()
            print("It's a draw")
            game_over = True
        else:
            new_game.print_board()
            print("Player ", player, " wins")
            game_over = True
