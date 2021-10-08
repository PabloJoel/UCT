import sys
sys.path.append("..")

import pygame
from visual.draw_board import draw_board
from visual.draw_moves import draw_moves

def draw_game(screen, size_screen, game, msg=None, moves=None):
    pygame.init()
    pygame.font.init()

    #caption
    pygame.display.set_caption("Checkers Game")

    #Draw board
    draw_board(screen, size_screen, game, msg)

    return draw_moves(screen, size_screen, game, moves)

    