"""
Main file
"""
import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg
from player import Player
import designed_levels as des_lvl
from hud import Hud
from menu import Menu, GameOverScreen, WinScreen
from enemy import Viking, VikingAxeThrower
from armament import Axe


# Global Variables
FPS = 50
WORLD_X = 960
WORLD_Y = 780
WORLD = pg.display.set_mode([WORLD_X, WORLD_Y])
LEVELS_NUMBER = 2
FORWARD_X = 600
BACKWARD_X = 120
# Tiles size x-width y-high
TX = 64
TY = 64


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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                try:
                    sys.exit()
                finally:
                    pass
            condition = screen.control_action(event)
            if isinstance(condition, str):
                return "next"
        pg.display.flip()
        clock.tick(FPS)
    return condition


def main():
    """
    Program main function
    """
    clock = pg.time.Clock()
    pg.init()
    pg.display.set_caption('Knight Adventures')
    pg.mixer.init()
    pg.mixer.music.load(os.path.join('music', 'music.mp3'))
    pg.mixer.music.play(-1, 0.0)
    run = True
    in_menu = True
    in_game = False
    current_level = 3
    menu = Menu(WORLD)

    while run:
        # Menu part
        while in_menu:
            WORLD.blit(menu.background, menu.background.get_rect())
            menu.show_controllers()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    try:
                        sys.exit()
                    finally:
                        run = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()

                    if menu.start_btn.show(mouse_pos):
                        in_game = True
                        in_menu = False

                    if menu.exit_btn.show(mouse_pos):
                        pg.quit()
                        try:
                            sys.exit()
                        finally:
                            run = False

            pg.display.flip()
            clock.tick(FPS)

        # Setup game
        game_over_screen = GameOverScreen(WORLD)
        win_screen = WinScreen(WORLD)
        enemies_list = pg.sprite.Group()
        armament_list = pg.sprite.Group()
        hud = Hud(0, 0)

        player = Player(0, WORLD_Y - TY)
        player_list = pg.sprite.Group()
        player_list.add(player)

        level, background, back_decorations, front_decorations = des_lvl.design_level(current_level, enemies_list, armament_list)

        ground_list = level.ground_list
        water_list = level.water_list
        plat_list = level.plat_list
        coins = level.coins_list
        gold_key = level.key
        doors = level.doors

        # Game Loop
        while in_game:
            lose = False

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    try:
                        sys.exit()
                    finally:
                        in_game = False
                        run = False

            win = player.collision_checker(ground_list, plat_list, coins, gold_key, doors, enemies_list)
            player.armament_collision_checker(armament_list)
            if player.life < 0:
                lose = True

            if player.stamina < 300:
                player.stamina += 1

            if player.rect.y > WORLD_Y + TY:
                player.fall_off_the_world()

            for enemy in enemies_list.sprites():
                if type(enemy) == Viking and not enemy.in_attack:
                    enemy.can_see_player((player.rect.x, player.rect.y), enemy.sight_range)
                if type(enemy) == VikingAxeThrower and not enemy.in_attack:
                    enemy.can_see_player((player.rect.x, player.rect.y), enemy.sight_range)
                react = enemy.controller()
                if react:
                    armament_list.add(react)

            for item in armament_list:
                item.controller()
                if not item.is_moving:
                    pg.sprite.spritecollide(item, pg.sprite.Group([x for x in armament_list if x != item]), True)
                if pg.sprite.spritecollide(item, ground_list, False) or pg.sprite.spritecollide(item, plat_list, False):
                    item.is_moving = False

            key = pg.key.get_pressed()
            if key[pg.K_d]:
                player.frame_counter += 0.5
                player.direction = "right"
                player.move(5, 0)

            if key[pg.K_a]:
                player.frame_counter += 0.5
                player.direction = "left"
                player.move(-5, 0)

            if key[pg.K_SPACE] and not player.is_jumping and not player.in_air:
                player.vel_y = -25
                player.is_jumping = True
                player.in_air = True

            if not key[pg.K_a] and not key[pg.K_d]:
                player.frame_counter = 0

            if pg.mouse.get_pressed()[0]:
                if player.stamina >= 100 and not player.in_attack:
                    player.stamina -= 100
                    player.in_attack = True

            player.attack_update()

            if player.rect.x >= FORWARD_X:
                scroll = player.rect.x - FORWARD_X
                player.rect.x = FORWARD_X
                player.start_location[0] -= scroll
                scroll_elements(plat_list, True, scroll)
                scroll_elements(ground_list, True, scroll)
                scroll_elements(water_list, True, scroll)
                scroll_elements(coins, True, scroll)
                scroll_elements(gold_key, True, scroll)
                scroll_elements(doors, True, scroll)
                scroll_elements(enemies_list, True, scroll)
                scroll_elements(armament_list, True, scroll)
                scroll_elements(back_decorations, True, scroll)
                scroll_elements(front_decorations, True, scroll)

            if player.rect.x <= BACKWARD_X:
                scroll = BACKWARD_X - player.rect.x
                player.rect.x = BACKWARD_X
                player.start_location[0] += scroll
                scroll_elements(plat_list, False, scroll)
                scroll_elements(ground_list, False, scroll)
                scroll_elements(water_list, False, scroll)
                scroll_elements(coins, False, scroll)
                scroll_elements(gold_key, False, scroll)
                scroll_elements(doors, False, scroll)
                scroll_elements(enemies_list, False, scroll)
                scroll_elements(armament_list, False, scroll)
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
            enemies_list.draw(WORLD)
            armament_list.draw(WORLD)
            front_decorations.draw(WORLD)
            water_list.draw(WORLD)
            hud.print_status(WORLD, player.score, player.life, key_status, player.stamina)
            pg.display.flip()
            clock.tick(FPS)

            if lose:
                screen_loop(lose, game_over_screen, clock)
                in_game = False
                in_menu = True
            if win:
                if screen_loop(win, win_screen, clock) == "next":
                    current_level += 1
                    if current_level > LEVELS_NUMBER:
                        current_level = 1
                    break
                else:
                    in_game = False
                    in_menu = True


if __name__ == '__main__':
    main()
