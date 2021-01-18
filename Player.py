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
ani = 9
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

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.location = [0, 30]
        self.frame = 0
        self.health = 10
        self.damage = 0
        self.score = 0
        self.is_jumping = True
        self.is_falling = True
        self.images = []
        for i in range(1, 9):
            img = pygame.image.load(os.path.join('images', 'player', str(i) + '.png')).convert_alpha()
            #img.convert_alpha()
            #img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def gravity(self):
        if self.is_jumping:
            self.movey += 3.2

    def control(self, x, y):
        """
        control player movement
        """
        self.movex = x

    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

    def update(self):
        """
        Update sprite position
        """

        # moving left
        if self.movex < 0:
            self.is_jumping = True
            self.frame += 1
            self.image = pygame.transform.flip(self.images[self.frame % 8], True, False)

        # moving right
        if self.movex > 0:
            self.is_jumping = True
            self.frame += 1
            self.image = self.images[self.frame % 8]

        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for g in ground_hit_list:
            self.movey = 0
            self.rect.bottom = g.rect.top
            self.is_jumping = False  # stop jumping

        # fall off the world
        if self.rect.y > worldy:
            self.health -=1
            print(self.health)
            self.rect.x = tx
            self.rect.y = ty

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for p in plat_hit_list:
            self.is_jumping = False  # stop jumping
            self.movey = 0
            if self.rect.bottom <= p.rect.bottom:
               self.rect.bottom = p.rect.top
            else:
               self.movey += 3.2

        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.movey -= 33  # how high to jump

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)

        self.rect.x += self.movex
        self.movex = 0
        self.rect.y += self.movey


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
    main = True

    player = Player()  # spawn player
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

    while main:
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
                    main = False
            if pygame.key.get_pressed()[pygame.K_d]:
                player.control(steps, 0)
                BGX -= 1.4  # Move both background images back
                BGX2 -= 1.4

            if pygame.key.get_pressed()[pygame.K_a]:
                player.control(-steps, 0)
                BGX += 1.4  # Move both background images back
                BGX2 += 1.4

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                player.jump()

        # scroll the world forward
        if player.rect.x >= forwardx:
            scroll = player.rect.x - forwardx
            player.rect.x = forwardx
            for p in plat_list:
                p.rect.x -= scroll

        # scroll the world backward
        if player.rect.x <= backwardx:
            scroll = backwardx - player.rect.x
            player.rect.x = backwardx
            for p in plat_list:
                p.rect.x += scroll

        world.blit(BG, backdropbox)
        player.update()
        player.gravity()
        player_list.draw(world)
        ground_list.draw(world)
        plat_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)


