import socket

def start_server_function(ip, port, username):

    server = socket.socket()

    server.bind((ip, port))

    print("Waiting for opponent at " + ip + " and port " + str(port))
    server.listen(1)

    conn, addr = server.accept()
    challenger = (conn.recv(2048)).decode()
    conn.send(username.encode())
    print(challenger + " connected")

    return conn


def start_client_function(ip, port, username):

    server = socket.socket()

    server.connect((ip, port))
    server.send(username.encode())
    challenger = (server.recv(2048)).decode()
    print("connected to " + challenger)

    return server


def send_move(conn, piece_pos, move_pos):
    send_msg = piece_pos + move_pos
    conn.send(send_msg.encode())


def wait_for_move(conn):
    print("Waiting for other player to select move...")

    other_players_turn = ""
    while other_players_turn == "":
        other_players_turn = conn.recv(2048)
        other_players_turn = other_players_turn.decode()

    piece_pos = other_players_turn[0:2]
    move_pos = other_players_turn[2:4]
    out = [piece_pos, move_pos]

    return out
