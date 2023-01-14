from .screen import IScreen
import pygame 
from constants import HEIGHT, WIDTH,IMAGE_SIZE,SQ_SIZE,IMAGES

class WelcomeScreen(IScreen):
    def __init__(self):
        super().__init__()
        self.__cross_img = IMAGES["cross"]
        self.__circle_img = IMAGES["circle"]


    def draw_screen(self,screen):

        # Title text screen 
        font = pygame.font.SysFont("Arial", 50)
        title = font.render("Welcome to the QUIXO",1,pygame.Color("White"))
        title_rect = title.get_rect(center=(400,200))

        # Text for instruction
        font_player = pygame.font.SysFont("Arial",20)
        player_text = font_player.render("Choose the player X as human player",1,pygame.Color("white"))
        player_rect = player_text.get_rect(center=(400,250))

        # Draw a black circle
        pygame.draw.circle(screen, "Black", [WIDTH/2, HEIGHT/2], HEIGHT/2-20)
        # Image positions
        cross_rect = self.__cross_img.get_rect(topleft=(SQ_SIZE + 1*IMAGE_SIZE,SQ_SIZE + 2*IMAGE_SIZE))
        screen.blit(self.__cross_img,cross_rect) 
        circle_rect = self.__circle_img.get_rect(topleft=(SQ_SIZE + 3*IMAGE_SIZE, SQ_SIZE + 2*IMAGE_SIZE))
        screen.blit(title,title_rect)
        screen.blit(player_text,player_rect)
        screen.blit(self.__circle_img,circle_rect) 

    

        