import sys
sys.path.append("..")

#import games
from typing import TYPE_CHECKING
from games.Tictactoe import TicTacToe

#import players
from players.RandomPlayer import RandomPlayer
from players.UCTPlayer import UCTPlayer


#import utilities
import copy

class ticmodel():

    def __init__(self, game):
        """Save the game, the state of the game wont be modified
        """
        self.game = game

    def play(self, player1=RandomPlayer(), player2=RandomPlayer(), show=True):
        """ Play the game. By default the players play randomly, but another type of player can be introduced.
            If show is set to False then this wont show messages (dont do with a human player because you wont see anything, this is used to gather data about
            random players)
        """
        current_game = copy.deepcopy(self.game)
        turn1 = current_game.next_player

        if show:
            print('Get ready to play')
        while(True):
            
            if turn1:
                player_color = '1'
            else:
                player_color = '2'

            if show:
                print(f'Player {player_color}')
                print('State of the game:')
                print(current_game)

            moves = current_game.generateMoves()
            if not moves:
                return '0'

            if show:
                print('Select a move:')
                ticmodel.printBoards(moves)

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

            if current_game.win():
                return player_color
            elif current_game.is_finished():
                return '0'

            turn1 = current_game.next_player
    
    def printBoards(list_boards):
        """Print a list of boards
        """
        i = 0
        for elem in list_boards:
            print(i)
            print(elem)
            i += 1

first = 0
second = 0
draw = 0
i = 0

while(i<100):
    gm = ticmodel(TicTacToe())
    winner = gm.play(player1=RandomPlayer(show=False), player2=UCTPlayer(game=TicTacToe(),type_game='tic',iter=5000), show=False)
    print(f'Winner:{winner}, Current game: {i}')
    if winner == '1':
        first += 1
    elif winner == '2':
        second += 1
    else:
        draw += 1
    i += 1

print(f'First:{first}, Second:{second}, Draw:{draw}')
