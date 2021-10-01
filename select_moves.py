from extra_funcs import strout
from move_checks import valid_moves, king_safe
from valid_moves import valid_moves
from make_move import make_move
from pygame_funcs import click_input, update_screen

def player_select_move(board, piece_location, player):
    piece_type = board[piece_location][1]
    list_of_possible_moves = valid_moves(board, piece_type, piece_location, player)
    print(list_of_possible_moves)
    selection = click_input()
    #selection = input("Select destination: ")

    if selection not in list_of_possible_moves:
        print("Invalid move please try again")
        return "null"
    else:
        test_board = board
        test_board = make_move(test_board, piece_location, selection)
        if king_safe(test_board, player):
            return selection
        else:
            print("You are still in Check")
            return "null"
        
        
def player_select_piece(board, player):
    while True:
        print("Turn: "+player)
        #selection = input("Select Piece (xy): ")
        selection = click_input()

        if board[selection] != "  ":
            if board[selection][0] == player:
                break
        print("Invalid selection, try again")
    return selection

