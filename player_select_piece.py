def player_select_piece(board, player):
    while True:
        print("Turn: "+player)
        selection = input("Select Piece (xy): ")

        if board[selection] != "  ":
            if board[selection][0] == player:
                break
        print("Invalid selection, try again")
    return selection
