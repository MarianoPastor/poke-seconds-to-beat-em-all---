import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button


class Volume(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path)     
        self.volume_flag = True
        self.back = Button([self.all_sprites,self.buttons_group],"back",None,40,YELLOW,None,WIDTH-100,50,screen=self.screen)
        
        self.volume_off_on = Button([self.all_sprites,self.buttons_group],"Set volume off - on",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.volume_up = Button([self.all_sprites,self.buttons_group],"Set volume up",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
        self.volume_down = Button([self.all_sprites,self.buttons_group],"Set volume down",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+200,screen=self.screen)

    def button_logic(self):
        if self.back.pressed_button():
            self.playing = False
        elif self.volume_off_on.pressed_button():
            self.volume_flag != self.volume_flag
            if self.volume_flag:
                self.volume_float = VOLUME
            elif not self.volume_flag:
                self.volume_float -= self.volume_float
        elif self.volume_up.pressed_button():
            self.volume_float += 0.1
        elif self.volume_down.pressed_button():
            self.volume_float -= 0.1

    def update(self):
        super().update()
        self.button_logic()
    
    
        
        