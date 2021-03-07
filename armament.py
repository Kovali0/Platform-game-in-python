"""
File with class for armament, weapons and traps.
"""
import os

import numpy as np
import pygame


class Bullet(pygame.sprite.Sprite):
    """
    Class which objects represent various thrown things.
    """

    def __init__(self, speed, distance, stays_on_the_map):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.speed = speed
        self.distance = distance
        self.current_direction = -1
        self.frame_counter = 0
        self.move_counter = 0
        self.stays_on_map = stays_on_the_map
        self.is_moving = True

    def set_images(self, path, sprites_number):
        """
        Method for setting image for armament object.
        :param path: disc directory with image
        :param sprites_number: number od images to load
        """
        for i in range(1, sprites_number):
            self.images.append(pygame.image.load(os.path.join(path, str(i) + ".png")))
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def set_start_position(self, x_loc, y_loc):
        """
        Set the bullet position, when it will be spawned
        :param x_loc: x coordinate
        :param y_loc: y coordinate
        """
        self.rect.x = x_loc
        self.rect.y = y_loc

    def move(self, x_interval, y_interval):
        """
        Move bullet with x and y coordinates interval
        :param x_interval: x coordinate interval
        :param y_interval: y coordinate interval
        """
        self.rect.x += x_interval
        self.rect.y += y_interval

    def update(self):
        """
        Method for update current image and create animation for bullet.
        """
        if self.is_moving:
            if self.frame_counter > len(self.images) * 5:
                self.frame_counter = 0
            if self.current_direction < 0:
                self.image = self.images[int(self.frame_counter) % len(self.images) - 1]
            else:
                self.image = pygame.transform.flip(self.images[int(self.frame_counter) % len(self.images) - 1], True, False)

    def controller(self, scroll=0):
        """
        Virtual method, which need to be implemented for movable bullet objects.
        """
        pass


class Axe(Bullet):
    """
    Axe class
    """
    def __init__(self, speed, stays_on_the_map, x_loc, y_loc, direction):
        Bullet.__init__(self, speed, 0, stays_on_the_map)
        self.current_direction = direction
        path = "images/enemies/ax_thrower_viking/thrown_axe"
        self.on_ground_img = pygame.image.load(os.path.join(path, "axe_in_ground.png"))
        self.set_images(path, 9)
        self.set_start_position(x_loc, y_loc)

    def controller(self, scroll=0):
        """
        Controller for movement and mechanics of axe.
        :param scroll: x scroll distance when screen is scrolled to left or right.
        """
        if self.is_moving:
            self.update()
            if self.frame_counter % len(self.images) == 0:
                self.move(self.current_direction * self.speed, 2)
            else:
                self.move(self.current_direction * self.speed, 0)
            self.move_counter += 1
            self.frame_counter += 0.5
        else:
            self.image = self.on_ground_img


class HeavyAxe(Bullet):
    """
    Heavy Axe class
    """
    def __init__(self, speed, stays_on_the_map, x_loc, y_loc, direction, player_location):
        Bullet.__init__(self, speed, 0, stays_on_the_map)
        self.player_loc = list(player_location)
        self.current_direction = direction
        self.speed = 3.0
        path = "images/enemies/boss/axe"
        self.on_ground_img = pygame.image.load(os.path.join(path, "axe_in_ground.png"))
        self.set_images(path, 10)
        self.destroy_platforms = True
        self.boss_pos = np.array([x_loc, y_loc])
        self.position = self.boss_pos
        self.set_start_position(x_loc, y_loc)

    def controller(self, scroll=0):
        """
        Controller for movement and mechanics of heavy axe.
        :param scroll: x scroll distance when screen is scrolled to left or right.
        """
        if self.is_moving:
            self.update()
            self.player_loc[0] += scroll
            self.boss_pos[0] += scroll
            self.position[0] += scroll
            self.rect.centerx, self.rect.centery = self.find_next_position()
            self.move_counter += 1
            self.frame_counter += 0.5
        else:
            self.image = self.on_ground_img

    def find_next_position(self):
        """
        Special method for calculating next heavy axe position.
        :return: next position tuple in x and y coordinates
        """
        player_pos = np.array([self.player_loc[0], self.player_loc[1]])
        delta_pos = player_pos - self.boss_pos
        normalized = delta_pos / np.linalg.norm(delta_pos)
        speed_vector = normalized * self.speed
        next_axe_pos = self.position + speed_vector
        self.position = self.position + speed_vector
        return next_axe_pos


class ShockWave(Bullet):
    """
    ShockWave class
    """
    def __init__(self, speed, stays_on_the_map, x_loc, distance, direction):
        Bullet.__init__(self, speed, 0, stays_on_the_map)
        self.distance = distance
        self.current_direction = direction
        path = "images/enemies/boss"
        self.images.append(pygame.image.load(os.path.join(path, "shockwave.png")))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.set_start_position(x_loc, 780 - 128)

    def controller(self, scroll=0):
        """
        Shockwave mechanic controll funtion.
        :param scroll: x scroll distance when screen is scrolled to left or right.
        """
        self.update()
        if self.frame_counter % len(self.images) == 0:
            self.move(self.current_direction * self.speed, 0)
        else:
            self.move(self.current_direction * self.speed, 0)
        self.move_counter += 1
        self.frame_counter += 1
        if self.move_counter == self.distance:
            self.kill()


class Trap(pygame.sprite.Sprite):
    """
    Traps class
    """

    def __init__(self, x_loc, y_loc, img, dmg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'items', img))
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.damage = dmg
        self.is_moving = False
