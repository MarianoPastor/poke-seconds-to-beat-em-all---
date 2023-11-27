import pygame, playing
from constants import *
from character import Character

class PlayableCharacter(Character):
    def __init__(self, sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y, power_jump):
        super().__init__(sprite_groups, image_surface, life, speed, sound_attack, sound_damage, sound_life_gain, size, center_x, center_y)
        self.rocks = {"tunder" : False, "water" : False,"leaf" : False,"fire" : False}
        self.jumping = False
        self.gravity = True
        self.power_jump = power_jump
        self.correction_of_directory_moves_r_l_a_i()

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        self.movements(keys)
        self.falling()
        self.attack(keys)

    def movements(self, keys) -> None:
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
        self.move_change()
            
            

    def falling(self):
        if self.jumping:
            self.gravity = True
        if self.gravity and self.rect.bottom <= FLOOR_LEVEL:
            self.rect.bottom += FALL
        else:
            self.gravity = False
            self.jumping = False

    def attack(self, keys):
        if self.rocks["tunder"] or self.rocks["water"] or self.rocks["leaf"] or self.rocks["fire"]:
            if keys[pygame.K_SPACE]:
                if self.movement_image == "left":
                    pass
                if self.movement_image == "right":
                    pass
                self.movement_image = "attack"
                playing.generate_sound(SHOOT_SOUND, VOLUME)
                self.rocks["tunder"] = False
                self.rocks["water"] = False
                self.rocks["leaf"] = False
                self.rocks["fire"] = False

    