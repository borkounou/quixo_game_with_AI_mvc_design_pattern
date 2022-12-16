import pygame 
import os 
WIDTH =800
HEIGHT =800

DIMENSION = 5

INDEX_LAST_ROW = DIMENSION -1 #
INDEX_LAST_COL = DIMENSION-1 #4


SQ_SIZE = WIDTH//DIMENSION # The size of square 160
IMAGE_SIZE = 100



# BG_COLOR =(189,148,118)
BG_COLOR =(0,46-0,63)

__dir_path = os.path.dirname(os.path.realpath(__file__))




IMAGES = {
    "blank":pygame.image.load(__dir_path + '/images/' + 'blank.png'),
    "cross": pygame.image.load(__dir_path + '/images/' + 'cross.png'),
    "circle":pygame.image.load(__dir_path + '/images/' + 'circle.png')
    }


PATH_BACKGROUND_IMAGE = "C:\\M2\\Software UE\\QUIXO_IA_FINAL\\QUIXO_IA_MASTER\\images\\bg2.jpg"




