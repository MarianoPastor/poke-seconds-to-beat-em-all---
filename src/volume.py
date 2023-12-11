import pygame
from constants import *
from window_screen import WindowScreen
from buttom import Button


class Volume(WindowScreen):
    def __init__(self,sprite_groups,music_path, volume_float, background_path,screen) -> None:   
        super().__init__(sprite_groups,music_path, volume_float, background_path,screen=screen)     
        self.back = Button([self.all_sprites_group],"back",None,40,YELLOW,None,WIDTH-100,50,screen=self.screen)
    
        self.volume_on = Button([self.all_sprites_group],"Set volume no",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-200,screen=self.screen)
        self.volume_off = Button([self.all_sprites_group],"Set volume off",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-150,screen=self.screen)
        self.volume_up = Button([self.all_sprites_group],"Set volume up",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-100,screen=self.screen)
        self.volume_down = Button([self.all_sprites_group],"Set volume down",None,40,PURPLE,YELLOW,WIDTH/2,HEIGHT/2-50,screen=self.screen)
    

    def button_logic(self):
        if self.back.pressed_button():
            self.active_bucle = False
            self.kill()

        elif self.volume_on.pressed_button():
            pygame.mixer.music.play()
        elif self.volume_off.pressed_button():
            pygame.mixer.music.stop()

        elif self.volume_up.pressed_button():
            current_volume = pygame.mixer.music.get_volume()
            new_volume = current_volume + 0.02
            pygame.mixer.music.set_volume(new_volume)
        elif self.volume_down.pressed_button():
            current_volume = pygame.mixer.music.get_volume()
            new_volume = current_volume - 0.02
            pygame.mixer.music.set_volume(new_volume)
       
       

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

    def sum_volume(sound, increment):
        current_volume = sound.get_volume()
        new_volume = max(current_volume + increment, 1.0) 
        sound.set_volume(new_volume)
        return new_volume
    
    def rest_volume(sound, increment):
        current_volume = sound.get_volume()
        new_volume = min(current_volume + increment, 0.0) 
        sound.set_volume(new_volume)
        return new_volume
