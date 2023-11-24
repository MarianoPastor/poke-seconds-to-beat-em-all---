import pygame
from constants import *
from utils import *

class Character(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, character_size, center_x, center_y):
        super().__init__(sprite_groups)
        self.image = pygame.transform.scale(image_surface,character_size)
        self.rect = self.image.get_rect(center = (center_x,center_y))
        self.mask_image = pygame.mask.from_surface(self.image)
        self.life = life
        self.speed = speed
        self.attack_damage = sound_attack
        self.sound_damage = sound_damage
        self.sound_life = sound_life_gain

    def damaged(self):
        generate_sound(DAMAGE_SOUND,VOLUME)
     