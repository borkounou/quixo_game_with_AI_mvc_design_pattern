
from .screen import IScreen
import pygame
from constants import IMAGES,HEIGHT, WIDTH,IMAGE_SIZE,DIMENSION,SQ_SIZE
class MainScreen(IScreen):
    def __init__(self):
        super().__init__()
        self.__blank_img = IMAGES["blank"]
        self.__cross_img = IMAGES["cross"]
        self.circle_img = IMAGES["circle"]
    
    def draw_screen(self,screen, board,win=False):
        pygame.draw.circle(screen, "Black", [WIDTH/2, HEIGHT/2], HEIGHT/2-20)
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                X = SQ_SIZE + col*IMAGE_SIZE
                Y = SQ_SIZE + row*IMAGE_SIZE


                if board[row][col]==0:
                    blank_rect = self.__blank_img.get_rect(topleft=(X,Y))
                    screen.blit(self.__blank_img,blank_rect) 
                   
                if board[row][col] ==1:
                    cross_rect = self.__cross_img.get_rect(topleft=(X,Y))
                    screen.blit(self.__cross_img,cross_rect) 

                if board[row][col]==-1:
                    circle_rect = self.circle_img.get_rect(topleft=(X,Y))
                    screen.blit(self.circle_img,circle_rect) 
                   
