from extra_funcs import strout
import numpy as np

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
        move_array.append(strout(px+2, py+1))
        move_array.append(strout(px+2, py-1))
        move_array.append(strout(px-2, py+1))
        move_array.append(strout(px-2, py-1))
        move_array.append(strout(px+1, py+2))
        move_array.append(strout(px-1, py+2))
        move_array.append(strout(px+1, py-2))
        move_array.append(strout(px-1, py-2))

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
        move_array.append(strout(px+1, py+0))
        move_array.append(strout(px+1, py+1))
        move_array.append(strout(px+0, py+1))
        move_array.append(strout(px-1, py+1))
        move_array.append(strout(px-1, py+0))
        move_array.append(strout(px-1, py-1))
        move_array.append(strout(px+0, py-1))
        move_array.append(strout(px+1, py-1))

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
        if int(x[0]) > 8:
            move_array.pop(move_array.index(x))
        if int(x[0]) < 1:
            move_array.pop(move_array.index(x))
        if int(x[1]) > 8:
            move_array.pop(move_array.index(x))
        if int(x[1]) < 1:
            move_array.pop(move_array.index(x))

    #remove non-unique values
    move_array = np.unique(move_array)

    return move_array
