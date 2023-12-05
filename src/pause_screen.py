import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button
from high_scores import HighScores
from controls import Controls
from volume import Volume




class PauseScreen(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path)  

        self.back = Button([self.all_sprites,self.buttons_group],"Back ",None,40,YELLOW,None,WIDTH-100,20,screen=self.screen)
        self.scores = Button([self.all_sprites,self.buttons_group],"Scores",None,40,YELLOW,None,WIDTH-100,50,screen=self.screen)
        self.volume_botton = Button([self.all_sprites,self.buttons_group],"Sounds",None,40,YELLOW,None,100,50,screen=self.screen)
        self.controls = Button([self.all_sprites,self.buttons_group],"CONTROLS",None,40,RED,WHITE,WIDTH/2,40,screen=self.screen)

        self.name = Button([self.all_sprites,self.buttons_group],"PAUSE",None,80,BLACK,WHITE,WIDTH/2,HEIGHT/2,screen=self.screen)
        
    def button_logic(self):
        if self.back.pressed_button():
            self.playing = False
            self.kill()
        elif self.scores.pressed_button():
            self.screen_seen = HighScores(sprite_groups=[self.all_sprites],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=FINISH_GAME_IMAGE,json_path=SCORES_JSON,order_manage=ORDER_MANAGE)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
            self.kill()
        elif self.controls.pressed_button():
            self.screen_seen = Controls(sprite_groups=[self.all_sprites],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
            self.kill()
        elif self.volume_botton.pressed_button():
            self.screen_seen = Volume(sprite_groups=[self.all_sprites],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
            self.kill()
            
    
    def update(self):
        super().update()
        self.button_logic()
    