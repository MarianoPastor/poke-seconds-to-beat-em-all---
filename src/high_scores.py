import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button



class HighScores(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path)     
        self.music = sprite_groups
        self.volume_background = VOLUME
        self.background = background_path
        self.start = Button([self.all_sprites,self.buttons_group],"init ",None,40,RED,None,WIDTH-100,100)
        self.scores = Button([self.all_sprites,self.buttons_group],"volume",None,40,RED,None,100,100)
                
    

    def run_game(self):
        while True:
           
            
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.exit_game()      


            self.update()
            self.draw()
            

            pygame.display.flip()
