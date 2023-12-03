import pygame, sys
from constants import *

class WindowScreen(pygame.sprite.Sprite):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None:
        super().__init__(sprite_groups)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        self.music_path = music_path
        self.volume_float = volume_float
        self.background_path = background_path

        self.all_sprites = pygame.sprite.Group()
        self.platforms_groups = pygame.sprite.Group()
        self.enemy_groups = pygame.sprite.Group()
        self.energy_ball_groups = pygame.sprite.Group()
        self.buttons_group = pygame.sprite.Group()

        self.playing = False
        self.load_music()

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

    def background_image_load(self)->None:
        bliting_image = pygame.image.load(self.background_path)
        bliting_image = pygame.transform.scale(bliting_image,SCREEN_TUPLE)
        bliting_image_rect = bliting_image.get_rect()
        self.screen.blit(bliting_image,bliting_image_rect)

    def mouse_pokeball(self,width : int = 20, height : int = 20)->None:
        image = pygame.image.load(POKEBALL_IMAGE)  
        image = pygame.transform.scale(image,(width,height))
        image_rect = image.get_rect()  
        mouse_x, mouse_y = pygame.mouse.get_pos()
        image_rect.center = (mouse_x, mouse_y)
        pygame.mouse.set_visible(False) 
        self.screen.blit(image,image_rect)

    def draw(self): 
        self.background_image_load()
        self.all_sprites.draw(self.screen)
        self.mouse_pokeball()
    
    def update(self):
        self.all_sprites.update()  
        pygame.display.flip()
    

    def run_game(self):
        while self.playing:
           
            
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.exit()      


            self.update()
            self.draw()
            

            pygame.display.flip()