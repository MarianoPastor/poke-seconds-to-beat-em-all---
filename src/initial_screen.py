from constants import *
from window_screen import WindowScreen
from buttom import Button
from volume import Volume
from high_scores import HighScores
from controls import Controls
from level_selection import LevelSelection
from volume import Volume



class InitialScreen(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen,data_player_score) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path, screen)  
        
        self.name_bottom = Button([self.all_sprites_group],"POKE-SECONDS!",None,45,RED,YELLOW,WIDTH/2,20,screen=self.screen)
        self.start_botton = Button([self.all_sprites_group],"Start ",None,40,YELLOW,BLACK,WIDTH-100,100,screen=self.screen)
        self.scores = Button([self.all_sprites_group],"Scores",None,40,YELLOW,BLACK,WIDTH-100,200,screen=self.screen)
        self.controls = Button([self.all_sprites_group],"Controls",None,40,YELLOW,BLACK,100,100,screen=self.screen)
        self.volume_botton = Button([self.all_sprites_group],"Sounds",None,40,YELLOW,BLACK,100,200,screen=self.screen)
        self.back_sound = Volume.load_music(self.music_path,self.volume_float)
        self.data_player_score = data_player_score
        
    def button_logic(self):   
        if self.start_botton.pressed_button():
            self.screen_seen = LevelSelection(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK,screen=self.screen)
            self.screen_seen.run_game()
        elif self.scores.pressed_button():
            self.screen_seen = HighScores(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=FINISH_GAME_IMAGE,json_path=SCORES_JSON,order_manage=ORDER_MANAGE,screen=self.screen)
            self.screen_seen.run_game()
        elif self.controls.pressed_button():
            self.screen_seen = Controls(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK,screen=self.screen)
            self.screen_seen.run_game()
        elif self.volume_botton.pressed_button():
            self.screen_seen = Volume(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK,screen=self.screen)
            self.screen_seen.run_game() 

    def update(self):
        super().update()
        self.button_logic()
        
    