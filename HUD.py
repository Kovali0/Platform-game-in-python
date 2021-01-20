import os
import pygame

'''
Global Variables
'''
WHITE = (255, 255, 255)


class Hud(pygame.sprite.Sprite):
    """
    HUD class
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.digits_images = []
        for i in range(10):
            img = pygame.image.load(os.path.join('images', 'hud', str(i) + '.png')).convert_alpha()
            self.digits_images.append(img)
        self.coin_image = pygame.image.load(os.path.join('images', 'hud', 'coin.png')).convert_alpha()
        self.x_image = pygame.image.load(os.path.join('images', 'hud', 'x.png')).convert_alpha()
        self.image = self.coin_image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.coin_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_score(self, sc):
        self.score = sc

    def status(self, world):
        world.blit(self.coin_image, (self.rect.x, self.rect.y))
        world.blit(self.x_image, (self.rect.x + 40, self.rect.y))
        world.blit(self.digits_images[self.score], (self.rect.x + 70, self.rect.y))

