import sys
sys.path.append("..")

import pygame
import time
import numpy as np

import games.CheckersGame as cg
import visual.draw_game as dg

def show_board(next_player, matrix_board, size_screen=500):
    board = cg.CheckersGame(next_player=next_player, matrix=matrix_board)
    screen = pygame.display.set_mode((size_screen,size_screen))
    dg.draw_game(screen, size_screen, board)

board = np.array([
                [0,0,0,11,0,2,0,2],
                [2,0,2,0,0,0,1,0],
                [0,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,0],
                [1,0,1,0,0,0,0,0],
                [0,1,0,1,0,1,0,1],
                [1,0,1,0,1,0,1,0],
            ])

show_board(True,board)
time.sleep(3)