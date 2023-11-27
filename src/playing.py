import pygame, sys, random
from playable_character import PlayableCharacter
from not_playable_character import NPC
from constants import *
from platforms import Platform
  

class Playing:
    def __init__(self) -> None:        
        pygame.init()
        self.music = LEVEL_SOUND
        self.volume_background = VOLUME
        self.background = LEVEL_1
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        pygame.display.set_caption("Poke-Seconds Beat em up!!!.")
        pygame.display.set_icon(pygame.image.load(POKEBALL_IMAGE))
        self.all_sprites = pygame.sprite.Group()
        self.platforms_groups = pygame.sprite.Group()
        self.enemy_groups = pygame.sprite.Group()
        self.player = PlayableCharacter(sprite_groups=[self.all_sprites],image_surface= PlayableCharacter.sticker_dictionary(self,PIKACHU_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_PLAYER,speed= SPEED_PLAYER,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_PLAYER,center_y=50,center_x=50,power_jump=JUMP_PLAYER)
        self.npc_1_1 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,CHARMANDER_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/1.3,center_x=WIDTH,movement=True)
        self.npc_1_2 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,BULBASAUR_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.1,center_x=50,movement=False)
        self.npc_1_3 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,SQUIRTLE_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/3,center_x=WIDTH-50,movement=False)
        self.npc_1_4 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ZAPDOS_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY_2,center_y=75,center_x=WIDTH/2,movement=False)
        self.load_music()
        self.platform_1 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/2,HEIGHT/1.5,200,20),BLACK)
        self.platform_2 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/3,HEIGHT/1.8,150,20),GREEN)
        self.platform_3 = Platform([self.all_sprites,self.platforms_groups],(75,HEIGHT/1.8,150,20),GREEN)
        self.platform_4 = Platform([self.all_sprites,self.platforms_groups],(WIDTH/1.5,HEIGHT/2.2,150,20),BLUE)
        self.platform_4 = Platform([self.all_sprites,self.platforms_groups],(WIDTH-75,HEIGHT/2.3,150,20),BLUE)
        
        
    

    def load_music(self)->None:
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.volume_background)

    def mouse_pokeball(self,width : int = 40, height : int = 40)->None:
        image = pygame.image.load(POKEBALL_IMAGE)  
        image = pygame.transform.scale(image,(width,height))
        image_rect = image.get_rect()  
        mouse_x, mouse_y = pygame.mouse.get_pos()
        image_rect.center = (mouse_x, mouse_y)
        pygame.mouse.set_visible(False)
        self.screen.blit(image, image_rect)  


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


    