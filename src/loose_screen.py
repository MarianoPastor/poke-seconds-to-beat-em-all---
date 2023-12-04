import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button



class Loose_screen(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path)  

        self.back = Button([self.all_sprites,self.buttons_group],"Back",None,40,YELLOW,None,100,50,screen=self.screen)
        self.losser = Button([self.all_sprites,self.buttons_group],"YOU LOOSE",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
        
    def button_logic(self):
        if self.back.pressed_button():
            self.playing = False

    def update(self):
        super().update()
        self.button_logic()
