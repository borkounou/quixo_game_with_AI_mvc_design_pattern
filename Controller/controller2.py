import pygame
from Players.players_factory import PlayersFactory

class Controller:
  def __init__(self, model, view):
    self.model = model
    self.view = view
    self.player = PlayersFactory(self.model)
    self.state = WelcomeScreenState()

  def controller_reset(self):
    self.model.reset_game()
    self.view.view_reset()
    self.__init__(self.model, self.view)

  def run_game(self):
    pygame.init()
    while self.model.running:
      for event in pygame.event.get():
        self.state.handle_event(self, event)

      self.state.update_game(self)
      pygame.display.update()
      self.view.clock.tick(30)

class WelcomeScreenState:
  def handle_event(self, controller, event):
    if event.type == pygame.QUIT:
      controller.model.gameOver()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
      controller.controller_reset()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      x, y = controller.model.get_mouse_coordinate(pygame.mouse.get_pos())
      controller.model.start_game = True
      controller.model.start_player(x, y)
      controller.state = MainScreenState()

  def update_game(self, controller):
    screen = controller.view.build_screen("welcome_screen")
    screen.draw_screen(controller.view.screen)

class MainScreenState:
  def handle_event(self, controller, event):
    if event.type == pygame.QUIT:
      controller.model.gameOver()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
      controller.controller_reset()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      x, y = controller.model.get_mouse_coordinate(pygame.mouse.get_pos())
      human_player = controller.player.play("human")
      human_player.playing(x, y)
    elif controller.model.player_turn == False:
      ai_player = controller.player.play("ai")
      ai_player.playing(controller.model.board)

  def update_game(self, controller):
    screen = controller.view.build_screen("main_screen")
    screen.draw_screen(controller.view.screen, controller.model.board)
    screen = controller.view.build_screen("game_screen")
    screen.draw_screen(controller.view.screen,controller.model.ai_move,controller.model.winner_state)
