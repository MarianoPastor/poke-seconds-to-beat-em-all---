import pygame
from constants import *

class Character(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, dictionary_surfaces, life, speed, sound_attack, sound_damage, sound_life_gain, character_size, center_x, center_y):
        super().__init__(sprite_groups)
        self.character_size = character_size
        self.dictionary_surfaces = dictionary_surfaces
        self.movement_image = self.dictionary_surfaces["left"]
        self.frame = 0
        self.image = pygame.transform.scale(self.movement_image[self.frame],self.character_size)
        self.rect = self.image.get_rect(center = (center_x,center_y))
        self.mask_image = pygame.mask.from_surface(self.image)
        self.life = life
        self.speed = speed
        self.attack_damage = sound_attack
        self.sound_damage = sound_damage
        self.sound_life = sound_life_gain
        self.time_update = pygame.time.get_ticks()
        self.time_frames = TIME_FRAME_CHANGE
        
    def move_change(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time_update >= self.time_frames:
            self.change_frame()
            self.time_update = time_now

    def damaged(self):
        self.generate_sound(DAMAGE_SOUND,VOLUME)
        self.life -= 0
     
    def sticker_dictionary(self, path, key1, cuant1, key2=None, cuant2=None, key3=None, cuant3=None):
        dictionary_moves = {}
        list_for_keys = []
        for num in range(cuant1):
            image = pygame.image.load(f"{path}\{num:02}.png").convert_alpha()
            list_for_keys.append(image)
        dictionary_moves[key1] = list_for_keys
        if key2:
            list_for_keys = []
            for num in range(cuant2):
                image = pygame.image.load(f"{path}\{cuant1+num:02}.png").convert_alpha()
                list_for_keys.append(image)
            dictionary_moves[key2] = list_for_keys
        if key3:
            list_for_keys = []
            for num in range(cuant3):
                image = pygame.image.load(f"{path}\{cuant1+cuant2+num:02}.png").convert_alpha()
                list_for_keys.append(image)
            dictionary_moves[key3] = list_for_keys
        return dictionary_moves

    def generate_sound(self,path: str, volume: float= VOLUME)->None:
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        pygame.mixer.Sound.play(sound)

    def change_frame(self):
        self.frame += 1
        if self.frame > len(self.movement_image)-1:
            self.frame = 0
        else:
            self.image = pygame.transform.scale(self.movement_image[self.frame],self.character_size)

    def correction_of_directory_moves_r_l_a_i(self):
        try:
            if not "right" in self.dictionary_surfaces:
                self.dictionary_surfaces["right"] = [pygame.transform.flip(image, True, False) for image in self.dictionary_surfaces["left"]]
            if not "left" in self.dictionary_surfaces:
                self.dictionary_surfaces["left"] = [pygame.transform.flip(image, True, False) for image in self.dictionary_surfaces["right"]]
            if not "attack" in self.dictionary_surfaces:
                self.dictionary_surfaces["attack"] = self.dictionary_surfaces["idle"]
            if not "idle" in self.dictionary_surfaces:
                self.dictionary_surfaces["idle"] = self.dictionary_surfaces["attack"]
        except:
            self.dictionary_surfaces["right"] = [pygame.Surface(SIZE_PLAYER,).fill(BLACK)]
            self.dictionary_surfaces["left"] = [pygame.Surface(SIZE_PLAYER,).fill(BLACK)]
            self.dictionary_surfaces["attack"] = [pygame.Surface(SIZE_PLAYER,).fill(BLACK)]
            self.dictionary_surfaces["idle"] = [pygame.Surface(SIZE_PLAYER,).fill(BLACK)]

    def correction_of_directory_moves_left_right(self):
        try:
            if not "right" in self.dictionary_surfaces:
                self.dictionary_surfaces["right"] = [pygame.transform.flip(image, True, False) for image in self.dictionary_surfaces["left"]]
            if not "left" in self.dictionary_surfaces:
                self.dictionary_surfaces["left"] = [pygame.transform.flip(image, True, False) for image in self.dictionary_surfaces["right"]]
        except:
            self.dictionary_surfaces["right"] = [pygame.Surface(SIZE_PLAYER,).fill(BLACK)]
            self.dictionary_surfaces["left"] = [pygame.Surface(SIZE_PLAYER,).fill(BLACK)]