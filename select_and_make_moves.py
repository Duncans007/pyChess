from extra_funcs import *
from select_and_make_move import *

def make_move(board, piece_location, move_to_space):
    test_board = board
    test_board[move_to_space] = test_board[piece_location]
    test_board[piece_location] = "  "
    return test_board


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
            return selection
        else:
            print("You are still in Check")
            return "null"
        
        
def player_select_piece(board, player):
    while True:
        print("Turn: "+player)
        selection = input("Select Piece (xy): ")

        if board[selection] != "  ":
            if board[selection][0] == player:
                break
        print("Invalid selection, try again")
    return selection
