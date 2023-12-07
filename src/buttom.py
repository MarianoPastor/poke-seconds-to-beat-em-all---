import pygame
from constants import *

class Button(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, text_for_blit, font, size_text, color_text, back_color, x, y,screen) -> None:
        super().__init__(sprite_groups)
        self.screen = screen
        self.font_load = pygame.font.Font(font, size_text)
        self.image = self.font_load.render(text_for_blit, True, color_text, back_color)
        self.rect = self.image.get_rect(center=(x, y))
        self.all_sprites_group = pygame.sprite.Group()
        

    def pressed_button(self):
        mouse_position = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()  
        if self.rect.collidepoint(mouse_position):
            if mouse_click[0]== True:
                return True
    
    def life_see(self,player_lifes):
        Button([self.all_sprites_group],f"Lifes: {player_lifes} ",None,30,PURPLE,YELLOW,WIDTH/2-100,HEIGHT-50,screen=self.screen)
    
    def time_see(self,time):
        Button([self.all_sprites_group],f"Time: {time} ",None,30,PURPLE,YELLOW,WIDTH/2+100,HEIGHT-50,screen=self.screen)   
