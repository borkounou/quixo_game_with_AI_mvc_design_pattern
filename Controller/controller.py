import pygame
from Players.players_factory import PlayersFactory
class Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view
        self.player = PlayersFactory(self.model)

    def __controller_reset(self):
        self.model.reset_game()
        self.view.view_reset()
        self.__init__(self.model, self.view)

    
    def run_game(self):

        pygame.init()
        while self.model.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.model.gameOver()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.__controller_reset()
                
                if event.type == pygame.MOUSEBUTTONDOWN and self.model.start_game ==False:
                    x,y = self.model.get_mouse_coordinate(pygame.mouse.get_pos())
                    self.model.start_game = True
                    self.model.start_player(x,y)

                if event.type ==pygame.MOUSEBUTTONDOWN and self.model.start_game:
                    x,y =  self.model.get_mouse_coordinate(pygame.mouse.get_pos())
                    human_player = self.player.play("human")
                    human_player.playing(x,y)

                # if self.model.player_turn == False:
                #     random_player = self.player.play("random")
                #     random_player.playing(self.model.board)
                
                if self.model.player_turn ==False:
                    ai_player = self.player.play("ai")
                    ai_player.playing(self.model.board)
                    

            if not self.model.start_game:
                screen = self.view.build_screen("welcome_screen")
                screen.draw_screen(self.view.screen)
            else:
                screen = self.view.build_screen("main_screen")
                screen.draw_screen(self.view.screen, self.model.board)
            
            pygame.display.update()
            self.view.clock.tick(30)


        









