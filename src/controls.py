import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button


class Controls(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path)  

        self.start = Button([self.all_sprites,self.buttons_group],"Start ",None,40,YELLOW,None,WIDTH-100,20,screen=self.screen)
        self.scores = Button([self.all_sprites,self.buttons_group],"Scores",None,40,YELLOW,None,WIDTH-100,50,screen=self.screen)
        self.initial = Button([self.all_sprites,self.buttons_group],"initial screen",None,40,YELLOW,None,100,20,screen=self.screen)
        self.sound = Button([self.all_sprites,self.buttons_group],"Sounds",None,40,YELLOW,None,100,50,screen=self.screen)
        self.controls = Button([self.all_sprites,self.buttons_group],"CONTROLS",None,40,RED,WHITE,WIDTH/2,40,screen=self.screen)

        self.up_explain = Button([self.all_sprites,self.buttons_group],"Key up ==> Jump",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.left_explain = Button([self.all_sprites,self.buttons_group],"Key left ==> Move left",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-100,screen=self.screen)
        self.right_explain = Button([self.all_sprites,self.buttons_group],"Key right ==> Move right",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
        self.espace_explain = Button([self.all_sprites,self.buttons_group],"Key espace ==> Attack",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+100,screen=self.screen)
        self.escape_explain = Button([self.all_sprites,self.buttons_group],"Key escape ==> Exit Game",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+200,screen=self.screen)

     
        
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
