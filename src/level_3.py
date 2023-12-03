import pygame, sys, random
from playable_character import PlayableCharacter
from not_playable_character import NPC
from boss import Boss
from constants import *
from platforms import Platform
from window_screen import WindowScreen
  

class Level3(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path)
        self.player = PlayableCharacter(sprite_groups=[self.all_sprites],image_surface= PlayableCharacter.sticker_dictionary(self,PIKACHU_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_PLAYER,speed= SPEED_PLAYER,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_PLAYER,center_y=50,center_x=50,power_jump=JUMP_PLAYER)
        self.npc_3_1 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ARTICUNO_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/1.3,center_x=WIDTH,movement=True,power_jump=JUMP_PLAYER)
        self.npc_3_2 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,MOLTRES_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.1,center_x=50,movement=False,power_jump=JUMP_PLAYER)
        self.npc_3_4 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ZAPDOS_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY_2,center_y=75,center_x=WIDTH/2,movement=False,power_jump=JUMP_PLAYER)
        #self.boss = Boss(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,MEWTWO_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/3,center_x=WIDTH-50,movement=False)
      
        self.platform_1 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/2,HEIGHT/2,200,20),BLACK,movement="WIDTH")
        self.platform_2 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/3,HEIGHT/2,150,20),GREEN,movement="HEIGHT")


    def random_number(self,numero_minimo:int=0,numero_maximo:int=20)->int:
        return random.randint(numero_minimo,numero_maximo)

    

    def background_image_load(self)->None:
        bliting_image = pygame.image.load(self.background)
        bliting_image = pygame.transform.scale(bliting_image,SCREEN_TUPLE)
        bliting_image_rect = bliting_image.get_rect()
        self.screen.blit(bliting_image,bliting_image_rect)

    def draw(self): 
        self.background_image_load()
        self.mouse_pokeball(20,20)
        self.all_sprites.draw(self.screen)
        
    
    def update(self):  
        self.all_sprites.update()
        pygame.display.flip()
    
    def exit_game(self)->None: 
        try:
            pygame.quit()
            sys.exit()
        except:
            None

    def run_game(self):
        while True:
            self.clock.tick(FPS)
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.exit_game()      


            self.update()
            self.draw()
            

            pygame.display.flip()


    