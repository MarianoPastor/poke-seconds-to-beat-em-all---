import pygame
from constants import *


class Rock(pygame.sprite.Sprite):
    def __init__(self,sprite_groups, image_surface, rock_size, center_x, center_y):
        super().__init__(sprite_groups)
        self.rock_size = rock_size
        self.image = image_surface
        self.image = pygame.transform.scale(self.image,self.rock_size)
        self.rect = self.image.get_rect(center = (center_x,center_y))
        self.mask_image = pygame.mask.from_surface(self.image)
