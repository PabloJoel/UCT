import sys
sys.path.append("..")

import random
from players.TicUCT import TicUCT
from players.BTree import BTree
from players.PlayerInterface import PlayerInterface
from players.UCT import UCT
from players.TicUCT import TicUCT

class UCTPlayer(PlayerInterface):

    def __init__(self, game, iter=100, choose='max_value', heurs=False, last_good_reply=False):
        self.iter = iter
        self.choose = choose

        self.uct = UCT(game)
        
        self.heurs = heurs
        self.last_good_reply = last_good_reply

    def chooseMove(self, enemy_move):
        """Choosen a move according to the chosen strategy
        """
        
        #Update according to the enemy move
        if not(enemy_move.same_board(self.uct.tree.game)):
            if not self.uct.tree.nodes:
                self.uct.tree = BTree(game=enemy_move, parent=None)
            else:
                find = False
                i = 0
                while(not find):
                    if (enemy_move.same_board(self.uct.tree.nodes[i].game)):
                        self.uct.tree = self.uct.tree.nodes[i]
                        self.uct.tree.parent = None
                        find = True
                    else:
                        i += 1

        #Iterate
        self.uct.tree = self.uct.search(self.heurs, self.last_good_reply, self.iter)

        #Choose new move
        if self.choose == 'max_value':
            if self.uct.tree.nodes[0].visits == 0:
                best_value = 0
            else:
                best_value = (self.uct.tree.nodes[0].value)/(self.uct.tree.nodes[0].visits)
            best_nodes = list()
            best_nodes.append(self.uct.tree.nodes[0])

            for node in self.uct.tree.nodes:
                if node.visits == 0:
                    value = 0
                else:
                    value = node.value/node.visits
                if value == best_value:
                    best_nodes.append(node)
                elif value > best_value:
                    best_nodes = list()
                    best_nodes.append(node)
                    best_value = value
        if self.choose == 'max_ucb1':
            best_value = UCT.UCB1(self.uct.tree.nodes[0])
            best_nodes = list()
            best_nodes.append(self.uct.tree.nodes[0])

            for node in self.uct.tree.nodes:
                value = UCT.UCB1(node)
                if value == best_value:
                    best_nodes.append(node)
                elif value > best_value:
                    best_nodes = list()
                    best_nodes.append(node)
                    best_value = value
        elif self.choose == 'max_visits':
            best_visits = self.uct.tree.nodes[0].visits
            best_nodes = list()
            best_nodes.append(self.uct.tree.nodes[0])

            for node in self.uct.tree.nodes:
                if node.visits == best_visits:
                    best_nodes.append(node)
                elif node.visits > best_visits:
                    best_node = list()
                    best_node.append(node)
                    best_visits = node.visits

        chosen = random.randint(0,len(best_nodes)-1)
        self.uct.tree = best_nodes[chosen]
        self.uct.tree.parent = None

        return self.uct.tree.game
        
        