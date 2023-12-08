import pygame, playing
from buttom import Button
from not_playable_character import NPC
from constants import *
from platforms import Platform
from levels_windows import LevelsWindows
from boss import Boss
from high_scores import HighScores

  

class Level3(LevelsWindows):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path,screen=screen)
        self.npc_3_1 = NPC(sprite_groups=[self.all_sprites_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ARTICUNO_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.1,center_x=50,movement=True,power_jump=JUMP_ENEMY)
        self.npc_3_2 = NPC(sprite_groups=[self.all_sprites_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ZAPDOS_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/3,center_x=WIDTH-50,movement=True,power_jump=JUMP_ENEMY)
        self.npc_3_3 = NPC(sprite_groups=[self.all_sprites_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,MOLTRES_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=85,center_x=WIDTH/2,movement=True,power_jump=JUMP_ENEMY)
        self.boss = Boss(sprite_groups=[self.all_sprites_group],image_surface= Boss.sticker_dictionary(self,MEWTWO_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_BOSS,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_BOSS,center_y=HEIGHT / 1.5,center_x=WIDTH-100,power_jump=JUMP_ENEMY,energy_ball_direccion=self.player.rect)
        self.platform_1 = Platform([self.all_sprites_group,self.platforms_group],(WIDTH/2,HEIGHT/1.5,75,10),WHITE,movement="HEIGHT")
        self.platform_2 = Platform([self.all_sprites_group,self.platforms_group],(WIDTH/3,HEIGHT/1.8,75,10),YELLOW,movement="WIDTH")
        self.name_botton = Button([self.all_sprites_group],"Second Level",None,35,BLACK,WHITE,WIDTH/2,20,screen=self.screen)
        self.pause_botton = Button([self.all_sprites_group],"Pause",None,35,BLACK,WHITE,WIDTH-50,20,screen=self.screen)
        self.volume_botton = Button([self.all_sprites_group],"volume",None,35,BLACK,WHITE,50,20,screen=self.screen)
        self.time_play_3 = TIME_FOR_LEVEL_3
        

    def gravity_invertion(self): 
        if self.boss.inverse_gravity:
            self.player.gravity = False
            self.player.rect.top -= SPEED_BOSS
            if self.player.rect.top <= 0:
                self.player.rect.top= 0
        else:
            self.player.gravity = True   

    
    def time_save(self):
        playing.Playing.player_dict["level_3_time"] = self.second_running
        playing.Playing.player_dict["total_time"] = playing.Playing.player_dict["level_3_time"] + playing.Playing.player_dict["level_2_time"] + playing.Playing.player_dict["level_1_time"]
        print(playing.Playing.player_dict)


    def level_logic(self):
        if len(self.enemy_groups) == 0:
            self.time_save()
            self.playing = False
            self.screen_level = HighScores(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=FINISH_GAME_IMAGE,json_path=SCORES_JSON,order_manage=ORDER_MANAGE)
            self.screen_level.playing = True
            self.screen_level.run_game()
            self.kill()


    def update(self):
        super().update()
        self.gravity_invertion()