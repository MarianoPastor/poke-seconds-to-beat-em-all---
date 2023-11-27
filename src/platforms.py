import pygame
from constants import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, rect_surface : pygame.Rect, color) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((rect_surface[2], rect_surface[3]))
        self.rect = self.image.get_rect(center = (rect_surface[0],rect_surface[1]))
        self.image.fill(color)