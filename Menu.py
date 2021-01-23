import os
import pygame

'''
Global Variables
'''


class Button:
    def __init__(self, x, y, path):
        self.image = pygame.image.load(os.path.join('images', 'menu', path)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.respond = False

    def show(self, pos):
        self.respond = False
        self.clicked = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.respond = True
                self.clicked = True
        return self.respond


class Menu:
    def __init__(self, world):
        self.world = world
        self.bg = pygame.image.load(os.path.join('images', 'menu', 'menu_background_small.png'))
        self.bg_rect = self.bg.get_rect()
        self.bg_x = self.bg_rect.width
        self.bg_y = self.bg_rect.height
        self.start_btn = Button(128, self.bg_y - 128, 'start.png')
        self.exit_btn = Button(self.bg_x - 128 * 2, self.bg_y - 128, 'exit.png')

    def show_controllers(self):
        self.world.blit(self.start_btn.image, self.start_btn.rect)
        self.world.blit(self.exit_btn.image, self.exit_btn.rect)


class GameOverScreen:
    def __init__(self, world):
        self.world = world
        self.bg = pygame.image.load(os.path.join('images', 'menu', 'game_over_background.png'))
        self.bg_rect = self.bg.get_rect()
        self.bg_x = self.bg_rect.width
        self.bg_y = self.bg_rect.height
        self.back_btn = Button(256, self.bg_y - 384, 'back.png')

    def show_controllers(self):
        self.world.blit(self.back_btn.image, self.back_btn.rect)
