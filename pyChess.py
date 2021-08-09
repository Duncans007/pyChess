import math
import numpy as np

#Draw board function
def draw_board(board):
    for x in range(16,-1,-1):
        if x%2==0:
            print("+----+----+----+----+----+----+----+----+")
        else:
            y_cord = int((x+1)/2)
            x_cord = int(1)
            print("| "+board[str(x_cord)+str(y_cord)]+" | "+board[str(x_cord+1)+str(y_cord)]+" | "+board[str(x_cord+2)+str(y_cord)]+" | "+board[str(x_cord+3)+str(y_cord)]+" | "+board[str(x_cord+4)+str(y_cord)]+" | "+board[str(x_cord+5)+str(y_cord)]+" | "+board[str(x_cord+6)+str(y_cord)]+" | "+board[str(x_cord+7)+str(y_cord)]+" | "+str(y_cord))
    print("^  1 ^  2 ^  3 ^  4 ^  5 ^  6 ^  7 ^  8 ^")


#Change turn function
def change_turn(turn):
    if turn == "w":
        turn = "b"
        print("Turn: Black")
    elif turn == "b":
        turn = "w"
        print("Turn: White")
    return turn


#IO function for perpetual piece selection until valid
def player_select_piece(board, player):
    while True:
        selection = input("Select Piece: ")

        if board[selection] != "  ":
            if board[selection][0] == player:
                break
        print("Invalid selection, try again")
    return selection


#Small function to facilitate concatenation of location numbers
def strout(x,y):
    out = str(int(x))+str(int(y))
    return out


#Test of valid moves for every piece in the game
def valid_moves(board, piece_type, piece_location, player):
    move_array = []
    px = int(piece_location[0])
    py = int(piece_location[1])

#Valid moves for pawn
    if piece_type == "p":
        if player == "w":
            mult = 1
        elif player == "b":
            mult = -1

        if board[strout(px,py+(1*mult))] == "  ":
            move_array.append(strout(px,py+(1*mult)))
            if (py == 2 or py == 7) and board[strout(px,py+(2*mult))] == "  ":
                move_array.append(strout(px,py+(2*mult)))
        try:
            if board[strout(px+1,py+(1*mult))] != "  " and board[strout(px+1,py+(1*mult))][0] != player:
                move_array.append(strout(px+1,py+(1*mult)))
        except KeyError:
            pass
        try:
            if board[strout(px-1,py+(1*mult))] != "  " and board[strout(px-1,py+(1*mult))][0] != player:
                move_array.append(strout(px-1,py+(1*mult)))
        except KeyError:
            pass

#Valid moves for Castle
    elif piece_type == "c":
        for y in [ [1,0],[0,1],[-1,0],[0,-1] ]:
            for x in range(1,8):
                move_array.append(strout(px+(x*y[0]),py+(x*y[1])))
                try:
                    if board[strout(px+(x*y[0]),py+(x*y[1]))] != "  ":
                        if board[strout(px+(x*y[0]),py+(x*y[1]))][0] == player:
                            move_array.pop(len(move_array)-1)
                        break
                except KeyError:
                    move_array.pop(len(move_array)-1)
                    break


#Valid moves for the horse
    elif piece_type == "h":
        move_array.append(str(int(px)+2)+str(int(py)+1))
        move_array.append(str(int(px)+2)+str(int(py)-1))
        move_array.append(str(int(px)-2)+str(int(py)+1))
        move_array.append(str(int(px)-2)+str(int(py)-1))
        move_array.append(str(int(px)+1)+str(int(py)+2))
        move_array.append(str(int(px)-1)+str(int(py)+2))
        move_array.append(str(int(px)+1)+str(int(py)-2))
        move_array.append(str(int(px)-1)+str(int(py)-2))

#Valid moves for the bishop
    elif piece_type == "b":
        for y in [ [1,-1],[-1,-1],[1,1],[-1,1] ]:
            for x in range(1,8):
                move_array.append(strout(px+(x*y[0]),py+(x*y[1])))
                try:
                    if board[strout(px+(x*y[0]),py+(x*y[1]))] != "  ":
                        if board[strout(px+(x*y[0]),py+(x*y[1]))][0] == player:
                            move_array.pop(len(move_array)-1)
                        break
                except KeyError:
                    move_array.pop(len(move_array)-1)
                    break

#Valid moves for the King
    elif piece_type == "k":
        move_array.append(str(int(px)+1)+str(int(py)+0))
        move_array.append(str(int(px)+1)+str(int(py)+1))
        move_array.append(str(int(px)+0)+str(int(py)+1))
        move_array.append(str(int(px)-1)+str(int(py)+1))
        move_array.append(str(int(px)-1)+str(int(py)+0))
        move_array.append(str(int(px)-1)+str(int(py)-1))
        move_array.append(str(int(px)+0)+str(int(py)-1))
        move_array.append(str(int(px)+1)+str(int(py)-1))

#Valid moves for the queen
    elif piece_type == "q":
        for y in [ [1,0],[0,1],[-1,0],[0,-1] ]:
            for x in range(1,8):
                move_array.append(strout(px+(x*y[0]),py+(x*y[1])))
                try:
                    if board[strout(px+(x*y[0]),py+(x*y[1]))] != "  ":
                        if board[strout(px+(x*y[0]),py+(x*y[1]))][0] == player:
                            move_array.pop(len(move_array)-1)
                        break
                except KeyError:
                    move_array.pop(len(move_array)-1)
                    break
        for y in [ [1,-1],[-1,-1],[1,1],[-1,1] ]:
            for x in range(1,8):
                move_array.append(strout(px+(x*y[0]),py+(x*y[1])))
                try:
                    if board[strout(px+(x*y[0]),py+(x*y[1]))] != "  ":
                        if board[strout(px+(x*y[0]),py+(x*y[1]))][0] == player:
                            move_array.pop(len(move_array)-1)
                        break
                except KeyError:
                    move_array.pop(len(move_array)-1)
                    break



    #cleanup
    #remove any extra moves that collide with wrong team or off board
    for i in range( len(move_array) - 1, -1, -1):
        x = move_array[i]
        try:
            if board[x] != "  ":
                if board[x][0] == player:
                    move_array.pop(move_array.index(x))
        except KeyError:
            move_array.pop(move_array.index(x))

    #double check for off-board
    for i in range( len(move_array) - 1, -1, -1):
        x = move_array[i]
        if int(x[0])>8:
            move_array.pop(move_array.index(x))
        if int(x[0])<1:
            move_array.pop(move_array.index(x))
        if int(x[1])>8:
            move_array.pop(move_array.index(x))
        if int(x[1])<1:
            move_array.pop(move_array.index(x))

    #remove non-unique values
    move_array = np.unique(move_array)

    return move_array


#IO function for player to select destination space
def player_select_move(board, piece_location, player):
    piece_type = board[piece_location][1]
    list_of_possible_moves = valid_moves(board, piece_type, piece_location, player)
    print(list_of_possible_moves)

    selection = input("Select destination: ")
    if selection not in list_of_possible_moves:
        print("Invalid move please try again")
        return "null"
    else:
        board[selection] = board[piece_location]
        board[piece_location] = "  "
        if king_safe(board, player) == True:
            return board
        else:
            print("You are still in Check")
            return "null"

#Check for check at the end of every turn and do not allow move if it results in check.
def king_safe(board, player):
    #find the king on the board
    for space, piece in board.items():
        if piece == player+"k":
            king_space = space

    #check all lines of sight to the king with large pieces
    #run the king's spot as each of the different pieces
    for x in ["c","h","b","q"]:
        print("x")
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

#TODO: Add checkmate!@!!!!
def player_test_win(board, player):
    return False

player_win = False
player_turn = "b"

#Initial board setup
board_dict = {
    "11": "wc",
    "12": "wp",
    "13": "  ",
    "14": "  ",
    "15": "  ",
    "16": "  ",
    "17": "bp",
    "18": "bc",

    "21": "wh",
    "22": "wp",
    "23": "  ",
    "24": "  ",
    "25": "  ",
    "26": "  ",
    "27": "bp",
    "28": "bh",

    "31": "wb",
    "32": "wp",
    "33": "  ",
    "34": "  ",
    "35": "  ",
    "36": "  ",
    "37": "bp",
    "38": "bb",

    "41": "wq",
    "42": "wp",
    "43": "  ",
    "44": "  ",
    "45": "  ",
    "46": "  ",
    "47": "bp",
    "48": "bq",

    "51": "wk",
    "52": "wp",
    "53": "  ",
    "54": "  ",
    "55": "  ",
    "56": "  ",
    "57": "bp",
    "58": "bk",

    "61": "wb",
    "62": "wp",
    "63": "  ",
    "64": "  ",
    "65": "  ",
    "66": "  ",
    "67": "bp",
    "68": "bb",

    "71": "wh",
    "72": "wp",
    "73": "  ",
    "74": "  ",
    "75": "  ",
    "76": "  ",
    "77": "bp",
    "78": "bh",

    "81": "wc",
    "82": "wp",
    "83": "  ",
    "84": "  ",
    "85": "  ",
    "86": "  ",
    "87": "bp",
    "88": "bc",
}

#Main game loop
while not player_win:

    draw_board(board_dict)
    player_turn = change_turn(player_turn)

    while True:
        player_selection = player_select_piece(board_dict, player_turn)
        player_move_select = player_select_move(board_dict, player_selection, player_turn)
        if player_move_select != "null":
            board_dict = player_move_select
            break

    if player_test_win(board_dict, player_turn):
        break
