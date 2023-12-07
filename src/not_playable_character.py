import pygame
from constants import *
from character import Character

class NPC(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y, power_jump, movement):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y, power_jump)
        self.rock = False
        self.movement_direction = "left"
        self.movement = movement
        self.correction_of_directory_moves_left_right()

    def left_right_moves(self):
        if self.movement:
            if self.rect.left <= 0:
                self.movement_direction = "right"
                self.movement_image = self.dictionary_surfaces["right"]
            elif self.rect.right >= WIDTH:
                self.movement_direction = "left"
                self.movement_image = self.dictionary_surfaces["left"]

            self.rect.left += SPEED_ENEMY if self.movement_direction == "right" else -SPEED_ENEMY
            
    def player_collide_enemy(player,group):
        collisions = pygame.sprite.spritecollide(player, group,dokill=False)
        if collisions and player.damage_flag:        
            player.life -= 1
            player.damage_flag = False
        elif not collisions and not player.damage_flag: 
            player.damage_flag = True

    def update(self):
        super().update()
        self.left_right_moves()
        
