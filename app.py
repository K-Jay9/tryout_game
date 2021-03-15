# Importing pg

import pygame as pg

# import avatar movements
from avatar import slide, throw, blade, run, jump, jump_attack, jump_throw, glide, idle, dead, climb, attack

# Importing the sounds from utility 
from utility import bloody, rock, whack, game_intro, evil_laugh


# All the Game constants
HEIGHT = 720
WIDTH = 540
NAME = "My awesome Game 2.0"



# initialing avatar statistics

'''

We create a Projectile or blade class here

'''

class Projectile(object):

    def __init__(self, x,y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.velo = 5 

    # Draw the projectile to the screen

    def draw(self, win):
        pass # look for the draw function for an image projectile



def redrawGameWindow():
    pass # This function redraws the window for game statistics etc


# initialising pygame
pg.init()

# The set up of the window
pg.display.set_caption(NAME)

# load in the logo
logo = pg.image.load('mylogo.png')

# Display the logo as the game's Icon
pg.display.set_icon(logo)

# create a surface on screen
screen = pg.display.set_mode((HEIGHT, WIDTH))

# loop control variable
running = True 

while running:
    # gets all the events from the eevnt queue
    for event in pg.event.get():

        if event.type == pg.QUIT:
            # exit the while loop if quit is the event
            running = False

pg.quit()

