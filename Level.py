import os
import pygame

'''
Global Variables
'''
BLUE = (80, 80, 155)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 0, 0)


class Platform(pygame.sprite.Sprite):
    """
    Simple platform class
    """

    def __init__(self, xloc, yloc, imgw, imgh, img, is_water=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'tiles', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc
        self.is_water = is_water


class Level:
    """
    Level class
    """

    def __init__(self, lvl, tx, ty, world_y, water_points, ground_len, plat_locations):
        self.level = lvl
        self.tx = tx
        self.ty = ty
        self.world_y = world_y
        self.ground_list = pygame.sprite.Group()
        self.water_list = pygame.sprite.Group()
        self.plat_list = pygame.sprite.Group()
        self.water_points = water_points
        self.plat_locations = plat_locations
        self.ground_len = ground_len
        self.gen_ground()
        self.platforms()

    def gen_ground(self):
        i = -10
        while i < self.ground_len:
            if i in self.water_points:
                water = Platform(i * self.tx, self.world_y - self.ty, self.tx, self.ty, 'water_tile_1.png', True)
                self.water_list.add(water)
            else:
                ground = Platform(i * self.tx, self.world_y - self.ty, self.tx, self.ty, 'green_tile_1.png')
                self.ground_list.add(ground)
            i = i + 1

    def platforms(self):
        i = 0
        while i < len(self.plat_locations):
            j = 0
            while j <= self.plat_locations[i][2]:
                plat = Platform((self.plat_locations[i][0] + (j * self.tx)), self.plat_locations[i][1], self.tx, self.ty, 'green_tile_2.png')
                self.plat_list.add(plat)
                j = j + 1
            i = i + 1