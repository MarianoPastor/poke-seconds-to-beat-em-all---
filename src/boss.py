import pygame
from constants import *
from character import Character
from random import randint

class Boss(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y,power_jump,energy_ball_direccion):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y,power_jump)
        self.energy_ball_attack = False
        self.energy_ball_direccion = energy_ball_direccion
        self.inverse_gravity= False
        self.movement_direction = "left"
        self.event_time_invertion = False
        self.inmortality = True
        self.count = randint(2,5)
        self.correction_of_directory_moves_left_right()
        

    def update(self):
        super().update()
        self.center_move_attack()


    def center_move_attack(self)->None:
            if self.rect.left <= WIDTH/2:
                self.movement_direction = "right"
                self.movement_image = self.dictionary_surfaces["right"]
            elif  self.rect.right >= WIDTH:
                self.movement_direction = "left"
                self.movement_image = self.dictionary_surfaces["left"]
            self.rect.left += self.speed if self.movement_direction == "right" else - self.speed  
            if self.rect.left == WIDTH/2:
                self.inverse_gravity= True
                self.count -= 1
            if self.count == 0:
                self.inverse_gravity= False
                self.count = randint(2,5)
            
    
            
            
                 


            