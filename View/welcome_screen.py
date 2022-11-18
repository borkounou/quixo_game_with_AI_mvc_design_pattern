from .screen import IScreen
import pygame 
from constants import HEIGHT, WIDTH,IMAGE_SIZE,SQ_SIZE,IMAGES

class WelcomeScreen(IScreen):
    def __init__(self):
        super().__init__()
        self.__cross_img = IMAGES["cross"]
        self.__circle_img = IMAGES["circle"]


    def draw_screen(self,screen):

        # Text for the screen 
        font = pygame.font.SysFont("Arial", 50)
        restart_button = font.render("Welcome to the QUIXO",1,pygame.Color("White"))
        tex_rect = restart_button.get_rect(center=(400,200))

        # screen.blit(self.__bagckground_image, self.bg_image_rect)
        pygame.draw.circle(screen, "Black", [WIDTH/2, HEIGHT/2], HEIGHT/2-20)
        X = SQ_SIZE + 1*IMAGE_SIZE
        Y = SQ_SIZE + 2*IMAGE_SIZE
        cross_rect = self.__cross_img.get_rect(topleft=(X,Y))
        screen.blit(self.__cross_img,cross_rect) 
        X1 = SQ_SIZE + 3*IMAGE_SIZE
        Y2 = SQ_SIZE + 2*IMAGE_SIZE
        circle_rect = self.__circle_img.get_rect(topleft=(X1,Y2))
        screen.blit(restart_button,tex_rect)
        screen.blit(self.__circle_img,circle_rect) 

    
    # def font_style(self,screen, text, font,color="White",pos=(200,200)):
    #     font = pygame.font.SysFont("Arial", font)
    #     restart_button = font.render(text,1,pygame.Color(color))
    #     tex_rect = restart_button.get_rect(center=(pos))
    #     screen.blit(restart_button,tex_rect)

        