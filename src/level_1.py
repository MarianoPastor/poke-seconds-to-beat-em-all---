import pygame,high_scores
from not_playable_character import NPC
from constants import *
from platforms import Platform
from buttom import Button
from levels_windows import LevelsWindows
from volume import Volume
from winner import Win




class Level1(LevelsWindows):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path,screen=screen)
        self.npc_1_1 = NPC(sprite_groups=[self.all_sprites_group,self.level_1_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,CHARMANDER_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=FLOOR_LEVEL-30,center_x=WIDTH-70,movement=True,power_jump=JUMP_PLAYER,fire_rock_deb=False,leaf_rock_deb=False,water_rock_deb=True,tunder_rock_deb=True)
        self.npc_1_2 = NPC(sprite_groups=[self.all_sprites_group,self.level_1_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,BULBASAUR_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.1,center_x=50,movement=False,power_jump=JUMP_PLAYER,fire_rock_deb=True,leaf_rock_deb=False,water_rock_deb=False,tunder_rock_deb=False)
        self.npc_1_3 = NPC(sprite_groups=[self.all_sprites_group,self.level_1_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,SQUIRTLE_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.8,center_x=WIDTH-50,movement=False,power_jump=JUMP_PLAYER,fire_rock_deb=False,leaf_rock_deb=True,water_rock_deb=False,tunder_rock_deb=True)
        self.npc_1_4 = NPC(sprite_groups=[self.all_sprites_group,self.level_1_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ZAPDOS_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=85,center_x=WIDTH/2,movement=False,power_jump=JUMP_PLAYER,fire_rock_deb=False,leaf_rock_deb=False,water_rock_deb=True,tunder_rock_deb=True)
        
        self.platform_1 = Platform([self.all_sprites_group,self.level_1_group,self.platforms_group],image_surface=PLATFORM_LOADED,size=(85,15),center_x=WIDTH/3,center_y=HEIGHT/1.5,movement="WIDTH")
        self.platform_2 = Platform([self.all_sprites_group,self.level_1_group,self.platforms_group],image_surface=PLATFORM_LOADED,size=(85,15),center_x=50,center_y=HEIGHT/1.8)
        self.platform_3 = Platform([self.all_sprites_group,self.level_1_group,self.platforms_group],image_surface=PLATFORM_LOADED,size=(85,15),center_x=WIDTH/1.5,center_y=HEIGHT/2.2,movement="WIDTH")
        self.platform_4 = Platform([self.all_sprites_group,self.level_1_group,self.platforms_group],image_surface=PLATFORM_LOADED,size=(85,15),center_x=WIDTH-80,center_y=HEIGHT/2.3)
        
        self.name_bottom = Button([self.all_sprites_group,self.level_1_group],"Fist Level",None,35,BLACK,WHITE,WIDTH/2,20,screen=self.screen)
        self.second_running = TIME_FOR_LEVEL_1
        self.old_time = pygame.time.get_ticks()
        self.data_player = high_scores.HighScores.json_load(self,data_path=DATA_PLAYER_JSON)

    def best_time(self):
        if self.time_1 < self.second_running:
            self.time_1 = self.second_running

    
    def level_logic(self):
            if len(self.enemy_groups) == 0:
                self.best_time()
                self.active_bucle = False
                self.presentation_music = Volume.load_music(PRESENTATION_SOUND,VOLUME)
                self.screen_seen = Win(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=FINISH_GAME_IMAGE,screen=self.screen,player=self.player,time=self.second_running)
                self.kill()
                self.screen_seen.run_game()
                print( self.data_player)
                self.data_player[0]["level_1_time"] = self.time_1
                self.data_player[0]["total_time"] = self.time_1
                self.data_player[0]["total_lifes"] = self.player.life
                self.data_player[1]["level_flag_2"] = True
                print( self.data_player)
                high_scores.HighScores.json_dump(json_path=DATA_PLAYER_JSON,data=self.data_player)
            self.loose_penalty()

    
    def update(self):
        super().update()
        self.level_logic()

    
    
    