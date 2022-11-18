from abc import ABCMeta, abstractmethod

class IPlayer(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,name):
        """Implements de name and player number"""

    @abstractmethod
    def playing(self, *args, **kwargs):
        """Implements """










# import math
# import numpy as np
# from numpy import random
# from board import Board

# def alphabeta(board, alpha, beta, depth):

#     isTerminal = board.isGameEnd()
#     if (isTerminal != 0 or depth == 0):  # Return board value if we hit terminal
#         score = evaluate(board, depth)
#         return (score, None)

#     depth -= 1

#     bestMove = None
#     if (board.turn == Board.X):
#         for move in board.getPossibleMoves():
#             s = Board(board)
#             s.play(move[0], move[1])
#             val = alphabeta(s, alpha, beta, depth)[0]
#             if (val > alpha):
#                 alpha = val
#                 bestMove = move
#             if (alpha >= beta):
#                 break
#         return (alpha, bestMove)
#     else:
#         for move in board.getPossibleMoves():
#             s = Board(board)
#             s.play(move[0], move[1])
#             val = alphabeta(s, alpha, beta, depth)[0]
#             if (val < beta):
#                 beta = val
#                 bestMove = move
#             if (alpha >= beta):
#                 break
#         return (beta, bestMove)


# def find_occurence(state, key):
#     occCount = 0
#     for r in range(0, 5):
#         row = state[r, :]
#         col = state[:, r]
#         y = np.where(row == key)[0]
#         z = np.where(col == key)[0]
#         if (len(y) == 4):
#             ok = (y[-1] - y[0] == len(y) - 1)
#             if (ok):
#                 occCount += 1
#         if (len(z) == 4):
#             ok = (z[-1] - z[0] == len(z) - 1)
#             if (ok):
#                 occCount += 1
#     return occCount

# # Evaluates the current game state
# def evaluate(board, depth):
#     isTerminal = board.isGameEnd()
#     if (isTerminal == Board.X):  # Maximizer won (X)
#         return 100 + depth  # Less moves is better
#     elif (isTerminal == Board.O):  # Minimizer Won (O)
#         return -100 - depth  # Less moves is better
#     else:  # Compare owned piece counts if we reach tree depth limit
#         value = 0
#         occValue = find_occurence(board.board,board.turn) * 5

#         if(board.board[2,2] == board.X):
#             value += 20
#         elif(board.board[2,2] == board.O):
#             value -= 20

#         if(board.turn == Board.O):
#             occValue *= -1

#         frequency = np.unique(board.board, return_counts=True)
#         uniqueCount = len(frequency[0])
#         if (uniqueCount == 3):  # Contains blank pieces
#             maximizerPieceCount = frequency[1][1]
#             minimizerPieceCount = frequency[1][2]
#         elif (uniqueCount > 1):
#             maximizerPieceCount = frequency[1][0]
#             minimizerPieceCount = frequency[1][1]

#         value += (maximizerPieceCount - minimizerPieceCount) + occValue
#         return value

# # Return the best move using alphabeta search
# def getBestMove(board, depthLevels):
#     possibleMoves = board.getPossibleMoves()
#     possibleMoveCount = len(possibleMoves)

#     # Iterative deepening based on possible move count
#     depth = 0
#     for depthLvl in depthLevels:
#         if (possibleMoveCount > depthLvl[1]):
#             depth = depthLvl[0]
#         else:
#             break

#     move = alphabeta(board, -math.inf, math.inf, depth)[1]

#     return move