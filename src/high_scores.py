import pygame,playing
from constants import *
from window_screen import WindowScreen
from buttom import Button
import json
from volume import Volume




class HighScores(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,json_path,order_manage) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path)     
        self.back = Button([self.all_sprites,self.buttons_group],"Back",None,40,YELLOW,None,WIDTH-100,50,screen=self.screen)
        self.volume_botton = Button([self.all_sprites,self.buttons_group],"Sounds",None,40,YELLOW,None,100,50,screen=self.screen)
        self.order_manage = order_manage
        self.json_path = json_path
        self.json = self.json_load()
        self.bubble_sort_by_total_time()
        
        self.first = Button([self.all_sprites,self.buttons_group],f"First: {self.json[0]['name']} Total time {self.json[0]['total_time']}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.second = Button([self.all_sprites,self.buttons_group],f"Second: {self.json[1]['name']} Total time {self.json[1]['total_time']}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
        self.third = Button([self.all_sprites,self.buttons_group],f"Third: {self.json[2]['name']} Total time {self.json[2]['total_time']}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+200,screen=self.screen)
    
    def player_creator(self):
        player = {"total_time":playing.Playing.total_time,"level_1_time":playing.Playing.total_time,"level_2_time":playing.Playing.total_time,"level_3_time":playing.Playing.total_time,"name":input("como te llamas?: ")[:5].upper()}
        self.json_add(player)

    def json_add(self,player):
        with open(SCORES_JSON, "a") as archive:
            json.dump(player, archive)

    def button_logic(self):
        if self.back.pressed_button():
            self.playing = False
            self.kill()
        elif self.volume_botton.pressed_button():
            self.screen_seen = Volume(sprite_groups=[self.all_sprites],music_path=PRESENTATION_SOUND,volume_float=VOLUME,background_path=CONTROLS_BK)
            self.screen_seen.playing = True
            self.screen_seen.run_game()
            self.kill()

    def json_load(self):
        with open(self.json_path, 'r') as archive:
            return json.load(archive)

    def json_dump(self):
        with open(self.json_path, 'w') as archive:
            json.dump(self.json[:3],archive)

    def bubble_sort_by_total_time(self):
        n = len(self.json)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # Compara los elementos basados en "total_time"
                if self.json[j]["total_time"] > self.json[j + 1]["total_time"]:
                    # Intercambia los elementos si están en el orden incorrecto
                    self.json[j], self.json[j + 1] = self.json[j + 1], self.json[j]


    def update(self):
        super().update()
        self.button_logic()
