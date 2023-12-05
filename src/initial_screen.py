import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button
from volume import Volume
from high_scores import HighScores
from controls import Controls
from level_1 import Level1



class InitialScreen(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path)  

        self.name_bottom = Button([self.all_sprites,self.buttons_group],"POKE-SECONDS!",None,45,RED,YELLOW,WIDTH/2,20,screen=self.screen)
        self.start_botton = Button([self.all_sprites,self.buttons_group],"Start ",None,40,YELLOW,BLACK,WIDTH-100,100,screen=self.screen)
        self.scores = Button([self.all_sprites,self.buttons_group],"Scores",None,40,YELLOW,BLACK,WIDTH-100,200,screen=self.screen)
        self.controls = Button([self.all_sprites,self.buttons_group],"Controls",None,40,YELLOW,BLACK,100,100,screen=self.screen)
        self.volume_botton = Button([self.all_sprites,self.buttons_group],"Sounds",None,40,YELLOW,BLACK,100,200,screen=self.screen)
        
    
    def button_logic(self):   
        if self.start_botton.pressed_button():
            self.screen_seen = Level1(sprite_groups=[self.all_sprites,self.level_1_group],music_path=LEVEL_SOUND,volume_float=VOLUME,background_path=LEVEL_1)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
            self.kill()
        elif self.scores.pressed_button():
            self.screen_seen = HighScores(sprite_groups=[self.all_sprites,self.scores_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=FINISH_GAME_IMAGE,json_path=SCORES_JSON,order_manage=ORDER_MANAGE)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
            self.kill()
        elif self.controls.pressed_button():
            self.screen_seen = Controls(sprite_groups=[self.all_sprites,self.controls_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
            self.kill()
        elif self.volume_botton.pressed_button():
            self.screen_seen = Volume(sprite_groups=[self.all_sprites, self.volume_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
            self.kill()    
        
    def update(self):
        super().update()
        self.button_logic()