import pygame
from constants import *
from random import randint


class Berry(pygame.sprite.Sprite):
    def __init__(self,sprite_groups, image_surface, berry_size, center_x, center_y):
        super().__init__(sprite_groups)
        self.berry_size = berry_size
        self.gravity= True
        self.image = image_surface
        self.image = pygame.transform.scale(self.image,self.berry_size)
        self.rect = self.image.get_rect(center = (center_x,center_y))
        self.mask_image = pygame.mask.from_surface(self.image)
        self.life_giver =  randint(-1,1)
        self.time_update = pygame.time.get_ticks()
        self.time_berry = randint(150,500)
        

    # def time_apear(self):
    #     time_now = pygame.time.get_ticks()
    #     berry_on = False
    #     if time_now - self.time_update >= self.time_berry:
    #         berry_on = True
    #         self.time_update = time_now
    #         return berry_on