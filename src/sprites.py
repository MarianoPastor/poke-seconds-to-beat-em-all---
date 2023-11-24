import pygame
from pygame.locals import *

class Sprites:
    def __init__(self,image) -> None:
        self.image_sheet = image

    
    def image_load(sprite_sheet,frame, width, heigth,scale = 1):
        image = pygame.Surface((width * frame,heigth))
        image.blit(sprite_sheet.subsurface((0,0,width,heigth)),(0,0))
        image = pygame.transform.scale(image,(scale*width, scale * heigth))
        return image