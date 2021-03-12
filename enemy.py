"""
File with enemies. Contain main Enemy interface and detailed enemies classes. Slime, Fish.
"""
import os

import numpy as np
import pygame
from math import copysign
from armament import Axe, HeavyAxe, ShockWave


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
        if self.move_counter >= self.distance:
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

    def __init__(self, img_list, attack_sprites, sight_range, throw_strength, direction=-2):
        Enemy.__init__(self, img_list)
        self.sight_range = sight_range
        self.throw_strength = throw_strength
        self.current_direction = direction
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
        """
        Spawn armament object - axe
        :return Axe armament object.
        """
        return Axe(self.throw_strength, True, self.rect.x, self.rect.y, copysign(1, self.current_direction))


class BossViking(Viking):
    """
    Viking boss
    """

    def __init__(self, img_list, attack_sprites, death_sprites, charge_sprites, sight_range):
        Viking.__init__(self, img_list, attack_sprites, sight_range)
        self.player_loc = ()
        self.sight_range = sight_range
        self.current_direction = 2
        self.health_points = 5
        self.in_attack = False
        self.in_charge = False
        self.is_death = False
        self.can_throw_axe = False
        self.drop_key = False
        self.immortal = 0
        self.attack_counter = 0
        self.attack_speed = 0.5
        self.attack_cooldown = 0
        self.axe_throw_cooldown = 0
        self.charge_cooldown = 0
        self.attack = []
        self.attack_sprites_len = len(attack_sprites)
        for img in attack_sprites:
            self.attack.append(pygame.image.load(os.path.join('images', 'enemies', 'boss', 'attack', str(img))).convert_alpha())
        self.charge = []
        self.charge_sprites_len = len(charge_sprites)
        for img in charge_sprites:
            self.charge.append(pygame.image.load(os.path.join('images', 'enemies', 'boss', 'charge', str(img))).convert_alpha())
        self.death = []
        self.death_sprites_len = len(death_sprites)
        self.death_counter = 0
        for img in death_sprites:
            self.death.append(pygame.image.load(os.path.join('images', 'enemies', 'boss', 'death', str(img))).convert_alpha())

    def controller(self):
        """
        Boss controller.
        """
        if not self.is_death:
            if self.immortal > 0:
                self.immortal -= 1

            if self.axe_throw_cooldown > 0:
                self.axe_throw_cooldown -= 1
            elif self.can_throw_axe:
                self.attack_update()
                if self.attack_counter == 5:
                    self.axe_throw_cooldown = 180
                    self.can_throw_axe = False
                    return self.throw_axe()

            if self.charge_cooldown > 0:
                self.charge_cooldown -= 1
            elif self.in_charge:
                self.charge_update()
                self.move(self.current_direction * 4, 0)
                self.move_counter += 4
                if self.attack_counter == 0:
                    self.charge_cooldown = 120
            elif self.attack_cooldown > 0:
                self.attack_cooldown -= 1
            elif self.in_attack and not self.can_throw_axe:
                self.attack_update()
                if self.attack_counter == 8:
                    self.attack_cooldown = 120
                    return ShockWave(8, True, self.rect.x, 50, copysign(1, self.current_direction))
            else:
                self.update_sprite()
                self.move(self.current_direction, 0)
                self.move_counter += 1

            if self.move_counter >= self.distance:
                self.current_direction *= -1
                self.move_counter *= -1
                self.in_charge = False
        else:
            if self.death_counter < 9:
                self.death_counter += 0.25
            if self.current_direction < 0:
                self.image = self.death[int(self.death_counter) % len(self.death)]
            else:
                self.image = pygame.transform.flip(self.death[int(self.death_counter) % len(self.death)], True, False)

    def can_see_player(self, player_loc, sight_range):
        """
        Checking if player is in viking's field of view.
        :param player_loc: current player location
        :param sight_range: sight_range for 64 tiles on the X axis
        """
        self.player_loc = player_loc
        if self.rect.y - 192 > player_loc[1]:
            self.can_throw_axe = True
            self.in_attack = True
        if self.current_direction > 0:
            if self.rect.y - 50 <= player_loc[1] <= self.rect.y + 64 * 2:
                if self.rect.x < player_loc[0] < self.rect.x + 64 * (sight_range/3):
                    self.in_attack = True
                elif self.rect.x < player_loc[0] < self.rect.x + 64 * sight_range:
                    self.in_charge = True
        if self.current_direction < 0:
            if self.rect.y - 50 <= player_loc[1] <= self.rect.y + 64 * 2:
                if self.rect.x > player_loc[0] > self.rect.x - 64 * (sight_range/3):
                    self.in_attack = True
                elif self.rect.x > player_loc[0] > self.rect.x - 64 * sight_range:
                    self.in_charge = True

    def charge_update(self):
        """
        Method for charge animation.
        """
        self.attack_counter += 0.5
        if self.current_direction < 0:
            self.image = self.charge[int(self.attack_counter) % self.attack_sprites_len]
        else:
            self.image = pygame.transform.flip(self.charge[int(self.attack_counter) % self.attack_sprites_len], True, False)
        if self.attack_counter >= self.attack_sprites_len * 4:
            self.attack_counter = 0
            self.in_attack = False
            self.in_charge = False

    def throw_axe(self):
        """
        Spawn armament object - heavy axe, when Boss is using throw attack.
        :return HeavyAxe object.
        """
        return HeavyAxe(5, True, self.rect.centerx, self.rect.centery, copysign(1, self.current_direction), self.player_loc)

    def get_hit(self, pts):
        """
        Method handling boss taken dmg.
        :param pts: damage points
        """
        if self.health_points - pts <= 0:
            self.is_death = True
            self.drop_key = True
        else:
            self.health_points -= pts
            self.immortal = 120
