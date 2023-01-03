# Import the necessary classes
from Model.board import Game_State
from View.view import View
from Controller.controller import Controller

def main():
    # Create the model, view, and controller
    model = Game_State()
    view = View()
    controller = Controller(model, view)

    # Run the game
    controller.run_game()

if __name__ == "__main__":
    main()
