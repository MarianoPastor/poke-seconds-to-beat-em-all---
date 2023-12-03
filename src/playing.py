import pygame
from initial_screen import InitialScreen
from level_1 import Level1
from level_2 import Level2
from level_3 import Level3
from high_scores import HighScores
from pause_screen import PauseScreen
from constants import *

class Playing():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Poke-Seconds Beat em up!!!.")
        pygame.display.set_icon(pygame.image.load(POKEBALL_IMAGE))
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)

        self.all_sprites = pygame.sprite.Group()
        self.platforms_groups = pygame.sprite.Group()
        self.enemy_groups = pygame.sprite.Group()
        self.energy_ball_groups = pygame.sprite.Group()
        self.buttons_group = pygame.sprite.Group()
       

        self.actual_window = "level_3"
        self.screen_load = self.screen_creator()
        
    # def button_collide(self):
    #     if self.start.rect.collidepoint(self.mouse_position):
    #         playing.Playing.actual_window = "level_1"
    #     elif self.scores.rect.collidepoint(self.mouse_position):
    #         playing.Playing.actual_window = "top_scores"
    #     elif self.controls.rect.collidepoint(self.mouse_position):
    #         playing.Playing.actual_window = "controls"
    #     elif self.start.rect.collidepoint(self.mouse_position):
    #         playing.Playing.actual_window = "sounds"
    

    def screen_creator(self):
            match self.actual_window:
                case "initial_screen":
                    load = InitialScreen(sprite_groups=[self.all_sprites],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=INTRO_BK)
                    
                case "level_1":
                    load = Level1(sprite_groups=[self.all_sprites],music_path=LEVEL_SOUND,volume_float=VOLUME,background_path=LEVEL_1)
                    
                case "level_2":
                    load = Level2(sprite_groups=[self.all_sprites],music_path=LEVEL_SOUND,volume_float=VOLUME,background_path=LEVEL_2)
                    
                case "level_3":
                    load = Level3(sprite_groups=[self.all_sprites],music_path=LEVEL_SOUND,volume_float=VOLUME,background_path=LEVEL_3)
                    
                case "high_scores":
                    load = HighScores(sprite_groups=[self.all_sprites],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=INTRO_BK)
                   
                case "pause_screen":
                    load = PauseScreen(TOASTY_SOUND,VOLUME,INTRO_BK)
                    
            return load
        
    
    def iniciate(self):
       while True:
        self.screen_load
        self.screen_load.playing = True
        self.screen_load.run_game()