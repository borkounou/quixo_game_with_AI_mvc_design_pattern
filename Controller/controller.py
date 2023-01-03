
import pygame
from Players.players_factory import PlayersFactory

class Controller:
    def __init__(self, model, view):
        # Initialize instance variables
        self.model = model
        self.view = view
        self.player = PlayersFactory(self.model)
        self.state = WelcomeScreenState()

    def controller_reset(self):
        # Reset the game model and view
        self.model.reset_game()
        self.view.view_reset()
        # Re-initialize the controller
        self.__init__(self.model, self.view)

    def run_game(self):
        # Initialize Pygame
        pygame.init()
        # Run the game loop
        while self.model.running:
            # Process events
            for event in pygame.event.get():
                self.state.handle_event(self, event)
            # Update the game state
            self.state.update_game(self)
            # Update the display
            pygame.display.update()
            # Wait to maintain a frame rate of 30 fps
            self.view.clock.tick(30)

class WelcomeScreenState:
    def handle_event(self, controller, event):
        """Process events and update the game state.

        Parameters:
        controller (Controller): The controller object.
        event (Event): The Pygame event object.
        """
        if event.type == pygame.QUIT:
            # Set the running attribute of the game model to False to stop the game loop
            controller.model.gameOver()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Reset the game
            controller.controller_reset()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse coordinates
            x, y = controller.model.get_mouse_coordinate(pygame.mouse.get_pos())
            # Start the game by setting start_game attribute of the game model to True
            # and setting the current player based on the mouse coordinates
            controller.model.start_game = True
            controller.model.start_player(x, y)
            # Set the game state to the main screen state
            controller.state = MainScreenState()

    def update_game(self, controller):
        """Update the game display.

        Parameters:
        controller (Controller): The controller object.
        """
        # Build the welcome screen
        screen = controller.view.build_screen("welcome_screen")
        # Draw the screen
        screen.draw_screen(controller.view.screen)


class MainScreenState:

  def handle_event(self, controller, event):
      """Process events and update the game state.

      Parameters:
      controller (Controller): The controller object.
      event (Event): The Pygame event object.
      """
      if event.type == pygame.QUIT:
          # Set the running attribute of the game model to False to stop the game loop
          controller.model.gameOver()
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
          # Reset the game
          controller.controller_reset()
      elif event.type == pygame.MOUSEBUTTONDOWN:
          # Get the mouse coordinates
          x, y = controller.model.get_mouse_coordinate(pygame.mouse.get_pos())
          # Get the human player object and call the playing method with the mouse coordinates as arguments
          human_player = controller.player.play("human")
          human_player.playing(x, y)
      elif controller.model.player_turn == False:
          # Get the AI player object and call the playing method with the game board as an argument
          ai_player = controller.player.play("ai")
          ai_player.playing(controller.model.board)

  def update_game(self, controller):
      """Update the game display.

      Parameters:
      controller (Controller): The controller object.
      """
      # Build the main screen
      screen = controller.view.build_screen("main_screen")
      # Draw the main screen
      screen.draw_screen(controller.view.screen, controller.model.board)
      # Build the game screen
      screen = controller.view.build_screen("game_screen")
      # Draw the game screen
      screen.draw_screen(
          controller.view.screen, controller.model.ai_move, controller.model.winner_state
      )

