from .screen import IScreen
import pygame 
from constants import HEIGHT, WIDTH,IMAGE_SIZE,SQ_SIZE,IMAGES

class GameScreen(IScreen):
    def __init__(self):
        super().__init__()


    def draw_screen(self,screen,move,winner_state):

        # Title text screen 
       
        font = pygame.font.SysFont("Arial", 30)
        if winner_state!= None:
            # print(f"Winner state is: {winner_state}")
            title = font.render(winner_state,1,pygame.Color("White"))
        else:
            title = font.render("Playing",1,pygame.Color("White"))
           

        title_rect = title.get_rect(center=(400,50))
        screen.blit(title,title_rect)

        # Text for instruction
        font_player = pygame.font.SysFont("Arial",20)
        if move is not None:
            player_text = font_player.render(f"AI moves from {move[0]} -to- {move[1]}",1,pygame.Color("white"))
        else:
            player_text = font_player.render(f"AI info",1,pygame.Color("white"))

        player_rect = player_text.get_rect(center=(400,100))

        screen.blit(player_text,player_rect)



    

        