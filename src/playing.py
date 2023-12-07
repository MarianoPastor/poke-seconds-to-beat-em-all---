import pygame
from constants import *
from initial_screen import InitialScreen
from name import Name

class Playing:
    def __init__(self):
        pygame.init()

        self.all_sprites_group = pygame.sprite.Group()
        self.background_group = pygame.sprite.Group()
        self.mouse_group = pygame.sprite.Group()
        self.rocks_group = pygame.sprite.Group()
        self.level_1_group = pygame.sprite.Group()
        self.level_2_group = pygame.sprite.Group()
        self.level_3_group = pygame.sprite.Group()     
        self.berry_group = pygame.sprite.Group()  
        self.enemy_groups = pygame.sprite.Group() 
        self.platforms_group = pygame.sprite.Group()  
        self.energy_ball_group = pygame.sprite.Group() 
        self.background_sprite = pygame.sprite.Sprite()
        
        pygame.display.set_caption("Poke-Seconds Beat em up!!!.")
        pygame.display.set_icon(pygame.image.load(POKEBALL_IMAGE))
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        self.player_dict = {}
        self.player_dict["name"] = Name(self.screen).name_input()
        self.initial_screen = InitialScreen(sprite_groups=[self.all_sprites_group], music_path=PRESENTATION_SOUND, volume_float=VOLUME, background_path=INTRO_BK,screen = self.screen)
        print(self.player_dict)
