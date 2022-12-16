
from Model.board import Board
from View.view import View
from Controller.controller import Controller
# import math

# from Players.ai_player import AIPlayer

if __name__ == "__main__":
    model = Board()
    view = View()
    # ai = AIPlayer(model)
    # # move = ai.getBestMove(model.board)
   
  
    # move = ai.alphabeta(model.board, -math.inf, math.inf, 3)
    # print(move)
    

    # (beta, bestMove) = ai.alphabeta(model, -100000,100000,1000)
    # print(beta,bestMove)
    controller = Controller(model, view)
    controller.run_game()