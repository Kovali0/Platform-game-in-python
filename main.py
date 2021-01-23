import os
import pygame
import sys
from Player import Player
from Level import Level
from HUD import Hud
from Menu import Menu, GameOverScreen
from Enemy import Slime

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


def scroll_elements(elements_list, forward, scroller):
    for el in elements_list:
        if forward:
            el.rect.x -= scroller
        else:
            el.rect.x += scroller


if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()
    run = True
    in_menu = True
    in_game = False
    mouse_pos = (0, 0)

    while run:
        '''
        Menu part
        '''
        menu = Menu(WORLD)
        while in_menu:
            WORLD.blit(menu.bg, menu.bg.get_rect())
            menu.show_controllers()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if menu.start_btn.show(mouse_pos):
                        in_game = True
                        in_menu = False

                    if menu.exit_btn.show(mouse_pos):
                        pygame.quit()
                        try:
                            sys.exit()
                        finally:
                            run = False

            pygame.display.flip()
            clock.tick(FPS)

        '''
        Setup game
        '''
        BG = pygame.image.load(os.path.join('images', 'backgrounds', 'clouds_background.png'))
        game_over_screen = GameOverScreen(WORLD)
        run = True

        player = Player(0, WORLD_Y - TY)  # spawn player
        player_list = pygame.sprite.Group()
        player_list.add(player)
        steps = 10

        hud = Hud(0, 0)

        p_loc = [(TX * 3, WORLD_Y - TY - 192, 3),
                 (TX * 8, WORLD_Y - TY - 384, 3),
                 (TX * 13, WORLD_Y - TY - 576, 6),
                 (TX * 21, WORLD_Y - TY - 384, 2),
                 (TX * 28, WORLD_Y - TY - 192, 1),
                 (TX * 31, WORLD_Y - TY - 384, 1),
                 (TX * 34, WORLD_Y - TY - 576, 3),
                 (TX * 39, WORLD_Y - TY - 192, 2),
                 (TX * 43, WORLD_Y - TY - 384, 2),
                 (TX * 49, WORLD_Y - TY - 384, 1),
                 (TX * 62, WORLD_Y - TY - 192, 0)]
        water_points = [-10, -9, -8, -7, -6, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 31, 60, 61, 62, 63, 64, 65]
        first_level = Level(1, TX, TY, WORLD_Y, water_points, 65, p_loc)
        coins_locations = [(-3, WORLD_Y - TY * 1.5),
                           (4, WORLD_Y - TY * 4.5),
                           (10, WORLD_Y - TY * 1.5),
                           (18, WORLD_Y - TY * 10.5),
                           (22, WORLD_Y - TY * 1.5),
                           (29, WORLD_Y - TY * 4.5),
                           (36, WORLD_Y - TY * 10.5),
                           (50, WORLD_Y - TY * 7.5),
                           (62.5, WORLD_Y - TY * 4.5)]
        first_level.set_coins(coins_locations)
        first_level.set_key((55, WORLD_Y - TY * 1.5))
        first_level.set_doors((44, WORLD_Y - TY * 9))

        blue_slime_imgs = ["slimeBlue.png"]
        blue_slime = Slime(blue_slime_imgs)
        blue_slime.set_enemy_location(TX * 10, WORLD_Y - TY * 2, 128)

        ground_list = first_level.ground_list
        water_list = first_level.water_list
        plat_list = first_level.plat_list
        coins = first_level.coins_list
        gold_key = first_level.key
        doors = first_level.doors

        enemies_list = pygame.sprite.Group()
        enemies_list.add(blue_slime)

        '''
        Game Loop
        '''
        while in_game:
            win = False
            lose = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        run = False

            win = player.collision_checker(ground_list, plat_list, coins, gold_key, doors, enemies_list)
            if player.life < 0:
                lose = True

            if player.rect.y > WORLD_Y + TY:
                player.fall_off_the_world()

            blue_slime.controller()

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
                scroll_elements(plat_list, True, scroll)
                scroll_elements(ground_list, True, scroll)
                scroll_elements(water_list, True, scroll)
                scroll_elements(coins, True, scroll)
                scroll_elements(gold_key, True, scroll)
                scroll_elements(doors, True, scroll)
                scroll_elements(enemies_list, True, scroll)

            if player.rect.x <= BACKWARD_X:
                scroll = BACKWARD_X - player.rect.x
                player.rect.x = BACKWARD_X
                scroll_elements(plat_list, False, scroll)
                scroll_elements(ground_list, False, scroll)
                scroll_elements(water_list, False, scroll)
                scroll_elements(coins, False, scroll)
                scroll_elements(gold_key, False, scroll)
                scroll_elements(doors, False, scroll)
                scroll_elements(enemies_list, False, scroll)

            key_status = 1 if player.has_key else 0
            WORLD.blit(BG, WORLD.get_rect())
            player.gravity()
            player.update()
            doors.draw(WORLD)
            player_list.draw(WORLD)
            ground_list.draw(WORLD)
            water_list.draw(WORLD)
            plat_list.draw(WORLD)
            coins.draw(WORLD)
            gold_key.draw(WORLD)
            enemies_list.draw(WORLD)
            hud.print_status(WORLD, player.score, player.life, key_status)
            pygame.display.flip()
            clock.tick(FPS)

            while lose:
                WORLD.blit(game_over_screen.bg, game_over_screen.bg.get_rect())
                game_over_screen.show_controllers()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        try:
                            sys.exit()
                        finally:
                            run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if game_over_screen.back_btn.show(mouse_pos):
                            print(mouse_pos)
                            lose = False
                            in_game = False
                            in_menu = True
                pygame.display.flip()
                clock.tick(FPS)
