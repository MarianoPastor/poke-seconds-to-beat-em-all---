import random,high_scores,pygame
from buttom import Button
from not_playable_character import NPC
from constants import *
from platforms import Platform
from levels_windows import LevelsWindows
from boss import Boss
from volume import Volume
from winner import Win


  

class Level3(LevelsWindows):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path,screen=screen)
        self.npc_3_1 = NPC(sprite_groups=[self.all_sprites_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ARTICUNO_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.1,center_x=50,movement=True,power_jump=JUMP_ENEMY,fire_rock_deb=True,leaf_rock_deb=False,water_rock_deb=False,tunder_rock_deb=True)
        self.npc_3_2 = NPC(sprite_groups=[self.all_sprites_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ZAPDOS_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/3,center_x=WIDTH-50,movement=True,power_jump=JUMP_ENEMY,fire_rock_deb=True,leaf_rock_deb=True,water_rock_deb=True,tunder_rock_deb=True)
        self.npc_3_3 = NPC(sprite_groups=[self.all_sprites_group,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,MOLTRES_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=85,center_x=WIDTH/2,movement=True,power_jump=JUMP_ENEMY,fire_rock_deb= False,leaf_rock_deb=False,water_rock_deb= True,tunder_rock_deb= True)
        self.boss = Boss(sprite_groups=[self.all_sprites_group],image_surface= Boss.sticker_dictionary(self,MEWTWO_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_BOSS,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_BOSS,center_y=HEIGHT / 1.5,center_x=WIDTH-100,power_jump=JUMP_ENEMY)
       
        self.flag_boss = True 
       
        self.platform_1 = Platform([self.all_sprites_group,self.platforms_group],image_surface=PLATFORM_LOADED,size=(85,15),center_x=WIDTH/2,center_y=HEIGHT/1.5,movement="HEIGHT")
        self.platform_2 = Platform([self.all_sprites_group,self.platforms_group],image_surface=PLATFORM_LOADED,size=(85,15),center_x=WIDTH/3,center_y=HEIGHT/1.8,movement="WIDTH")
       
        self.name_botton = Button([self.all_sprites_group],"Second Level",None,35,BLACK,WHITE,WIDTH/2,20,screen=self.screen)
        self.pause_botton = Button([self.all_sprites_group],"Pause",None,35,BLACK,WHITE,WIDTH-50,20,screen=self.screen)
        self.volume_botton = Button([self.all_sprites_group],"volume",None,35,BLACK,WHITE,50,20,screen=self.screen)
        self.second_running = TIME_FOR_LEVEL_3
        self.data_player = high_scores.HighScores.json_load(self,data_path=DATA_PLAYER_JSON)

    def gravity_invertion(self): 
        if self.boss.rect.left <= WIDTH / 2:
            self.boss.count -= 1    
        if self.boss.inverse_gravity:
            self.player.gravity = False
            self.player.jumping = False
            self.player.rect.top -= self.boss.speed 
            if self.player.rect.top <= 10:
                self.player.rect.top = 10
        if self.boss.count == 0:
            self.boss.inverse_gravity != self.boss.inverse_gravity
            self.boss.count = random.randint(2,3)
        
    
    def best_time(self):
        if self.time_3 < self.second_running:
            self.time_3 = self.second_running

    
    def level_logic(self):
        if len(self.enemy_groups) <= 0 and not self.flag_boss:
            self.best_time()
            self.active_bucle = False
            self.presentation_music = Volume.load_music(PRESENTATION_SOUND,VOLUME)
            self.screen_seen = Win(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=FINISH_GAME_IMAGE,screen=self.screen,player=self.player,time=self.second_running)
            self.kill()
            self.screen_seen.run_game()
            print(self.data_player)
            self.data_player[0]["level_3_time"] = self.time_3
            self.data_player[0]["total_lifes"] = self.player.life + self.data_player[0]["total_lifes"]
            print(self.data_player)
            high_scores.HighScores.json_dump(json_path=DATA_PLAYER_JSON,data=self.data_player)
        self.loose_penalty()

    def energy_collide_boss(self):
        collisions = pygame.sprite.spritecollide(self.boss, self.energy_ball_group,dokill=False)
        if collisions and not self.boss.inmortality: 
            self.flag_boss = False     
            self.kill()
       

    def update(self):
        super().update()
        self.level_logic()
        self.fireball_event(self.npc_3_3)
        Boss.boss_collide_player(self=self.boss,player=self.player)
        self.gravity_invertion()
        self.energy_collide_boss()
        