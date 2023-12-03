import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button
import json



class HighScores(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,json_path,order_manage) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path)     
        self.start = Button([self.all_sprites,self.buttons_group],"Start ",None,40,YELLOW,None,WIDTH-100,20,screen=self.screen)
        self.initial = Button([self.all_sprites,self.buttons_group],"initial screen",None,40,YELLOW,None,100,20,screen=self.screen)
        self.sound = Button([self.all_sprites,self.buttons_group],"Sounds",None,40,YELLOW,None,100,50,screen=self.screen)
        self.high_scores = Button([self.all_sprites,self.buttons_group],"HIGH SCORES",None,40,RED,WHITE,WIDTH/2,40,screen=self.screen)
        self.order_manage = order_manage
        self.json_path = json_path
        self.json = self.json_load()
        self.bubble_sort_by_total_time()
        
        self.first = Button([self.all_sprites,self.buttons_group],f"First: {self.json[0]['name']} Total time {self.json[0]['total_time']}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.second = Button([self.all_sprites,self.buttons_group],f"Second: {self.json[1]['name']} Total time {self.json[1]['total_time']}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
        self.third = Button([self.all_sprites,self.buttons_group],f"Third: {self.json[2]['name']} Total time {self.json[2]['total_time']}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+200,screen=self.screen)

    def json_load(self):
        with open(self.json_path, 'r') as archive:
            return json.load(archive)

    def json_dump(self):
        with open(self.json_path, 'w') as archive:
            self.json = json.dump(self.json,archive,indent=4)

    def bubble_sort_by_total_time(self):
        n = len(self.json)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # Compara los elementos basados en "total_time"
                if self.json[j]["total_time"] < self.json[j + 1]["total_time"]:
                    # Intercambia los elementos si están en el orden incorrecto
                    self.json[j], self.json[j + 1] = self.json[j + 1], self.json[j]


    def draw(self):
        super().draw()
        print(self.json)

    def update(self):
        super().update()

    def run_game(self):
        while True:
           
            
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    self.exit()      


            self.update()
            self.draw()
            

            pygame.display.flip()
