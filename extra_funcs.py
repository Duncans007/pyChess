def draw_board(board):
    for x in range(16,-1,-1):
        if x % 2 == 0:
            print("+----+----+----+----+----+----+----+----+")
        else:
            y_cord = int((x+1)/2)
            x_cord = int(1)
            print("| "+board[str(x_cord)+str(y_cord)]+" | "+board[str(x_cord+1)+str(y_cord)]+" | "+board[str(x_cord+2)+str(y_cord)]+" | "+board[str(x_cord+3)+str(y_cord)]+" | "+board[str(x_cord+4)+str(y_cord)]+" | "+board[str(x_cord+5)+str(y_cord)]+" | "+board[str(x_cord+6)+str(y_cord)]+" | "+board[str(x_cord+7)+str(y_cord)]+" | "+str(y_cord))
    print("^  1 ^  2 ^  3 ^  4 ^  5 ^  6 ^  7 ^  8 ^")


def change_turn(turn):
    if turn == "w":
        return "b"
    elif turn == "b":
        return "w"


def strout(x,y):
    out = str(int(x))+str(int(y))
    return out
