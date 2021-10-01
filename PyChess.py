#Pychess
#Entirely text-based chess

from extra_funcs import *
from move_checks import *
from select_moves import *
from socket_functions import *
from valid_moves import valid_moves
from make_move import make_move

#Initial board setup
player_turn = "b"
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


if __name__ == "__main__":
    server_client = ""
    while server_client.upper() not in ["SERVER", "CLIENT", "LOCAL"]:
        server_client = input("Is this the \"SERVER\", the \"CLIENT\", or \"LOCAL\" on the same terminal : ")


    if server_client.upper() == "LOCAL":
        player_color = "w"
        local_lock = True
    else:
        ip = input("IP Address: ")
        port = input("Port: ")
        port = int(port)
        username = input("Username: ")
        local_lock = False

        if server_client.upper() == "SERVER":
            player_color = "w"
            conn = start_server_function(ip, port, username)
        elif server_client.upper() == "CLIENT":
            player_color = "b"
            conn = start_client_function(ip, port, username)



    #Main game loop
    while True:

        player_turn = change_turn(player_turn)

        if is_player_in_checkmate(board_dict, player_turn):
            if player_turn == "b":
                print("Checkmate for Black, White wins!")
            elif player_turn == "w":
                print("Checkmate for White, Black wins!")
            break

        draw_board(board_dict)

        if local_lock:
            player_color = player_turn

        if player_turn == player_color:

            while True:

                player_selection = player_select_piece(board_dict, player_turn)
                player_move_select = player_select_move(board_dict, player_selection, player_turn)

                if player_move_select != "null":

                    #board_dict = make_move(board_dict, player_selection, player_move_select)

                    if not local_lock:
                        send_move(conn, player_selection, player_move_select)
                    break

        else:
            other_move = wait_for_move(conn)
            board_dict = make_move(board_dict, other_move[0], other_move[1])