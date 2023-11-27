import pygame
from pygame.sprite import _Group
from constants import *

class Platforms(pygame.sprite.Sprite):
    def __init__(self, groups: _Group, rect_surface : pygame.Rect) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((rect_surface[2], rect_surface[3]))
        self.rect = self.image.get_rect(topleft = (rect_surface[0],rect_surface[1]))
        self.image.fill(BLACK)