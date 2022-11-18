from Controller.quixo_controller import QuixoController
from Model.board import Board
from Model.move import Move
from Model.winner import Winner
from View.quixo_view import QuixoView
from Controller.controller import Controller
from View.view import View
from Model.players.random_player import RandomPlayer





if __name__ =="__main__":

    game_board = Board()
    move = Move()
    winner = Winner()
    view = View()
    random_player = RandomPlayer("random")
    quixo = Controller(game_board, move, winner, view,random_player)
    quixo.main_loop_test()



