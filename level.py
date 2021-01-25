"""
File with classes use to create level.
"""
import os
import pygame

# Global Variables
BLUE = (80, 80, 155)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 0, 0)


class Platform(pygame.sprite.Sprite):
    """
    Basic platform class
    """
    def __init__(self, loc_x, loc_y, img, is_water=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'tiles', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = loc_x
        self.rect.y = loc_y
        self.is_water = is_water


class Level:
    """
    Level class
    """
    def __init__(self, lvl, tile_x, tile_y, world_y, water_points, ground_len, plat_locations):
        self.level = lvl
        self.tile_x = tile_x
        self.tile_y = tile_y
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
        """
        Ground builder
        """
        i = -10
        while i < self.ground_len:
            if i in self.water_points:
                water = Platform(i * self.tile_x, self.world_y - self.tile_y, 'water_tile_1.png', True)
                self.water_list.add(water)
            else:
                ground = Platform(i * self.tile_x, self.world_y - self.tile_y, 'green_tile_1.png')
                self.ground_list.add(ground)
            i = i + 1

    def platforms(self):
        """
        Platforms builder
        """
        i = 0
        while i < len(self.plat_locations):
            j = 0
            while j <= self.plat_locations[i][2]:
                plat = Platform((self.plat_locations[i][0] + (j * self.tile_x)), self.plat_locations[i][1], 'green_tile_2.png')
                self.plat_list.add(plat)
                j = j + 1
            i = i + 1

    def set_coins(self, locations):
        """
        Coins setter on the level
        :param locations: list of tuples with x and y locations for coins
        """
        for location in locations:
            x_loc, y_loc = location
            coin = Coin(x_loc * self.tile_x, y_loc)
            self.coins_list.add(coin)

    def set_key(self, location):
        """
        Key setter on the level
        :param location: location in form of tuple with key location
        """
        x_loc, y_loc = location
        key = Key(x_loc * self.tile_x, y_loc)
        self.key.add(key)

    def set_doors(self, location):
        """
        Doors setter on the level
        :param location: location in form of tuple with doors location
        """
        x_loc, y_loc = location
        doors = Doors(x_loc * self.tile_x, y_loc)
        self.doors.add(doors)


class Coin(pygame.sprite.Sprite):
    """
    Coin class
    """
    def __init__(self, x_loc, y_loc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'items', 'gold_coin.png')).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x_loc, y_loc)


class Key(pygame.sprite.Sprite):
    """
    Key class
    """
    def __init__(self, x_loc, y_loc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'items', 'key.png')).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x_loc, y_loc)


class Doors(pygame.sprite.Sprite):
    """
    Doors class
    """
    def __init__(self, x_loc, y_loc):
        pygame.sprite.Sprite.__init__(self)
        self.doors = []
        self.doors.append(pygame.image.load(os.path.join('images', 'tiles', 'closed_doors.png')).convert_alpha())
        self.doors.append(pygame.image.load(os.path.join('images', 'tiles', 'open_doors.png')).convert_alpha())
        self.image = self.doors[0]
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc

    def open_doors(self):
        """
        Change doors sprite from closed to opened doors.
        """
        self.image = self.doors[1]
