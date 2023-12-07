import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button
from level_1 import Level1
from level_2 import Level2
from level_3 import Level3
from volume import Volume



class LevelSelection(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path,screen=screen)  

        
        self.back = Button([self.all_sprites_group],"Back",None,40,YELLOW,None,100,50,screen=self.screen)
        self.controls = Button([self.all_sprites_group],"Level Selection",None,40,RED,WHITE,WIDTH/2,40,screen=self.screen)

        self.level_1_choice = Button([self.all_sprites_group],"Level 1",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.level_2_choice = Button([self.all_sprites_group],"Level 2",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-100,screen=self.screen)
        self.level_3_choice = Button([self.all_sprites_group],"Level 3",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
       
        
    def button_logic(self):
        if self.back.pressed_button():
            self.active_bucle = False
            self.kill()
        elif self.level_1_choice.pressed_button():
            self.screen_level = Level1(sprite_groups=[self.all_sprites_group],music_path=LEVEL_SOUND,volume_float=VOLUME,background_path=LEVEL_1,screen=self.screen)
            self.screen_level.run_game()
            #self.kill()
        elif self.level_2_choice.pressed_button():
            if self.flag_level_2:
                self.screen_level = Level2(sprite_groups=[self.all_sprites_group],music_path=LEVEL_SOUND,volume_float=VOLUME,background_path=LEVEL_2,screen=self.screen)
                self.screen_level.run_game()
                #self.kill()
        elif self.level_3_choice.pressed_button():    
            if self.flag_level_3:
                self.screen_level = Level3(sprite_groups=[self.all_sprites_group],music_path=LEVEL_SOUND,volume_float=VOLUME,background_path=LEVEL_3,screen=self.screen)
                self.screen_level.run_game()
                #self.kill

    def update(self):
        super().update()
        self.button_logic()