
import pygame 
import os
from constants import IMAGES,HEIGHT, WIDTH,IMAGE_SIZE,DIMENSION,SQ_SIZE,BG_COLOR
from .screen_factory import ScreenFactory


from .welcome_screen import WelcomeScreen
from .main_screen import MainScreen
import pygame 
from constants import HEIGHT, WIDTH, BG_COLOR
dir_path = os.path.dirname(os.path.realpath(__file__))
# open(dir_path + '/images/' + 'bg2.jpg')
class View:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.screen.fill(BG_COLOR)
        self.__bagckground_image = pygame.transform.scale(pygame.image.load('C:\\M2\\Software UE\\QUIXO_FINAL_MVC\\QUIXO-MASTER-GAME\\images\\bg2.jpg').convert(),(WIDTH,HEIGHT))
        self.bg_image_rect = self.__bagckground_image.get_rect(topleft=(0,0))
        self.screen.blit(self.__bagckground_image, self.bg_image_rect)

    @staticmethod
    def build_screen(screen_type):
        if screen_type =="welcome_screen":
            return WelcomeScreen()

        if screen_type == "main_screen":
            return  MainScreen()
        
        print("Invalid screen type")
        return None

# class View(ScreenFactory):

#     def __init__(self):
#         super().__init__()
#         self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
#         self.clock = pygame.time.Clock()
#         self.screen.fill(BG_COLOR)
#         self.__bagckground_image = pygame.transform.scale(pygame.image.load("images/bg2.jpg").convert(),(WIDTH,HEIGHT))
#         self.bg_image_rect = self.__bagckground_image.get_rect(topleft=(0,0))
#         self.screen.blit(self.__bagckground_image, self.bg_image_rect)








