import math 
from .players import IPlayer
import sys
import copy
sys.setrecursionlimit(10000000)

import concurrent.futures

class AIPlayer(IPlayer):
    # Initialise the constructor
    def __init__(self,name,game):
        # The name of the game of player 
        self.name = name
        self.game_state = game
        # Create a thread pool with 4 worker threads
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    def alphabeta(self, board, alpha, beta, depth):
        """Perform an alpha-beta search to find the best move.

        Parameters:
        board (numpy array): The current game state.
        alpha (int): The current maximum lower bound.
        beta (int): The current minimum upper bound.
        depth (int): The current search depth.

        Returns:
        tuple: The score and best move for the current game state.
        """
        # Check if the current game state is a terminal state or the maximum search depth has been reached
        is_terminal = self.game_state.isGameEndFinal()
        if is_terminal != 0 or depth == 0:
            # Return the score and no best move for terminal states
            score = self.evaluate(board, depth, is_terminal)
            return score, None

        # Decrement the depth for the next search
        depth -= 1
        best_move = None

        if self.game_state.turn == self.game_state.O:
            # Iterate through all possible moves and choose the move with the highest score
            for move in self.game_state.get_possible_moves():
                # Make a deep copy of the board to prevent the original board from being modified
                board = copy.deepcopy(board)
                if board[move[0]] != 0:
                    # Skip this move if the starting position is already occupied
                    continue
                self.game_state.play(board, move[0], move[1])
                # Submit the recursive call to the thread pool
                future = self.executor.submit(self.alphabeta, board, alpha, beta, depth)
                # Wait for the result and retrieve the value and best move
                val, _ = future.result()
                if val > alpha:
                    alpha = val
                    best_move = move
                if alpha >= beta:
                    break
            return alpha, best_move

        else:
            # Iterate through all possible moves and choose the move with the lowest score
            for move in self.game_state.get_possible_moves():
                    board = copy.deepcopy(board)
                    if board[move[0]] != 0:
                        continue
                    self.game_state.play(board, move[0], move[1])
                    # Submit the recursive call to the thread pool
                    future = self.executor.submit(self.alphabeta, board, alpha, beta, depth)
                    # Wait for the result and retrieve the value and best move
                    val, _ = future.result()
                    if val < beta:
                        beta = val
                        best_move = move
                    if alpha >= beta:
                        break

            return beta, best_move


    def evaluate(self, board, depth, is_terminal):
        # If X has won, return a score based on the depth
        if is_terminal == self.game_state.X:
            return 10 - depth
        # If O has won, return a score based on the depth
        elif is_terminal == self.game_state.O:
            return depth - 10
        else:
            # Initialize the X and O scores to 0
            x_score = 0
            o_score = 0
            # Iterate over the rows and columns of the board
            for row in range(5):
                x_count = 0
                o_count = 0
                for col in range(5):
                    # Count the number of X's and O's in the current row and column
                    if board[row][col] == self.game_state.X:
                        x_count += 1
                    elif board[row][col] == self.game_state.O:
                        o_count += 1
                # If there are 5 X's in the current row, increment the X score
                if x_count == 5:
                    x_score += 1
                # If there are 5 O's in the current row, increment the O score
                if o_count == 5:
                    o_score += 1
            for col in range(5):
                x_count = 0
                o_count = 0
                for row in range(5):
                    # Count the number of X's and O's in the current column
                    if board[row][col] == self.game_state.X:
                        x_count += 1
                    elif board[row][col] == self.game_state.O:
                        o_count += 1
                # If there are 5 X's in the current column, increment the X score
                if x_count == 5:
                    x_score += 1
                # If there are 5 O's in the current column, increment the O score
                if o_count == 5:
                    o_score += 1
            # Initialize the X and O counts to 0
            x_count = 0
            o_count = 0
            # Count the number of X's and O's on the descending diagonal
            for i in range(5):
                if board[i][i] == self.game_state.X:
                    x_count += 1
                elif board[i][i] == self.game_state.O:
                    o_count += 1
            # If there are 5 X's on the descending diagonal, increment the X score
            if x_count == 5:
                x_score += 1
            # If there are 5 O's on the descending diagonal, increment the O score
            if o_count == 5:
                o_score += 1
            # Initialize the X and O counts to 0
            x_count = 0
            o_count = 0
            # Count the number of X's and O's on the ascending diagonal
            for i in range(5):
                if board[i][4-i] == self.game_state.X:
                    x_count += 1
                elif board[i][4-i] == self.game_state.O:
                    o_count += 1
            # If there are 5 X's on the ascending diagonal, increment the X score
            if x_count == 5:
                x_score += 1
            # If there are 5 O's on the ascending diagonal, increment the O score
            if o_count == 5:
                o_score += 1
            # Return the difference
            return x_score - o_score


    def playing(self, board):
        # Set the depth for the minimax algorithm
        depth = 3
        # Get the best move from the minimax algorithm
        move = self.alphabeta(board, -math.inf, math.inf, depth)[1]
        
        state = self.game_state.isGameEndFinal()

        # Check if the game has ended
        game_ended = self.game_state.isGameEndFinal()
        
        # If a move was returned by the minimax algorithm
        if move is not None:
            # Make the move on the board
            self.game_state.move.move_tiles(board, move[0], move[1], self.game_state.O)
            # Toggle the player turn
            self.game_state.player_turn = not self.game_state.player_turn
            # Save the AI's move
            self.game_state.ai_move = move
            
        # If no move was returned (either because the game has ended or because the minimax algorithm returned None)
        else:
            # If the AI has won the game
            if state == self.game_state.O:
                self.game_state.winner_state = "AI wins"
            # If the human player has won the game
            elif state == self.game_state.X:
                self.game_state.winner_state ="Human wins"
            # If the game has ended in a draw
            elif self.game_state.isGameEnd():
                self.game_state.winner_state = "Draw:no winner"
            # If the game has not yet ended
            else:
                # If it's the AI's turn
                if self.game_state.player_turn==False:
                    self.game_state.winner_state="Ai VS Human"
                # If it's the human player's turn
                else:
                    self.game_state.winner_state = "Human Vs AI"

