
from Model.board import Board
from View.view import View
from Controller.controller import Controller

if __name__ == "__main__":
    model = Board()
    view = View()
    controller = Controller(model, view)
    controller.run_game()