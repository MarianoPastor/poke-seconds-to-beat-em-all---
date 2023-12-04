from typing import Any
import pygame
from constants import *

class Button(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, text_for_blit, font, size_text, color_text, back_color, x, y,screen) -> None:
        super().__init__(sprite_groups)
        self.screen = screen
        self.all_sprites = sprite_groups
        self.font_load = pygame.font.Font(font, size_text)
        self.image = self.font_load.render(text_for_blit, True, color_text, back_color)
        self.rect = self.image.get_rect(center=(x, y))
        self.all_sprites = pygame.sprite.Group()
        self.buttons_group = pygame.sprite.Group()
        

    def pressed_button(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()  
        if self.rect.collidepoint(mouse_position):
            if mouse_click[0]== True:
                return True
    
    def life_see(self,player_lifes):
        Button([self.all_sprites,self.buttons_group],f"Lifes: {player_lifes} ",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT-50,screen=self.screen)
    
    