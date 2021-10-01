import pygame
from time import sleep

from extra_funcs import *
from move_checks import *
from select_moves import *
from socket_functions import *
from valid_moves import valid_moves
from make_move import make_move

color_dict = {
    "light_sq":(138, 120, 93),
    "dark_sq":(87, 58, 46),
    "select_sq":(28, 27, 239)
}

images = {
    "wk":'piece_images/king_w.png',
    "wq":'piece_images/queen_w.png',
    "wc":'piece_images/rook_w.png',
    "wh":'piece_images/knight_w.png',
    "wb":'piece_images/bishop_w.png',
    "wp":'piece_images/pawn_w.png',

    "bk": 'piece_images/king_b.png',
    "bq": 'piece_images/queen_b.png',
    "bc": 'piece_images/rook_b.png',
    "bh": 'piece_images/knight_b.png',
    "bb": 'piece_images/bishop_b.png',
    "bp": 'piece_images/pawn_b.png'
}

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

width, height = 800, 800
rows, cols = 8, 8
sq_size = width//cols

running = True
player_turn = "b"

def draw_board_background(window):
    window.fill(color_dict["light_sq"])
    for row in range(0,rows):
        for col in range(row % 2, rows, 2):
            pygame.draw.rect(window, color_dict["dark_sq"], (row*sq_size, col*sq_size, sq_size, sq_size))

def draw_board_pieces(window, board):
    for space in board:
        if board_dict[space] != "  ":
            image = pygame.image.load(images[board_dict[space]])
            image.convert()
            image = scale_image(image)
            image_rect = image.get_rect()
            image_rect.center = tile_to_coords(space[0], space[1])
            window.blit(image, image_rect)

def scale_image(image):
    #Scale height to fit fraction of box size
    frac = 0.9
    ix, iy = image.get_size()
    aspect = ix/iy
    iy_new = frac * sq_size
    ix_new = aspect * iy_new
    return pygame.transform.scale(image, (round(ix_new),round(iy_new)))

def tile_to_coords(x_tile,y_tile):
    x_coord = ((int(x_tile)-1) * sq_size) + (sq_size//2)
    y_coord = ((9-int(y_tile)-1) * sq_size) + (sq_size//2)
    return x_coord, y_coord

def coords_to_tile(x_coord,y_coord):
    x_tile = (x_coord//100)+1
    y_tile = 8-(y_coord//100)
    return x_tile, y_tile

def update_screen(game_screen, board):
    draw_board_background(game_screen)
    draw_board_pieces(game_screen, board)
    pygame.display.update()

def click_input():
    while True:
        for event in pygame.event.get():
            # Handles exiting on X
            if event.type == pygame.QUIT:
                pygame.quit()

            # Handles on-screen clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                xpos, ypos = pygame.mouse.get_pos()
                xtile, ytile = coords_to_tile(xpos, ypos)
                outp = str(xtile)+str(ytile)
                return outp

if __name__ == "__main__":
    #setup pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PyChess by Duncan Stevenson")


    while running:
        player_turn = change_turn(player_turn)

        if is_player_in_checkmate(board_dict, player_turn):
            if player_turn == "b":
                print("Checkmate for Black, White wins!")
            elif player_turn == "w":
                print("Checkmate for White, Black wins!")
            sleep(5)
            pygame.quit()

        update_screen(screen, board_dict)

        while True:
            player_selection = player_select_piece(board_dict, player_turn)
            player_move_select = player_select_move(board_dict, player_selection, player_turn)
            if player_move_select != "null":
                # board_dict = make_move(board_dict, player_selection, player_move_select)
                break

    pygame.quit()