import pygame
from constants import *
from initial_screen import InitialScreen
from name import Name

class Playing:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Poke-Seconds Beat em up!!!.")
        pygame.display.set_icon(pygame.image.load(POKEBALL_IMAGE))
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        self.player_dict = {}
        self.player_name = Name(self.screen).name_input()
        self.player_dict["name"]: self.player_name
        self.all_sprites_group = pygame.sprite.Group()
        self.initial_screen = InitialScreen(sprite_groups=[self.all_sprites_group], music_path=PRESENTATION_SOUND, volume_float=VOLUME, background_path=INTRO_BK,screen = self.screen)
