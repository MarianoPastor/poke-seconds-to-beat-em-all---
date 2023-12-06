import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button
from volume import Volume



class Controls(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path,screen)  

        
        self.back = Button([self.all_sprites_group],"Back",None,40,YELLOW,None,100,50,screen=self.screen)
        self.controls = Button([self.all_sprites_group],"CONTROLS",None,40,RED,WHITE,WIDTH/2,40,screen=self.screen)

        self.up_explain = Button([self.all_sprites_group,],"Key up ==> Jump",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.left_explain = Button([self.all_sprites_group],"Key left ==> Move left",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-100,screen=self.screen)
        self.right_explain = Button([self.all_sprites_group],"Key right ==> Move right",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
        self.espace_explain = Button([self.all_sprites_group],"Key espace ==> Attack",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+100,screen=self.screen)
        self.escape_explain = Button([self.all_sprites_group],"Key escape ==> Exit Game",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+200,screen=self.screen)
        Volume.load_music(self.music_path,self.volume_float)

    def button_logic(self):
        if self.back.pressed_button():
            self.active_bucle = False
            self.kill()

    def update(self):
        super().update()
        self.button_logic()
        
