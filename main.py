"""
Main file
"""
import os
import sys

from armament import HeavyAxe

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg
from player import Player
import designed_levels as des_lvl
from hud import Hud
from menu import Menu, GameOverScreen, WinScreen
from enemy import Viking, VikingAxeThrower, BossViking

# Global Variables
FPS = 50
WORLD_X = 960
WORLD_Y = 780
WORLD = pg.display.set_mode([WORLD_X, WORLD_Y])
LEVELS_NUMBER = 6
FORWARD_X = 600
BACKWARD_X = 300
# Tiles size x-width y-high
TX = 64
TY = 64


def scroll_elements(elements_list, scroller):
    """
    Method which scroll items, tiles and rest things coordinates when player move on screen.
    :param elements_list: list of objects that need to be changed
    :param scroller:
    """
    for element in elements_list:
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


def connect_controller():
    pg.joystick.init()
    if pg.joystick.get_count() > 0:
        js = pg.joystick.Joystick(0)
        js.init()
        return js
    return None


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
    pg.mixer.music.set_volume(0.3)
    run = True
    in_menu = True
    in_game = False
    scroll = 0
    current_level = 6
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

        level, background, back_decorations, front_decorations = des_lvl.design_level(current_level, enemies_list,
                                                                                      armament_list)

        ground_list = level.ground_list
        water_list = level.water_list
        plat_list = level.plat_list
        coins = level.coins_list
        gold_key = level.key
        doors = level.doors

        if current_level >= 5:
            pg.mixer.music.load(os.path.join('music', 'vikings_music.mp3'))
            pg.mixer.music.play(-1, 0.0)
            pg.mixer.music.set_volume(0.3)
        else:
            pg.mixer.music.load(os.path.join('music', 'music.mp3'))
            pg.mixer.music.play(-1, 0.0)
            pg.mixer.music.set_volume(0.3)

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

            if current_level == 6:
                hud.print_boss_status(WORLD, enemies_list.sprites()[0])

            player.buildings_collision_checker(level.buildings)
            win = player.collision_checker(ground_list, plat_list, coins, gold_key, doors, enemies_list)
            player.armament_collision_checker(armament_list)

            player.is_moving = False
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
                if type(enemy) == BossViking and not enemy.in_attack:
                    enemy.can_see_player((player.rect.x, player.rect.y), enemy.sight_range)
                react = enemy.controller()
                if react:
                    armament_list.add(react)
                if current_level == 6 and enemy.drop_key:
                    level.set_key((enemy.rect.centerx / 64, enemy.rect.centery - 32))
                    enemy.drop_key = False

            for item in armament_list:
                item.controller(scroll)
                if not item.is_moving:
                    pg.sprite.spritecollide(item, pg.sprite.Group([x for x in armament_list if x != item]), True)
                if pg.sprite.spritecollide(item, ground_list, False):
                    item.is_moving = False
                if type(item) != HeavyAxe and pg.sprite.spritecollide(item, plat_list, False):
                    item.is_moving = False
                else:
                    for building in level.buildings:
                        if pg.sprite.spritecollide(item, building.walls_list, False):
                            item.is_moving = False

            if game_pad := connect_controller():
                js = {"L": game_pad.get_axis(0),
                      "Btn_X": game_pad.get_button(0),
                      "Btn_O": game_pad.get_button(1)}
            else:
                js = {}

            key = pg.key.get_pressed()
            if key[pg.K_d] or js.get("L", 0) > 0.8:
                player.is_moving = True
                player.frame_counter += 0.5
                player.direction = "right"
                player.move(5, 0)

            if key[pg.K_a] or js.get("L", 0) < -0.8:
                player.is_moving = True
                player.frame_counter += 0.5
                player.direction = "left"
                player.move(-5, 0)

            if (key[pg.K_SPACE] or js.get("Btn_X", 0)) and not player.is_jumping and not player.in_air:
                player.vel_y = -25
                player.is_jumping = True
                player.in_air = True

            if pg.mouse.get_pressed()[0] or js.get("Btn_O", 0):
                if player.stamina >= 100 and not player.in_attack:
                    player.stamina -= 100
                    player.in_attack = True
                    pg.mixer.Channel(1).play(pg.mixer.Sound(os.path.join('music', 'sword_slash.mp3')))

            if not player.is_moving:
                player.frame_counter += 0.5

            player.attack_update()

            if player.rect.x <= BACKWARD_X:
                scroll = BACKWARD_X - player.rect.x
                player.rect.x = BACKWARD_X
                player.start_location[0] += scroll
            elif player.rect.x >= FORWARD_X:
                scroll = FORWARD_X - player.rect.x
                player.rect.x = FORWARD_X
                player.start_location[0] += scroll
            else:
                scroll = 0

            scroll_elements(plat_list, scroll)
            scroll_elements(ground_list, scroll)
            scroll_elements(water_list, scroll)
            scroll_elements(coins, scroll)
            scroll_elements(gold_key, scroll)
            scroll_elements(doors, scroll)
            scroll_elements(enemies_list, scroll)
            scroll_elements(armament_list, scroll)
            scroll_elements(back_decorations, scroll)
            scroll_elements(front_decorations, scroll)
            for building in level.buildings:
                scroll_elements(building.walls_list, scroll)
                scroll_elements(building.back_list, scroll)
                scroll_elements(building.decorations_list, scroll)
                scroll_elements(building.front_elements_list, scroll)

            key_status = 1 if player.has_key else 0
            WORLD.blit(background, WORLD.get_rect())
            player.gravity()
            player.update()
            for building in level.buildings:
                building.build_fundaments(WORLD)
            back_decorations.draw(WORLD)
            doors.draw(WORLD)
            player_list.draw(WORLD)
            ground_list.draw(WORLD)
            plat_list.draw(WORLD)
            for building in level.buildings:
                building.build_front(WORLD)
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
                pg.mixer.Channel(4).play(pg.mixer.Sound(os.path.join('music', 'lose_in_level.mp3')))
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
