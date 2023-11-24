import os

#screen
SCREEN_TUPLE = (600, 500)
WIDTH, HEIGHT = SCREEN_TUPLE

#time, text and more
FPS = 60
SIZE_TEXT = 40
VOLUME = 1.00

SPEED_PLAYER = WIDTH / 50
JUMP_PLAYER = HEIGHT / 25
LIFE_PLAYER = 3
SIZE_PLAYER = (WIDTH / 5, HEIGHT / 5) 
FALL = -10
JUMP_ENEMY = 10
SIZE_ENEMY = (WIDTH / 5, HEIGHT / 5) 
LIFE_ENEMY = 1
SPEED_ENEMY = WIDTH / 50

#colors in RGB
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#paths
path = os.getcwd()
REAL_PATH = os.path.join(path,"assets")

#background paths
LEVEL_1 = os.path.join(REAL_PATH,"images\image_level_01.jpg")


#sounds paths
DAMAGE_SOUND = os.path.join(REAL_PATH,"sounds\damage_sound.mp3")
LEVEL_SOUND = os.path.join(REAL_PATH,"sounds\level_sound.mp3")  
LIFE_SOUND = os.path.join(REAL_PATH,"sounds\life_sound.mp3")
PRESENTATION_SOUND = os.path.join(REAL_PATH,"sounds\presentation_sound.wav")
SHOOT_SOUND = os.path.join(REAL_PATH,"sounds\shoot_sound.mp3")
TOASTY_SOUND = os.path.join(REAL_PATH,"sounds\\toasty_sound.mp3")

#image paths
ARTICUNO_SPRITES_LEFT = os.path.join(REAL_PATH,"images\\articuno_sprites.png")
BEEDRIL_SPRITES_LEFT = os.path.join(REAL_PATH,"images\\beedrill_sprites.png")
BULBASAUR_SPRITES_LEFT = os.path.join(REAL_PATH,"images\\bulbasaur_sprites.png")
CHARMANDER_SPRITES_LEFT = os.path.join(REAL_PATH,"images\charmander_sprites.png")
FINISH_GAME_IMAGE = os.path.join(REAL_PATH,"images\\finish_game_image.jpg")
FIRE_IMAGE = os.path.join(REAL_PATH,"images\\fire_image.png")
FRUIT_IMAGE = os.path.join(REAL_PATH,"images\\fruit_image.png")
MEWTWO_SPRITES_LEFT = os.path.join(REAL_PATH,"images\mewtwo_sprites.png")
MOLTRES_SPRITES_LEFT = os.path.join(REAL_PATH,"images\moltres_sprites.png")
PIKACHU_SPRITES_LEFT = os.path.join(REAL_PATH,"images\pikachu_sprites.png")
SHOOT_IMAGE = os.path.join(REAL_PATH,"images\shoot_image.png")
SNORLAX_SPRITES_LEFT = os.path.join(REAL_PATH,"images\snorlax_prites.png")
SQUIRTLE_SPRITES_LEFT = os.path.join(REAL_PATH,"images\squirtle_sprites.png")
TUNDER_IMAGE = os.path.join(REAL_PATH,"images\\thunder_image.png")
WHATER_IMAGE = os.path.join(REAL_PATH,"images\whater_image.png")
ZAPDOS_SPRITES_LEFT = os.path.join(REAL_PATH,"images\zapdos_sprites.png")
POKEBALL_IMAGE = os.path.join(REAL_PATH,"images\pokeball_image.png")