import pygame
from playable_character import PlayableCharacter
from not_playable_character import NPC
from constants import *
from platforms import Platform
from window_screen import WindowScreen
from buttom import Button
from berrys import Berry

class Level1(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path)
        self.player = PlayableCharacter(sprite_groups=[self.all_sprites],image_surface= PlayableCharacter.sticker_dictionary(self,PIKACHU_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_PLAYER,speed= SPEED_PLAYER,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_PLAYER,center_y=HEIGHT/1.3,center_x=50,power_jump=JUMP_PLAYER)
        self.npc_1_1 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,CHARMANDER_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/1.3,center_x=WIDTH-100,movement=True,power_jump=JUMP_PLAYER)
        self.npc_1_2 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,BULBASAUR_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.1,center_x=50,movement=False,power_jump=JUMP_PLAYER)
        self.npc_1_3 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,SQUIRTLE_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/3,center_x=WIDTH-50,movement=False,power_jump=JUMP_PLAYER)
        self.npc_1_4 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ZAPDOS_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY_2,center_y=85,center_x=WIDTH/2,movement=False,power_jump=JUMP_PLAYER)
        self.platform_1 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/2,HEIGHT/1.5,200,20),BLACK)
        self.platform_2 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/3,HEIGHT/1.8,150,20),GREEN)
        self.platform_3 = Platform([self.all_sprites,self.platforms_groups],(75,HEIGHT/1.8,150,20),GREEN)
        self.platform_4 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/1.5,HEIGHT/2.2,150,20),BLUE)
        self.platform_4 = Platform([self.all_sprites,self.platforms_groups],(WIDTH-75,HEIGHT/2.3,150,20),BLUE)
        self.name_bottom = Button([self.all_sprites,self.buttons_group],"Fist Level",None,35,BLACK,WHITE,WIDTH/2,20,screen=self.screen)
        self.pause_bottom = Button([self.all_sprites,self.buttons_group],"Pause",None,35,BLACK,WHITE,WIDTH-50,20,screen=self.screen)
        self.volume_bottom = Button([self.all_sprites,self.buttons_group],"volume",None,35,BLACK,WHITE,50,20,screen=self.screen)
        self.berry = Berry(sprite_groups=[self.all_sprites,self.berry_groups],image_surface=pygame.image.load(FRUIT_IMAGE),berry_size=BERRY_SIZE,center_x=WIDTH/2,center_y=HEIGHT/2,screen=self.screen)

    def draw(self): 
        super().draw()

    def update(self):
        super().update()
    
    def run_game(self):
        while self.playing:
            self.clock.tick(FPS)
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.exit()      


            self.update()
            self.draw()
            

            pygame.display.flip()