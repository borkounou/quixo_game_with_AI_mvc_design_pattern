from abc import ABCMeta, abstractmethod
import pygame 
from constants import IMAGES,HEIGHT, WIDTH,IMAGE_SIZE,DIMENSION,SQ_SIZE,BG_COLOR

class IScreen(metaclass=ABCMeta):

    @abstractmethod
    def draw_screen(self,*args, **kwargs):
        """Implements different screens to display"""


        

    



