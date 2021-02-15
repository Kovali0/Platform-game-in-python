"""
File with all menu and screens classes
"""
import os
import pygame


class Button:
    """
    Custom button class for pygame controls.
    """
    def __init__(self, x_loc, y_loc, path):
        self.image = pygame.image.load(os.path.join('images', 'menu', path)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x_loc
        self.rect.y = y_loc
        self.clicked = False
        self.respond = False

    def show(self, pos):
        """
        Show button and check if mouse click on button.
        :param pos: mouse position on the screen
        """
        self.respond = False
        self.clicked = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.respond = True
                self.clicked = True
        return self.respond


class Menu:
    """
    Main game menu class
    """
    def __init__(self, world):
        self.world = world
        self.background = pygame.image.load(os.path.join('images', 'menu', 'menu_background_small.png'))
        self.bg_rect = self.background.get_rect()
        self.bg_x = self.bg_rect.width
        self.bg_y = self.bg_rect.height
        self.start_btn = Button(128, self.bg_y - 128, 'start.png')
        self.exit_btn = Button(self.bg_x - 128 * 2, self.bg_y - 128, 'exit.png')

    def show_controllers(self):
        """
        Show all buttons and others controls for main menu screen.
        """
        self.world.blit(self.start_btn.image, self.start_btn.rect)
        self.world.blit(self.exit_btn.image, self.exit_btn.rect)


class GameOverScreen:
    """
    Game over screen class
    """
    def __init__(self, world):
        self.world = world
        self.background = pygame.image.load(os.path.join('images', 'menu', 'game_over_background.png'))
        self.bg_rect = self.background.get_rect()
        self.bg_x = self.bg_rect.width
        self.bg_y = self.bg_rect.height
        self.back_btn = Button(256, self.bg_y - 384, 'back.png')

    def show_controllers(self):
        """
        Show all buttons and others controls for game over screen.
        """
        self.world.blit(self.back_btn.image, self.back_btn.rect)

    def control_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.back_btn.show(mouse_pos):
                return False
        return True


class WinScreen:
    """
    Win screen class
    """
    def __init__(self, world):
        self.world = world
        self.background = pygame.image.load(os.path.join('images', 'menu', 'win_background.png'))
        self.bg_rect = self.background.get_rect()
        self.bg_x = self.bg_rect.width
        self.bg_y = self.bg_rect.height
        self.back_btn = Button(128, self.bg_y - 128, 'back.png')
        self.next_btn = Button(self.bg_x - 256, self.bg_y - 128, 'next.png')

    def show_controllers(self):
        """
        Show all buttons and others controls for level win screen.
        """
        self.world.blit(self.back_btn.image, self.back_btn.rect)
        self.world.blit(self.next_btn.image, self.next_btn.rect)

    def control_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.back_btn.show(mouse_pos):
                return False
            if self.next_btn.show(mouse_pos):
                return "next"
        return True
