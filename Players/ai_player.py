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

    def alphabeta(self, board, alpha, beta, depth):
        is_terminal = self.game_state.isGameEndFinal()
        if is_terminal != 0 or depth == 0:
            score = self.evaluate(board, depth, is_terminal)
            return score, None

        depth -= 1
        best_move = None

        if self.game_state.turn == self.game_state.O:
            for move in self.game_state.get_possible_moves():
                board = copy.deepcopy(board)
                if board[move[0]] != 0:
                    continue
                self.game_state.play2(board, move[0], move[1])
                val, _ = self.alphabeta(board, alpha, beta, depth)
                if val > alpha:
                    alpha = val
                    best_move = move
                if alpha >= beta:
                    break
            return alpha, best_move

        else:
            for move in self.game_state.get_possible_moves():
                board = copy.deepcopy(board)
                if board[move[0]] != 0:
                    continue
                self.game_state.play2(board, move[0], move[1])
                val, _ = self.alphabeta(board, alpha, beta, depth)
                if val < beta:
                    beta = val
                    best_move = move
                if alpha >= beta:
                    break

            return beta, best_move

    
    def evaluate(self, board, depth, isTerminal):

        value = 0

        if isTerminal == self.game_state.O:
            value = 100 + depth
        elif isTerminal == self.game_state.X:
            value = -100 - depth
        else:
            occValue = self.find_occurrence(board, 1) * 5

            if board[2, 2] == self.game_state.O:
                value += 20
            elif board[2, 2] == self.game_state.X:
                value -= 20
            else:
                occValue *= -1

            frequency = np.unique(board, return_counts=True)
            unique_count = len(frequency[0])
            if unique_count == 3:
                maximizer_piece_count = frequency[1][0]
                minimizer_piece_count = frequency[1][1]
            elif unique_count > 1:
                maximizer_piece_count = frequency[1][0]
                minimizer_piece_count = frequency[1][1]

            value += maximizer_piece_count - minimizer_piece_count + occValue

        return value

    def find_occurrence(self, state, key):
        occ_count = 0
        for r in range(5):
            row = state[r, :]
            col = state[:, r]
            y = np.where(row == key)[0]
            z = np.where(col == key)[0]
            if len(y) == 4:
                if y[-1] - y[0] == len(y) - 1:
                    occ_count += 1
            if len(z) == 4:
                if z[-1] - z[0] == len(z) - 1:
                    occ_count += 1
        return occ_count

    # Return the best move using alphabeta search
    def playing(self, board):
        depth = 3
        move = self.alphabeta(board, -math.inf, math.inf, depth)[1]

        state = self.game_state.isGameEndFinal()
        if move is not None:
            self.game_state.move.move_tiles(board, move[0], move[1], self.game_state.O)
            self.game_state.player_turn = not self.game_state.player_turn
            self.game_state.ai_move = move
                
        else:
            if state == self.game_state.O:
                pl = "AI wins"
                self.game_state.winner_state =pl
                print(self.game_state.winner_state)
            elif state == self.game_state.X:
                self.game_state.winner_state ="Human wins"
            elif self.game_state.isGameEnd():
                self.game_state.winner_state = "Draw:no winner"
            else:
                self.game_state.winner_state="AI's turn" if self.game_state.player_turn else "Human's turn"
          