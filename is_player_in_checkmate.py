from king_safe import *
from valid_moves import *
from make_move import *

def is_player_in_checkmate(board, player):
    if not king_safe(board, player):
        for space, piece in board.items():
            if piece[0] == player:
                possible_moves = valid_moves(board, piece[1], space, player)
                for x in possible_moves:
                    possible_outcome = make_move(board, space, x)
                    if king_safe(possible_outcome, player):
                        return True
    return False