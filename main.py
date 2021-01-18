import os

import pygame
from pygame.locals import *
import sys
import random

'''
Variables
'''

worldx = 960
worldy = 720
fps = 40
PLA_ANIMATIONS_NUMBER = 9
world = pygame.display.set_mode([worldx, worldy])
forwardx  = 600
backwardx = 120

BLUE = (80, 80, 155)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 0, 0)

tx = 64
ty = 64

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.location = [0, 30]
        self.frame_counter = 0
        self.is_jumping = True
        self.is_falling = True
        self.images = []
        for i in range(1, PLA_ANIMATIONS_NUMBER):
            img = pygame.image.load(os.path.join('images', 'player', str(i) + '.png')).convert_alpha()
            self.images.append(img)
        self.image = self.images[0]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        if self.frame_counter > 100:
            self.frame_counter = 0
        if dx > 0:
            self.image = self.images[self.frame_counter % 8]
        else:
            self.image = pygame.transform.flip(self.images[self.frame_counter % 8], True, False)


# x location, y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'tiles', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc


class Level:
    def ground(lvl, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                ground = Platform(gloc[i], worldy - ty, tx, ty, 'green_tile_1.png')
                ground_list.add(ground)
                i = i + 1

        if lvl == 2:
            print("Level " + str(lvl))

        return ground_list

    # x location, y location, img width, img height, img file
    def platform(lvl, tx, ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        if lvl == 1:
            ploc.append((200, worldy - ty - 128, 3))
            ploc.append((300, worldy - ty - 256, 3))
            ploc.append((550, worldy - ty - 128, 4))
            while i < len(ploc):
                j = 0
                while j <= ploc[i][2]:
                    plat = Platform((ploc[i][0] + (j * tx)), ploc[i][1], tx, ty, 'green_tile_2.png')
                    plat_list.add(plat)
                    j = j + 1
                print('run' + str(i) + str(ploc[i]))
                i = i + 1

        if lvl == 2:
            print("Level " + str(lvl))

        return plat_list


if __name__ == '__main__':
    '''
    Setup
    '''
    BG = pygame.image.load(os.path.join('images', 'backgrounds', 'clouds_background.png'))
    BGX = 0
    BGX2 = BG.get_width()
    clock = pygame.time.Clock()
    pygame.init()
    backdropbox = world.get_rect()
    run = True

    player = Player(0, 30)  # spawn player
    player.rect.x = 0  # go to x
    player.rect.y = 30  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10

    eloc = []
    eloc = [300, worldy - ty - 80]
    gloc = []

    i = 0
    while i <= (worldx / tx) + tx:
        gloc.append(i * tx)
        i = i + 1

    ground_list = Level.ground(1, gloc, tx, ty)
    plat_list = Level.platform(1, tx, ty)

    '''
    Main Loop
    '''

    while run:
        if BGX < BG.get_width() * -1:  # If our bg is at the -width then reset its position
            BGX = BG.get_width()

        if BGX2 < BG.get_width() * -1:
            BGX2 = BG.get_width()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    run = False

        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            player.frame_counter += 1
            player.update(5, 0)
            BGX -= 1.4  # Move both background images back
            BGX2 -= 1.4

        if key[pygame.K_a]:
            player.frame_counter += 1
            player.update(-5, 0)
            BGX += 1.4  # Move both background images back
            BGX2 += 1.4

        if key[pygame.K_SPACE]:
            player.jump()

        if key[pygame.K_a] is False and key[pygame.K_d] is False:
            player.frame_counter = 0

        world.blit(BG, backdropbox)
        player_list.draw(world)
        ground_list.draw(world)
        plat_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)


