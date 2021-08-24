def make_move(board, piece_location, move_to_space):
    test_board = board
    test_board[move_to_space] = test_board[piece_location]
    test_board[piece_location] = "  "
    return test_board
