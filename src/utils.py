import random
from constants import *
import pygame
import sys

def random_number(numero_minimo:int=0,numero_maximo:int=20)->int:
    return random.randint(numero_minimo,numero_maximo)

def texto(text:str ,font = None, size_text : int = SIZE_TEXT,color : tuple = BLACK,x : float = WIDTH / 2,y : float = HEIGHT / 2,screen : pygame.surface = any) -> None:
    try:
        font = pygame.font.Font(font,size_text)
        texto_superficie = font.render(text,True,color)
        texto_rect = texto_superficie.get_rect()
        texto_rect.center = (x, y)
        bliteo_texto = screen.blit(texto_superficie, texto_rect)
    except:
        bliteo_texto = None
    return bliteo_texto




def generate_sound(path: str, volume: float= 0.6)->None:
    sound = pygame.mixer.Sound(path)
    sound.set_volume(volume)
    pygame.mixer.Sound.play(sound)

def mouse_pokeball(screen:pygame.surface,width : int = 40, height : int = 40)->None:
    # hace que imagen siga a mouse
    image = pygame.image.load(POKEBALL_IMAGE)  
    image = pygame.transform.scale(image,(width,height))
    image_rect = image.get_rect()  
    mouse_x, mouse_y = pygame.mouse.get_pos()
    image_rect.center = (mouse_x, mouse_y)
    pygame.mouse.set_visible(False)
    screen.blit(image, image_rect)  

def background_image_load(screen:pygame.surface,image:str)->None:
    bliting_image = pygame.image.load(image)
    bliting_image = pygame.transform.scale(bliting_image,SCREEN_TUPLE)
    bliting_image_rect = bliting_image.get_rect()
    screen.blit(bliting_image,bliting_image_rect)