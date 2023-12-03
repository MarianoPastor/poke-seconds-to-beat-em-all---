import pygame
from constants import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, rect_surface : pygame.Rect , color : tuple, movement: str="stay") -> None:
        super().__init__(groups)
        self.movement = movement.upper()
        self.image = pygame.Surface((rect_surface[2], rect_surface[3]))
        self.rect = self.image.get_rect(center = (rect_surface[0],rect_surface[1]))
        self.image.fill(color)

    def left_right_moves(self)->None:
        if self.movement == "WIDTH": 
                if self.rect.left <= 0:
                    self_moving_now = "right"
                elif  self.rect.right >= WIDTH:
                    self_moving_now = "left"
                self.rect.left += PLATFORM_SPEED if self_moving_now == "right" else - PLATFORM_SPEED
        elif self.movement == "HEIGHT": 
                if self.rect.top <= 0:
                    self_moving_now = "down"
                elif  self.rect.right >= HEIGHT:
                    self_moving_now = "up"
                self.rect.bottom += PLATFORM_SPEED if self_moving_now == "right" else - PLATFORM_SPEED
        else:
            pass