import pygame
from constants import *
from character import Character
from energy_ball import EnergyBall


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

        
    def attack(self,keys):
        if self.rocks["tunder"] or self.rocks["water"] or self.rocks["leaf"] or self.rocks["fire"]:
            if keys[pygame.K_SPACE]:
                x,y = self.rect.center
                if self.direction_attack == "left":
                    self.energy_ball = EnergyBall(sprite_groups=[self.all_sprites,self.energy_ball_group],image_surface=pygame.image.load(SHOOT_IMAGE),energy_size=(50,50),center_x=x-40,center_y=y,speed=-ATTACK_SPEED,direction=self.direction_attack,power_rocks=self.rocks)
                if self.direction_attack == "right":
                    self.energy_ball = EnergyBall(sprite_groups=[self.all_sprites,self.energy_ball_group],image_surface=pygame.image.load(SHOOT_IMAGE),energy_size=(50,50),center_x=x+40,center_y=y,speed=ATTACK_SPEED,direction=self.direction_attack,power_rocks=self.rocks)
                self.movement_image = self.dictionary_surfaces["attack"]
                self.generate_sound(SHOOT_SOUND, VOLUME)
                self.rocks["tunder"] = False
                self.rocks["water"] = False
                self.rocks["leaf"] = False
                self.rocks["fire"] = False

    def loose_penalty(self):
       if self.life <= 0:
            return True
             
            
    def update(self) -> None:
        super().update()
        self.falling()
        keys = pygame.key.get_pressed()
        self.movements(keys)
        self.attack(keys)
       
    