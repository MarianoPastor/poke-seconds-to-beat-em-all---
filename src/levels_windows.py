import pygame, playing
from playable_character import PlayableCharacter
from volume import Volume
from not_playable_character import NPC
from constants import *
from energy_ball import EnergyBall
from window_screen import WindowScreen
from buttom import Button
from berrys import Berry
from rocks import Rock
from pause_screen import PauseScreen
from random import randint




class LevelsWindows(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path,screen=screen)
        self.player = PlayableCharacter(sprite_groups=[self.all_sprites_group],image_surface= PlayableCharacter.sticker_dictionary(self,PIKACHU_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_PLAYER,speed= SPEED_PLAYER,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_PLAYER,center_y=HEIGHT/1.3,center_x=50,power_jump=JUMP_PLAYER)
        self.pause_botton = Button([self.all_sprites_group,self.level_1_group],"Pause",None,35,BLACK,WHITE,WIDTH-50,20,screen=self.screen)
        self.volume_botton = Button([self.all_sprites_group,self.level_1_group],"volume",None,35,BLACK,WHITE,50,20,screen=self.screen)
        self.back = Button([self.all_sprites_group],"Back",None,35,BLACK,WHITE,50,50,screen=self.screen)
        self.second_running = TIME_FOR_LEVEL_1
        self.sound_levels = Volume.load_music(self.music_path,self.volume_float)
        

    

    def rock_logic(self):
        collisions = pygame.sprite.spritecollide(self.player, self.rocks_group, True)
        if collisions:        
            if self.leaf_rock in collisions:
                self.player.rocks["leaf"] = True
            elif self.fire_rock in collisions:
                self.player.rocks["fire"] = True
            elif self.water_rock in collisions:
                self.player.rocks["water"] = True
            elif self.tunder_rock in collisions:
                self.player.rocks["tunder"] = True
        else:
            if self.player.rocks["leaf"] == False:
                self.leaf_rock = Rock(sprite_groups=[self.all_sprites_group, self.rocks_group], image_surface=pygame.image.load(LEAF_IMAGE), rock_size=ROCK_SIZE, center_x=WIDTH / 1.5, center_y=HEIGHT / 2.2 - 40)
            if self.player.rocks["fire"] == False:
                self.fire_rock = Rock(sprite_groups=[self.all_sprites_group,self.rocks_group],image_surface=pygame.image.load(FIRE_IMAGE),rock_size=ROCK_SIZE,center_x=WIDTH/4,center_y=FLOOR_LEVEL-50)
            if self.player.rocks["water"] == False:
                self.water_rock = Rock(sprite_groups=[self.all_sprites_group,self.rocks_group],image_surface=pygame.image.load(WHATER_IMAGE),rock_size=ROCK_SIZE,center_x=WIDTH-50,center_y=HEIGHT-100)
            if self.player.rocks["tunder"] == False:
                self.tunder_rock = Rock(sprite_groups=[self.all_sprites_group,self.rocks_group],image_surface=pygame.image.load(TUNDER_IMAGE),rock_size=ROCK_SIZE,center_x=70,center_y=100)

    def berry_logic(self):
        collisions = pygame.sprite.spritecollide(self.player, self.berry_group, True)
        if not len(self.berry_group):
            self.berry = Berry(sprite_groups=[self.all_sprites_group,self.berry_group],image_surface=pygame.image.load(FRUIT_IMAGE),berry_size=BERRY_SIZE,center_x=randint(50,WIDTH-50),center_y=randint(50,HEIGHT-50))
        elif self.berry in collisions:
            self.player.life += self.berry.life_giver    


    def button_logic(self):
        if self.pause_botton.pressed_button():
            self.screen_seen = PauseScreen(sprite_groups=[self.all_sprites_group],music_path=TOASTY_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK,screen=self.screen)
            self.screen_seen.run_game()
        elif self.volume_botton.pressed_button():
            self.screen_seen = Volume(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK,screen=self.screen)
            self.screen_seen.run_game()
        elif self.back.pressed_button():
            self.active_bucle = False
            self.presentation_music = Volume.load_music(self.music_path,self.volume_float)
            self.kill()

    def energy_creator(self): 
        if self.player.energy_ball_flag:
            x,y = self.player.rect.center
            EnergyBall(sprite_groups=[self.all_sprites_group, self.energy_ball_group], image_surface=pygame.image.load(SHOOT_IMAGE), energy_size=(40, 40), center_x=x, center_y=y, speed=-ATTACK_SPEED, direction=self.player.direction_attack,screen=self.screen)
            self.player.energy_ball_flag = False