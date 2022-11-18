
import pygame 
from constants import IMAGES,HEIGHT, WIDTH,IMAGE_SIZE,DIMENSION,SQ_SIZE,BG_COLOR

class QuixoView:

    def __init__(self) :
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.screen.fill(BG_COLOR)
        self.__blank_img = IMAGES["blank"]
        self.__cross_img = IMAGES["cross"]
        self.circle_img = IMAGES["circle"]
        self.__bagckground_image = pygame.transform.scale(pygame.image.load("images/bg2.jpg").convert(),(WIDTH,HEIGHT))
        self.bg_image_rect = self.__bagckground_image.get_rect(topleft=(0,0))
        self.screen.blit(self.__bagckground_image, self.bg_image_rect)


    def draw_board(self,screen, board):

        # screen.blit(self.__bagckground_image, self.bg_image_rect)
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


    def blink_board_for_winner(self, screen):
        pass

    def opening_game(self,screen):
        screen.blit(self.__bagckground_image, self.bg_image_rect)
        pygame.draw.circle(screen, "Black", [WIDTH/2, HEIGHT/2], HEIGHT/2-20)
        X = SQ_SIZE + 1*IMAGE_SIZE
        Y = SQ_SIZE + 2*IMAGE_SIZE
        cross_rect = self.__cross_img.get_rect(topleft=(X,Y))
        screen.blit(self.__cross_img,cross_rect) 
        X1 = SQ_SIZE + 3*IMAGE_SIZE
        Y2 = SQ_SIZE + 2*IMAGE_SIZE
        circle_rect = self.circle_img.get_rect(topleft=(X1,Y2))
        screen.blit(self.circle_img,circle_rect) 

    
    def game_over(self, screen):
        screen.blit(self.__bagckground_image, self.bg_image_rect)
        pygame.draw.circle(screen, "Black", [WIDTH/2, HEIGHT/2], HEIGHT/2-20)

        self.font_style(screen, "Game over", 50, "White",(400,250))
        self.font_style(screen, "Restart",30,"Blue", (400,350))
        self.font_style(screen, "Restart",30,"Blue", (400,350))
        self.font_style(screen, "Exit",30,"Red", (400,450))

    def font_style(self,screen, text, font,color="White",pos=(200,200)):
        font = pygame.font.SysFont("Arial", font)
        restart_button = font.render(text,1,pygame.Color(color))
        tex_rect = restart_button.get_rect(center=(pos))
        screen.blit(restart_button,tex_rect)
        

    
    
       
       




    









