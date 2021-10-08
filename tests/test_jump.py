from games.CheckersGame import CheckersGame
import numpy as np

def test_jump1():
    #black moves
    #transformation after a jump move (posibility to eat but movement must stop)
    input = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,2,0,2,0,2,0],
                [0,1,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])

    output1 = np.array([
                [0,0,0,11,0,0,0,0],
                [0,0,0,0,2,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])

    res = list()
    res.append(CheckersGame(next_player=False, matrix=output1))

    gameIn = CheckersGame(next_player=True, matrix=input)
    assert gameIn.generateMoves() == res

def test_jump2():
    #black moves
    #movility (jumps) of a queen (3 moves) and a peon (1)
    input = np.array([
                [0,0,0,0,0,0,0,0],
                [0,2,0,22,2,0,2,0],
                [0,0,11,0,0,0,0,0],
                [0,2,0,2,2,0,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])

    output1 = np.array([
                [11,0,0,0,0,0,0,0],
                [0,0,0,22,2,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,2,0,2,2,0,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    output2 = np.array([
                [0,0,0,0,11,0,0,0],
                [0,2,0,0,2,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,2,0,2,2,0,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    output3 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,2,0,22,2,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,2,2,0,0,0],
                [11,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    #peon to queen (7,2) left
    output4 = np.array([
                [0,0,11,0,0,0,0,0],
                [0,0,0,22,2,0,2,0],
                [0,0,11,0,0,0,0,0],
                [0,0,0,2,2,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    #peon to queen (7,2) right
    output5 = np.array([
                [0,0,11,0,0,0,0,0],
                [0,2,0,0,2,0,2,0],
                [0,0,11,0,0,0,0,0],
                [0,2,0,0,2,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    output6 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,2,0,22,2,0,2,0],
                [0,0,11,0,0,0,0,0],
                [0,2,0,2,2,1,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    res = list()
    res.append(CheckersGame(next_player=False, matrix=output1))
    res.append(CheckersGame(next_player=False, matrix=output2))
    res.append(CheckersGame(next_player=False, matrix=output3))
    res.append(CheckersGame(next_player=False, matrix=output4))
    res.append(CheckersGame(next_player=False, matrix=output5))
    res.append(CheckersGame(next_player=False, matrix=output6))

    gameIn = CheckersGame(next_player=True, matrix=input)
    assert gameIn.generateMoves() == res

def test_jump3():
    #black moves
    #limits of movements
    input = np.array([
                [0,2,0,0,0,0,0,2],
                [0,0,0,0,0,2,1,0],
                [0,2,0,0,1,0,0,0],
                [0,0,11,0,0,0,0,0],
                [0,2,0,2,0,0,0,0],
                [0,0,0,0,1,2,0,0],
                [2,2,0,0,0,0,11,0],
                [1,1,0,0,0,2,0,2],
            ])
    
    output1 = np.array([
                [0,2,0,0,0,0,11,2],
                [0,0,0,0,0,0,1,0],
                [0,2,0,0,0,0,0,0],
                [0,0,11,0,0,0,0,0],
                [0,2,0,2,0,0,0,0],
                [0,0,0,0,1,2,0,0],
                [2,2,0,0,0,0,11,0],
                [1,1,0,0,0,2,0,2],
            ])
    
    output2 = np.array([
                [0,2,0,0,0,0,0,2],
                [11,0,0,0,0,2,1,0],
                [0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,2,0,2,0,0,0,0],
                [0,0,0,0,1,2,0,0],
                [2,2,0,0,0,0,11,0],
                [1,1,0,0,0,2,0,2],
            ])
    
    output3 = np.array([
                [0,2,0,0,0,0,0,2],
                [0,0,0,0,0,2,1,0],
                [0,2,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,2,0,0,0,0],
                [0,0,0,0,1,2,0,0],
                [2,0,0,0,0,0,11,0],
                [1,1,11,0,0,2,0,2],
            ])

    output4 = np.array([
                [0,2,0,0,0,0,0,2],
                [0,0,0,0,0,2,1,0],
                [0,2,0,0,1,0,0,0],
                [0,0,11,0,0,0,0,0],
                [0,2,0,2,11,0,0,0],
                [0,0,0,0,1,0,0,0],
                [2,2,0,0,0,0,0,0],
                [1,1,0,0,0,2,0,2],
            ])
    
    output5 = np.array([
                [0,2,0,0,0,0,0,2],
                [0,0,1,0,0,2,1,0],
                [0,0,0,0,1,0,0,0],
                [0,0,11,0,0,0,0,0],
                [0,0,0,2,0,0,0,0],
                [0,0,0,0,1,2,0,0],
                [2,0,0,0,0,0,11,0],
                [0,1,0,0,0,2,0,2],
            ])
    
    output6 = np.array([
                [0,2,0,0,0,0,0,2],
                [0,0,0,0,0,2,1,0],
                [0,2,0,0,1,0,0,0],
                [0,0,11,0,1,0,0,0],
                [0,2,0,0,0,0,0,0],
                [0,0,0,0,1,2,0,0],
                [2,0,0,0,0,0,11,0],
                [0,1,0,0,0,2,0,2],
            ])

    res = list()
    res.append(CheckersGame(next_player=False, matrix=output1))
    res.append(CheckersGame(next_player=False, matrix=output2))
    res.append(CheckersGame(next_player=False, matrix=output3))
    res.append(CheckersGame(next_player=False, matrix=output4))
    res.append(CheckersGame(next_player=False, matrix=output5))
    res.append(CheckersGame(next_player=False, matrix=output6))

    gameIn = CheckersGame(next_player=True, matrix=input)
    assert gameIn.generateMoves() == res

def test_jump4():
    #white moves
    #transformation after a jump move (posibility to eat but movement must stop)
    input = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,2],
                [0,0,1,0,1,0,1,2],
                [0,0,0,0,0,0,1,0],
            ])

    output1 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,2],
                [0,0,0,0,1,0,1,2],
                [0,0,0,22,0,0,1,0],
            ])

    output2 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,0],
                [0,0,1,0,1,0,0,2],
                [0,0,0,0,0,22,1,0],
            ])
 

    res = list()
    res.append(CheckersGame(next_player=True, matrix=output1))
    res.append(CheckersGame(next_player=True, matrix=output2))

    gameIn = CheckersGame(next_player=False, matrix=input)
    assert gameIn.generateMoves() == res

def test_jump5():
    #white moves
    #movility (jumps) of a queen and a peon
    input = np.array([
                [0,1,0,0,0,0,0,0],
                [22,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,2,0],
                [0,0,0,2,0,1,0,1],
                [0,0,1,0,2,0,0,0],
                [0,0,0,0,0,1,0,2],
                [0,0,1,0,0,0,1,0],
                [0,22,0,0,0,0,0,0],
            ])

    output1 = np.array([
                [0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,22,2,0,1,0,1],
                [0,0,1,0,2,0,0,0],
                [0,0,0,0,0,1,0,2],
                [0,0,1,0,0,0,1,0],
                [0,22,0,0,0,0,0,0],
            ])

    output2 = np.array([
                [0,1,0,0,0,0,0,0],
                [22,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,2,0],
                [0,0,0,0,0,1,0,1],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,1,0,2],
                [0,0,0,0,0,0,1,0],
                [0,22,0,22,0,0,0,0],
            ])

    output3 = np.array([
                [0,1,0,0,0,0,0,0],
                [22,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,2,0],
                [0,0,0,2,0,1,0,1],
                [0,0,1,0,2,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0],
                [0,22,0,0,0,22,0,0],
            ])

    output4 = np.array([
                [0,1,0,0,0,0,0,0],
                [22,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,2,0],
                [0,22,0,2,0,1,0,1],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,1,0,2],
                [0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0],
            ])

    
    res = list()
    res.append(CheckersGame(next_player=True, matrix=output1))
    res.append(CheckersGame(next_player=True, matrix=output2))
    res.append(CheckersGame(next_player=True, matrix=output3))
    res.append(CheckersGame(next_player=True, matrix=output4))

    gameIn = CheckersGame(next_player=False, matrix=input)
    assert gameIn.generateMoves() == res

def test_jump6():
    #white moves
    #limits of movements
    input = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,2,0,0,0,0,0],
                [0,0,0,1,0,0,2,0],
                [0,0,0,0,0,1,0,1],
                [0,0,1,0,0,0,0,0],
                [0,22,0,1,0,0,0,0],
                [0,0,1,0,0,0,0,0],
            ])

    output1 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,0,0,2,1,0,1],
                [0,0,1,0,0,0,0,0],
                [0,22,0,1,0,0,0,0],
                [0,0,1,0,0,0,0,0],
            ])

    output2 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,2,0,0,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,1],
                [0,0,1,0,2,0,0,0],
                [0,22,0,1,0,0,0,0],
                [0,0,1,0,0,0,0,0],
            ])

    output3 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,2,0,0,0,0,0],
                [0,0,0,1,0,0,2,0],
                [0,0,0,22,0,1,0,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,1,0,0,0,0,0],
            ])

    res = list()
    res.append(CheckersGame(next_player=True, matrix=output1))
    res.append(CheckersGame(next_player=True, matrix=output2))
    res.append(CheckersGame(next_player=True, matrix=output3))

    gameIn = CheckersGame(next_player=False, matrix=input)
    assert gameIn.generateMoves() == res