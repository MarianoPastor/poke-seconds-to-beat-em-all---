import pygame
from constants import *
from character import Character

class NPC(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y)
        self.rock = False
        self.gravity= True
        self.movement_direction = "left"
        

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
                self.generate_sound(SHOOT_SOUND,VOLUME)
                self.rock = False

# def left_right_moves(self)->None:
#     if self.rect.left <= 0:
#         self.movement_direction = "left"
#     elif  self.rect.right >= WIDTH:
#         self.movement_direction = "left"

#     if self.movement_direction == "right":
#         self.rect.left += SPEED_ENEMY
#     elif self.movement_direction == "left":
#         self.rect.left -= SPEED_ENEMY