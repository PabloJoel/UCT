import sys
sys.path.append("..")

import visual.GameModel as gm

#Game
from games.CheckersGame import CheckersGame

#import players
from players.RandomPlayer import RandomPlayer
from players.UCTPlayer import UCTPlayer

def write_res(iter, heur, lgr, white, black, draw):
    if heur:
        nombre = 'UCT vs UCT heur '+str(iter)+'.txt'
    elif lgr:
        nombre = 'UCT vs UCT lgr '+str(iter)+'.txt'
    else:
        nombre = 'UCT vs UCT '+str(iter)+'.txt'

    file = open(nombre,'a')
    file.write(f'White: {white}, Black: {black}, Draw: {draw}')
    file.close()

white = 0
black = 0
draw = 0
i = 0

mcts_iter1 = 700
heur1 = False
last_good_reply1 = False


mcts_iter2 = 700
heur2 = True
last_good_reply2 = False

choose_move = 'max_value'

while(i<100):
    player1 = UCTPlayer(player=True,game=CheckersGame(),iter=mcts_iter1,choose=choose_move, heurs=heur1,last_good_reply=last_good_reply1)
    #player1 = RandomPlayer(show=False)
    player2 = UCTPlayer(player=False,game=CheckersGame(),iter=mcts_iter2,choose=choose_move, heurs=heur2,last_good_reply=last_good_reply2)
    
    model = gm.GameModel(CheckersGame())
    winner = model.play(player1=player1, player2=player2, show=False)
    
    #print(f'Winner:{winner}, Current game: {i}, MCTS iter2: {mcts_iter2}, Heur2: {heur2}, Last Good Reply2: {last_good_reply2}, Choose:{choose_move}')
    print(f'Winner:{winner}, Current game: {i}, MCTS iter1: {mcts_iter1}, Heur1: {heur1}, Last Good Reply: {last_good_reply1}, MCTS iter2: {mcts_iter2}, Heur2: {heur2}, Last Good Reply2: {last_good_reply2}, Choose:{choose_move}')
    
    if winner == 'Black':
        black += 1
    elif winner == 'White':
        white += 1
    elif winner == 'Draw':
        draw += 1
    i += 1

total = black+white+draw
print(f'Black:{black}, White:{white}, Draw:{draw}')
print(f'Black:{(black/total)*100}, White:{(white/total)*100}, Draw:{(draw/total)*100}')

write_res(mcts_iter2, heur2, last_good_reply2, white, black, draw)

