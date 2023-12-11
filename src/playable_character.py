import pygame
from constants import *
from character import Character
from volume import Volume


class PlayableCharacter(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y, power_jump,tunder_rock,leaf_rock,water_rock,fire_rock):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y,power_jump)
        self.tunder_rock = tunder_rock
        self.water_rock = water_rock
        self.leaf_rock = leaf_rock
        self.fire_rock = fire_rock
        self.correction_of_directory_moves_r_l_a_i()
        

    def movements(self,keys) -> None:
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.left -= self.speed
            if not self.movement_image == self.dictionary_surfaces["left"]:
                self.movement_image = self.dictionary_surfaces["left"]
                self.frame = 0
            if keys[pygame.K_UP] and not self.jumping and self.rect.top >= 0:
                self.rect.y -= self.power_jump
                self.jumping = True
        elif keys[pygame.K_RIGHT]and self.rect.right <= WIDTH:
            self.rect.right += self.speed
            if not self.movement_image == self.dictionary_surfaces["right"]:
                self.movement_image = self.dictionary_surfaces["right"]
                self.frame = 0
            if keys[pygame.K_UP] and not self.jumping and self.rect.top >= 0:
                self.rect.y -= self.power_jump
                self.jumping = True
        elif keys[pygame.K_UP] and not self.jumping and self.rect.top >= 0:
            self.rect.y -= self.power_jump
            self.jumping = True
        else:
            self.gravity = True
            self.movement_image = self.dictionary_surfaces["idle"]
        

    def attack(self, keys):
        if self.tunder_rock or self.water_rock or self.fire_rock or self.leaf_rock:
            if keys[pygame.K_a]:
                self.energy_ball_flag = True
                Volume.sound_fx(SHOOT_SOUND, fx_volume_variable)
                self.direction_attack = "left"
                self.movement_image = self.dictionary_surfaces["attack"]
                self.tunder_rock = False
                self.water_rock = False
                self.leaf_rock = False
                self.fire_rock = False
            elif keys[pygame.K_d]:
                self.energy_ball_flag = True
                Volume.sound_fx(SHOOT_SOUND, fx_volume_variable)
                self.direction_attack = "right"
                self.movement_image = self.dictionary_surfaces["attack"]
                self.tunder_rock = False
                self.water_rock = False
                self.leaf_rock = False
                self.fire_rock = False
               
            
    def update(self) -> None:
        keys = pygame.key.get_pressed()
        super().update()
        self.falling()
        self.movements(keys)
        self.attack(keys)