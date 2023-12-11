from constants import *
from window_screen import WindowScreen
from buttom import Button
import json




class HighScores(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,json_path,order_manage,screen) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path,screen)     
        self.back = Button([self.all_sprites_group],"Back",None,40,YELLOW,None,WIDTH-100,50,screen=self.screen)
        self.order_manage = order_manage
        self.json_path = json_path
        self.json_data = self.json_load(data_path=self.json_path)
        self.data_player = self.json_load(data_path=DATA_PLAYER_JSON)
        self.bubble_sort_by_total_time()
        self.json_data.append(self.data_player[0])
        self.bubble_sort_by_total_time()
        self.json_dump(self.json_path,self.json_data)
        
        
        
        self.first = Button([self.all_sprites_group],f"First: {self.json_data[0]['name']} Total time {self.json_data[0]['total_time']}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.second = Button([self.all_sprites_group],f"Second: {self.json_data[1]['name']} Total time {self.json_data[1]['total_time']}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
        self.third = Button([self.all_sprites_group],f"Third: {self.json_data[2]['name']} Total time {self.json_data[2]['total_time']}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+200,screen=self.screen)

    def button_logic(self):
        if self.back.pressed_button():
            self.active_bucle = False
            self.kill()

    def json_load(self,data_path):
        with open(data_path, 'r') as archive:
            return json.load(archive)

    def json_dump(json_path, data):
        with open(json_path, 'w') as archive:
            json.dump(data, archive)


    def bubble_sort_by_total_time(self):
        n = len(self.json_data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.json_data[j]["total_time"] < self.json_data[j + 1]["total_time"]:
                    self.json_data[j], self.json_data[j + 1] = self.json_data[j + 1], self.json_data[j]
        self.json_data[:2]

    def update(self):
        super().update()
        self.button_logic()
