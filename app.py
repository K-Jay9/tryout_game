# Importing pg

import pygame as pg

# import avatar movements
from avatar import slide, throw, blade, run, jump, jump_attack, jump_throw, glide, idle, dead, climb, attack


# All the Game constants
HEIGHT = 720
WIDTH = 540
NAME = "My awesome Game 2.0"
x = 0
y = 0



def main():
    
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

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)

if __name__ == '__main__':
    main()