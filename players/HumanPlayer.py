import sys
sys.path.append("..")

from players.PlayerInterface import PlayerInterface

class HumanPlayer(PlayerInterface):
    
    def chooseMove(self, moves):
        """Choose a move entered by the console
        """
        chosen = int(input('Move selected: '))
        return moves[chosen]
