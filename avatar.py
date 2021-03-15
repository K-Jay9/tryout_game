
'''
The sprites of the avatar and also the enemy
'''

# import the necessary libraries


import pygame as pg

# avatar images for activity
attack = [pg.image.load(f'images/Attack__00{i}.png') for i in range(10)]


climb = [pg.image.load(f'images/Climb_00{i}.png') for i in range(10)]

dead = [pg.image.load(f'images/Dead__00{i}.png') for i in range(10)]

glide = [pg.image.load(f'images/Glide_00{i}.png') for i in range(10)]

idle = [pg.image.load(f'images/Idle__00{i}.png') for i in range(10)]

jump = [pg.image.load(f'images/Jump__00{i}.png') for i in range(10)]

jump_attack = [pg.image.load(f'images/Jump_Attack__00{i}.png') for i in range(10)]

jump_throw = [pg.image.load(f'images/Jump_Throw__00{i}.png') for i in range(10)]

run = [pg.image.load(f'images/Run__00{i}.png') for i in range(10)]

slide = [pg.image.load(f'images/Slide__00{i}.png') for i in range(10)]

throw = [pg.image.load(f'images/Throw__00{i}.png') for i in range(10)]


# or dagger
blade = pg.image.load('images/Kunai.png')




# loading the sprites of the game
all_sprite_list = pg.sprite.Group()
n = 1
j = -10
while n <= 16:
    image = pg.image.load(f"Theme/png/Tiles/Tile ({n}).png")

    tile = pg.sprite.Sprite()
    tile.image = image
    tile.rect = image.get_rect()
    tile.rect.x = j
    tile.rect.y = 450
    all_sprite_list.add(tile)
    n += 1
    j += 50

print(len(all_sprite_list))



# The class Player of the avatar

class Player(object):
    def __init__(self, x,y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.standing = True
        self.right = False
        self.left = False
        self.walkCount = 0

        
        # Initialise the booleans next
    '''
    Tinker with the following class methods
    '''
    def draw(self, win): # the equivalence of moving for the enemy
        now = run[0]
        now = pg.transform.scale(now, (50,50))
        win.blit(now, (self.x, self.y))
                

    def hit(self):
        pass




class Enemy(object):

    def __init__(self, x,y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end

    '''
    Tinker with the following class methods
    '''
    def draw(self):
        pass

    def move(self):
        pass

    def hit(self):
        pass

    
