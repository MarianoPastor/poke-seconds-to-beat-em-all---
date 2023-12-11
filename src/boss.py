import pygame
from constants import *
from character import Character
from random import randint

class Boss(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y,power_jump):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y,power_jump)
        self.inverse_gravity= False
        self.movement_direction = "left"
        self.inmortality = True
        self.count = randint(1,3)
        self.correction_of_directory_moves_left_right()


    def movement(self):
        if self.rect.left <= WIDTH / 2:
            self.movement_direction = "right"
            self.movement_image = self.dictionary_surfaces["right"]
            self.count - 1
        elif self.rect.right >= WIDTH:
            self.movement_direction = "left"
            self.movement_image = self.dictionary_surfaces["left"]
        if self.count <= 0:
            self.inverse_gravity != self.inverse_gravity
            self.count = randint(1,3)

        if self.movement_direction == "right":
            self.rect.left += self.speed
        if self.movement_direction == "left":
            self.rect.left -= self.speed
        self.inmortality = False if self.movement_direction == "right" else True

    def boss_collide_player(self,player):
        if pygame.sprite.collide_mask(self, player):
            if player.damage_flag:        
                player.life -= 1
                player.damage_flag = False
        else:
            player.damage_flag = True
        
    def update(self) -> None:
        super().update()
        self.movement()
