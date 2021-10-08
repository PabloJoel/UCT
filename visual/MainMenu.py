import pygame
import os

import sys
sys.path.append("..")

from visual.OptionBox import OptionBox
import visual.InputBox as ib
import visual.Button as bt

import players.RandomPlayer as rp
import players.HumanPlayer as hp
import players.UCTPlayer as up

import games.CheckersGame as cg

pygame.init()
pygame.font.init()

def menu(screen, size_screen):
    #Caption
    pygame.display.set_caption("Game Menu")

    #Background image 
    menu_background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'images','madera blanco.jpg'))
    menu_background = pygame.transform.scale(menu_background, (size_screen, size_screen))

    #Fonts
    IndieFlowerFont = os.path.join(os.path.dirname(__file__), 'images','IndieFlower.ttf')
    
    font_box = pygame.font.Font(IndieFlowerFont, int(size_screen/38))
    font_player = pygame.font.Font(IndieFlowerFont, int(size_screen/30))
    font_game = pygame.font.Font(IndieFlowerFont, int(size_screen/20))

    #Option Box to select a player
    list1 = OptionBox(size_screen/2, size_screen/2.6, size_screen*0.22, size_screen*0.053, 
        (255, 255, 255), (172, 232, 242), (77, 106, 149), 
        font_box, ["Human Player", "Random Player", "UCT Player"])

    list2 = OptionBox(size_screen/2, size_screen/1.69, size_screen*0.22, size_screen*0.053, 
        (255, 255, 255), (172, 232, 242), (77, 106, 149), 
        font_box, ["Human Player", "Random Player", "UCT Player"])

    #Modifications for MCTS
    mods1 = OptionBox(size_screen/1.4, size_screen/2, size_screen*0.15, size_screen*0.053, 
        (255, 255, 255), (172, 232, 242), (77, 106, 149), 
        font_box, ["None", "Heur", "LGR"])

    mods2 = OptionBox(size_screen/1.4, size_screen/1.4, size_screen*0.15, size_screen*0.053, 
        (255, 255, 255), (172, 232, 242), (77, 106, 149), 
        font_box, ["None", "Heur", "LGR"])

    #Player choosed
    player1, player2 = 0,0

    #Modification choosed
    mod1, mod2 = 0,0

    #Input box to input number of iterations
    input_box1 = ib.InputBox(size_screen/2, size_screen/2.2, size_screen*0.1, size_screen*0.053, '100')
    input_box2 = ib.InputBox(size_screen/2, size_screen/1.51, size_screen*0.1, size_screen*0.053, '100')
    input_boxes = [input_box1, input_box2]

    #Button to start
    start_button = bt.Button('Start',size_screen/2.3, size_screen/1.11, size_screen*0.1,size_screen*0.053,font_player,(77,106,149),'white')

    #Show data of player 1
    data1_on = False 
    data1_off_button = bt.Button('Show data',size_screen/3, size_screen/1.95, size_screen*0.16,size_screen*0.053,font_box,(77,106,149),'white')
    data1_on_button  = bt.Button('Show data',size_screen/3, size_screen/1.95, size_screen*0.16,size_screen*0.053,font_box,'white',(77,106,149))

    #Show data of player 2
    data2_on = False 
    data2_off_button = bt.Button('Show data',size_screen/3, size_screen/1.38, size_screen*0.16,size_screen*0.053,font_box,(77,106,149),'white')
    data2_on_button  = bt.Button('Show data',size_screen/3, size_screen/1.38, size_screen*0.16,size_screen*0.053,font_box,'white',(77,106,149))

    #Main loop
    running = True
    while running:
        #Events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes: #Events for input box
                box.handle_event(event)
            if start_button.click_on_button(event):
                return create_player(player1, int(input_box1.text), mod1, data1_on, player2, int(input_box2.text), mod2, data2_on)
            if data1_on_button.click_on_button(event) or data1_off_button.click_on_button(event):
                data1_on = not data1_on
            if data2_on_button.click_on_button(event) or data2_off_button.click_on_button(event):
                data2_on = not data2_on

        #Change player 1 chosen
        chosen_player = list1.update(events)
        if chosen_player >= 0:
            player1 = chosen_player

        #Change player 2 chosen
        chosen_player = list2.update(events)
        if chosen_player >= 0:
            player2 = chosen_player

        #Change modification for player 1 mcts chosen
        chosen_mod = mods1.update(events)
        if chosen_mod >= 0:
            mod1 = chosen_mod

        #Change modification for player 2 mcts chosen
        chosen_mod = mods2.update(events)
        if chosen_mod >= 0:
            mod2 = chosen_mod

        #Draw the background
        screen.blit(menu_background,(0,0))

        #Draw the option box again
        list1.draw(screen)
        list2.draw(screen)

        #Draw the button again
        start_button.show(screen)

        if data1_on:
            data1_on_button.show(screen)
        else:
            data1_off_button.show(screen)

        if data2_on:
            data2_on_button.show(screen)
        else:
            data2_off_button.show(screen)

        #Checkers title
        label = font_game.render("Checkers", 1, (77,106,149))
        screen.blit(label, (size_screen/2.5, size_screen/5))

        #Player 1 text
        label = font_player.render("Player 1:", 1, (77,106,149))
        screen.blit(label, (size_screen/3, size_screen/2.65))

        #Player 2 text
        label = font_player.render("Player 2:", 1, (77,106,149))
        screen.blit(label, (size_screen/3, size_screen/1.72))

        #Update the info of the input box
        for box in input_boxes:
            box.update()

        #If MCTS Player is chosen the display the input box for the number of iterations
        if player1 == 2:
            label = font_box.render("Number of iterations:", 1, (77,106,149))
            screen.blit(label, (size_screen/6, size_screen/2.2))
            input_box1.draw(screen)

            label = font_box.render("Modification:", 1, (77,106,149))
            screen.blit(label, (size_screen/1.85, size_screen/1.95))
            mods1.draw(screen)

        if player2 == 2:
            label = font_box.render("Number of iterations:", 1, (77,106,149))
            screen.blit(label, (size_screen/5, size_screen/1.51))
            input_box2.draw(screen)

            label = font_box.render("Modification:", 1, (77,106,149))
            screen.blit(label, (size_screen/1.85, size_screen/1.38))
            mods2.draw(screen)

        pygame.display.flip()

    return 'Quit'

def create_player(player1, iter1, mod1, data1_on, player2, iter2, mod2, data2_on):
        if player1 == 0:
            pl1 = hp.HumanPlayer()
        elif player1 == 1:
            pl1 = rp.RandomPlayer(show=False)
        elif player1 == 2:
            if mod1 == 0:
                pl1 = up.UCTPlayer(game=cg.CheckersGame(), iter=iter1)
            elif mod1 == 1:
                pl1 = up.UCTPlayer(game=cg.CheckersGame(), iter=iter1, heurs=True)
            elif mod1 == 2:
                pl1 = up.UCTPlayer(game=cg.CheckersGame(), iter=iter1, last_good_reply=True)
        
        if player2 == 0:
            pl2 = hp.HumanPlayer()
        elif player2 == 1:
            pl2 = rp.RandomPlayer(show=False)
        elif player2 == 2:
            if mod2 == 0:
                pl2 = up.UCTPlayer(game=cg.CheckersGame(), iter=iter2)
            elif mod2 == 1:
                pl2 = up.UCTPlayer(game=cg.CheckersGame(), iter=iter2, heurs=True)
            elif mod2 == 2:
                pl2 = up.UCTPlayer(game=cg.CheckersGame(), iter=iter2, last_good_reply=True)
        
        return (pl1,pl2,data1_on,data2_on)