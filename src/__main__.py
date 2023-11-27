import pygame
from pygame.locals import *
from constants import *
import playing

if "__main__.py":
    game = playing.Playing(LEVEL_1,LEVEL_SOUND,VOLUME,SCREEN_TUPLE)
    players_group = pygame.sprite.Group
game.run_game()