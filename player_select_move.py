from king_safe import *
from valid_moves import *
from make_move import *

def player_select_move(board, piece_location, player):
    piece_type = board[piece_location][1]
    list_of_possible_moves = valid_moves(board, piece_type, piece_location, player)
    print(list_of_possible_moves)

    selection = input("Select destination: ")
    if selection not in list_of_possible_moves:
        print("Invalid move please try again")
        return "null"
    else:
        board = make_move(board, piece_location, selection)
        if king_safe(board, player):
            return board
        else:
            print("You are still in Check")
            return "null"