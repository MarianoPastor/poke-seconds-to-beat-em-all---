import pygame, sys, playable_character, not_playable_character
from constants import *
from utils import *

class Playing:
    def __init__(self,background,music,volume_background) -> None:        
        pygame.init()
        self.music = music
        self.volume_background = volume_background
        self.background = background
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        pygame.display.set_caption("Poke-Seconds Beat em up!!!.")
        pygame.display.set_icon(pygame.image.load(POKEBALL_IMAGE))
        self.all_sprites = pygame.sprite.Group()
        self.player = playable_character.PlayableCharacter(sprite_groups=[self.all_sprites],image_surface= pygame.image.load(FRUIT_IMAGE),life= LIFE_PLAYER,speed= SPEED_PLAYER,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_PLAYER,center_y=50,center_x=50,power_jump=JUMP_PLAYER)
        self.npc = not_playable_character.NPC(sprite_groups=[self.all_sprites],image_surface= pygame.image.load(ARTICUNO_SPRITES_LEFT),life= LIFE_ENEMY,speed= SPEED_ENEMY,sound_attack= SHOOT_SOUND,sound_damage= DAMAGE_SOUND,sound_life_gain= LIFE_SOUND,size= SIZE_ENEMY,center_y=300,center_x=300,power_jump=JUMP_ENEMY)
        self.load_music()

    def load_music(self)->None:
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.volume_background)


    def draw(self):
        background_image_load(screen=self.screen,image=self.background)
        self.all_sprites.draw(self.screen)
        mouse_pokeball(self.screen,20,20)
    
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
        
            self.draw()
            self.update()
            

            pygame.display.flip()


    