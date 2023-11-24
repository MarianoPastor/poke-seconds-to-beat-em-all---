import pygame
from constants import *
from utils import *
from character import Character

class NPC(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y, power_jump):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y)
        self.rock = False
        self.gravity= True
        self.power_jump = power_jump

    def update(self):
        keys = pygame.key.get_pressed()
        self.attack(keys)
        

    def attack(self,keys):
        if self.rock:
            if keys[pygame.K_SPACE]:
                if keys[pygame.K_LEFT]:
                    pass
                if keys[pygame.K_RIGHT]:
                    pass  
                generate_sound(SHOOT_SOUND,VOLUME)
                self.rock = False

