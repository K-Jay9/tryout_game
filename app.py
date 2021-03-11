# Importing pg

import pygame as pg

HEIGHT = 720
WIDTH = 540
NAME = "My awesome Game 2.0"


def main():
    
    # initialising pygame
    pg.init()

    # The set up of the window
    pg.display.set_caption(NAME)



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)

if __name__ == '__main__':
    main()