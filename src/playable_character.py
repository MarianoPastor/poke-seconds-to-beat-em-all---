import pygame
from constants import *
from character import Character
from volume import Volume
import level_1


class PlayableCharacter(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y, power_jump):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y,power_jump)
        self.rocks = {"tunder" : False, "water" : False,"leaf" : False,"fire" : False}
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
        if self.rocks["tunder"] or self.rocks["water"] or self.rocks["leaf"] or self.rocks["fire"]:
            if keys[pygame.K_SPACE]:
                self.movement_image = self.dictionary_surfaces["attack"]
                Volume.sound_fx(SHOOT_SOUND, VOLUME)
                self.energy_ball_flag = True
                self.rocks["tunder"] = False
                self.rocks["water"] = False
                self.rocks["leaf"] = False
                self.rocks["fire"] = False
                level_1.Level1.generate_energy_ball(self)
                

    def loose_penalty(self):
       if self.life <= 0:
            return True
    
            
    def update(self) -> None:
        keys = pygame.key.get_pressed()
        super().update()
        self.falling()
        self.movements(keys)
        self.attack(keys)