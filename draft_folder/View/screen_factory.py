from .welcome_screen import WelcomeScreen
from .main_screen import MainScreen
import pygame 
from constants import HEIGHT, WIDTH, BG_COLOR

class ScreenFactory:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.screen.fill(BG_COLOR)
        self.__bagckground_image = pygame.transform.scale(pygame.image.load("images/bg2.jpg").convert(),(WIDTH,HEIGHT))
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






