import pygame

import sys
sys.path.append("..")

import games.CheckersGame as cg
from visual.MainMenu import menu
import visual.VisualModel as vm

class Game_Start():

    def __init__(self, size):
        self.size_screen = size

    def start(self):
        pygame.init()
        pygame.font.init()

        #Screen creation
        screen = pygame.display.set_mode((self.size_screen,self.size_screen))

        #Main loop
        running = True
        while running:
            #Events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            #Menu to select type of players
            res = menu(screen, self.size_screen)

            if isinstance(res, str):
                running = False
            elif isinstance(res, tuple):
                #Play the game
                vm.play(screen, self.size_screen, cg.CheckersGame(), res[0], res[1], res[2], res[3])

        pygame.quit()
        quit()

gs = Game_Start(500)
gs.start()