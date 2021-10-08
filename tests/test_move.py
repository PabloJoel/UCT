from games.CheckersGame import CheckersGame
import numpy as np

def test_move1():
    #black moves
    #jump so no simple move
    input = np.array([
                [2,0,0,0,0,0,0,0],
                [0,11,0,0,0,0,0,0],
                [0,0,0,0,2,0,0,0],
                [0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    output1 = np.array([
                [2,0,0,0,0,0,0,0],
                [0,11,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])



    res = list()
    res.append(CheckersGame(next_player=False, matrix=output1))
    
    gameIn = CheckersGame(next_player=True, matrix=input)
    assert gameIn.generateMoves() == res

def test_move2():
    #black moves
    #only simple moves
    input = np.array([
                [0,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,11,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [11,0,0,0,0,0,0,0],
            ])
    
    output1 = np.array([
                [0,0,0,0,0,11,0,2],
                [0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,11,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [11,0,0,0,0,0,0,0],
            ])

    output2 = np.array([
                [0,0,0,0,0,0,11,2],
                [0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,11,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [11,0,0,0,0,0,0,0],
            ])

    output3 = np.array([
                [0,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0],
                [0,11,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [11,0,0,0,0,0,0,0],
            ])
    
    output4 = np.array([
                [0,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,11,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [11,0,0,0,0,0,0,0],
            ])

    output5 = np.array([
                [0,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,11,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [11,0,0,0,0,0,0,0],
            ])
    
    output6 = np.array([
                [0,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,11,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [11,0,0,0,0,0,0,0],
            ])

    output7 = np.array([
                [0,0,0,0,0,0,0,2],
                [0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,11,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,11,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])



    res = list()
    res.append(CheckersGame(next_player=False, matrix=output1))
    res.append(CheckersGame(next_player=False, matrix=output2))
    res.append(CheckersGame(next_player=False, matrix=output3))
    res.append(CheckersGame(next_player=False, matrix=output4))
    res.append(CheckersGame(next_player=False, matrix=output5))
    res.append(CheckersGame(next_player=False, matrix=output6))
    res.append(CheckersGame(next_player=False, matrix=output7))
    
    gameIn = CheckersGame(next_player=True, matrix=input)
    assert gameIn.generateMoves() == res

def test_move3():
    #black moves
    #no moves
    input = np.array([
                [2,0,11,0,2,0,0,0],
                [0,11,0,1,2,2,0,0],
                [2,0,2,0,2,0,0,0],
                [0,2,0,1,0,0,0,0],
                [1,0,0,0,2,0,0,0],
                [0,2,0,2,0,0,0,0],
                [0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
            ])


    res = list()
    
    gameIn = CheckersGame(next_player=True, matrix=input)
    assert gameIn.generateMoves() == res

def test_move4():
    #white moves
    #jump so no simple move
    input = np.array([
                [1,0,0,0,0,0,1,0],
                [0,22,0,0,0,0,0,0],
                [0,0,0,0,1,0,1,0],
                [0,0,0,22,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,2,0,0],
                [0,0,2,0,0,0,1,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    output1 = np.array([
                [1,0,0,0,0,0,1,0],
                [0,22,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,22],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,2,0,0],
                [0,0,2,0,0,0,1,0],
                [0,0,0,0,0,0,0,0],
            ])
    
    output2 = np.array([
                [1,0,0,0,0,0,1,0],
                [0,22,0,0,0,0,0,0],
                [0,0,0,0,1,0,1,0],
                [0,0,0,22,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,2,0,0,0,0,0],
                [0,0,0,0,0,0,0,22],
            ])
    
    res = list()
    res.append(CheckersGame(next_player=True, matrix=output1))
    res.append(CheckersGame(next_player=True, matrix=output2))
    
    gameIn = CheckersGame(next_player=False, matrix=input)
    assert gameIn.generateMoves() == res

def test_move5():
    #white moves
    #only simple moves
    input = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,22],
                [0,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,1,0,2,0,0],
                [0,1,0,0,0,0,0,0],
            ])
    
    output1 = np.array([
                [0,0,0,0,0,0,22,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,1,0,2,0,0],
                [0,1,0,0,0,0,0,0],
            ])

    output2 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,22,0],
                [0,2,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,1,0,2,0,0],
                [0,1,0,0,0,0,0,0],
            ])

    output3 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,22],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [1,0,2,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,1,0,2,0,0],
                [0,1,0,0,0,0,0,0],
            ])

    output4 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,22],
                [0,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,1,0,0,0,0],
                [0,1,0,0,22,0,0,0],
            ])

    output5 = np.array([
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,22],
                [0,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [2,0,0,1,0,0,0,0],
                [0,1,0,0,0,0,22,0],
            ])
    
    res = list()
    res.append(CheckersGame(next_player=True, matrix=output1))
    res.append(CheckersGame(next_player=True, matrix=output2))
    res.append(CheckersGame(next_player=True, matrix=output3))
    res.append(CheckersGame(next_player=True, matrix=output4))
    res.append(CheckersGame(next_player=True, matrix=output5))
    
    gameIn = CheckersGame(next_player=False, matrix=input)
    assert gameIn.generateMoves() == res

def test_move6():
    #white moves
    #no moves
    input = np.array([
                [0,0,0,0,0,2,0,1],
                [0,0,0,0,1,0,22,0],
                [2,0,0,1,0,1,0,1],
                [0,1,0,0,1,0,0,0],
                [0,0,2,0,0,0,0,0],
                [0,1,0,1,0,0,0,0],
                [1,0,0,0,2,0,2,0],
                [0,0,0,1,0,22,0,1],
            ])

    res = list()
    
    gameIn = CheckersGame(next_player=False, matrix=input)
    assert gameIn.generateMoves() == res