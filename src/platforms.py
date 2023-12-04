import pygame
from constants import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, rect_surface : pygame.Rect , color : tuple, movement: str="stay") -> None:
        super().__init__(groups)
        self.movement = movement.upper()
        self.image = pygame.Surface((rect_surface[2], rect_surface[3]))
        self.rect = self.image.get_rect(center = (rect_surface[0],rect_surface[1]))
        self.mask_image = pygame.mask.from_surface(self.image)
        self.image.fill(color)
        self.moving_now = "stay"

    def left_right_moves(self)->None:
        if self.movement == "WIDTH": 
                if self.rect.left <= 0:
                    self.moving_now = "right"
                elif  self.rect.right >= WIDTH:
                    self.moving_now = "left"
                self.rect.left += PLATFORM_SPEED if self.moving_now == "right" else - PLATFORM_SPEED
        elif self.movement == "HEIGHT": 
                if self.rect.top <= 0:
                    self.moving_now = "down"
                if  self.rect.bottom >= HEIGHT-50:
                    self.moving_now = "up"
                self.rect.top += PLATFORM_SPEED if self.moving_now == "down" else - PLATFORM_SPEED
        else:
            pass

    def update(self) -> None:
        self.left_right_moves()
        