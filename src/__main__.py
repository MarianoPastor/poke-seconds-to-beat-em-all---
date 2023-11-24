import pygame
from pygame.locals import *
from constants import *
from utils import *
import playing

if "__main__.py":
    game = playing.Playing(LEVEL_1,PRESENTATION_SOUND,VOLUME)
    players_group = pygame.sprite.Group
    game.run_game()
