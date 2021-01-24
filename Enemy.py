import os
import pygame

'''
Global Variables
'''
PLA_ANIMATIONS_NUMBER = 9


class Enemy(pygame.sprite.Sprite):
    """
    Enemy interface
    """

    def __init__(self, img_list):
        pygame.sprite.Sprite.__init__(self)
        self.frame_counter = 0
        self.images = []
        for ig in img_list:
            self.images.append(pygame.image.load(os.path.join('images', 'enemies', str(ig))).convert_alpha())
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.current_direction = 2
        self.movement_direction = 'horizontal'
        self.move_counter = 0
        self.distance = 200
        self.gravity = 0

    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy
        self.frame_counter += 1

    def update_sprite(self, vertical=False):
        if self.frame_counter > len(self.images) * 20:
            self.frame_counter = 0
        if self.current_direction < 0:
            self.image = self.images[self.frame_counter % len(self.images) - 1]
        else:
            self.image = pygame.transform.flip(self.images[self.frame_counter % len(self.images) - 1], True, vertical)

    def set_enemy_location(self, x, y, distance):
        self.rect.x = x
        self.rect.y = y
        self.distance = distance


class Slime(Enemy):
    """
    Simple enemy Slime class
    """

    def controller(self):
        self.update_sprite()
        self.move(self.current_direction, 0)
        self.move_counter += 1
        if self.move_counter == self.distance:
            self.current_direction *= -1
            self.move_counter *= -1


class Fish(Enemy):
    """
    Simple enemy Fish class
    """

    def __init__(self, img_list, world_y):
        Enemy.__init__(self, img_list)
        self.world_y = world_y

    def controller(self):
        self.update_sprite(True)
        self.move(0, self.current_direction + self.gravity)
        self.move_counter += 1
        if self.current_direction < 0 or self.rect.y > self.world_y:
            self.gravity = 0
        else:
            self.gravity = 2
        if self.move_counter == self.distance:
            self.current_direction *= -1
            self.move_counter *= -1
