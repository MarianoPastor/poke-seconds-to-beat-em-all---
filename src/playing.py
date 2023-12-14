import pygame
from constants import *
from initial_screen import InitialScreen
from name import Name
import high_scores


class Playing:
    def __init__(self):
        pygame.init()

        self.all_sprites_group = pygame.sprite.Group()
        
        pygame.display.set_caption("Poke-Seconds Beat em up!!!.")
        pygame.display.set_icon(pygame.image.load(POKEBALL_IMAGE))
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        self.player_dict = {"total_time":3.00,"level_1_time":1.00,"level_2_time":1.00,"level_3_time": 1.00,"name":"xxx","total_lifes":4},{"level_flag_2" : True,"level_flag_3": True}
        self.name_input = Name(self.screen).name_input()
        self.player_dict[0]["name"] = self.name_input
        high_scores.HighScores.json_dump(json_path=DATA_PLAYER_JSON,data=self.player_dict)
        self.initial_screen = InitialScreen(sprite_groups=[self.all_sprites_group], music_path=PRESENTATION_SOUND, volume_float=VOLUME, background_path=INTRO_BK,screen = self.screen,data_player_score= self.player_dict)
