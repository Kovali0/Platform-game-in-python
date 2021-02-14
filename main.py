"""
Main file
"""
import os
import sys
import pygame
from player import Player
from level import Level, Decoration
from hud import Hud
from menu import Menu, GameOverScreen, WinScreen
from enemy import Slime, Fish


# Global Variables
FPS = 50
WORLD_X = 960
WORLD_Y = 780
WORLD = pygame.display.set_mode([WORLD_X, WORLD_Y])
FORWARD_X = 600
BACKWARD_X = 120
# Tiles size x-width y-high
TX = 64
TY = 64
ENEMIES_LIST = pygame.sprite.Group()


def scroll_elements(elements_list, forward, scroller):
    """
    Method which scroll items, tiles and rest things coordinates when player move on screen.
    :param elements_list: list of objects that need to be changed
    :param forward: bool if change location forward or backward
    :param scroller:
    """
    for element in elements_list:
        if forward:
            element.rect.x -= scroller
        else:
            element.rect.x += scroller


def screen_loop(condition, screen, clock):
    """
    Special loop for menu screen, after game for e.g. game over or in the level.
    :param condition: bool variable
    :param screen: which screen should be draw
    :param clock: clock
    """
    while condition:
        WORLD.blit(screen.background, screen.background.get_rect())
        screen.show_controllers()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    pass
            condition = screen.control_action(event)
        pygame.display.flip()
        clock.tick(FPS)
    return condition


def decoration_level_1():
    """
    Setup decorations for first level
    :return: list of back_decorations and front_decorations
    """
    back_decorations = pygame.sprite.Group()
    back_decorations.add(Decoration(-4, WORLD_Y - TY * 2, "rock.png"))
    back_decorations.add(Decoration(-3, WORLD_Y - TY * 2, "bush.png"))
    back_decorations.add(Decoration(-2, WORLD_Y - TY * 2, "grass.png"))
    back_decorations.add(Decoration(2, WORLD_Y - TY * 2, "fence.png"))
    back_decorations.add(Decoration(3, WORLD_Y - TY * 2, "way_sign_right.png"))
    back_decorations.add(Decoration(6, WORLD_Y - TY * 2, "bush.png"))
    back_decorations.add(Decoration(7, WORLD_Y - TY * 2, "bush.png"))
    back_decorations.add(Decoration(8, WORLD_Y - TY * 2, "mushroom_brown.png"))
    back_decorations.add(Decoration(13, WORLD_Y - TY * 2, "mushroom_red.png"))
    back_decorations.add(Decoration(17, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(18, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(19, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(23, WORLD_Y - TY * 2, "rock.png"))
    back_decorations.add(Decoration(24, WORLD_Y - TY * 2, "rock.png"))
    back_decorations.add(Decoration(32, WORLD_Y - TY * 2, "fence.png"))
    back_decorations.add(Decoration(32, WORLD_Y - TY * 2, "grass.png"))
    back_decorations.add(Decoration(33, WORLD_Y - TY * 2, "fence.png"))
    back_decorations.add(Decoration(38, WORLD_Y - TY * 2, "grass.png"))
    back_decorations.add(Decoration(43, WORLD_Y - TY * 8, "stone_tile_1.png"))
    back_decorations.add(Decoration(44, WORLD_Y - TY * 8, "stone_tile_1.png"))
    back_decorations.add(Decoration(45, WORLD_Y - TY * 8, "stone_tile_1.png"))
    back_decorations.add(Decoration(43, WORLD_Y - TY * 9, "stone_tile_1.png"))
    back_decorations.add(Decoration(43, WORLD_Y - TY * 9, "torch.png"))
    back_decorations.add(Decoration(44, WORLD_Y - TY * 9, "stone_tile_1.png"))
    back_decorations.add(Decoration(45, WORLD_Y - TY * 9, "stone_tile_1.png"))
    back_decorations.add(Decoration(45, WORLD_Y - TY * 9, "torch.png"))
    back_decorations.add(Decoration(43, WORLD_Y - TY * 10, "stone_tile_2.png"))
    back_decorations.add(Decoration(44, WORLD_Y - TY * 10, "stone_tile_3.png"))
    back_decorations.add(Decoration(44, WORLD_Y - TY * 10, "window.png"))
    back_decorations.add(Decoration(45, WORLD_Y - TY * 10, "stone_tile_2.png", True))
    back_decorations.add(Decoration(52, WORLD_Y - TY * 2, "grass.png"))
    back_decorations.add(Decoration(56, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    back_decorations.add(Decoration(57, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    back_decorations.add(Decoration(57, WORLD_Y - TY * 3, "wooden_box_crate.png"))
    back_decorations.add(Decoration(58, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    back_decorations.add(Decoration(58, WORLD_Y - TY * 3, "wooden_box_crate.png"))
    back_decorations.add(Decoration(59, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    front_decorations = pygame.sprite.Group()
    front_decorations.add(Decoration(3, WORLD_Y - TY * 2, "grass.png"))
    front_decorations.add(Decoration(4, WORLD_Y - TY * 2, "grass.png"))
    front_decorations.add(Decoration(16, WORLD_Y - TY * 2, "rock.png"))
    front_decorations.add(Decoration(24, WORLD_Y - TY * 2, "grass.png"))
    front_decorations.add(Decoration(34, WORLD_Y - TY * 2, "fence.png"))
    front_decorations.add(Decoration(35, WORLD_Y - TY * 2, "fence.png"))
    front_decorations.add(Decoration(36, WORLD_Y - TY * 2, "fence.png"))
    front_decorations.add(Decoration(36, WORLD_Y - TY * 11, "fence.png"))
    front_decorations.add(Decoration(37, WORLD_Y - TY * 11, "fence.png"))
    front_decorations.add(Decoration(44, WORLD_Y - TY * 2, "mushroom_brown.png"))
    front_decorations.add(Decoration(45, WORLD_Y - TY * 2, "bush.png"))
    front_decorations.add(Decoration(55, WORLD_Y - TY * 2, "mushroom_red.png"))
    front_decorations.add(Decoration(57, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    front_decorations.add(Decoration(58, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    front_decorations.add(Decoration(58, WORLD_Y - TY * 3, "wooden_box_crate.png"))

    return back_decorations, front_decorations


def design_first_level() -> Level:
    """
    Function for designing and creating first level.
    :return: first level object
    """
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
    blue_slime_1 = Slime(blue_slime_imgs)
    blue_slime_1.set_enemy_location(TX * 10, WORLD_Y - TY * 2, 128)
    blue_slime_2 = Slime(blue_slime_imgs)
    blue_slime_2.set_enemy_location(TX * 16, WORLD_Y - TY * 11, 100)
    blue_slime_3 = Slime(blue_slime_imgs)
    blue_slime_3.set_enemy_location(TX * 35, WORLD_Y - TY * 11, 40)
    blue_slime_4 = Slime(blue_slime_imgs)
    blue_slime_4.set_enemy_location(TX * 50, WORLD_Y - TY * 2, 192)
    blue_slime_5 = Slime(blue_slime_imgs)
    blue_slime_5.set_enemy_location(TX * 52, WORLD_Y - TY * 2, 192)

    blue_fish_imgs = ["fishBlue.png"]
    blue_fish_1 = Fish(blue_fish_imgs, WORLD_Y)
    blue_fish_1.set_enemy_location(TX * 18, WORLD_Y - TY * 1, 100)
    blue_fish_2 = Fish(blue_fish_imgs, WORLD_Y)
    blue_fish_2.set_enemy_location(TX * 28, WORLD_Y - TY * 1, 100)
    blue_fish_3 = Fish(blue_fish_imgs, WORLD_Y)
    blue_fish_3.set_enemy_location(TX * 61, WORLD_Y - TY * 1, 100)

    ENEMIES_LIST.add(blue_slime_1)
    ENEMIES_LIST.add(blue_slime_2)
    ENEMIES_LIST.add(blue_slime_3)
    ENEMIES_LIST.add(blue_slime_4)
    ENEMIES_LIST.add(blue_slime_5)
    ENEMIES_LIST.add(blue_fish_1)
    ENEMIES_LIST.add(blue_fish_2)
    ENEMIES_LIST.add(blue_fish_3)
    return first_level


def main():
    """
    Program main function
    """
    clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join('music', 'music.mp3'))
    pygame.mixer.music.play(-1, 0.0)
    run = True
    in_menu = True
    in_game = False

    while run:

        # Menu part
        menu = Menu(WORLD)
        while in_menu:
            WORLD.blit(menu.background, menu.background.get_rect())
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

        # Setup game
        background = pygame.image.load(os.path.join('images', 'backgrounds', 'clouds_background.png'))
        game_over_screen = GameOverScreen(WORLD)
        win_screen = WinScreen(WORLD)
        run = True

        player = Player(0, WORLD_Y - TY)
        player_list = pygame.sprite.Group()
        player_list.add(player)

        hud = Hud(0, 0)

        ENEMIES_LIST.empty()
        first_level = design_first_level()
        back_decorations, front_decorations = decoration_level_1()

        ground_list = first_level.ground_list
        water_list = first_level.water_list
        plat_list = first_level.plat_list
        coins = first_level.coins_list
        gold_key = first_level.key
        doors = first_level.doors

        # Game Loop
        while in_game:
            win = False
            lose = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        in_game = False
                        run = False

            win = player.collision_checker(ground_list, plat_list, coins, gold_key, doors, ENEMIES_LIST)
            if player.life < 0:
                lose = True

            if player.stamina < 300:
                player.stamina += 1

            if player.rect.y > WORLD_Y + TY:
                player.fall_off_the_world()

            for enemy in ENEMIES_LIST.sprites():
                enemy.controller()

            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                player.frame_counter += 1
                player.direction = "right"
                player.move(5, 0)

            if key[pygame.K_a]:
                player.frame_counter += 1
                player.direction = "left"
                player.move(-5, 0)

            if key[pygame.K_SPACE] and not player.is_jumping and not player.in_air:
                player.vel_y = -25
                player.is_jumping = True
                player.in_air = True

            if not key[pygame.K_a] and not key[pygame.K_d]:
                player.frame_counter = 0

            if pygame.mouse.get_pressed()[0]:
                if player.stamina >= 100 and not player.in_attack:
                    player.stamina -= 100
                    player.attack_counter = 0
                    player.in_attack = True

            player.attack_update()

            if player.rect.x >= FORWARD_X:
                scroll = player.rect.x - FORWARD_X
                player.rect.x = FORWARD_X
                scroll_elements(plat_list, True, scroll)
                scroll_elements(ground_list, True, scroll)
                scroll_elements(water_list, True, scroll)
                scroll_elements(coins, True, scroll)
                scroll_elements(gold_key, True, scroll)
                scroll_elements(doors, True, scroll)
                scroll_elements(ENEMIES_LIST, True, scroll)
                scroll_elements(back_decorations, True, scroll)
                scroll_elements(front_decorations, True, scroll)

            if player.rect.x <= BACKWARD_X:
                scroll = BACKWARD_X - player.rect.x
                player.rect.x = BACKWARD_X
                scroll_elements(plat_list, False, scroll)
                scroll_elements(ground_list, False, scroll)
                scroll_elements(water_list, False, scroll)
                scroll_elements(coins, False, scroll)
                scroll_elements(gold_key, False, scroll)
                scroll_elements(doors, False, scroll)
                scroll_elements(ENEMIES_LIST, False, scroll)
                scroll_elements(back_decorations, False, scroll)
                scroll_elements(front_decorations, False, scroll)

            key_status = 1 if player.has_key else 0
            WORLD.blit(background, WORLD.get_rect())
            player.gravity()
            player.update()
            back_decorations.draw(WORLD)
            doors.draw(WORLD)
            player_list.draw(WORLD)
            ground_list.draw(WORLD)
            plat_list.draw(WORLD)
            coins.draw(WORLD)
            gold_key.draw(WORLD)
            ENEMIES_LIST.draw(WORLD)
            front_decorations.draw(WORLD)
            water_list.draw(WORLD)
            hud.print_status(WORLD, player.score, player.life, key_status, player.stamina)
            pygame.display.flip()
            clock.tick(FPS)

            if lose:
                screen_loop(lose, game_over_screen, clock)
                in_game = False
                in_menu = True
            if win:
                screen_loop(win, win_screen, clock)
                in_game = False
                in_menu = True


if __name__ == '__main__':
    main()
