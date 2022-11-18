from Model.board import Board
from Model.move import Move
from Model.winner import Winner
from Controller.controller import Controller
from View.view import View
from Model.players.players_factory import PlayersFactory

if __name__ =="__main__":
    game_board = Board()
    move = Move()
    winner = Winner()
    view = View()
    players =PlayersFactory#RandomPlayer("random")
    quixo = Controller(game_board, move, winner, view,players)
    quixo.main_loop()



