import pygame, sys
from constants import *
from window_screen import WindowScreen


class PauseScreen(WindowScreen):
    def __init__(self,music,volume,background) -> None:        
        pygame.init()
        self.music = music
        self.volume_background = volume
        self.background = background
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_TUPLE)
        pygame.display.set_caption("Poke-Seconds Beat em up!!!.")
        pygame.display.set_icon(pygame.image.load(POKEBALL_IMAGE))
        self.all_sprites = pygame.sprite.Group()
        self.platforms_groups = pygame.sprite.Group()
        self.enemy_groups = pygame.sprite.Group()
        self.load_music()
        

    def draw(self): 
        self.all_sprites.draw(self.screen)
        
    
    def update(self):  
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


    