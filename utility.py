

'''
This file contains game's development backend stuff
'''

import pygame as pg 

# impact sounds

# initialising pygame
pg.init()

bloody = pg.mixer.Sound('sounds/bloody.wav')
whack = pg.mixer.Sound('./sounds/whack.wav')
rock = pg.mixer.Sound('./sounds/rock.wav')


# game status sounds
# level_up = pg.mixer.Sound('./sounds/level_up.mp3')
# game_over = pg.mixer.Sound('./sounds/game_over.mp3')

game_intro = pg.mixer.Sound('./sounds/futuristic_dark.wav')
evil_laugh = pg.mixer.Sound('./sounds/evil_laugh.wav')


