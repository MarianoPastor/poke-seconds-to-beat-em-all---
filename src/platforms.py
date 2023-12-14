import pygame
from constants import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, image_surface : pygame.surface , size : tuple,center_x,center_y, movement: str="stay") -> None:
        super().__init__(groups)
        self.movement = movement.lower()
        self.image = image_surface
        self.size = size
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = self.image.get_rect(center = (center_x,center_y))
        self.mask = pygame.mask.from_surface(self.image)
        self.moving_now = "stay"


    def platform_height_or_width_moves(self)->None:
        if self.movement == "width": 
                if self.rect.left <= 0:
                    self.moving_now = "right"
                elif  self.rect.right >= WIDTH:
                    self.moving_now = "left"
                self.rect.left += PLATFORM_SPEED if self.moving_now == "right" else - PLATFORM_SPEED
        elif self.movement == "height": 
                if self.rect.top <= 0:
                    self.moving_now = "down"
                if  self.rect.bottom >= HEIGHT-50:
                    self.moving_now = "up"
                self.rect.top += PLATFORM_SPEED if self.moving_now == "down" else - PLATFORM_SPEED
        else:
            self.moving_now = "stay"

    def platform_logic(player,group):
        collition = pygame.sprite.spritecollide(player,group,dokill=False)
        
        if len(list(collition)) > 0:
                player.jumping = False
                player.rect.bottom = collition[0].rect.top
                player.rect.top = collition[0].rect.top - player.rect.height 
                
        else:
            player.falling()

    def update(self) -> None:
        self.platform_height_or_width_moves()