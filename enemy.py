"""
File with enemies. Contain main Enemy interface and detailed enemies classes. Slime, Fish.
"""
import os
import pygame
from armament import Axe


class Enemy(pygame.sprite.Sprite):
    """
    Enemy interface
    """

    def __init__(self, img_list):
        pygame.sprite.Sprite.__init__(self)
        self.frame_counter = 0
        self.images = []
        for img in img_list:
            self.images.append(pygame.image.load(os.path.join('images', 'enemies', str(img))).convert_alpha())
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.current_direction = 2
        self.movement_direction = 'horizontal'
        self.move_counter = 0
        self.distance = 200
        self.gravity = 0

    def move(self, x_step=0, y_step=0):
        """
        This change the enemy position in game.
        :param x_step:
        :param y_step:
        :return:
        """
        self.rect.x += x_step
        self.rect.y += y_step
        self.frame_counter += 1

    def update_sprite(self, vertical=False):
        """
        Method for update current image and create animation for enemy.
        :param vertical: enemy movement direction
        """
        if self.frame_counter > len(self.images) * 20:
            self.frame_counter = 0
        if self.current_direction < 0:
            self.image = self.images[self.frame_counter % len(self.images) - 1]
        else:
            self.image = pygame.transform.flip(self.images[self.frame_counter % len(self.images) - 1], True, vertical)

    def set_enemy_location(self, x_loc, y_loc, distance = 0):
        """
        Method for place enemy location on the game world with distance.
        :param x_loc: location on x axis
        :param y_loc: location on y axis
        :param distance: how many steps enemy will make during the move cycle
        """
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.distance = distance


class Slime(Enemy):
    """
    Simple enemy Slime class
    """

    def controller(self):
        """
        Main controller method for slime.
        """
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
        """
        Main controller method for fish.
        """
        self.update_sprite(True)
        self.move(0, self.current_direction)
        self.move_counter += 2
        #TODO add gravity
        #if self.current_direction < 0 or self.rect.y > self.world_y:
        #    self.gravity = 0
        #else:
        #    self.gravity = 2
        if self.move_counter == self.distance:
            self.current_direction *= -1
            self.move_counter *= -1


class Viking(Enemy):
    """
    Advanced enemy Viking class with attack
    """

    def __init__(self, img_list, attack_sprites, sight_range):
        Enemy.__init__(self, img_list)
        self.sight_range = sight_range
        self.current_direction = -2
        self.in_attack = False
        self.attack_counter = 0
        self.attack_speed = 0.5
        self.attack = []
        self.attack_sprites_len = len(attack_sprites)
        for img in attack_sprites:
            self.attack.append(pygame.image.load(os.path.join('images', 'enemies', 'viking', 'attack', str(img))).convert_alpha())

    def controller(self):
        """
        Main viking controller method.
        """
        if self.in_attack:
            self.attack_update()
            self.move(self.current_direction * 3, 0)
            self.move_counter += 3
        else:
            self.update_sprite()
            self.move(self.current_direction, 0)
            self.move_counter += 1
        if self.move_counter == self.distance:
            self.current_direction *= -1
            self.move_counter *= -1

    def attack_update(self):
        """
        Method for attack animation.
        """
        self.attack_counter += self.attack_speed
        if self.current_direction < 0:
            self.image = self.attack[int(self.attack_counter) % self.attack_sprites_len]
        else:
            self.image = pygame.transform.flip(self.attack[int(self.attack_counter) % self.attack_sprites_len], True, False)
        if self.attack_counter >= self.attack_sprites_len:
            self.attack_counter = 0
            self.in_attack = False

    def can_see_player(self, player_loc, sight_range):
        """
        Checking if player is in viking's field of view.
        :param player_loc: current player location
        :param sight_range: sight_range for 64 tiles on the X axis
        """
        if self.current_direction > 0:
            if self.rect.y - 50 <= player_loc[1] <= self.rect.y + 64 * 2 and self.rect.x < player_loc[0] < self.rect.x + 64 * sight_range:
                self.in_attack = True
        if self.current_direction < 0:
            if self.rect.y - 50 <= player_loc[1] <= self.rect.y + 64 * 2 and self.rect.x > player_loc[0] > self.rect.x - 64 * sight_range:
                self.in_attack = True


class VikingAxeThrower(Viking):
    """
    Advanced enemy Viking Axe Thrower, who attack on distance and stand in one place.
    """

    def __init__(self, img_list, attack_sprites, sight_range, throw_strength):
        Enemy.__init__(self, img_list)
        self.sight_range = sight_range
        self.throw_strength = throw_strength
        self.current_direction = -2
        self.in_attack = False
        self.attack_counter = 0
        self.attack_speed = 0.25
        self.attack = []
        self.attack_sprites_len = len(attack_sprites)
        for img in attack_sprites:
            self.attack.append(pygame.image.load(os.path.join('images', 'enemies', 'ax_thrower_viking', 'attack', str(img))).convert_alpha())

    def controller(self):
        """
        Viking Axe Thrower controller.
        """
        if self.in_attack:
            self.attack_update()
            if self.attack_counter == 5:
                return self.throw_axe()
        else:
            self.update_sprite()
            self.frame_counter += 1

    def throw_axe(self):
        return Axe(self.throw_strength, True, self.rect.x, self.rect.y)
