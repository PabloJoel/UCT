import sys
sys.path.append("..")

#Utils
import random
import copy
import numpy as np

#Tree
from players.BTree import BTree

class TicUCT():

    def __init__(self, game):
        self.tree = BTree(game=game, parent=None)
        
    def search(self, heurs=False, max_iter=100):
        tree = copy.deepcopy(self.tree)

        #Initialize tree
        movs = tree.game.generateMoves()
        for new_game in movs:
            tree.nodes.append(BTree(game=new_game, parent=tree))

        iter = 0
        while(iter < max_iter):
            selected_node = TicUCT.selection(tree)
            sim_value = TicUCT.simulation(selected_node, heurs)
            TicUCT.backpropagation(selected_node, sim_value)
            iter += 1

        return tree

    def selection(node):
        if node.game.is_finished():
            return node
        else:
            if not node.nodes: #Leaf node
                if node.visits > 0: #Already visited
                    #Expand
                    movs = node.game.generateMoves()
                    for new_game in movs:
                        node.nodes.append(BTree(game=new_game, parent=node))
                    return node.nodes[0]
                else: #Non visited node
                    return node
            else: #Non leaf node
                best_node = node.nodes[0]
                best_ucb = TicUCT.UCB1(node.nodes[0])
                for subnode in node.nodes[1:]:
                    ucb = TicUCT.UCB1(subnode)
                    if ucb > best_ucb:
                        best_ucb = ucb
                        best_node = subnode
                return TicUCT.selection(best_node)

    def simulation(node, heurs): 
        winner = TicUCT.__play(node.game,heurs)
        return winner
    
    def __play(game,heurs):
        current_game = copy.deepcopy(game)
        turn1 = current_game.next_player

        while(True):
            
            if turn1:
                player_color = '1'
            else:
                player_color = '2'

            moves = current_game.generateMoves()
            if not moves:
                return '0'

            chosen = random.randint(0, len(moves)-1)
            current_game = moves[chosen]

            if current_game.win():
                return player_color
            elif current_game.is_finished():
                return '0'

            turn1 = current_game.next_player

    def backpropagation(node, value):
        node.visits += 1
        if value == '1' and node.game.next_player == False:
            node.value += 1
        elif value == '2' and node.game.next_player == True:
            node.value += 1
        elif value == '0':
            node.value += 0.25

        if node.parent is not None:
            TicUCT.backpropagation(node.parent, value)

    def UCB1(node, expl_const=(1/(np.sqrt(2)))):
        """Basic UCB1 function
        """
        if node.visits == 0:
            return float('inf')
        else:
            exploitation = (node.value/node.visits)

            inside_square_root = (2*(np.log(node.parent.visits)))/node.visits 
            exploration  = 2*expl_const*(np.sqrt(inside_square_root))

            return (exploitation + exploration)
