
class BTree():
    #Bidirectional Tree

    def __init__(self, game, parent, value=0, visits=0, nodes=None):
        """Tree for Monte Carlo Tree Search. 
                -Game is the move that is being analyzed
                -Parent is the parent of the node
                -Value is value of the node
                -Visits is the number of times it has been visited
                -Nodes is a list of nodes descending directly from this node
        """
        self.game = game
        self.parent = parent
        self.value = value
        self.visits = visits

        if nodes is None:
            self.nodes = list()
        else:
            self.nodes = nodes

    def pprint_tree(self, _prefix="", _last=True):
        print(_prefix, "`- " if _last else "|- ", "Times visited:",self.visits," Value:",self.value, sep="")
        _prefix += "   " if _last else "|  "
        child_count = len(self.nodes)
        for i, child in enumerate(self.nodes):
            _last = i == (child_count - 1)
            child.pprint_tree(_prefix, _last)
