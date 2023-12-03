import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button





class InitialScreen(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path)  


        self.start = Button([self.all_sprites,self.buttons_group],"Start ",None,40,YELLOW,BLACK,WIDTH-100,100,screen=self.screen)
        self.scores = Button([self.all_sprites,self.buttons_group],"Scores",None,40,YELLOW,BLACK,WIDTH-100,200,screen=self.screen)
        self.controls = Button([self.all_sprites,self.buttons_group],"Controls",None,40,YELLOW,BLACK,100,100,screen=self.screen)
        self.sound = Button([self.all_sprites,self.buttons_group],"Sounds",None,40,YELLOW,BLACK,100,200,screen=self.screen)
        
     
        
    def draw(self):
        super().draw()

    def update(self):
        super().update()
    
    def run_game(self):
        while self.playing:
           
            
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.exit()      


            self.update()
            self.draw()
            

            pygame.display.flip()

    


    