import sys
sys.path.append("..")

#import utilities
import time
import pygame

import visual.draw_game as dg
import players.UCTPlayer as up
import players.HumanPlayer as hp

def play(screen, screen_size, game, player1, player2, data1_on, data2_on):
    """ Play the game
    """
    pygame.init()

    current_game = game
    turn1 = current_game.next_player
    all_moves = dict()

    dg.draw_game(screen, screen_size, current_game)

    running = True
    while(running):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                
        msg = None

        if turn1:
            next_player_color = 'White'
        else:
            next_player_color = 'Black'

        moves = current_game.generateMoves()
        
        if not moves:
            #No moves, player loose
            running = False
            msg = f'{next_player_color} has won'
            dg.draw_game(screen, screen_size, current_game, msg) 
        else:
            start = time.time()

            #Human player chooses a move
            if (turn1 and isinstance(player1, hp.HumanPlayer)) or (not turn1 and isinstance(player2, hp.HumanPlayer)):
                chosen = dg.draw_game(screen, screen_size, game=current_game, moves=moves)
                
                end = time.time()
                dif = end-start
                print_data(turn1, data1_on, data2_on, dif, player1, player2)
            else:
            #Non human player chooses a move
                if turn1:
                    if isinstance(player1, up.UCTPlayer):
                        chosen = player1.chooseMove(current_game)
                    elif not isinstance(player1, hp.HumanPlayer):
                        chosen = player1.chooseMove(moves)
                else:
                    if isinstance(player2, up.UCTPlayer):
                        chosen = player2.chooseMove(current_game)
                    elif not isinstance(player2, hp.HumanPlayer):
                        chosen = player2.chooseMove(moves)
                
                end = time.time()
                dif = end-start

                print_data(turn1, data1_on, data2_on, dif, player1, player2)

                if dif < 1:
                    time.sleep(1-dif)

            #Repeat position
            if current_game in all_moves:
                all_moves[current_game] += 1
            else:
                all_moves.update({current_game:1})

            # Draw because of definition 1.32.1
            if all_moves[current_game] > 2:
                msg = 'Draw because of condition 1.32.1'
                running = False

            # Draw because of definition 1.32.2
            if current_game.cond1 > 40 and current_game.cond2 > 40:
                msg = 'Draw because of condition 1.32.2'
                running = False
            
            current_game = chosen
            dg.draw_game(screen, screen_size, game=current_game, msg=msg)
            turn1 = current_game.next_player
    time.sleep(3)


def print_data(turn1, data1_on, data2_on, time, player1, player2):
    if (turn1 and data1_on) or ( (not turn1) and data2_on):
        if turn1:
            print(f'Black player time: {time}')
        else:
            print(f'White player time: {time}')

        if (turn1 and isinstance(player1, up.UCTPlayer)):
            player1.uct.tree.pprint_tree()
        elif ( (not turn1) and isinstance(player2, up.UCTPlayer)):
            player2.uct.tree.pprint_tree()