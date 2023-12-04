import pygame
from constants import *

class EnergyBall(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, image_surface, energy_size, center_x, center_y, speed, direction, power_rocks):
        super().__init__(sprite_groups)
        self.energy_size = energy_size
        self.speed = speed
        self.direccion = direction
        self.original_image = image_surface  # Guardar la imagen original
        self.image = pygame.transform.scale(self.original_image, self.energy_size)
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.rect.left += self.speed
        self.mask_image = pygame.mask.from_surface(self.image)
        self.time_update = pygame.time.get_ticks()
        self.time_frames = TIME_FRAME_CHANGE
        self.power = power_rocks

    def move_change(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time_update >= self.time_frames:
            self.image = pygame.transform.rotate(self.original_image, 45.00)
            self.time_update = time_now

    def movement(self):
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.kill()
        self.move_change()
    
    def update(self) -> None:
        self.movement()