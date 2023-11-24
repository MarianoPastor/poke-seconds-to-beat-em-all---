import pygame
from constants import *
from utils import *
from character import Character

class PlayableCharacter(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y, power_jump):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y)
        self.rock = False
        self.gravity= False
        self.power_jump = power_jump
        



    def update(self):
        keys = pygame.key.get_pressed()
        if self.gravity:
            self.rect.y -= 10
        elif self.rect.bottom == HEIGHT:
            self.gravity = False
        self.keys(keys)
        self.attack(keys)
        



    def keys(self,keys):
        if self.rect.left >= 0 and keys[pygame.K_LEFT] and \
            not keys[pygame.K_RIGHT] and \
            not keys[pygame.K_DOWN]:
            self.rect.left -= self.speed  
        elif self.rect.right <= WIDTH and \
            not keys[pygame.K_LEFT]  and \
            keys[pygame.K_RIGHT] and \
            not keys[pygame.K_DOWN]:
            self.rect.left += self.speed
        elif self.rect.top >= 0 and \
            keys[pygame.K_UP] and \
            not keys[pygame.K_DOWN]:
            self.rect.bottom -= self.power_jump
        elif self.rect.bottom <= WIDTH and \
            not keys[pygame.K_UP] and \
            keys[pygame.K_DOWN]:
            self.rect.bottom += self.speed
    



    def attack(self,keys):
        if self.rock:
            if keys[pygame.K_SPACE]:
                if keys[pygame.K_LEFT]:
                    pass
                if keys[pygame.K_RIGHT]:
                    pass  
                generate_sound(SHOOT_SOUND,VOLUME)
                self.rock = False
        



    def gravity_status(self):
            self.rect.y += 10 if self.gravity else 0

    
    
    
           
        




