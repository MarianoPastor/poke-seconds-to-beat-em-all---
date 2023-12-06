import pygame, sys
from constants import *
from mouse import Mouse
from constants import *



class WindowScreen(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, music_path, volume_float, background_path,screen) -> None:
        super().__init__(sprite_groups)

        self.screen = screen
        self.active_bucle = True
        #self.player_dict = playing.Playing.player_dict
        
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
        
        self.background_path = background_path
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load(self.background_path)
        self.image = pygame.transform.scale(self.image, SCREEN_TUPLE)
        self.rect = self.image.get_rect()
        background_sprite = pygame.sprite.Sprite()
        background_sprite.image = self.image
        background_sprite.rect = self.rect
        self.background_group.add(background_sprite)
        
        self.music_path = music_path
        self.volume_float = volume_float



        self.mouse = Mouse(sprite_groups=[self.mouse_group],image_surface=pygame.image.load(POKEBALL_IMAGE),mouse_size=MOUSE_SIZE)


    def draw(self): 
        self.background_group.draw(self.screen)
        self.all_sprites_group.draw(self.screen)
        self.mouse_group.draw(self.screen)
       
    
    def update(self):
        self.background_group.update()
        self.all_sprites_group.update()
        self.mouse_group.update()
        
        


    def run_game(self):
        while self.active_bucle:
            self.time = pygame.time.get_ticks()
            self.clock.tick(FPS)
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.update()
            
            self.draw()

            pygame.display.flip()
