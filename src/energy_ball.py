import pygame
from constants import *

class EnergyBall(pygame.sprite.Spryte):
    def __init__(self, image_surface : pygame.surface,character_size : tuple, direction : str, 
    speed_ball : int, center_x : int, center_y : int):
        super.__init__()
        self.image = pygame.transform.scale(image_surface,character_size)
        self.rect_image = self.image.get_rect(center = (center_x,center_y))
        self.direction = direction
        self.speed_ball = speed_ball

    