import pygame, sys
from constants import *
from mouse import Mouse
from constants import *
from buttom import Button




class WindowScreen(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, music_path, volume_float, background_path,screen) -> None:
        super().__init__(sprite_groups)
        
        
        self.FX_off_flag = True
        self.volume_flag = True
        self.volume_correction = 0 
        self.fx_correction = 0 
        self.fx_float = 0
        self.flag_level_2 = True
        self.flag_level_3 = True

        self.second_running = 20

        self.screen = screen
        self.active_bucle = True
        
        self.all_sprites_group = pygame.sprite.Group()
        self.background_group = pygame.sprite.Group()
        self.mouse_group = pygame.sprite.Group()
        self.rocks_group = pygame.sprite.Group()
        self.level_1_group = pygame.sprite.Group()
        self.level_2_group = pygame.sprite.Group()
        self.level_3_group = pygame.sprite.Group()     
        self.berry_group = pygame.sprite.Group()  
        self.enemy_groups = pygame.sprite.Group() 
        self.platforms_group = pygame.sprite.Group()  
        self.energy_ball_group = pygame.sprite.Group() 
        background_sprite = pygame.sprite.Sprite()
        
        self.background_path = background_path
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load(self.background_path)
        self.image = pygame.transform.scale(self.image, SCREEN_TUPLE)
        self.rect = self.image.get_rect()
        
        background_sprite.image = self.image
        background_sprite.rect = self.rect
        self.background_group.add(background_sprite)
        
        self.music_path = music_path
        self.volume_float = volume_float + self.volume_correction
        self.fx_float =  self.fx_float + self.fx_correction

        self.mouse = Mouse(sprite_groups=[self.mouse_group],image_surface=pygame.image.load(POKEBALL_IMAGE),mouse_size=MOUSE_SIZE)


    def draw(self): 
        self.background_group.draw(self.screen)
        self.all_sprites_group.draw(self.screen)
        self.energy_ball_group.draw(self.screen)
        self.mouse_group.draw(self.screen)
        
       
    def update(self):
        self.background_group.update()
        self.all_sprites_group.update()
        self.energy_ball_group.update()
        self.mouse_group.update()
        
        
        


    def run_game(self):
        while self.active_bucle:
            self.clock.tick(FPS)
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.update()
            
            self.draw()

            pygame.display.flip()
