import sys
sys.path.append("..")

from typing import TYPE_CHECKING

#import players
from players.RandomPlayer import RandomPlayer
from players.UCTPlayer import UCTPlayer


#import utilities
import copy

class GameModel():

    def __init__(self, game):
        """Save the game, the state of the game wont be modified
        """
        self.game = game

    def play(self, player1= RandomPlayer(), player2= RandomPlayer(), show=True):
        """ Play the game. By default the players play randomly, but another type of player can be introduced.
            If show is set to False then this wont show messages (dont do with a human player because you wont see anything, this is used to gather data about
            random players)
        """
        current_game = copy.deepcopy(self.game)
        turn1 = current_game.next_player
        all_moves = dict()

        if show:
            print('Get ready to play')
        while(True):
            
            if turn1:
                player_color = 'Black'
            else:
                player_color = 'White'

            if show:
                print(f'Player {player_color}')
                print('State of the game:')
                print(current_game)

            moves = current_game.generateMoves()
            if not moves:
                if show:
                    print(f'{player_color} has lost')
                if player_color == 'Black':
                    return 'White'
                else:
                    return 'Black'
            else:
                if show:
                    print('Select a move:')
                    GameModel.printBoards(moves, all_moves)

                if turn1:
                    if isinstance(player1, UCTPlayer):
                        chosen = player1.chooseMove(current_game)
                    else:
                        chosen = player1.chooseMove(moves)
                else:
                    if isinstance(player2, UCTPlayer):
                        chosen = player2.chooseMove(current_game)
                    else:
                        chosen = player2.chooseMove(moves)

                current_game = chosen

                #Repeat position
                if current_game in all_moves:
                    all_moves[current_game] += 1
                else:
                    all_moves.update({current_game:1})

                # Draw because of definition 1.32.1
                if all_moves[current_game] > 2:
                    if show:
                        print('Draw because of condition 1.32.1')
                    return 'Draw'

                # Draw because of definition 1.32.2
                if current_game.cond1 > 40 and current_game.cond2 > 40:
                    if show:
                        print('Draw because of condition 1.32.2')
                    return 'Draw'

                turn1 = current_game.next_player
    
    def printBoards(list_boards, all_moves):
        """Print a list of boards
        """
        i = 0
        for elem in list_boards:
            if (elem in all_moves and all_moves[elem] > 2): #Draw because of definition 1.32.1
                print(f'{i} - This move leads to a draw because of condition 1.32.1')
            elif elem.cond1 >= 40 and elem.cond2 >= 40: #Draw because of definition 1.32.2
                print(f'{i} - This move leads to a draw because of condition 1.32.2')
            else:
                print(i)
            print(elem)
            i += 1



