from not_playable_character import NPC
from constants import *
from platforms import Platform
from buttom import Button
from levels_windows import LevelsWindows
import pygame,playing




class Level1(LevelsWindows):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path,screen=screen)
        self.npc_1_1 = NPC(sprite_groups=[self.all_sprites_group,self.level_1_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,CHARMANDER_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=FLOOR_LEVEL-30,center_x=WIDTH-70,movement=True,power_jump=JUMP_PLAYER)
        self.npc_1_2 = NPC(sprite_groups=[self.all_sprites_group,self.level_1_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,BULBASAUR_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.1,center_x=50,movement=False,power_jump=JUMP_PLAYER)
        self.npc_1_3 = NPC(sprite_groups=[self.all_sprites_group,self.level_1_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,SQUIRTLE_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.8,center_x=WIDTH-50,movement=False,power_jump=JUMP_PLAYER)
        self.npc_1_4 = NPC(sprite_groups=[self.all_sprites_group,self.level_1_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ZAPDOS_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=85,center_x=WIDTH/2,movement=False,power_jump=JUMP_PLAYER)
        self.platform_1 = Platform([self.all_sprites_group,self.level_1_group,self.platforms_group],(WIDTH/2,HEIGHT/1.5,90,10),BLACK,movement="WIDTH")
        self.platform_2 = Platform([self.all_sprites_group,self.level_1_group,self.platforms_group],(WIDTH/3,HEIGHT/1.8,75,10),GREEN,movement="WIDTH")
        self.platform_3 = Platform([self.all_sprites_group,self.level_1_group,self.platforms_group],(50,HEIGHT/1.8,75,10),GREEN)
        self.platform_4 = Platform([self.all_sprites_group,self.level_1_group,self.platforms_group],(WIDTH/1.5,HEIGHT/2.2,75,10),BLUE,movement="WIDTH")
        self.platform_4 = Platform([self.all_sprites_group,self.level_1_group,self.platforms_group],(WIDTH-80,HEIGHT/2.3,75,10),BLUE)
        self.name_bottom = Button([self.all_sprites_group,self.level_1_group],"Fist Level",None,35,BLACK,WHITE,WIDTH/2,20,screen=self.screen)
        self.second_running = TIME_FOR_LEVEL_1
        self.old_time = pygame.time.get_ticks()

    def time_save(self):
        playing.Playing.player_dict["level_1_time"] = self.second_running    
        print(playing.Playing.player_dict)