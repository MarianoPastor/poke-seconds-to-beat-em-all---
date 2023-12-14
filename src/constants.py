import os,pygame

#screen
SCREEN_TUPLE = (1000, 700)
WIDTH, HEIGHT = SCREEN_TUPLE

#time, text and more
TIME_FOR_LEVEL_1 = 30
TIME_FOR_LEVEL_2 = 40
TIME_FOR_LEVEL_3 = 50
FPS = 60
SIZE_TEXT = 40
VOLUME = 1.00
FX_VOLUME = 1
fx_change = 0
fx_volume_variable = FX_VOLUME + fx_change
FLOOR_LEVEL = HEIGHT - 50
TIME_FRAME_CHANGE = 100
ORDER_MANAGE = "total_time"
BERRY_SIZE = (40,45)
TIME_BERRYS = 300
ROCK_SIZE = (40,45)
MOUSE_SIZE = (25,25)
SPEED_PLAYER = 15
ATTACK_SPEED = 10
JUMP_PLAYER = HEIGHT / 3
LIFE_PLAYER = 5
SIZE_PLAYER = (WIDTH / 10, HEIGHT / 10) 
FALL = 10
JUMP_ENEMY = 10
SIZE_ENEMY = (WIDTH / 10, HEIGHT / 10) 
LIFE_ENEMY = 1
SPEED_ENEMY = 7
SIZE_BOSS = (WIDTH / 8, HEIGHT / 8)
LIFE_BOSS = 1
SPEED_BOSS = 7
PLATFORM_SPEED = 5

#dictionary of debility
DEBILITY_TUNDER = "tunder"
DEBILITY_WATER = "water"
DEBILITY_LEAF = "leaf"
DEBILITY_FIRE = "fire"


#colors in RGB
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#paths
comence_path = os.getcwd()
REAL_PATH_ASSETS = os.path.join(comence_path,"assets")
PATH_IMAGES = os.path.join(REAL_PATH_ASSETS,"images")
PATH_SOUNDS = os.path.join(REAL_PATH_ASSETS,"sounds")
PATH_ICONS_AND_MORE = os.path.join(PATH_IMAGES,"icons_and_more")

#background paths
BACKGROUNDS = os.path.join(PATH_IMAGES,"backgrounds")
LEVEL_1 = os.path.join(BACKGROUNDS,"level_01.jpg")
LEVEL_2 = os.path.join(BACKGROUNDS,"level_02.jpg")
LEVEL_3 = os.path.join(BACKGROUNDS,"level_03.jpg")
INTRO_BK = os.path.join(BACKGROUNDS,"intro_screen.jpg")
FINISH_GAME_IMAGE = os.path.join(BACKGROUNDS,"finish_game_image.jpg")
CONTROLS_BK = os.path.join(BACKGROUNDS,"controls_bk.jpg")


#scores paths
SCORES_JSON = os.path.join(comence_path,"src\scores.json")
DATA_PLAYER_JSON = os.path.join(comence_path,"src\data_player.json")

#sounds paths
DAMAGE_SOUND = os.path.join(PATH_SOUNDS,"damage_sound.mp3")
LEVEL_SOUND = os.path.join(PATH_SOUNDS,"level_sound.wav")  
LIFE_SOUND = os.path.join(PATH_SOUNDS,"life_sound.mp3")
PRESENTATION_SOUND = os.path.join(PATH_SOUNDS,"presentation_sound.wav")
SHOOT_SOUND = os.path.join(PATH_SOUNDS,"shoot_sound.mp3")
TOASTY_SOUND = os.path.join(PATH_SOUNDS,"toasty_sound.mp3")

#image paths
PIKACHU_SPRITES = os.path.join(PATH_IMAGES,"pikachu")
CHARMANDER_SPRITES = os.path.join(PATH_IMAGES,"charmander")
BULBASAUR_SPRITES = os.path.join(PATH_IMAGES,"bulbasaur")
SQUIRTLE_SPRITES = os.path.join(PATH_IMAGES,"squirtle")
MOLTRES_SPRITES = os.path.join(PATH_IMAGES,"moltres")
ZAPDOS_SPRITES = os.path.join(PATH_IMAGES,"zapdos")
ARTICUNO_SPRITES = os.path.join(PATH_IMAGES,"articuno")
BEEDRIL_SPRITES = os.path.join(PATH_IMAGES,"beedrill")
SNORLAX_SPRITES = os.path.join(PATH_IMAGES,"snorlax")
MEWTWO_SPRITES = os.path.join(PATH_IMAGES,"mewtwo")

#png paths
PLATFORM = os.path.join(PATH_ICONS_AND_MORE,"platform.png")
FIRE_IMAGE = os.path.join(PATH_ICONS_AND_MORE,"fire_image.png")
TUNDER_IMAGE = os.path.join(PATH_ICONS_AND_MORE,"thunder_image.png")
WHATER_IMAGE = os.path.join(PATH_ICONS_AND_MORE,"whater_image.png")
LEAF_IMAGE = os.path.join(PATH_ICONS_AND_MORE,"leaf_image.png")
ENERGY_BALL_IMAGE = os.path.join(PATH_ICONS_AND_MORE,"shoot_image.png")
FIREBALL_IMAGE = os.path.join(PATH_ICONS_AND_MORE,"fireball.png")

FRUIT_IMAGE = os.path.join(PATH_ICONS_AND_MORE,"fruit_image.png")
POKEBALL_IMAGE = os.path.join(PATH_ICONS_AND_MORE,"pokeball_image.png")

#image loaded
PLATFORM_LOADED = pygame.image.load(PLATFORM)