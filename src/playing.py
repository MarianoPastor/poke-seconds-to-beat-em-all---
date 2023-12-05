import pygame
import pygame
from initial_screen import InitialScreen
from constants import *

class Playing:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Poke-Seconds Beat em up!!!.")
        pygame.display.set_icon(pygame.image.load(POKEBALL_IMAGE))
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        self.clock = pygame.time.Clock()
        self.time_play_1 = 1000
        self.time_play_2 = 1000
        self.time_play_3 = 1000
        self.total_time = self.time_play_1 + self.time_play_2 + self.time_play_3
        self.all_sprites = pygame.sprite.Group()
        self.screen_load = InitialScreen(sprite_groups=[self.all_sprites], music_path=PRESENTATION_SOUND, volume_float=VOLUME, background_path=INTRO_BK)

    def exit(self):
        pygame.quit()
        quit()

    def run_game(self):
        self.screen_load.playing = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

            self.screen_load.run_game()

            self.clock.tick(FPS)
            pygame.display.flip()