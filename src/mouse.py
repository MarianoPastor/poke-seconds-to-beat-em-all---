import pygame
from constants import *

class Mouse(pygame.sprite.Sprite):
    def __init__(self,sprite_groups, image_surface, mouse_size):
        super().__init__(sprite_groups)
        
        self.mouse_size = mouse_size
        self.image = image_surface
        self.image = pygame.transform.scale(self.image,self.mouse_size)
        self.rect = self.image.get_rect(center = pygame.mouse.get_pos())
        self.mask_image = pygame.mask.from_surface(self.image)
        self.mouse_group = pygame.sprite.Group()
        pygame.mouse.set_visible(False)
        mouse_sprite = pygame.sprite.Sprite()
        mouse_sprite.image = self.image
        mouse_sprite.rect = self.rect
        self.mouse_group.add(mouse_sprite)

    def update(self) -> None:
        self.rect.center = pygame.mouse.get_pos()