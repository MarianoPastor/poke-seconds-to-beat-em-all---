import pygame
from playable_character import PlayableCharacter
from buttom import Button
from not_playable_character import NPC
from constants import *
from platforms import Platform
from window_screen import WindowScreen
  

class Level3(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path)
        
        self.player = PlayableCharacter(sprite_groups=[self.all_sprites],image_surface= PlayableCharacter.sticker_dictionary(self,PIKACHU_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_PLAYER,speed= SPEED_PLAYER,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_PLAYER,center_y= HEIGHT / 1.07,center_x= 50,power_jump=JUMP_PLAYER)
        self.npc_3_1 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ARTICUNO_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.1,center_x=50,movement=True,power_jump=JUMP_PLAYER)
        self.npc_3_2 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ZAPDOS_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/3,center_x=WIDTH-50,movement=True,power_jump=JUMP_PLAYER)
        self.npc_3_3 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,MOLTRES_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY_2,center_y=85,center_x=WIDTH/2,movement=True,power_jump=JUMP_PLAYER)
        
        self.platform_1 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/2,HEIGHT/1.5,200,20),BLACK)
        self.platform_2 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/3,HEIGHT/1.8,150,20),GREEN)
        
        self.name_bottom = Button([self.all_sprites,self.buttons_group],"Second Level",None,35,BLACK,WHITE,WIDTH/2,20,screen=self.screen)
        self.pause_bottom = Button([self.all_sprites,self.buttons_group],"Pause",None,35,BLACK,WHITE,WIDTH-50,20,screen=self.screen)
        self.volume_bottom = Button([self.all_sprites,self.buttons_group],"volume",None,35,BLACK,WHITE,50,20,screen=self.screen)
        
    def draw(self): 
        super().draw()

    def update(self):
        super().update()
    
    def run_game(self):
        super().run_game()