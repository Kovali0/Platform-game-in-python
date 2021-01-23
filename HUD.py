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
        self.digits_images = []
        for i in range(10):
            img = pygame.image.load(os.path.join('images', 'hud', str(i) + '.png')).convert_alpha()
            self.digits_images.append(img)
        self.coin_image = pygame.image.load(os.path.join('images', 'hud', 'coin.png')).convert_alpha()
        self.x_image = pygame.image.load(os.path.join('images', 'hud', 'x.png')).convert_alpha()
        self.slash_image = pygame.image.load(os.path.join('images', 'hud', 'slash.png')).convert_alpha()
        self.heart_images = []
        self.heart_images.append(pygame.image.load(os.path.join('images', 'hud', 'empty_heart.png')).convert_alpha())
        self.heart_images.append(pygame.image.load(os.path.join('images', 'hud', 'half_heart.png')).convert_alpha())
        self.heart_images.append(pygame.image.load(os.path.join('images', 'hud', 'full_heart.png')).convert_alpha())
        self.key_images = []
        self.key_images.append(pygame.image.load(os.path.join('images', 'hud', 'empty_key.png')).convert_alpha())
        self.key_images.append(pygame.image.load(os.path.join('images', 'hud', 'gold_key.png')).convert_alpha())
        self.blue_images = []
        self.blue_images.append(pygame.image.load(os.path.join('images', 'hud', 'blue_empty_element.png')).convert_alpha())
        self.blue_images.append(pygame.image.load(os.path.join('images', 'hud', 'blue_element.png')).convert_alpha())
        self.rect = self.coin_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def print_status(self, world, score, life, key_status, player_stamina):
        world.blit(self.coin_image, (self.rect.x, self.rect.y))
        world.blit(self.x_image, (self.rect.x + 40, self.rect.y))
        world.blit(self.digits_images[score], (self.rect.x + 70, self.rect.y))
        world.blit(self.slash_image, (self.rect.x + 100, self.rect.y))
        world.blit(self.digits_images[9], (self.rect.x + 130, self.rect.y))
        world.blit(self.heart_images[life], (self.rect.x, self.rect.y + 50))
        world.blit(self.key_images[key_status], (self.rect.x, self.rect.y + 100))
        s1 = 1 if player_stamina >= 100 else 0
        s2 = 1 if player_stamina >= 200 else 0
        s3 = 1 if player_stamina == 300 else 0
        world.blit(self.blue_images[s1], (self.rect.x, self.rect.y + 150))
        world.blit(self.blue_images[s2], (self.rect.x + 50, self.rect.y + 150))
        world.blit(self.blue_images[s3], (self.rect.x + 100, self.rect.y + 150))