# Import the necessary classes
from Model.board import GameState
from View.view import View
from Controller.controller import Controller

def main():
    # Create the model, view, and controller
    model = GameState()
    view = View()
    controller = Controller(model, view)

    # Run the game
    controller.run_game()

if __name__ == "__main__":
    main()
