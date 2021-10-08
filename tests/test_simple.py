from games.CheckersGame import CheckersGame
import numpy as np

def test_simple1():
    #black moves
    #transformation after a simple move (posibility to eat but movement must stop)
    input = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,1,0,2,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])

    output1 = np.array([
                [0,11,0,0,0,0,0,0],
                [0,0,0,0,2,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    output2 = np.array([
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
    res.append(CheckersGame(next_player=False, matrix=output2))
    
    gameIn = CheckersGame(next_player=True, matrix=input)
    assert gameIn.generateMoves() == res

def test_simple2():
    #black moves
    #movility of a queen (4 moves) and a peon (2)
    input = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,11,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0],
            ])

    output1 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,11,0,0,0,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0],
            ])
    
    output2 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,11,0,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0],
            ])
    
    output3 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,11,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0],
            ])
    
    output4 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,11,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0],
            ])

    output5 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,11,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    output6 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,11,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,1,0,0,0,0,0],
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

def test_simple3():
    #black moves
    #limits of movements
    input = np.array([
                [1,0,0,0,0,0,0,1],
                [0,1,0,1,0,0,1,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,2,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,1],
            ])

    output1 = np.array([
                [1,0,11,0,0,0,0,1],
                [0,0,0,1,0,0,1,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,2,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,1],
            ])
    
    output2 = np.array([
                [1,0,11,0,0,0,0,1],
                [0,1,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,2,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,1],
            ])

    output3 = np.array([
                [1,0,0,0,11,0,0,1],
                [0,1,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,2,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,1],
            ])

    output4 = np.array([
                [1,0,0,0,0,11,0,1],
                [0,1,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,2,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,1],
            ])
    
    output5 = np.array([
                [1,0,0,0,0,0,0,1],
                [0,1,0,1,0,0,1,0],
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,0,2,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,1],
            ])

    output6 = np.array([
                [1,0,0,0,0,0,0,1],
                [0,1,0,1,0,0,1,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,2,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,1],
            ])

    output7 = np.array([
                [1,0,0,0,0,0,0,1],
                [0,1,0,1,0,0,1,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,1,0,2,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,1],
            ])

    output8 = np.array([
                [1,0,0,0,0,0,0,1],
                [0,1,0,1,0,0,1,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,2,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1],
            ])

    output9 = np.array([
                [1,0,0,0,0,0,0,1],
                [0,1,0,1,0,0,1,0],
                [0,0,0,0,0,0,0,0],
                [0,1,0,0,0,2,0,0],
                [0,0,1,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0],
            ])


    res = list()
    res.append(CheckersGame(next_player=False, matrix=output1))
    res.append(CheckersGame(next_player=False, matrix=output2))
    res.append(CheckersGame(next_player=False, matrix=output3))
    res.append(CheckersGame(next_player=False, matrix=output4))
    res.append(CheckersGame(next_player=False, matrix=output5))
    res.append(CheckersGame(next_player=False, matrix=output6))
    res.append(CheckersGame(next_player=False, matrix=output7))
    res.append(CheckersGame(next_player=False, matrix=output8))
    res.append(CheckersGame(next_player=False, matrix=output9))
    
    gameIn = CheckersGame(next_player=True, matrix=input)
    assert gameIn.generateMoves() == res

def test_simple4():
    #white moves
    #transformation after a simple move (posibility to eat but movement must stop)
    input = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,2,0,1,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])

    output1 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,2,0,1,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])

    output2 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0],
                [0,22,0,0,0,0,0,0],
            ])

    output3 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0],
                [0,0,0,22,0,0,0,0],
            ])

    res = list()
    res.append(CheckersGame(next_player=True, matrix=output1))
    res.append(CheckersGame(next_player=True, matrix=output2))
    res.append(CheckersGame(next_player=True, matrix=output3))
    
    gameIn = CheckersGame(next_player=False, matrix=input)
    assert gameIn.generateMoves() == res

def test_simple5():
    #white moves
    #movility of a queen (4 moves) and 2 peon (2)
    input = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,2,0,0,0,0],
                [0,0,22,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,0,0,0,0,0,0],
            ])

    output1 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,22,0,2,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,0,0,0,0,0,0],
            ])

    output2 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,22,0,2,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    output3 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,2,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,22,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,0,0,0,0,0,0],
            ])

    output4 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,2,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,1,22,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,0],
                [0,0,0,0,0,0,0,0],
            ])

    output5 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,2,0,0,0,0],
                [0,0,22,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,22,0,0],
            ])

    output6 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,2,0,0,0,0],
                [0,0,22,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,22],
            ])


    res = list()
    res.append(CheckersGame(next_player=True, matrix=output1))
    res.append(CheckersGame(next_player=True, matrix=output2))
    res.append(CheckersGame(next_player=True, matrix=output3))
    res.append(CheckersGame(next_player=True, matrix=output4))
    res.append(CheckersGame(next_player=True, matrix=output5))
    res.append(CheckersGame(next_player=True, matrix=output6))
    
    gameIn = CheckersGame(next_player=False, matrix=input)
    assert gameIn.generateMoves() == res

def test_simple6():
    #white moves
    #limits of movements
    input = np.array([
                [2,0,0,0,0,0,0,2],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,2,0,0,0],
                [0,22,0,0,0,0,0,0],
                [2,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,22,0],
            ])

    output1 = np.array([
                [2,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,2,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,2,0,0,0],
                [0,22,0,0,0,0,0,0],
                [2,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,22,0],
            ])

    output2 = np.array([
                [2,0,0,0,0,0,0,2],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [0,22,0,2,0,0,0,0],
                [2,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,22,0],
            ])

    output3 = np.array([
                [2,0,0,0,0,0,0,2],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [0,22,0,0,0,2,0,0],
                [2,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,22,0],
            ])

    output4 = np.array([
                [2,0,0,0,0,0,0,2],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,22,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,22,0],
            ])

    output5 = np.array([
                [2,0,0,0,0,0,0,2],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,2,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,22,0,0,0,0,2],
                [0,0,0,0,0,0,22,0],
            ])

    output6 = np.array([
                [2,0,0,0,0,0,0,2],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,2,0,0,0],
                [0,22,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,2],
                [0,22,0,0,0,0,22,0],
            ])

    output7 = np.array([
                [2,0,0,0,0,0,0,2],
                [0,1,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,0,0,2,0,0,0],
                [0,22,0,0,0,0,0,0],
                [2,0,0,0,0,22,0,2],
                [0,0,0,0,0,0,0,0],
            ])


    res = list()
    res.append(CheckersGame(next_player=True, matrix=output1))
    res.append(CheckersGame(next_player=True, matrix=output2))
    res.append(CheckersGame(next_player=True, matrix=output3))
    res.append(CheckersGame(next_player=True, matrix=output4))
    res.append(CheckersGame(next_player=True, matrix=output5))
    res.append(CheckersGame(next_player=True, matrix=output6))
    res.append(CheckersGame(next_player=True, matrix=output7))
    
    gameIn = CheckersGame(next_player=False, matrix=input)
    assert gameIn.generateMoves() == res