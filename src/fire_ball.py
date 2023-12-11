import pygame
from constants import *

class FireBall(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, image_surface, energy_size, center_x, center_y, speed,screen,player):
        super().__init__(sprite_groups)
        self.player = player
        self.screen = screen
        self.energy_size = energy_size
        self.speed = speed
        self.image = image_surface
        self.image = pygame.transform.scale(self.image, self.energy_size)
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.mask = pygame.mask.from_surface(self.image)
    

    def movement(self):
        self.rect.centery += self.speed
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.kill()
    
    def fireball_colide_player(self):
        if pygame.sprite.collide_mask(self,self.player):
            self.player.life -= 1
            self.kill()
            
       
    def update(self):
        super().update()
        self.movement()
        self.fireball_colide_player()

    