import pygame, random
from constants import *
from character import Character

class NPC(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y,power_jump,movement):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y,power_jump)
        self.rock = False
        self.movement_direction = "left"
        self.movement = movement
        self.correction_of_directory_moves_left_right()
        
    def random_number(self,numero_minimo:int=0,numero_maximo:int=20)->int:
        return random.randint(numero_minimo,numero_maximo)


    def attack(self):
        keys = pygame.event.get()
        if self.rock:
            if keys[pygame.K_SPACE]:
                if keys[pygame.K_LEFT]:
                    pass
                if keys[pygame.K_RIGHT]:
                    pass  
                self.generate_sound(SHOOT_SOUND,VOLUME)
                self.rock = False


    def left_right_moves(self)->None:
        if self.movement: 
            if self.rect.left <= 0:
                self.movement_direction = "right"
            elif  self.rect.right >= WIDTH:
                self.movement_direction = "left"

            if self.movement_image == self.dictionary_surfaces["right"]:
                self.movement_image = self.dictionary_surfaces["right"]
            if self.movement_image == self.dictionary_surfaces["left"]:
                self.movement_image = self.dictionary_surfaces["left"]
            self.rect.left += SPEED_ENEMY if self.movement_direction == "right" else - SPEED_ENEMY
            self.move_change()
            
    def draw(self):
        self.attack()
        self.left_right_moves()
        
    def update(self) -> None:
        pygame.display.flip()