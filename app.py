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



# initialising pygame
pg.init()

# The set up of the window
pg.display.set_caption(NAME)

# load in the logo and background Image
logo = pg.image.load('mylogo.png')
bg = pg.image.load('./Theme/png/BG.png')
bg = pg.transform.scale(bg, (HEIGHT, WIDTH))

# Display the logo as the game's Icon
pg.display.set_icon(logo)

# create a surface on screen
screen = pg.display.set_mode((HEIGHT, WIDTH))

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
    # This function redraws the window for game statistics etc
    screen.blit(bg, (0,0))

    pg.display.update()



# loop control variable
running = True 

while running:
    # gets all the events from the eevnt queue
    for event in pg.event.get():

        if event.type == pg.QUIT:
            # exit the while loop if quit is the event
            running = False

    # redrawing the window
    redrawGameWindow()

pg.quit()

