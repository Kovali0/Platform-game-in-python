"""
File with class for armament, weapons and traps.
"""
import os
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
        for i in range(1, sprites_number):
            self.images.append(pygame.image.load(os.path.join(path, str(i) + ".png")))
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def set_start_position(self, x_loc, y_loc):
        self.rect.x = x_loc
        self.rect.y = y_loc

    def move(self, x_interval, y_interval):
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


class Axe(Bullet):
    """
    Axe class
    """
    def __init__(self, speed, stays_on_the_map, x_loc, y_loc):
        Bullet.__init__(self, speed, 0, stays_on_the_map)
        path = "images/enemies/ax_thrower_viking/thrown_axe"
        self.on_ground_img = pygame.image.load(os.path.join(path, "axe_in_ground.png"))
        self.set_images(path, 9)
        self.set_start_position(x_loc, y_loc)

    def controller(self):
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

    def controller(self):
        pass
