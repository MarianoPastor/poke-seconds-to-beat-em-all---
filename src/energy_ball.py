import pygame
from constants import *

class EnergyBall(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, image_surface, energy_size, center_x, center_y, speed, direction,screen):
        super().__init__(sprite_groups)
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


    def energy_colide_grup(self,group):
        pygame.sprite.groupcollide(self, group,True,True)
    
    def energy_colide_player(self,character):
        pygame.sprite.collide_mask(self,character)

    def draw(self): 
        self.draw(self.screen)
       
    def update(self):
        super().update()
        self.movement()

   
    
    