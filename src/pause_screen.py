from constants import *
from window_screen import WindowScreen
from buttom import Button



class PauseScreen(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path,screen=screen)  

        self.back = Button([self.all_sprites_group],"Back ",None,40,YELLOW,None,WIDTH-100,40,screen=self.screen)
        self.name = Button([self.all_sprites_group],"PAUSE",None,80,BLACK,WHITE,WIDTH/2,HEIGHT/2,screen=self.screen)

    def button_logic(self):
        if self.back.pressed_button():
            self.active_bucle = False
            self.kill()
    
    def update(self):
        super().update()
        self.button_logic()
    