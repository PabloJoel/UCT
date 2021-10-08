import sys
sys.path.append("..")

from players.PlayerInterface import PlayerInterface
import random

class RandomPlayer(PlayerInterface):

    def __init__(self, show=True):
        self.show = show

    def chooseMove(self, moves):
        """Choosen a move randomly
        """
        chosen = random.randint(0, len(moves)-1)
        if self.show:
            print(f'Move selected: {chosen}')
        return moves[chosen]
