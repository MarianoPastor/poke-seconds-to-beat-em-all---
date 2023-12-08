from constants import *
from window_screen import WindowScreen
from buttom import Button
from volume import Volume


class Looser(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen,player,time) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path,screen)  

        self.player = player
        self.time = time
        self.looser = Button([self.all_sprites_group,],"YOU LOOSE!",None,80,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.life_rm = Button([self.all_sprites_group],f"Lifes remaining {self.player.life}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-100,screen=self.screen)
        self.time_rm = Button([self.all_sprites_group],f"Time remaining {self.time}",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
        self.back = Button([self.all_sprites_group],"Back ",None,40,PURPLE,YELLOW,WIDTH-100,40,screen=self.screen)

    def button_logic(self):
        if self.back.pressed_button():
            self.active_bucle = False
            self.kill()
            self.back_sound = Volume.load_music(self.music_path,self.volume_float)

    def update(self):
        super().update()
        self.button_logic()
        
