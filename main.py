import os
import pygame
import sys
from pygame.locals import *
import random
from Player import Player
from Level import Level, Platform

'''
Global Variables
'''
FPS = 50
WORLD_X = 960
WORLD_Y = 780
WORLD = pygame.display.set_mode([WORLD_X, WORLD_Y])
FORWARD_X = 600
BACKWARD_X = 120
# Tiles size x-width y-high
TX = 64
TY = 64

if __name__ == '__main__':
    '''
    Setup
    '''
    BG = pygame.image.load(os.path.join('images', 'backgrounds', 'clouds_background.png'))
    BGX = 0
    BGX2 = BG.get_width()
    clock = pygame.time.Clock()
    pygame.init()
    backdropbox = WORLD.get_rect()
    run = True

    player = Player(0, WORLD_Y - TY)  # spawn player
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10

    p_loc = [(TX * 3, WORLD_Y - TY - 192, 3),
             (TX * 8, WORLD_Y - TY - 384, 3),
             (TX * 13, WORLD_Y - TY - 576, 6),
             (TX * 21, WORLD_Y - TY - 384, 2),
             (TX * 28, WORLD_Y - TY - 192, 1),
             (TX * 31, WORLD_Y - TY - 384, 1),
             (TX * 34, WORLD_Y - TY - 576, 3),
             (TX * 39, WORLD_Y - TY - 192, 2),
             (TX * 43, WORLD_Y - TY - 384, 2),
             (TX * 49, WORLD_Y - TY - 384, 1)]
    water_points = [-10, -9, -8, -7, -6, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 31, 60, 61, 62, 63, 64, 65]
    first_level = Level(1, TX, TY, WORLD_Y, water_points, 65, p_loc)

    ground_list = first_level.ground_list
    water_list = first_level.water_list
    plat_list = first_level.plat_list

    '''
    Game Loop
    '''
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    run = False

        player.collision_checker(ground_list, plat_list)

        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            player.frame_counter += 1
            player.direction = "right"
            player.move(5, 0)

        if key[pygame.K_a]:
            player.frame_counter += 1
            player.direction = "left"
            player.move(-5, 0)

        if key[pygame.K_SPACE] and player.is_jumping == False and player.in_air == False:
            player.vel_y = -25
            player.is_jumping = True
            player.in_air = True

        if key[pygame.K_a] is False and key[pygame.K_d] is False:
            player.frame_counter = 0

        if player.rect.x >= FORWARD_X:
            scroll = player.rect.x - FORWARD_X
            player.rect.x = FORWARD_X
            for p in plat_list:
                p.rect.x -= scroll
            for g in ground_list:
                g.rect.x -= scroll
            for w in water_list:
                w.rect.x -= scroll

        if player.rect.x <= BACKWARD_X:
            scroll = BACKWARD_X - player.rect.x
            player.rect.x = BACKWARD_X
            for p in plat_list:
                p.rect.x += scroll
            for g in ground_list:
                g.rect.x += scroll
            for w in water_list:
                w.rect.x += scroll

        WORLD.blit(BG, backdropbox)
        player.gravity()
        player.update()
        player_list.draw(WORLD)
        ground_list.draw(WORLD)
        water_list.draw(WORLD)
        plat_list.draw(WORLD)
        pygame.display.flip()
        clock.tick(FPS)
