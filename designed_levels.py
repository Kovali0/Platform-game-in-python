"""
File with levels designed
"""
import os
import pygame
from level import Level, Decoration
from enemy import Slime, Fish, Viking, VikingAxeThrower

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
    first_level = Level(1, TX, TY, WORLD_Y, water_points, 65, p_loc, "green_tile_1.png", "green_tile_2.png")
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


def design_second_level(enemies) -> Level:
    """
    Function for designing and creating second level.
    :return: first level object
    """
    p_loc = [(TX * 31, WORLD_Y - TY - 192, 2),
             (TX * 34, WORLD_Y - TY - 384, 1),
             (TX * 35, WORLD_Y - TY - 128, 2),
             (TX * 39, WORLD_Y - TY - 576, 6),
             (TX * 42, WORLD_Y - TY - 192, 5),
             (TX * 45, WORLD_Y - TY - 384, 3),
             (TX * 52, WORLD_Y - TY - 384, 2),
             (TX * 58, WORLD_Y - TY - 384, 0),
             (TX * 60, WORLD_Y - TY - 576, 3),
             (TX * 63, WORLD_Y - TY - 192, 5),
             (TX * 66, WORLD_Y - TY - 576, 0),
             (TX * 70, WORLD_Y - TY - 576, 5),
             (TX * 79, WORLD_Y - TY - 576, 0)]
    water_points = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
                    5, 6, 7, 8,
                    30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                    75, 76, 77, 78, 79, 80]
    second_level = Level(2, TX, TY, WORLD_Y, water_points, 80, p_loc, "green_tile_1.png", "green_tile_2.png")
    coins_locations = [(4.5, WORLD_Y - TY * 1.5),
                       (16.5, WORLD_Y - TY * 1.5),
                       (26.5, WORLD_Y - TY * 1.5),
                       (39.5, WORLD_Y - TY * 6.5),
                       (42, WORLD_Y - TY * 10.5),
                       (46.5, WORLD_Y - TY * 4.5),
                       (55, WORLD_Y - TY * 1.5),
                       (64.5, WORLD_Y - TY * 4.5),
                       (66.5, WORLD_Y - TY * 10.5)]
    second_level.set_coins(coins_locations)
    second_level.set_key((79.5, WORLD_Y - TY * 10.5))
    second_level.set_doors((72, WORLD_Y - TY * 3))

    green_slime_imgs = ["slimeGreen.png"]
    green_slime_1 = Slime(green_slime_imgs)
    green_slime_1.set_enemy_location(TX * 15, WORLD_Y - TY * 2, 80)
    green_slime_2 = Slime(green_slime_imgs)
    green_slime_2.set_enemy_location(TX * 20, WORLD_Y - TY * 2, 85)
    green_slime_3 = Slime(green_slime_imgs)
    green_slime_3.set_enemy_location(TX * 25, WORLD_Y - TY * 2, 80)
    green_slime_4 = Slime(green_slime_imgs)
    green_slime_4.set_enemy_location(TX * 42, WORLD_Y - TY * 11, 60)
    green_slime_5 = Slime(green_slime_imgs)
    green_slime_5.set_enemy_location(TX * 45, WORLD_Y - TY * 5, 60)
    green_slime_6 = Slime(green_slime_imgs)
    green_slime_6.set_enemy_location(TX * 55, WORLD_Y - TY * 2, 90)
    green_slime_7 = Slime(green_slime_imgs)
    green_slime_7.set_enemy_location(TX * 65, WORLD_Y - TY * 5, 45)
    green_slime_8 = Slime(green_slime_imgs)
    green_slime_8.set_enemy_location(TX * 71, WORLD_Y - TY * 2, 65)
    green_slime_9 = Slime(green_slime_imgs)
    green_slime_9.set_enemy_location(TX * 72.5, WORLD_Y - TY * 11, 60)

    blue_fish_imgs = ["fishBlue.png"]
    blue_fish_1 = Fish(blue_fish_imgs, WORLD_Y)
    blue_fish_1.set_enemy_location(TX * 7, WORLD_Y - TY * 1, 100)

    enemies.add(green_slime_1)
    enemies.add(green_slime_2)
    enemies.add(green_slime_3)
    enemies.add(green_slime_4)
    enemies.add(green_slime_5)
    enemies.add(green_slime_6)
    enemies.add(green_slime_7)
    enemies.add(green_slime_8)
    enemies.add(green_slime_9)
    enemies.add(blue_fish_1)
    return second_level


def decoration_level_2():
    """
    Setup decorations for first level
    :return: list of back_decorations and front_decorations
    """
    back_decorations = pygame.sprite.Group()
    back_decorations.add(Decoration(1, WORLD_Y - TY * 4.5, "small_green_tree.png"))
    back_decorations.add(Decoration(2, WORLD_Y - TY * 1.8, "big_bush.png"))
    back_decorations.add(Decoration(3.5, WORLD_Y - TY * 2, "rock.png"))
    back_decorations.add(Decoration(10, WORLD_Y - TY * 2, "way_sign_right.png"))
    back_decorations.add(Decoration(12, WORLD_Y - TY * 4.5, "small_green_tree.png"))
    back_decorations.add(Decoration(14, WORLD_Y - TY * 1.75, "red_flower.png"))
    back_decorations.add(Decoration(16, WORLD_Y - TY * 4.65, "small_green_tree.png"))
    back_decorations.add(Decoration(17.5, WORLD_Y - TY * 4.65, "small_green_tree.png"))
    back_decorations.add(Decoration(21, WORLD_Y - TY * 4.25, "big_green_tree.png"))
    back_decorations.add(Decoration(24, WORLD_Y - TY * 1.85, "big_bush.png"))
    back_decorations.add(Decoration(26, WORLD_Y - TY * 1.85, "big_bush.png", True))
    back_decorations.add(Decoration(28.5, WORLD_Y - TY * 1.90, "big_rock.png"))
    back_decorations.add(Decoration(35, WORLD_Y - TY * 4, "fence.png"))
    back_decorations.add(Decoration(36, WORLD_Y - TY * 4, "fence.png"))
    back_decorations.add(Decoration(41, WORLD_Y - TY * 11, "wooden_box_crate.png"))
    back_decorations.add(Decoration(42, WORLD_Y - TY * 12, "wooden_box_crate.png"))
    back_decorations.add(Decoration(43.5, WORLD_Y - TY * 5, "fence.png"))
    back_decorations.add(Decoration(44.5, WORLD_Y - TY * 5, "fence.png"))
    back_decorations.add(Decoration(51.5, WORLD_Y - TY * 1.85, "big_bush.png"))
    back_decorations.add(Decoration(52, WORLD_Y - TY * 4.65, "small_green_tree.png"))
    back_decorations.add(Decoration(53, WORLD_Y - TY * 8, "wooden_box_crate.png"))
    back_decorations.add(Decoration(53.5, WORLD_Y - TY * 1.80, "red_flower.png", True))
    back_decorations.add(Decoration(55, WORLD_Y - TY * 2, "bush.png", True))
    back_decorations.add(Decoration(55.5, WORLD_Y - TY * 4.25, "big_green_tree.png"))
    back_decorations.add(Decoration(57, WORLD_Y - TY * 2, "mushroom_red.png"))
    back_decorations.add(Decoration(60.5, WORLD_Y - TY * 4.65, "small_green_tree.png"))
    back_decorations.add(Decoration(61, WORLD_Y - TY * 2, "mushroom_brown.png"))
    back_decorations.add(Decoration(61, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(62, WORLD_Y - TY * 2, "mushroom_red.png"))
    back_decorations.add(Decoration(62, WORLD_Y - TY * 4.25, "big_green_tree.png"))
    back_decorations.add(Decoration(64, WORLD_Y - TY * 5, "wooden_box_crate.png"))
    back_decorations.add(Decoration(65, WORLD_Y - TY * 5, "wooden_box_crate.png"))
    back_decorations.add(Decoration(66, WORLD_Y - TY * 5, "wooden_box_crate.png"))
    back_decorations.add(Decoration(73.5, WORLD_Y - TY * 4.50, "big_green_tree.png", True))
    back_decorations.add(Decoration(70, WORLD_Y - TY * 2, "wooden_stick_1.png"))
    back_decorations.add(Decoration(70, WORLD_Y - TY * 3, "torch_2.png"))
    back_decorations.add(Decoration(71, WORLD_Y - TY * 2, "wood_tile_4.png"))
    back_decorations.add(Decoration(72, WORLD_Y - TY * 2, "wood_tile_3.png"))
    back_decorations.add(Decoration(73, WORLD_Y - TY * 2, "wood_tile_4.png", True))
    back_decorations.add(Decoration(71, WORLD_Y - TY * 3, "wood_tile_4.png"))
    back_decorations.add(Decoration(72, WORLD_Y - TY * 3, "wood_tile_3.png"))
    back_decorations.add(Decoration(73, WORLD_Y - TY * 3, "wood_tile_4.png", True))
    back_decorations.add(Decoration(73, WORLD_Y - TY * 3, "window.png"))
    back_decorations.add(Decoration(71, WORLD_Y - TY * 4, "wood_tile_2.png"))
    back_decorations.add(Decoration(72, WORLD_Y - TY * 4, "wood_tile_1.png"))
    back_decorations.add(Decoration(72, WORLD_Y - TY * 4, "pennant_horse.png"))
    back_decorations.add(Decoration(73, WORLD_Y - TY * 4, "wood_tile_2.png", True))
    front_decorations = pygame.sprite.Group()
    front_decorations.add(Decoration(1, WORLD_Y - TY * 2, "fence.png"))
    front_decorations.add(Decoration(2, WORLD_Y - TY * 2, "fence.png"))
    front_decorations.add(Decoration(3, WORLD_Y - TY * 2, "fence.png"))
    front_decorations.add(Decoration(4, WORLD_Y - TY * 4.65, "small_green_tree.png"))
    front_decorations.add(Decoration(9, WORLD_Y - TY * 1.70, "water_plant.png"))
    front_decorations.add(Decoration(15, WORLD_Y - TY * 2, "mushroom_brown.png"))
    front_decorations.add(Decoration(19.75, WORLD_Y - TY * 2, "grass.png"))
    front_decorations.add(Decoration(20, WORLD_Y - TY * 2, "grass.png", True))
    front_decorations.add(Decoration(23.25, WORLD_Y - TY * 1.70, "big_grass.png"))
    front_decorations.add(Decoration(24, WORLD_Y - TY * 2, "bush.png"))
    front_decorations.add(Decoration(25, WORLD_Y - TY * 1.85, "big_bush.png"))
    front_decorations.add(Decoration(26.25, WORLD_Y - TY * 2, "bush.png"))
    front_decorations.add(Decoration(29, WORLD_Y - TY * 1.70, "water_plant.png"))
    front_decorations.add(Decoration(39, WORLD_Y - TY * 11, "fence.png"))
    front_decorations.add(Decoration(40, WORLD_Y - TY * 11, "fence.png"))
    front_decorations.add(Decoration(42, WORLD_Y - TY * 11, "wooden_box_crate.png"))
    front_decorations.add(Decoration(43, WORLD_Y - TY * 11, "wooden_box_crate.png"))
    front_decorations.add(Decoration(43, WORLD_Y - TY * 12, "wooden_box_crate.png"))
    front_decorations.add(Decoration(44, WORLD_Y - TY * 11, "wooden_box_crate.png", True))
    front_decorations.add(Decoration(46, WORLD_Y - TY * 8, "fence.png"))
    front_decorations.add(Decoration(47, WORLD_Y - TY * 8, "way_sign_right.png"))
    front_decorations.add(Decoration(50, WORLD_Y - TY * 1.70, "water_plant.png"))
    front_decorations.add(Decoration(52.5, WORLD_Y - TY * 1.70, "big_grass.png"))
    front_decorations.add(Decoration(54.25, WORLD_Y - TY * 4.65, "small_green_tree.png"))
    front_decorations.add(Decoration(57, WORLD_Y - TY * 4.25, "big_green_tree.png", True))
    front_decorations.add(Decoration(58.85, WORLD_Y - TY * 1.9, "blue_flower.png", True))
    front_decorations.add(Decoration(59.5, WORLD_Y - TY * 2, "grass.png"))
    front_decorations.add(Decoration(60, WORLD_Y - TY * 11, "fence.png"))
    front_decorations.add(Decoration(62, WORLD_Y - TY * 11, "fence.png"))
    front_decorations.add(Decoration(64.5, WORLD_Y - TY * 2, "rock.png", True))
    front_decorations.add(Decoration(66, WORLD_Y - TY * 2, "grass.png", True))
    front_decorations.add(Decoration(70.85, WORLD_Y - TY * 2, "wooden_box_crate.png", True))
    front_decorations.add(Decoration(74, WORLD_Y - TY * 2, "rock.png", True))
    return back_decorations, front_decorations


def design_third_level(enemies) -> Level:
    """
    Function for designing and creating third level.
    :return: first level object
    """
    p_loc = [(TX * -5, WORLD_Y - TY - 192, 0),
             (TX * -5, WORLD_Y - TY - 384, 0),
             (TX * 0, WORLD_Y - TY - 576, 4),
             (TX * 15, WORLD_Y - TY - 192, 2),
             (TX * 21, WORLD_Y - TY - 384, 4),
             (TX * 29, WORLD_Y - TY - 576, 3),
             (TX * 37, WORLD_Y - TY - 576, 7),
             (TX * 43, WORLD_Y - TY - 192, 3),
             (TX * 51, WORLD_Y - TY - 192, 0),
             (TX * 53, WORLD_Y - TY - 384, 2),
             (TX * 65, WORLD_Y - TY - 384, 6),
             (TX * 67, WORLD_Y - TY - 576, 2),
             (TX * 75, WORLD_Y - TY - 384, 5),
             (TX * 85, WORLD_Y - TY - 576, 1),
             (TX * 92, WORLD_Y - TY - 576, 1)]
    water_points = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
                    10, 11, 12, 13, 14,
                    35, 36, 37, 38, 39,
                    55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
                    97, 98, 99, 100, 101, 102, 102, 103, 104, 105, 106, 107, 108, 109, 110]
    third_level = Level(2, TX, TY, WORLD_Y, water_points, 110, p_loc, "dirt_tile_1.png", "orange_tile_1.png")
    bridges_loc = [(TX * 56, WORLD_Y - TY - 384, 8),
                   (TX * 87, WORLD_Y - TY - 576, 4)]
    third_level.build_bridges(bridges_loc)

    coins_locations = [(2.5, WORLD_Y - TY * 10.5),
                       (25, WORLD_Y - TY * 1.5),
                       (38.5, WORLD_Y - TY * 10.5),
                       (51.5, WORLD_Y - TY * 4.5),
                       (62.5, WORLD_Y - TY * 10.5),
                       (70.5, WORLD_Y - TY * 1.5),
                       (77, WORLD_Y - TY * 7.5),
                       (88.5, WORLD_Y - TY * 10.5),
                       (92, WORLD_Y - TY * 4.5)]
    third_level.set_coins(coins_locations)
    third_level.set_key((92, WORLD_Y - TY * 1.5))
    third_level.set_doors((8, WORLD_Y - TY * 3))

    #green_purple_img = ["slimePurple.png"]
    #green_purple_1 = Slime(green_purple_img)
    #green_purple_1.set_enemy_location(TX * 23, WORLD_Y - TY * 8, 50)
    #green_purple_2 = Slime(green_purple_img)
    #green_purple_2.set_enemy_location(TX * 25, WORLD_Y - TY * 2, 120)
    #green_purple_3 = Slime(green_purple_img)
    #green_purple_3.set_enemy_location(TX * 25, WORLD_Y - TY * 2, 65)
    #green_purple_4 = Slime(green_purple_img)
    #green_purple_4.set_enemy_location(TX * 40, WORLD_Y - TY * 11, 65)
    #green_purple_5 = Slime(green_purple_img)
    #green_purple_5.set_enemy_location(TX * 44.5, WORLD_Y - TY * 5, 50)
    #green_purple_6 = Slime(green_purple_img)
    #green_purple_6.set_enemy_location(TX * 51, WORLD_Y - TY * 2, 90)
    #green_purple_7 = Slime(green_purple_img)
    #green_purple_7.set_enemy_location(TX * 68, WORLD_Y - TY * 11, 40)
#
    #blue_fish_img = ["fishBlue.png"]
    #blue_fish_1 = Fish(blue_fish_img, WORLD_Y)
    #blue_fish_1.set_enemy_location(TX * 12.5, WORLD_Y - TY * 1, 100)
    #blue_fish_2 = Fish(blue_fish_img, WORLD_Y)
    #blue_fish_2.set_enemy_location(TX * 37, WORLD_Y - TY * 1, 100)

    viking_img = ["viking/walk/0.png", "viking/walk/0.png", "viking/walk/1.png", "viking/walk/1.png",
                  "viking/walk/2.png", "viking/walk/2.png", "viking/walk/3.png", "viking/walk/3.png",
                  "viking/walk/4.png", "viking/walk/4.png", "viking/walk/5.png", "viking/walk/5.png",
                  "viking/walk/6.png", "viking/walk/6.png", "viking/walk/7.png", "viking/walk/7.png",
                  "viking/walk/8.png", "viking/walk/8.png", "viking/walk/9.png", "viking/walk/9.png"]
    viking_attack_img = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]
    viking_1 = Viking(viking_img, viking_attack_img, 3)
    viking_1.set_enemy_location(TX * 78, WORLD_Y - TY * 2.5, 300)
    viking_2 = Viking(viking_img, viking_attack_img, 3)
    viking_2.set_enemy_location(TX * 89, WORLD_Y - TY * 11.5, 145)

    axe_thrower_img = ["ax_thrower_viking/idle/0.png", "ax_thrower_viking/idle/0.png", "ax_thrower_viking/idle/1.png",
                       "ax_thrower_viking/idle/1.png", "ax_thrower_viking/idle/2.png", "ax_thrower_viking/idle/2.png",
                       "ax_thrower_viking/idle/3.png", "ax_thrower_viking/idle/3.png", "ax_thrower_viking/idle/4.png",
                       "ax_thrower_viking/idle/4.png", "ax_thrower_viking/idle/5.png", "ax_thrower_viking/idle/5.png",
                       "ax_thrower_viking/idle/6.png", "ax_thrower_viking/idle/6.png", "ax_thrower_viking/idle/7.png",
                       "ax_thrower_viking/idle/7.png", "ax_thrower_viking/idle/8.png", "ax_thrower_viking/idle/8.png",
                       "ax_thrower_viking/idle/9.png", "ax_thrower_viking/idle/9.png"]
    axe_thrower_attack_img = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "2.png", "6.png", "7.png", "8.png",
                              "9.png", "10.png", "10.png", "11.png", "12.png"]
    axe_thrower_1 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 10, 30)
    axe_thrower_1.set_enemy_location(TX * 28, WORLD_Y - TY * 2.05)

    #enemies.add(green_purple_1)
    #enemies.add(green_purple_2)
    #enemies.add(green_purple_3)
    #enemies.add(green_purple_4)
    #enemies.add(green_purple_5)
    #enemies.add(green_purple_6)
    #enemies.add(green_purple_7)
    #enemies.add(blue_fish_1)
    #enemies.add(blue_fish_2)
    enemies.add(viking_1)
    enemies.add(viking_2)
    enemies.add(axe_thrower_1)
    return third_level


def decoration_level_3():

    """
    Setup decorations for first level
    :return: list of back_decorations and front_decorations
    """
    back_decorations = pygame.sprite.Group()
    front_decorations = pygame.sprite.Group()
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

    if level_id == 2:
        background = pygame.image.load(os.path.join('images', 'backgrounds', 'green_lands_background.png'))
        second_level = design_second_level(enemies)
        back_decorations, front_decorations = decoration_level_2()
        return second_level, background, back_decorations, front_decorations

    if level_id == 3:
        background = pygame.image.load(os.path.join('images', 'backgrounds', 'orange_background.png'))
        third_level = design_third_level(enemies)
        back_decorations, front_decorations = decoration_level_3()
        return third_level, background, back_decorations, front_decorations
