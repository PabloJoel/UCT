import sys
sys.path.append("..")

#Utils
import random
import copy
import numpy as np

#Tree
from players.BTree import BTree

class UCT():

    def __init__(self, game):
        self.tree = BTree(game=game, parent=None)
        
        #Last Good Reply
        self.good_replies = dict()
        
    def search(self, heurs, last_good_reply, max_iter=100):
        tree = copy.deepcopy(self.tree)

        """
        #Initialize tree
        movs = tree.game.generateMoves()
        for new_game in movs:
            tree.nodes.append(BTree(game=new_game, parent=tree))
        """
        movs = tree.game.generateMoves()
        #Only 1 move possible
        if len(movs)==1:
            tree.nodes.append(BTree(game=movs[0], parent=tree))
            return tree

        #Check if there is a winning
        for mov in movs:
            finish, winner = mov.is_finished()
            if finish and winner == tree.game.next_player: #Winning move
                tree.nodes.append(BTree(game=mov, parent=tree))
                """
                new_nodes = list()
                new_nodes.append(node)
                tree.nodes = new_nodes
                """
                return tree

        iter = 0
        while(iter < max_iter):
            selected_node = self.selection(tree)
            sim_value = self.simulation(selected_node, heurs, last_good_reply)
            UCT.backpropagation(selected_node, sim_value)
            iter += 1

        return tree

    def selection(self, node):
        if node.game.is_finished()[0]:
            return node
        else:
            if not node.nodes: #Leaf node
                if node.visits > 0: #Already visited
                    #Expand
                    movs = node.game.generateMoves()
                    for new_game in movs:
                        node.nodes.append(BTree(game=new_game, parent=node))
                    
                    #LGR POLICY
                    if node.game.mov in self.good_replies:
                        good_replies = list()
                        for subnode in node.nodes:
                            if self.good_replies[node.game.mov] == subnode.game.mov:
                                good_replies.append(subnode)
                        
                        if not good_replies:
                            chosen = random.randint(0,len(node.nodes)-1)
                            return node.nodes[chosen]
                        else:
                            chosen = random.randint(0,len(good_replies)-1)
                            return good_replies[chosen]  
                    else:    
                        chosen = random.randint(0,len(node.nodes)-1)
                        return node.nodes[chosen]
                else: #Non visited node
                    return node
            else: #Non leaf node
                best_nodes = list() 
                best_nodes.append(node.nodes[0])

                best_ucb = UCT.UCB1(node.nodes[0])
                for subnode in node.nodes[1:]:
                    ucb = UCT.UCB1(subnode)
                    if ucb == best_ucb:
                        best_nodes.append(subnode)
                    elif ucb > best_ucb:
                        best_nodes = list()
                        best_nodes.append(subnode)
                        best_ucb = ucb

                #LGR POLICY
                if node.game.mov in self.good_replies and len(best_nodes)>1:
                        good_replies = list()
                        for node_option in best_nodes:
                            if self.good_replies[node.game.mov] == node_option.game.mov:
                                good_replies.append(node_option)
                        
                        if not good_replies:
                            chosen = random.randint(0,len(best_nodes)-1)
                            return self.selection(best_nodes[chosen])
                        else:
                            chosen = random.randint(0,len(good_replies)-1)
                            return good_replies[chosen]
                else:
                    chosen = random.randint(0,len(best_nodes)-1)
                    return self.selection(best_nodes[chosen])

    def simulation(self, node, heurs, last_good_reply): 
        winner = self.__play(node.game,heurs, last_good_reply)
        return winner

    def __play(self, game, heurs, last_good_reply):
        current_game = copy.deepcopy(game)
        turn1 = current_game.next_player
        all_moves = dict()
        all_moves_repeat = list()

        #my_player = self.tree.game
        my_player = self.tree.game.next_player

        while(True): 
            if turn1:
                player_color = 'Black'
            else:
                player_color = 'White'

            moves = current_game.generateMoves()
            if not moves:
                #No moves, player looses
                if player_color == 'Black':
                    if not my_player and last_good_reply:
                        self.__save_good_replies(all_moves_repeat,my_player)
                    elif last_good_reply:
                        self.__remove_bad_replies(all_moves_repeat,my_player)
                    return 'White'
                else:
                    if my_player and last_good_reply:
                        self.__save_good_replies(all_moves_repeat,my_player)
                    elif last_good_reply:
                        self.__remove_bad_replies(all_moves_repeat,my_player)
                    return 'Black'
            else:
                #Last good reply simulation
                if last_good_reply and turn1==my_player and len(all_moves_repeat)>0:
                    if current_game.mov in self.good_replies:
                        good_reply = self.good_replies[current_game.mov]
                        
                        found = False
                        i=0
                        while(not found and i < len(moves)):
                            if moves[i].mov == good_reply:
                                found = True
                                chosen = i
                            else:
                                i += 1
                        if not found:
                            chosen = random.randint(0, len(moves)-1)
                    else:
                        chosen = random.randint(0, len(moves)-1)
                elif heurs:
                    #Heuristic simulation
                    best_moves = [0]
                    best_value = moves[0].heuristic_eval()
                    index = 1

                    for move in moves[1:]:
                        value = move.heuristic_eval()
                        if value == best_value:
                            best_moves.append(index)
                        elif value > best_value:
                            best_moves.clear()
                            best_moves.append(index)
                        index += 1
                    
                    chosen = random.randint(0, len(best_moves)-1)
                else:
                    #Random simulation
                    chosen = random.randint(0, len(moves)-1)
                current_game = moves[chosen]

                all_moves_repeat.append(current_game)
                
                #Repeat position
                if current_game in all_moves:
                    all_moves[current_game] += 1
                else:
                    all_moves.update({current_game:1})

                # Draw because of definition 1.32.1
                if all_moves[current_game] > 2:
                    self.__save_good_replies(all_moves_repeat,my_player)
                    return 'Draw'

                # Draw because of definition 1.32.2
                if current_game.cond1 > 40 and current_game.cond2 > 40:
                    self.__save_good_replies(all_moves_repeat,my_player)
                    return 'Draw'
                turn1 = current_game.next_player

    def backpropagation(node, value):
        node.visits += 1
        if value == 'Black' and node.game.next_player == False:
            node.value += 1
        elif value == 'White'  and node.game.next_player == True:
            node.value += 1
        elif value == 'Draw':
            node.value += 0.25

        #node.value += value
        if node.parent is not None:
            UCT.backpropagation(node.parent, value)

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

    def __save_good_replies(self, all_moves, player_color):
        i = 0
        if player_color == 'Black':
            pl = True
        else:
            pl = False

        if not all_moves:
            return

        if not(all_moves[0].next_player) == pl:
            i = 1

        while(i < len(all_moves)-1):
            self.good_replies.update({all_moves[i].mov:all_moves[i+1].mov})
            i += 2


    def __remove_bad_replies(self, all_moves, player_color):
        i = 0
        if player_color == 'Black':
            pl = True
        else:
            pl = False

        if not all_moves:
            return
            
        if not(all_moves[0].next_player) == pl:
            i = 1

        while(i < len(all_moves)-1):
            if all_moves[i].mov in self.good_replies and all_moves[i+1].mov == self.good_replies[all_moves[i].mov]:
                self.good_replies.pop(all_moves[i].mov)
            i += 2
