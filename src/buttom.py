import pygame
from constants import *


class Button(pygame.sprite.Sprite):
    def __init__(self,sprite_groups, text_for_blit, font, size_text, color_text, back_color , x, y) -> None:
        super().__init__(sprite_groups)
        self.font_load = pygame.font.Font(font,size_text)
        self.image = self.font_load.render(text_for_blit,True,color_text,back_color)
        self.rect = self.image.get_rect(center = (x,y))
        self.all_sprites = pygame.sprite.Group()
        self.buttoms_group = pygame.sprite.Group()
    


