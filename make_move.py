def make_move(board, piece_location, move_to_space):
    board[move_to_space] = board[piece_location]
    board[piece_location] = "  "
    return board