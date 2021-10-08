import sys
import os
sys.path.append("..")

from visual.select_game import select_game
import pygame

def draw_moves(screen, screen_size, game, moves):
    pygame.init()

    yellow_marks = dict()

    if moves is not None:
        rect_moves = dict()

        for move in moves:
            if game.next_player:
                current_tiles = game.black_tiles
                next_tiles = move.black_tiles
            else:
                current_tiles = game.white_tiles
                next_tiles = move.white_tiles

            for tile in next_tiles:
                if not (tile in current_tiles):
                    col = (tile[1]+1)*(screen_size/10)
                    row = (7-tile[0]+1)*(screen_size/10)

                    pos = [col,row]
                    if tuple(pos) in rect_moves:
                        yellow_marks[tuple(rect_moves[tuple(pos)])].append(move)
                    else:
                        mark = create_yellow(screen_size)
                        rect = screen.blit(mark,(col,row))#col,row

                        rect_moves.update({tuple(pos):rect})
                        
                        aux = list()
                        aux.append(move)
                        yellow_marks.update({tuple(rect):aux})
                   
        
            pygame.display.update()
        
        running = True
        while(running):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for rect in yellow_marks:
                        aux_rect = pygame.Rect((rect[0], rect[1]),(rect[2], rect[3]))
                        if aux_rect.collidepoint(x,y):
                            if len(yellow_marks[rect]) == 1:
                                return yellow_marks[rect][0]
                            else:
                                return select_game(screen, screen_size, yellow_marks[rect])
                                
#Create a yellow tile to show a posible move
def create_yellow(screen_size):
    tile_size = int(screen_size/10)
    yellow = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images','yellow_mark.png'))
    yellow = pygame.transform.scale(yellow, (tile_size, tile_size))
    return yellow