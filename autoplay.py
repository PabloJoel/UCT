import sys
sys.path.append("..")

import visual.GameModel as gm

#Game
from games.CheckersGame import CheckersGame

#import players
from players.RandomPlayer import RandomPlayer
from players.UCTPlayer import UCTPlayer

def play(games, player1_type, player2_type, iters1=None, iters2=None, heur1=None, heur2=None, lgr1=None, lgr2=None, choose_move1=None, choose_move2=None):
    black = 0
    white = 0
    draw  = 0
    i = 0
    while(i<games):
        player1 = create_player(player1_type, iters1, heur1, lgr1, choose_move1)
        player2 = create_player(player2_type, iters2, heur2, lgr2, choose_move2)
        
        model = gm.GameModel(CheckersGame())
        winner = model.play(player1=player1, player2=player2, show=False)

        ret = return_info(player1, player2, iters1, iters2, heur1, heur2, lgr1, lgr2, choose_move1, choose_move2, winner, i)
        print(ret)

        if winner == 'Black':
            black += 1
        elif winner == 'White':
            white += 1
        elif winner == 'Draw':
            draw += 1
        i += 1

    write_res(ret.replace(":"," "), black, white, draw)

def write_res(title, black, white, draw):
    nombre = title + '.txt'

    file = open(nombre,'a')
    file.write(f'White: {white}, Black: {black}, Draw: {draw}')
    file.close()

def create_player(player,iters,heur,lgr,choose):
    if player=="rand":
        return RandomPlayer(show=False)
    else:
        return UCTPlayer(game=CheckersGame(),iter=iters, choose=choose, heurs=heur,last_good_reply=lgr)

def return_info(player1, player2, iters1, iters2, heur1, heur2, lgr1, lgr2, choose_move1, choose_move2, winner, current_game_number):
    prnt = str()

    if player1=="rand":
        prnt = prnt + 'Rand vs '
    else:
        prnt = prnt + 'UCT vs '

    if player1=="rand":
        prnt = prnt + 'Rand '
    else:
        prnt = prnt + 'UCT '
    
    prnt = f'Winner:{winner}, Current game: {current_game_number}'
    if player1=="UCT":
        prnt = prnt + f' MCTS iter1: {iters1}, Heur1: {heur1}, Last Good Reply1: {lgr1}, Choose Move1: {choose_move1}'
    elif player2=="UCT":
        prnt = prnt + f' MCTS iter2: {iters2}, Heur2: {heur2}, Last Good Reply2: {lgr2}, Choose Move2: {choose_move2}'

    return prnt
