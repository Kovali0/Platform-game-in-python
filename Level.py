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
        self.coins_list = pygame.sprite.Group()
        self.key = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.water_points = water_points
        self.plat_locations = plat_locations
        self.ground_len = ground_len
        self.ground()
        self.platforms()

    def ground(self):
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

    def set_coins(self, locations):
        for i in range(len(locations)):
            x, y = locations[i]
            coin = Coin(x * self.tx, y)
            self.coins_list.add(coin)

    def set_key(self, location):
        x, y = location
        key = Key(x * self.tx, y)
        self.key.add(key)

    def set_doors(self, location):
        x, y = location
        doors = Doors(x * self.tx, y)
        self.doors.add(doors)


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'items', 'gold_coin.png')).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'items', 'key.png')).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Doors(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.doors = []
        self.doors.append(pygame.image.load(os.path.join('images', 'tiles', 'closed_doors.png')).convert_alpha())
        self.doors.append(pygame.image.load(os.path.join('images', 'tiles', 'open_doors.png')).convert_alpha())
        self.image = self.doors[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def open_doors(self):
        self.image = self.doors[1]