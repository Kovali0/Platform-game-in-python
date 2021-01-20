import os
import pygame

'''
Global Variables
'''
PLA_ANIMATIONS_NUMBER = 9


class Player(pygame.sprite.Sprite):
    """
    Player class
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.start_location = (x, y)
        self.frame_counter = 0
        self.direction = "right"
        self.is_jumping = True
        self.is_falling = True
        self.in_air = True
        self.life = 2
        self.score = 0
        self.has_key = False
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
        self.vel_y = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        self.is_jumping = False
        if self.frame_counter > 100:
            self.frame_counter = 0
        if self.direction == 'right':
            self.image = self.images[self.frame_counter % 8]
        else:
            self.image = pygame.transform.flip(self.images[self.frame_counter % 8], True, False)

    def gravity(self):
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.rect.y += self.vel_y

    def collision_checker(self, ground_list, plat_list, coins, key, doors):
        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
        for g in ground_hit_list:
            self.vel_y = 0
            self.rect.bottom = g.rect.top
            self.in_air = False

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        for p in plat_hit_list:
            self.in_air = False
            self.vel_y = 0
            if self.rect.bottom <= p.rect.bottom:
                self.rect.bottom = p.rect.top
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

    def fall_off_the_world(self):
        self.life -= 1
        self.reset()

    def reset(self):
        self.frame_counter = 0
        self.direction = "right"
        self.is_jumping = True
        self.is_falling = True
        self.in_air = True
        self.rect.x = self.start_location[0]
        self.rect.y = self.start_location[1]
        self.vel_y = 0
        self.update()
