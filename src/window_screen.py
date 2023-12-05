import pygame, sys
from constants import *
from mouse import Mouse
from constants import *



class WindowScreen(pygame.sprite.Sprite):
    def __init__(self, sprite_groups, music_path, volume_float, background_path) -> None:
        super().__init__(sprite_groups)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        self.music_path = music_path
        self.volume_float = volume_float
        self.background_path = background_path
        self.time = pygame.time.get_ticks()

        self.image = pygame.image.load(self.background_path)
        self.image = pygame.transform.scale(self.image, SCREEN_TUPLE)
        self.rect = self.image.get_rect()

        self.background_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.platforms_group = pygame.sprite.Group()
        self.enemy_groups = pygame.sprite.Group()
        self.energy_ball_group = pygame.sprite.Group()
        self.buttons_group = pygame.sprite.Group()
        self.berry_group = pygame.sprite.Group()
        self.rocks_group = pygame.sprite.Group()
        self.mouse_group = pygame.sprite.Group()
        self.level_1_group = pygame.sprite.Group()
        self.level_2_group = pygame.sprite.Group()
        self.level_3_group = pygame.sprite.Group()
        self.pause_group = pygame.sprite.Group()
        self.loose_group = pygame.sprite.Group()
        self.scores_group = pygame.sprite.Group()
        self.controls_group = pygame.sprite.Group()
        self.volume_group = pygame.sprite.Group()
        
        background_sprite = pygame.sprite.Sprite()
        background_sprite.image = self.image
        background_sprite.rect = self.rect
        self.background_group.add(background_sprite)
        
        self.mouse = Mouse(sprite_groups=[self.mouse_group,self.all_sprites],image_surface=pygame.image.load(POKEBALL_IMAGE),mouse_size=MOUSE_SIZE)
        self.playing = False
        self.load_music()
    
        self.all_sprites.empty()
        
    
        
    def exit()->None: 
        try:
            pygame.quit()
            sys.exit()
        except:
            None
    
    def load_music(self)->None:
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.volume_float)

    # def background_image_load(self)->None:
    #     bliting_image = pygame.image.load(self.background_path)
    #     bliting_image = pygame.transform.scale(bliting_image,SCREEN_TUPLE)
    #     bliting_image_rect = bliting_image.get_rect()
    #     self.screen.blit(bliting_image,bliting_image_rect)

    def draw(self): 
        #self.background_image_load()
        self.background_group.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.mouse_group.draw(self.screen)
        self.energy_ball_group.draw(self.screen)
        
        
    
    def update(self):
        self.background_group.update()
        self.all_sprites.update()
        self.mouse_group.update()
        self.energy_ball_group.update()


    def run_game(self):
        while True:
            try:
                self.clock.tick(FPS)
                event_list = pygame.event.get()
                for event in event_list:
                    if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        self.exit()

                self.update()
                self.draw()

                if not self.playing:
                    self.all_sprites.empty()
                    return

                pygame.display.flip()

            except Exception as e:
                print(f"Error: {e}")
                self.playing = False
                break
