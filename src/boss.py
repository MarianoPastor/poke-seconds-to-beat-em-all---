import pygame
from constants import *
from character import Character

class Boss(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y,movement,energy_ball_direccion):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y)
        self.energy_ball_attack = False
        self.energy_ball_direccion = energy_ball_direccion
        self.inverse_gravity= False
        self.movement_direction = "idle"
        self.movement = movement
        self.correction_of_directory_moves_left_right()
        

    def update(self):
        self.left_right_moves(self.movement)
        #self.attack(keys)
    

    def attack(self):
        if self.rock:
            if keys[pygame.K_SPACE]:
                if keys[pygame.K_LEFT]:
                    pass
                if keys[pygame.K_RIGHT]:
                    pass  
                self.generate_sound(SHOOT_SOUND,VOLUME)
                self.rock = False


    def left_right_moves(self,bool)->None:
        if bool: 
            if self.rect.left <= 0:
                self.movement_direction = "right"
            elif  self.rect.right >= WIDTH:
                self.movement_direction = "left"
            self.movement_image == self.dictionary_surfaces["right"] if self.movement_direction == "right" else self.dictionary_surfaces["left"]
            self.rect.left += SPEED_ENEMY if self.movement_direction == "right" else - SPEED_ENEMY

            