import pygame
from constants import *

class EnergyBall(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, image_surface, energy_size, center_x, center_y, speed, direction,screen,fire_rock,leaf_rock,water_rock,tunder_rock):
        super().__init__(sprite_groups)
        self.fire_rock = fire_rock
        self.water_rock = water_rock
        self.leaf_rock = leaf_rock
        self.tunder_rock = tunder_rock
        self.screen = screen
        self.energy_size = energy_size
        self.speed = speed
        self.direccion = direction
        self.image = image_surface
        self.image = pygame.transform.scale(self.image, self.energy_size)
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.mask = pygame.mask.from_surface(self.image)
        

    def movement(self):
        if self.direccion == "left":
            self.rect.centerx -= self.speed
        elif self.direccion == "right":
            self.rect.centerx += self.speed
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.kill()


    def draw(self): 
        self.draw(self.screen)
       
    def update(self):
        super().update()
        self.movement()