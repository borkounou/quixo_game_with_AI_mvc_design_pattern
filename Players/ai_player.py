import math 
import numpy as np 
from .players import IPlayer
import sys
import copy
sys.setrecursionlimit(1000000)

class AIPlayer(IPlayer):
    def __init__(self,name,game):
        self.name = name
        self.game_state = game

    def alphabeta(self,board,alpha,beta,depth):
        # isTerminal = self.game_state.winner.winner_check(board)
        isTerminal = self.game_state.isGameEndFinal()
        if( isTerminal!=0 or depth ==0):
            score = self.evaluate(board, depth, isTerminal)
            return (score,None)

        depth = depth -1 
        bestMove = None 
        if self.game_state.turn ==self.game_state.O:
            for move in self.game_state.get_possible_moves():
                board = copy.deepcopy(board)
                if board[move[0]] != 0:
                    continue
                self.game_state.play2(board,move[0], move[1])
                val = self.alphabeta(board, alpha, beta, depth)[0]
                if (val > alpha):
                    alpha = val
                    bestMove = move
                if (alpha >= beta):
                    break
            return (alpha, bestMove)

        else:
            for move in self.game_state.get_possible_moves():
                board = copy.deepcopy(board)
                if board[move[0]] != 0:
                    continue
                self.game_state.play2(board,move[0], move[1])
                val = self.alphabeta(board, alpha, beta, depth)[0]
                if (val < beta):
                    beta = val
                    bestMove = move
                
                if (alpha >= beta):
                    break
            
            
            return (beta, bestMove)


    def evaluate(self,board, depth,isTerminal):
        # Maximizer won (O)
        if (isTerminal == self.game_state.O):  
            # Less moves is better
            return 100 + depth  
        # Minimizer Won (X)
        elif (isTerminal == self.game_state.X):  
            # Less moves is better
            return -100 - depth  
         # Compare owned piece counts if we reach tree depth limit
        else: 
            value = 0
            occValue = self.find_occurence(board,1) * 5

            if(board[2,2] == self.game_state.O):
                value = value + 20
            elif(board[2,2] == self.game_state.X):
                value = value - 20
            else:
                occValue *= -1

            frequency = np.unique(board, return_counts=True)
            uniqueCount = len(frequency[0])
            if (uniqueCount == 3):  # Contains blank pieces

                maximizerPieceCount = frequency[1][0]
                minimizerPieceCount = frequency[1][1]
            elif (uniqueCount > 1):
                maximizerPieceCount = frequency[1][0]
                minimizerPieceCount = frequency[1][1]

            value = value + (maximizerPieceCount - minimizerPieceCount) + occValue
            return value


    def find_occurence(self,state, key):
            occCount =0
            for r in range(0,5):
                row = state[r,:]
                col = state[:,r]
                y =np.where(row==key)[0]
                z = np.where(col ==key)[0]
                if(len(y)==4):
                    ok = (y[-1]- y[0]==len(y)-1)
                    if(ok):
                        occCount+=1
                if len(z) ==4:
                    ok =(z[-1]- z[0]==len(z)-1)
                    if ok:
                        occCount+=1
            return occCount

    # Return the best move using alphabeta search
    def playing(self,board):
        depth = 4
        move = self.alphabeta(board, -math.inf, math.inf, depth)[1]
        # move = self.alphabeta(board, -1000, 1000, depth)
        print(f"ai move and score are: {move}")
        state =self.game_state.isGameEndFinal()
        if move!=None:
            self.game_state.move.move_tiles(board,move[0],move[1],self.game_state.O)
            self.game_state.player_turn = not self.game_state.player_turn


        else:
            if state ==-1:
                print(f"Player ai winssssss")
            elif state ==1:
                print(f"Player human winssssss")

            else:
                print("Draw none wins")
           


   







        