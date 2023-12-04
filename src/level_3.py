import pygame, playing
from playable_character import PlayableCharacter
from buttom import Button
from not_playable_character import NPC
from constants import *
from platforms import Platform
from window_screen import WindowScreen
from boss import Boss
from pause_screen import PauseScreen
from volume import Volume
from rocks import Rock
from berrys import Berry
from high_scores import HighScores

  

class Level3(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path)
        
        self.player = PlayableCharacter(sprite_groups=[self.all_sprites],image_surface= PlayableCharacter.sticker_dictionary(self,PIKACHU_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_PLAYER,speed= SPEED_PLAYER,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_PLAYER,center_y= HEIGHT / 1.07,center_x= 50,power_jump=JUMP_PLAYER)
        
        self.npc_3_1 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ARTICUNO_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/2.1,center_x=50,movement=True,power_jump=JUMP_ENEMY)
        self.npc_3_2 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,ZAPDOS_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=HEIGHT/3,center_x=WIDTH-50,movement=True,power_jump=JUMP_ENEMY)
        self.npc_3_3 = NPC(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= NPC.sticker_dictionary(self,MOLTRES_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=85,center_x=WIDTH/2,movement=True,power_jump=JUMP_ENEMY)
        self.boss = Boss(sprite_groups=[self.all_sprites,self.enemy_groups],image_surface= Boss.sticker_dictionary(self,MEWTWO_SPRITES,"left",3),life= LIFE_ENEMY,speed= SPEED_BOSS,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_BOSS,center_y=HEIGHT / 1.5,center_x=WIDTH-100,power_jump=JUMP_ENEMY,energy_ball_direccion=self.player.rect)
        self.platform_1 = Platform([self.all_sprites,self.platforms_group],(WIDTH/2,HEIGHT/1.5,200,20),WHITE,movement="HEIGHT")
        self.platform_2 = Platform([self.all_sprites,self.platforms_group],(WIDTH/3,HEIGHT/1.8,150,20),YELLOW,movement="WIDTH")
        
        self.name_botton = Button([self.all_sprites,self.buttons_group],"Second Level",None,35,BLACK,WHITE,WIDTH/2,20,screen=self.screen)
        self.pause_botton = Button([self.all_sprites,self.buttons_group],"Pause",None,35,BLACK,WHITE,WIDTH-50,20,screen=self.screen)
        self.volume_botton = Button([self.all_sprites,self.buttons_group],"volume",None,35,BLACK,WHITE,50,20,screen=self.screen)
        

    def gravity_invertion(self): 
        if self.boss.inverse_gravity:
            self.player.gravity = False
            self.player.rect.top -= SPEED_BOSS
            if self.player.rect.top <= 0:
                self.player.rect.top= 0
        else:
            self.player.gravity = True   

    def rock_logic(self):
        collisions = pygame.sprite.spritecollide(self.player, self.rocks_group, True)
        # Verificar si hay colisiones con algún objeto del grupo
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
            # No hay colisiones, crear el objeto Rock si aún no está en la pantalla
            if self.player.rocks["leaf"] == False:
                self.leaf_rock = Rock(sprite_groups=[self.all_sprites, self.rocks_group], image_surface=pygame.image.load(LEAF_IMAGE), rock_size=ROCK_SIZE, center_x=WIDTH / 1.5, center_y=HEIGHT / 2.2 - 40)
            if self.player.rocks["fire"] == False:
                self.fire_rock = Rock(sprite_groups=[self.all_sprites,self.rocks_group],image_surface=pygame.image.load(FIRE_IMAGE),rock_size=ROCK_SIZE,center_x=WIDTH/4,center_y=FLOOR_LEVEL-50)
            if self.player.rocks["water"] == False:
                self.water_rock = Rock(sprite_groups=[self.all_sprites,self.rocks_group],image_surface=pygame.image.load(WHATER_IMAGE),rock_size=ROCK_SIZE,center_x=WIDTH-50,center_y=HEIGHT-100)
            if self.player.rocks["tunder"] == False:
                self.tunder_rock = Rock(sprite_groups=[self.all_sprites,self.rocks_group],image_surface=pygame.image.load(TUNDER_IMAGE),rock_size=ROCK_SIZE,center_x=70,center_y=100)

    def berry_logic(self):
        collisions = pygame.sprite.spritecollide(self.player, self.berry_group, True)
        # Verificar si hay colisiones con algún objeto del grupo
        if len(collisions) <= 0:
            # No hay colisiones, crear el objeto berry si aún no está en la pantalla
            self.berry = Berry(sprite_groups=[self.all_sprites,self.berry_group],image_surface=pygame.image.load(FRUIT_IMAGE),berry_size=BERRY_SIZE,center_x=WIDTH/2+30,center_y=HEIGHT/2+50)
        elif self.berry in collisions:
            self.player.life += self.berry.life_giver    

    def platform_logic(self):
        for platform in self.platforms_group:
            if self.player.mask_collide(platform):
                # Hay colisión, ajusta la posición y establece las propiedades del jugador
                self.player.rect.bottom = platform.rect.top
                self.player.jumping = False
                self.player.gravity = False
                break
        else:
            # No hay colisiones, el jugador está cayendo
            self.player.falling()

    
    def button_logic(self):
        if self.pause_botton.pressed_button():
            self.screen_seen = PauseScreen(sprite_groups=[self.all_sprites],music_path=TOASTY_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
        elif self.volume_botton.pressed_button():
            self.screen_seen = Volume(sprite_groups=[self.all_sprites],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
    
    def time_save(self):
        playing.Playing.time_play_3 == self.time if self.playing == False else 0 

    def level_logic(self):
        if len(self.enemy_groups) == 0:
            self.time_save()
            HighScores.player_creator()
            self.playing = False
            self.screen_level = HighScores(sprite_groups=[self.all_sprites],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=FINISH_GAME_IMAGE,json_path=SCORES_JSON,order_manage=ORDER_MANAGE)
            self.screen_level.playing = True
            self.screen_level.run_game()

    def update(self):
        super().update()
        Button.life_see(self.player.life)
        self.gravity_invertion()
        self.button_logic()
        self.rock_logic()
        self.berry_logic()
        self.platform_logic()
        self.level_logic()