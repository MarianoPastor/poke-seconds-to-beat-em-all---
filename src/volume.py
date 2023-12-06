import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button


class Volume(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path,screen=screen)     
        self.FX_off_flag = True
        self.volume_flag = True
        self.back = Button([self.all_sprites_group],"back",None,40,YELLOW,None,WIDTH-100,50,screen=self.screen)
        self.volume_off_on = Button([self.all_sprites_group],"Set volume off - on",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.FX_off_on = Button([self.all_sprites_group],"Set FX_colume off - on",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-150,screen=self.screen)
        self.volume_up = Button([self.all_sprites_group],"Set volume up",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2,screen=self.screen)
        self.volume_up = Button([self.all_sprites_group],"Set FX_volume up",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+50,screen=self.screen)
        self.volume_down = Button([self.all_sprites_group],"Set volume down",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+150,screen=self.screen)
        self.volume_down = Button([self.all_sprites_group],"Set FX_volume down",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2+200,screen=self.screen)
        Volume.load_music(self.music_path,self.volume_float)

    def button_logic(self):
        if self.back.pressed_button():
            self.active_bucle = False
            self.kill()
        elif self.volume_off_on.pressed_button():
            self.volume_flag != self.volume_flag
            VOLUME - VOLUME if not self.volume_flag else VOLUME == 1 
        elif self.FX_off_on.pressed_button():
            self.FX_off_on != self.FX_off_on
            FX_VOLUME - FX_VOLUME if not self.volume_flag else FX_VOLUME == 1 
        elif self.volume_up.pressed_button():
            self.volume_float += 0.1
        elif self.volume_down.pressed_button():
            self.volume_float -= 0.1

    def load_music(path: str, volume: float= VOLUME)->None:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume)

    def sound_fx(path: str, volume: float= VOLUME)->None:
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        pygame.mixer.Sound.play(sound)

    def update(self):
        super().update()
        self.button_logic()
    
    
        
        