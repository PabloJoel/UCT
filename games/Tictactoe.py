import sys
sys.path.append("..")

import copy
from games.GameInterface import GameInterface

class TicTacToe(GameInterface):
    
    def __init__(self, board=None, next_player=True):
        """Constructor: it can take the parameters to create an specific board (black tiles and white tiles) or a numpy matrix
            (the board) or no parameters to create the default board
        """
        if board is None:
            self.board = [[0,0,0],[0,0,0],[0,0,0]]
        else:
            self.board = board
        self.next_player = next_player

    def generateMoves(self):
        """Generate all the posible moves, they are return as a list of boards
        """
        if self.next_player == True:
            token = 1
        else:
            token = 2

        moves = list()
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    new_board = copy.deepcopy(self.board)
                    new_board[row][col] = token
                    moves.append(TicTacToe(new_board, not self.next_player))
        
        return moves

    def __eq__(self, other):
        """Equals function to compare two CheckersGame to know if they are the same game
        """
        if self.next_player == other.next_player and self.board == other.board:
            return True
        else:
            return False

    def same_board(self, other):
        """Equals function to compare two CheckersGame to know if they are the same game
        """
        if self.board == other.board:
            return True
        else:
            return False

    def __hash__(self):
        return hash( (hash(tuple(self.board)), hash(self.next_player)) )            

    def __str__(self):
        """To string function of the board
        """
        res = f'{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}\n{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}\n{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}'
        return res

    def win(self):
        if self.board[0][0] != 0 and self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2]:
            return True
        elif self.board[0][2] != 0 and self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2]:
            return True
        elif self.board[2][0] != 0 and self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2]:
            return True
        elif self.board[0][0] != 0 and self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0]:
            return True
        elif self.board[0][1] != 0 and self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1]:
            return True
        elif self.board[1][0] != 0 and self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2]:
            return True
        elif self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return True
        elif self.board[0][2] != 0 and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return True
        else:
            return False
    
    def is_finished(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    return False
        return True

