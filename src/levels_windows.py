import pygame,random
from platforms import Platform
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
from fire_ball import FireBall 
from looser import Looser




class LevelsWindows(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None: 
        super().__init__(sprite_groups=sprite_groups,music_path=music_path,volume_float=volume_float,background_path=background_path,screen=screen)
        self.player = PlayableCharacter(sprite_groups=[self.all_sprites_group],image_surface= PlayableCharacter.sticker_dictionary(self,PIKACHU_SPRITES,"left",4,"attack",4,"idle",3),life= LIFE_PLAYER,speed= SPEED_PLAYER,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_PLAYER,center_y=HEIGHT/1.3,center_x=50,power_jump=JUMP_PLAYER,tunder_rock=False,leaf_rock=False,water_rock=False,fire_rock=False)
        self.pause_botton = Button([self.all_sprites_group,self.level_1_group],"Pause",None,35,BLACK,WHITE,WIDTH-50,20,screen=self.screen)
        self.volume_botton = Button([self.all_sprites_group,self.level_1_group],"volume",None,35,BLACK,WHITE,50,20,screen=self.screen)
        self.back = Button([self.all_sprites_group],"Back",None,35,BLACK,WHITE,50,50,screen=self.screen)
        self.second_running = TIME_FOR_LEVEL_1
        self.back_sound = Volume.load_music(self.music_path,self.volume_float)
        self.time_reversal = pygame.time.get_ticks()
        self.time_for_attack = pygame.time.get_ticks()
        self.time_attack = 2000

    
    
    def time_reversal_event(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time_reversal >= 500:
            self.second_running -= 0.5
            self.time_reversal = time_now
        self.time_see = Button([self.all_sprites_group],f"Time: {self.second_running} ",None,30,PURPLE,YELLOW,WIDTH/2+100,HEIGHT-50,screen=self.screen)           
        

    def loose_penalty(self):
       if self.player.life <= 0 or self.second_running <= 0:
        Volume.sound_fx(TOASTY_SOUND,fx_volume_variable )
        self.active_bucle = False
        self.presentation_music = Volume.load_music(PRESENTATION_SOUND,VOLUME)
        self.screen_seen = Looser(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=FINISH_GAME_IMAGE,screen=self.screen,player=self.player,time=self.second_running)
        self.kill()
        self.screen_seen.run_game()

    def rock_logic(self):
        collisions = pygame.sprite.spritecollide(self.player, self.rocks_group, True)
        if collisions:        
            if self.leaf_rock in collisions:
                self.player.leaf_rock = True
            elif self.fire_rock in collisions:
                 self.player.fire_rock = True
            elif self.water_rock in collisions:
                self.player.water_rock= True
            elif self.tunder_rock in collisions:
                self.player.tunder_rock = True
        else:
            if not self.player.leaf_rock:
                self.leaf_rock = Rock(sprite_groups=[self.all_sprites_group, self.rocks_group], image_surface=pygame.image.load(LEAF_IMAGE), rock_size=ROCK_SIZE, center_x=WIDTH / 1.5, center_y=HEIGHT / 2.2 - 40)
            if not self.player.fire_rock:
                self.fire_rock = Rock(sprite_groups=[self.all_sprites_group,self.rocks_group],image_surface=pygame.image.load(FIRE_IMAGE),rock_size=ROCK_SIZE,center_x=WIDTH/4,center_y=FLOOR_LEVEL-50)
            if not self.player.water_rock:
                self.water_rock = Rock(sprite_groups=[self.all_sprites_group,self.rocks_group],image_surface=pygame.image.load(WHATER_IMAGE),rock_size=ROCK_SIZE,center_x=WIDTH-50,center_y=HEIGHT-100)
            if not self.player.tunder_rock:
                self.tunder_rock = Rock(sprite_groups=[self.all_sprites_group,self.rocks_group],image_surface=pygame.image.load(TUNDER_IMAGE),rock_size=ROCK_SIZE,center_x=70,center_y=100)

    def berry_logic(self):
        berrys_collided = pygame.sprite.spritecollide(self.player, self.berry_group, True)
        try:
            self.player.life += berrys_collided[0].life_giver
            Volume.sound_fx(LIFE_SOUND,fx_volume_variable)
        except:
            self.player.life += 0
        if not len(self.berry_group):
            self.berry = Berry(sprite_groups=[self.all_sprites_group,self.berry_group],image_surface=pygame.image.load(FRUIT_IMAGE),berry_size=BERRY_SIZE,center_x=random.randint(50,WIDTH-50),center_y=random.randint(50,HEIGHT-50),life_giver=random.randint(-1,1))

    def button_logic(self):
        if self.pause_botton.pressed_button():
            self.screen_seen = PauseScreen(sprite_groups=[self.all_sprites_group],music_path=TOASTY_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK,screen=self.screen)
            self.screen_seen.run_game()
        elif self.volume_botton.pressed_button():
            self.screen_seen = Volume(sprite_groups=[self.all_sprites_group],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK,screen=self.screen)
            self.screen_seen.run_game()
        elif self.back.pressed_button():
            self.active_bucle = False
            self.kill()
            self.back_sound = Volume.load_music(PRESENTATION_SOUND,VOLUME)

    def energy_creator(self): 
        if self.player.energy_ball_flag:
            x,y = self.player.rect.center
            EnergyBall(sprite_groups=[self.all_sprites_group, self.energy_ball_group], image_surface=pygame.image.load(ENERGY_BALL_IMAGE), energy_size=(40, 40), center_x=x, center_y=y, speed=ATTACK_SPEED, direction=self.player.direction_attack,screen=self.screen,fire_rock=self.player.fire_rock,leaf_rock=self.player.leaf_rock,water_rock=self.player.water_rock,tunder_rock=self.player.tunder_rock)
            self.player.energy_ball_flag = False
            self.player.tunder_rock = False
            self.player.water_rock = False
            self.player.leaf_rock = False
            self.player.fire_rock = False
    
                        
    def energy_collide_enemy(self):
        colide = pygame.sprite.groupcollide(self.energy_ball_group,self.enemy_groups,True,True)
        if colide:
            Volume.sound_fx(DAMAGE_SOUND,fx_volume_variable)



    def fireball_event(self,character):
        try:
            if character in self.enemy_groups:
                time_now = pygame.time.get_ticks()
                if time_now - self.time_for_attack >= self.time_attack:
                    FireBall([self.all_sprites_group,self.enemy_attack],pygame.image.load(FIREBALL_IMAGE),(40,40),character.rect.centerx,character.rect.centery,ATTACK_SPEED,self.screen,player=self.player)
                    self.time_for_attack = time_now
                    self.time_attack = random.randrange(2000,5000)
        except:
            print("no character")

    def update(self):
        super().update()
        Button.life_see(self=self,player_lifes=self.player.life)
        NPC.player_collide_enemy(player=self.player,group=self.enemy_groups)
        Platform.platform_logic(self.player,self.platforms_group)
        self.energy_creator()
        self.rock_logic()
        self.button_logic()
        self.berry_logic()
        self.time_reversal_event()
        self.energy_collide_enemy()