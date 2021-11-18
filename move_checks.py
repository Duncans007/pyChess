from make_move import make_move
from valid_moves import valid_moves

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





def king_safe(board, player):
    #find the king on the board
    for space, piece in board.items():
        if piece == player+"k":
            king_space = space

    #check all lines of sight to the king with large pieces
    #run the king's spot as each of the different pieces
    for x in ["c","h","b","q"]:
        possible_attacks = valid_moves(board,x,king_space,player)
        for y in possible_attacks:
            if board[y][1] == x and board[y][0] != player:
                return False

    #check diagonals for pawns
    x = int(king_space[0])
    y = int(king_space[1])
    if player == "w":
        if board[str(x+1)+str(y+1)] == "bp" or board[str(x-1)+str(y+1)] == "bp":
            return False
    elif player == "b":
        if board[str(x+1)+str(y-1)] == "wp" or board[str(x-1)+str(y-1)] == "wp":
            return False

    return True
