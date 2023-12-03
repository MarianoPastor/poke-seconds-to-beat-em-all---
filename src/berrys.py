import pygame
from constants import *
from random import randint


class Berry(pygame.sprite.Sprite):
    def __init__(self,sprite_groups, image_surface, berry_size, center_x, center_y,screen):
        super().__init__(sprite_groups)
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.berry_size = berry_size
        self.gravity= True
        self.image = image_surface
        self.image = pygame.transform.scale(self.image,self.berry_size)
        self.rect = self.image.get_rect(center = (center_x,center_y))
        self.mask_image = pygame.mask.from_surface(self.image)
        self.life_giver =  randint(-1,1)


    def update(self) -> None:
        print("BUT UPDATE")
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        print("BUT DRAW")