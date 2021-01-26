"""
File with player class
"""
import os
import pygame

# Global Variables
PLA_ANIMATIONS = 10


class Player(pygame.sprite.Sprite):
    """
    Player class
    """

    def __init__(self, x_loc, y_loc):
        pygame.sprite.Sprite.__init__(self)
        self.start_location = (x_loc, y_loc)
        self.frame_counter = 0
        self.direction = "right"
        self.is_jumping = True
        self.is_falling = True
        self.in_air = True
        self.life = 2
        self.immortal_time = 20
        self.score = 0
        self.has_key = False
        self.walk = []
        for i in range(PLA_ANIMATIONS):
            img = pygame.image.load(os.path.join('images', 'player', 'walk', str(i) + '.png')).convert_alpha()
            self.walk.append(img)
        self.image = self.walk[0]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.vel_y = 0
        self.in_attack = False
        self.attack_counter = 0
        self.attack = []
        for i in range(PLA_ANIMATIONS):
            img = pygame.image.load(os.path.join('images', 'player', 'attack', str(i) + '.png')).convert_alpha()
            self.attack.append(img)
        self.stamina = 300

    def move(self, x_step=0, y_step=0):
        """
        This change the player position in game.
        :param x_step: steps to move on x axis
        :param y_step: steps to move on y axis
        """
        self.rect.x += x_step
        self.rect.y += y_step

    def update(self):
        """
        Method for update current image and create animation for player.
        """
        if self.immortal_time > 0:
            self.immortal_time -= 1
        if not self.in_attack:
            self.is_jumping = False
            if self.frame_counter > 100:
                self.frame_counter = 0
            if self.direction == 'right':
                self.image = self.walk[self.frame_counter % 8]
            else:
                self.image = pygame.transform.flip(self.walk[self.frame_counter % 8], True, False)

    def attack_update(self):
        """
        Method for attack animation.
        """
        if self.in_attack:
            self.attack_counter += 1
            if self.direction == 'right':
                self.image = self.attack[self.attack_counter % PLA_ANIMATIONS - 1]
            else:
                self.image = pygame.transform.flip(self.attack[self.attack_counter % PLA_ANIMATIONS - 1], True, False)
        if self.attack_counter == PLA_ANIMATIONS:
            self.in_attack = False

    def gravity(self):
        """
        Add gravity for player model in game.
        """
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.rect.y += self.vel_y

    def collision_checker(self, ground_list, plat_list, coins, key, doors, enemies_list):
        """
        Checker of player collision with anything in the game world.
        :param ground_list: list of all ground sprites (created with tiles)
        :param plat_list: list of sprites which represent platforms
        :param coins: list of coins sprite
        :param key: key sprite
        :param doors: doors sprite
        :param enemies_list: list of all enemies sprite
        :return: bool
        """
        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for ground in ground_hit_list:
            self.vel_y = 0
            self.rect.bottom = ground.rect.top
            self.in_air = False

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for plat in plat_hit_list:
            self.in_air = False
            self.vel_y = 0
            if self.rect.bottom <= plat.rect.bottom:
                self.rect.bottom = plat.rect.top
            else:
                self.vel_y += 3

        if pygame.sprite.spritecollide(self, coins, True):
            self.score += 1
            print(str(self.score))

        if pygame.sprite.spritecollide(self, key, True):
            self.has_key = True
            try:
                doors.sprites()[0].open_doors()
            except IndexError:
                pass
            print("Get key!")

        if pygame.sprite.spritecollide(self, doors, False) and self.has_key:
            print("Win game!")
            return True

        if self.in_attack:
            pygame.sprite.spritecollide(self, enemies_list, True)
        else:
            if pygame.sprite.spritecollide(self, enemies_list, False):
                if self.immortal_time == 0:
                    self.life -= 1
                    self.immortal_time = 20
                    if self.direction == 'right':
                        self.reset(self.rect.x - 64 * 3)
                    else:
                        self.reset(self.rect.x + 64 * 3)

        return False

    def fall_off_the_world(self):
        """
        Method to run when player fall fo the world and lose hp.
        """
        self.life -= 1
        self.reset(self.start_location[0])

    def reset(self, x_loc=0):
        """
        Method which reset player status.
        :param x_loc: param to set player location on X axis after reset
        """
        self.frame_counter = 0
        self.direction = "right"
        self.is_jumping = True
        self.is_falling = True
        self.in_air = True
        self.rect.x = x_loc
        self.rect.y = self.start_location[1] - 64 * 3
        self.vel_y = 0
        self.update()