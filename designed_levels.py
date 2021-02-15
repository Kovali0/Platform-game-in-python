"""
File with levels designed
"""
import os
import pygame
from level import Level, Decoration
from enemy import Slime, Fish


# Global Variables
WORLD_Y = 780
# Tiles size x-width y-high
TX = 64
TY = 64


def design_first_level(enemies) -> Level:
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

    enemies.add(blue_slime_1)
    enemies.add(blue_slime_2)
    enemies.add(blue_slime_3)
    enemies.add(blue_slime_4)
    enemies.add(blue_slime_5)
    enemies.add(blue_fish_1)
    enemies.add(blue_fish_2)
    enemies.add(blue_fish_3)
    return first_level


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


def design_level(level_id, enemies):
    """
    Design level and return all needed things.
    :param level_id: which level should be created
    :param enemies: global list of enemies
    :return: level object, background, back decorations list and front decorations list
    """
    if level_id == 1:
        background = pygame.image.load(os.path.join('images', 'backgrounds', 'clouds_background.png'))
        first_level = design_first_level(enemies)
        back_decorations, front_decorations = decoration_level_1()
        return first_level, background, back_decorations, front_decorations
