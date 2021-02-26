"""
File with levels designed
"""
import os
import pygame
import numpy as np
from armament import Trap
from level import Level, Decoration, Building
from enemy import Slime, Fish, Viking, VikingAxeThrower

# Global Variables
WORLD_Y = 780
# Tiles size x-width y-high
TX = 64
TY = 64
# Images path
viking_img = ["viking/walk/0.png", "viking/walk/0.png", "viking/walk/1.png", "viking/walk/1.png",
              "viking/walk/2.png", "viking/walk/2.png", "viking/walk/3.png", "viking/walk/3.png",
              "viking/walk/4.png", "viking/walk/4.png", "viking/walk/5.png", "viking/walk/5.png",
              "viking/walk/6.png", "viking/walk/6.png", "viking/walk/7.png", "viking/walk/7.png",
              "viking/walk/8.png", "viking/walk/8.png", "viking/walk/9.png", "viking/walk/9.png"]
viking_attack_img = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]

axe_thrower_img = ["ax_thrower_viking/idle/0.png", "ax_thrower_viking/idle/0.png", "ax_thrower_viking/idle/1.png",
                   "ax_thrower_viking/idle/1.png", "ax_thrower_viking/idle/2.png", "ax_thrower_viking/idle/2.png",
                   "ax_thrower_viking/idle/3.png", "ax_thrower_viking/idle/3.png", "ax_thrower_viking/idle/4.png",
                   "ax_thrower_viking/idle/4.png", "ax_thrower_viking/idle/5.png", "ax_thrower_viking/idle/5.png",
                   "ax_thrower_viking/idle/6.png", "ax_thrower_viking/idle/6.png", "ax_thrower_viking/idle/7.png",
                   "ax_thrower_viking/idle/7.png", "ax_thrower_viking/idle/8.png", "ax_thrower_viking/idle/8.png",
                   "ax_thrower_viking/idle/9.png", "ax_thrower_viking/idle/9.png"]
axe_thrower_attack_img = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "2.png", "6.png", "7.png", "8.png",
                          "9.png", "10.png", "10.png", "11.png", "12.png"]


def design_first_level(enemies, armament) -> Level:
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


def design_second_level(enemies, armament) -> Level:
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
    Setup decorations for 2nd level
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


def design_third_level(enemies, armament) -> Level:
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
             (TX * 75, WORLD_Y - TY - 384, 2),
             (TX * 79, WORLD_Y - TY - 192, 1),
             (TX * 81, WORLD_Y - TY - 576, 1),
             (TX * 87, WORLD_Y - TY - 576, 1)]
    water_points = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
                    10, 11, 12, 13, 14,
                    35, 36, 37, 38, 39,
                    55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65,
                    97, 98, 99, 100, 101, 102, 102, 103, 104, 105, 106, 107, 108, 109, 110]
    third_level = Level(3, TX, TY, WORLD_Y, water_points, 110, p_loc, "dirt_tile_1.png", "orange_tile_1.png")
    bridges_loc = [(TX * 56, WORLD_Y - TY - 384, 8),
                   (TX * 83, WORLD_Y - TY - 576, 3)]
    third_level.build_bridges(bridges_loc)

    coins_locations = [(2.5, WORLD_Y - TY * 10.5),
                       (25, WORLD_Y - TY * 1.5),
                       (38.5, WORLD_Y - TY * 10.5),
                       (51.5, WORLD_Y - TY * 4.5),
                       (62.5, WORLD_Y - TY * 10.5),
                       (70.5, WORLD_Y - TY * 1.5),
                       (85, WORLD_Y - TY * 10.5),
                       (94.5, WORLD_Y - TY * 9.5),
                       (96.5, WORLD_Y - TY * 4.5)]
    third_level.set_coins(coins_locations)
    third_level.set_key((94.5, WORLD_Y - TY * 2))
    third_level.set_doors((7, WORLD_Y - TY * 3))

    tower_struct = np.array([[0,  0,  0,  0,  0,  0, 0],
                                  [0,  0,  0,  0,  0,  0, 0],
                                  [0, -2,  0, -2,  0, -2, 0],
                                  [0,  1,  1,  1,  1,  1, 0],
                                  [0,  1, -1, -1, -1,  1, 0],
                                  [0,  1, -1, -1, -1,  1, 0],
                                  [0, -1, -1, -1, -1, -1, 0],
                                  [0, -1, -1, -1, -1, -1, 0],
                                  [0,  1, -1, -1, -1,  1, 0],
                                  [0,  1, -1, -1, -1,  1, 0],
                                  [0,  1, -1, -1, -1,  1, 0]])
    tower_walls_img = ["stone_tile_1.png"]
    tower_back_img = ["stone_tile_1.png", "stone_tile_5.png"]
    tower = Building(WORLD_Y, 91, tower_struct, tower_back_img, tower_walls_img)
    tower.add_front(0, 2, "stone_tile_5.png")
    tower.add_front(2, 2, "stone_tile_5.png")
    tower.add_front(4, 2, "stone_tile_5.png")
    tower.add_front(6, 2, "stone_tile_5.png")
    tower.add_front(0, 3, "stone_tile_2.png", False, True)
    tower.add_front(6, 3, "stone_tile_2.png", True, True)
    tower.add_decoration(2, 5, "chain.png")
    tower.add_decoration(2, 6, "chain.png")
    tower.add_decoration(2, 7, "chain.png")
    tower.add_decoration(4, 5, "chain.png")
    tower.add_decoration(4, 6, "chain.png")
    tower.add_decoration(4, 7, "chain.png")
    tower.add_decoration(1, 6, "torch.png")
    tower.add_decoration(5, 6, "torch.png")
    tower.add_decoration(3, 4.5, "pennant_swords.png")
    third_level.buildings.append(tower)

    spikes_1 = Trap(TX * 93, WORLD_Y - TY * 2, "spikes.png", 1)
    spikes_2 = Trap(TX * 94, WORLD_Y - TY * 2, "spikes.png", 1)
    spikes_3 = Trap(TX * 95, WORLD_Y - TY * 2, "spikes.png", 1)
    armament.add(spikes_1)
    armament.add(spikes_2)
    armament.add(spikes_3)

    green_purple_img = ["slimePurple.png"]
    green_purple_1 = Slime(green_purple_img)
    green_purple_1.set_enemy_location(TX * 23, WORLD_Y - TY * 8, 50)
    green_purple_2 = Slime(green_purple_img)
    green_purple_2.set_enemy_location(TX * 25, WORLD_Y - TY * 2, 120)
    green_purple_3 = Slime(green_purple_img)
    green_purple_3.set_enemy_location(TX * 25, WORLD_Y - TY * 2, 65)
    green_purple_4 = Slime(green_purple_img)
    green_purple_4.set_enemy_location(TX * 40, WORLD_Y - TY * 11, 65)
    green_purple_5 = Slime(green_purple_img)
    green_purple_5.set_enemy_location(TX * 44.5, WORLD_Y - TY * 5, 50)
    green_purple_6 = Slime(green_purple_img)
    green_purple_6.set_enemy_location(TX * 51, WORLD_Y - TY * 2, 90)
    green_purple_7 = Slime(green_purple_img)
    green_purple_7.set_enemy_location(TX * 68, WORLD_Y - TY * 11, 40)

    blue_fish_img = ["fishBlue.png"]
    blue_fish_1 = Fish(blue_fish_img, WORLD_Y)
    blue_fish_1.set_enemy_location(TX * 12.5, WORLD_Y - TY * 1, 100)
    blue_fish_2 = Fish(blue_fish_img, WORLD_Y)
    blue_fish_2.set_enemy_location(TX * 37, WORLD_Y - TY * 1, 100)

    viking_1 = Viking(viking_img, viking_attack_img, 3)
    viking_1.set_enemy_location(TX * 78, WORLD_Y - TY * 2.5, 300)
    viking_2 = Viking(viking_img, viking_attack_img, 3)
    viking_2.set_enemy_location(TX * 84.5, WORLD_Y - TY * 11.5, 110)

    axe_thrower_1 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 10, 5)
    axe_thrower_1.set_enemy_location(TX * 68, WORLD_Y - TY * 8.05)

    enemies.add(green_purple_1)
    enemies.add(green_purple_2)
    enemies.add(green_purple_3)
    enemies.add(green_purple_4)
    enemies.add(green_purple_5)
    enemies.add(green_purple_6)
    enemies.add(green_purple_7)
    enemies.add(blue_fish_1)
    enemies.add(blue_fish_2)
    enemies.add(viking_1)
    enemies.add(viking_2)
    enemies.add(axe_thrower_1)
    return third_level


def decoration_level_3():

    """
    Setup decorations for 3rd level
    :return: list of back_decorations and front_decorations
    """
    back_decorations = pygame.sprite.Group()
    back_decorations.add(Decoration(0, WORLD_Y - TY * 9, "orange_tree.png", True))
    back_decorations.add(Decoration(2, WORLD_Y - TY * 1.7, "red_flower.png", True))
    back_decorations.add(Decoration(3, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    back_decorations.add(Decoration(4, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    back_decorations.add(Decoration(4, WORLD_Y - TY * 3, "wooden_box_crate.png"))
    back_decorations.add(Decoration(5, WORLD_Y - TY * 2, "sandstone_2.png"))
    back_decorations.add(Decoration(6, WORLD_Y - TY * 2, "sandstone_3.png"))
    back_decorations.add(Decoration(7, WORLD_Y - TY * 2, "sandstone_3.png"))
    back_decorations.add(Decoration(8, WORLD_Y - TY * 2, "sandstone_2.png", True))
    back_decorations.add(Decoration(5, WORLD_Y - TY * 3, "sandstone_7.png"))
    back_decorations.add(Decoration(6, WORLD_Y - TY * 3, "sandstone_1.png"))
    back_decorations.add(Decoration(7, WORLD_Y - TY * 3, "sandstone_1.png"))
    back_decorations.add(Decoration(8, WORLD_Y - TY * 3, "sandstone_7.png", True))
    back_decorations.add(Decoration(5, WORLD_Y - TY * 4, "sandstone_5.png"))
    back_decorations.add(Decoration(6, WORLD_Y - TY * 4, "sandstone_6.png"))
    back_decorations.add(Decoration(7, WORLD_Y - TY * 4, "sandstone_6.png"))
    back_decorations.add(Decoration(8, WORLD_Y - TY * 4, "sandstone_5.png", True))
    back_decorations.add(Decoration(4, WORLD_Y - TY * 5, "orange_tile_2.png"))
    back_decorations.add(Decoration(5, WORLD_Y - TY * 5, "orange_tile_3.png"))
    back_decorations.add(Decoration(6, WORLD_Y - TY * 5, "orange_tile_3.png"))
    back_decorations.add(Decoration(7, WORLD_Y - TY * 5, "orange_tile_3.png"))
    back_decorations.add(Decoration(8, WORLD_Y - TY * 5, "orange_tile_3.png"))
    back_decorations.add(Decoration(9.25, WORLD_Y - TY * 4.5, "small_green_tree.png"))
    back_decorations.add(Decoration(9, WORLD_Y - TY * 5, "orange_tile_2.png", True))
    back_decorations.add(Decoration(6, WORLD_Y - TY * 3, "window.png"))
    back_decorations.add(Decoration(9, WORLD_Y - TY * 3.5, "signboard_tavern.png"))
    back_decorations.add(Decoration(9, WORLD_Y - TY * 2, "way_sign_right.png"))
    back_decorations.add(Decoration(8.8, WORLD_Y - TY * 1.7, "water_plant.png", True))
    back_decorations.add(Decoration(15.4, WORLD_Y - TY * 1.7, "red_flower.png"))
    back_decorations.add(Decoration(21, WORLD_Y - TY * 8, "fence.png"))
    back_decorations.add(Decoration(22, WORLD_Y - TY * 8, "fence.png"))
    back_decorations.add(Decoration(23, WORLD_Y - TY * 8, "fence.png"))
    back_decorations.add(Decoration(28, WORLD_Y - TY * 2.05, "orange_bush_2.png"))
    back_decorations.add(Decoration(29.5, WORLD_Y - TY * 2.05, "orange_bush_2.png"))
    back_decorations.add(Decoration(29, WORLD_Y - TY * 4.28, "orange_tree_1.png"))
    back_decorations.add(Decoration(30, WORLD_Y - TY * 4.28, "orange_tree_1.png"))
    back_decorations.add(Decoration(30.5, WORLD_Y - TY * 2.05, "orange_bush_2.png"))
    back_decorations.add(Decoration(33, WORLD_Y - TY * 5.18, "birch_without_leaves.png"))
    back_decorations.add(Decoration(33, WORLD_Y - TY * 2, "orange_bush_2.png"))
    back_decorations.add(Decoration(40.6, WORLD_Y - TY * 1.8, "purple_flower.png"))
    back_decorations.add(Decoration(42, WORLD_Y - TY * 2, "mushroom_red.png"))
    back_decorations.add(Decoration(43.4, WORLD_Y - TY * 5, "fence.png"))
    back_decorations.add(Decoration(45.6, WORLD_Y - TY * 5, "fence.png"))
    back_decorations.add(Decoration(45.5, WORLD_Y - TY * 2.05, "orange_bush_2.png"))
    back_decorations.add(Decoration(47, WORLD_Y - TY * 2.05, "orange_bush_2.png"))
    back_decorations.add(Decoration(49.5, WORLD_Y - TY * 9, "orange_tree.png", True))
    back_decorations.add(Decoration(50.8, WORLD_Y - TY * 2.83, "orange_bush_1.png"))
    back_decorations.add(Decoration(68.5, WORLD_Y - TY * 8, "wooden_box_crate.png"))
    back_decorations.add(Decoration(67, WORLD_Y - TY * 1.9, "big_rock.png"))
    back_decorations.add(Decoration(71, WORLD_Y - TY * 4.28, "orange_tree_1.png"))
    back_decorations.add(Decoration(72, WORLD_Y - TY * 2, "orange_bush_2.png"))
    back_decorations.add(Decoration(73, WORLD_Y - TY * 2, "wood_tile_4.png"))
    back_decorations.add(Decoration(74, WORLD_Y - TY * 2, "wood_tile_3.png"))
    back_decorations.add(Decoration(75, WORLD_Y - TY * 2, "wood_tile_4.png", True))
    back_decorations.add(Decoration(75.3, WORLD_Y - TY * 2, "wooden_box_crate.png", True))
    back_decorations.add(Decoration(73, WORLD_Y - TY * 3, "wood_tile_4.png"))
    back_decorations.add(Decoration(74, WORLD_Y - TY * 3, "wood_tile_3.png"))
    back_decorations.add(Decoration(75, WORLD_Y - TY * 3, "wood_tile_4.png", True))
    back_decorations.add(Decoration(73, WORLD_Y - TY * 4, "wood_tile_2.png"))
    back_decorations.add(Decoration(74, WORLD_Y - TY * 4, "wood_tile_1.png"))
    back_decorations.add(Decoration(75, WORLD_Y - TY * 4, "wood_tile_2.png", True))
    back_decorations.add(Decoration(73, WORLD_Y - TY * 4, "torch.png", True))
    back_decorations.add(Decoration(74, WORLD_Y - TY * 3, "window.png"))
    back_decorations.add(Decoration(76, WORLD_Y - TY * 8, "wooden_stick_1.png"))
    back_decorations.add(Decoration(76, WORLD_Y - TY * 9, "wooden_stick_2.png"))
    back_decorations.add(Decoration(76, WORLD_Y - TY * 10, "torch_2.png"))
    back_decorations.add(Decoration(78, WORLD_Y - TY * 2.83, "orange_bush_1.png", True))
    back_decorations.add(Decoration(80, WORLD_Y - TY * 8.75, "long_orange_tree.png"))
    back_decorations.add(Decoration(85, WORLD_Y - TY * 8.7, "tree_without_leaves.png"))
    back_decorations.add(Decoration(86.5, WORLD_Y - TY * 2, "rock.png"))
    back_decorations.add(Decoration(87.5, WORLD_Y - TY * 2, "mushroom_brown.png"))
    back_decorations.add(Decoration(82, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(83, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(84, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(85, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(86, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(87, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(91, WORLD_Y - TY * 2, "orange_bush_2.png"))
    front_decorations = pygame.sprite.Group()
    front_decorations.add(Decoration(2, WORLD_Y - TY * 2, "fence.png"))
    front_decorations.add(Decoration(3, WORLD_Y - TY * 2, "fence.png"))
    front_decorations.add(Decoration(4, WORLD_Y - TY * 2, "fence.png"))
    front_decorations.add(Decoration(5, WORLD_Y - TY * 2, "grass.png"))
    front_decorations.add(Decoration(5.2, WORLD_Y - TY * 2, "grass.png", True))
    front_decorations.add(Decoration(5.4, WORLD_Y - TY * 2, "grass.png", True))
    front_decorations.add(Decoration(6, WORLD_Y - TY * 2, "bush.png"))
    front_decorations.add(Decoration(14.8, WORLD_Y - TY * 1.7, "water_plant.png"))
    front_decorations.add(Decoration(18, WORLD_Y - TY * 2.83, "orange_bush_1.png"))
    front_decorations.add(Decoration(24, WORLD_Y - TY * 2, "mushroom_brown.png"))
    front_decorations.add(Decoration(25, WORLD_Y - TY * 1.9, "big_rock.png"))
    front_decorations.add(Decoration(27, WORLD_Y - TY * 4.28, "big_orange_tree.png"))
    front_decorations.add(Decoration(29, WORLD_Y - TY * 2.05, "orange_bush_2.png"))
    front_decorations.add(Decoration(31, WORLD_Y - TY * 2, "mushroom_red.png"))
    front_decorations.add(Decoration(32.5, WORLD_Y - TY * 2.05, "orange_bush_2.png"))
    front_decorations.add(Decoration(33.5, WORLD_Y - TY * 8.75, "long_orange_tree.png"))
    front_decorations.add(Decoration(38, WORLD_Y - TY * 11, "wooden_box_crate.png"))
    front_decorations.add(Decoration(39, WORLD_Y - TY * 12, "wooden_box_crate.png"))
    front_decorations.add(Decoration(39, WORLD_Y - TY * 11, "wooden_box_crate.png"))
    front_decorations.add(Decoration(40, WORLD_Y - TY * 11, "wooden_box_crate.png"))
    front_decorations.add(Decoration(41, WORLD_Y - TY * 11, "wooden_box_crate.png"))
    front_decorations.add(Decoration(40, WORLD_Y - TY * 2, "rock.png"))
    front_decorations.add(Decoration(43.8, WORLD_Y - TY * 2.05, "orange_bush_2.png"))
    front_decorations.add(Decoration(45.5, WORLD_Y - TY * 1.9, "big_rock.png"))
    front_decorations.add(Decoration(44.5, WORLD_Y - TY * 2.05, "orange_bush_2.png", True))
    front_decorations.add(Decoration(45.85, WORLD_Y - TY * 1.9, "big_rock.png", True))
    front_decorations.add(Decoration(50, WORLD_Y - TY * 2, "mushroom_brown.png"))
    front_decorations.add(Decoration(50.4, WORLD_Y - TY * 2, "mushroom_brown.png"))
    front_decorations.add(Decoration(52, WORLD_Y - TY * 2, "mushroom_red.png"))
    front_decorations.add(Decoration(53, WORLD_Y - TY * 8, "fence.png"))
    front_decorations.add(Decoration(54, WORLD_Y - TY * 8, "fence.png"))
    front_decorations.add(Decoration(55, WORLD_Y - TY * 8, "fence.png"))
    front_decorations.add(Decoration(66, WORLD_Y - TY * 1.85, "purple_flower.png", True))
    front_decorations.add(Decoration(68, WORLD_Y - TY * 2.05, "orange_bush_2.png"))
    front_decorations.add(Decoration(70, WORLD_Y - TY * 8, "fence.png"))
    front_decorations.add(Decoration(71, WORLD_Y - TY * 8, "fence.png"))
    front_decorations.add(Decoration(84.8, WORLD_Y - TY * 5.18, "birch_without_leaves.png"))
    front_decorations.add(Decoration(89.5, WORLD_Y - TY * 5.18, "birch_without_leaves.png"))
    front_decorations.add(Decoration(91.5, WORLD_Y - TY * 2, "grass.png"))
    return back_decorations, front_decorations


def design_fourth_level(enemies, armament) -> Level:
    """
    Function for designing and creating third level.
    :return: first level object
    """
    p_loc = [(TX * -10, WORLD_Y - 64 * 10, 0),
             (TX * -6, WORLD_Y - 64 * 7, 0),
             (TX * -2, WORLD_Y - 64 * 7, 2),
             (TX * 4, WORLD_Y - 64 * 10, 1),
             (TX * 9, WORLD_Y - 64 * 10, 0),
             (TX * 15, WORLD_Y - 64 * 10, 2),
             (TX * 20, WORLD_Y - 64 * 7, 2),
             (TX * 27, WORLD_Y - 64 * 8, 0),
             (TX * 30, WORLD_Y - 64 * 8, 0),
             (TX * 34, WORLD_Y - 64 * 10, 1),
             (TX * 46, WORLD_Y - 64 * 10, 4),
             (TX * 55, WORLD_Y - 64 * 10, 0),
             (TX * 60, WORLD_Y - 64 * 10, 0),
             (TX * 76, WORLD_Y - 64 * 10, 2),
             (TX * 84, WORLD_Y - 64 * 7, 0),
             (TX * 87, WORLD_Y - 64 * 10, 2),
             (TX * 95.5, WORLD_Y - 64 * 10, 0)]
    water_points = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
                    5, 6, 7, 8, 9,
                    27, 28, 29, 30,
                    36, 37, 38, 39,
                    51, 52, 53, 54,
                    76, 77, 78, 79,
                    81, 82, 83, 84,
                    94, 95, 96, 97, 98, 99, 100]
    fourth_level = Level(4, TX, TY, WORLD_Y, water_points, 100, p_loc, "snow_tile_1.png", "blue_tile_1.png")
    bridges_loc = [(TX * 28, WORLD_Y - 64 * 8, 1),
                   (TX * 56, WORLD_Y - 64 * 10, 3)]
    fourth_level.build_bridges(bridges_loc)

    coins_locations = [(-9.5, WORLD_Y - TY * 12),
                       (18.5, WORLD_Y - TY * 2.5),
                       (40.5, WORLD_Y - TY * 1.5),
                       (41.5, WORLD_Y - TY * 7.5),
                       (53, WORLD_Y - TY * 4.5),
                       (57.5, WORLD_Y - TY * 10.5),
                       (69.5, WORLD_Y - TY * 12.3),
                       (80.5, WORLD_Y - TY * 1.5),
                       (96, WORLD_Y - TY * 12)]
    fourth_level.set_coins(coins_locations)
    fourth_level.set_key((69.5, WORLD_Y - TY * 9))
    fourth_level.set_doors((91.5, WORLD_Y - TY * 6))

    mountain_1_struct = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 2, 2, 0, 0, 0, 0],
                                  [0, 0, 1, 1, 2, 0, 0, 0],
                                  [0, 2, 1, 1, 1, 2, 0, 0],
                                  [2, 1, 1, 1, 1, 1, 2, 2]])
    mountain_1_walls_img = ["dirt_tile_1.png", "snow_tile_1.png"]
    mountain_1 = Building(WORLD_Y, 11, mountain_1_struct, [], mountain_1_walls_img)
    fourth_level.buildings.append(mountain_1)

    mountain_2_struct = np.array([[0, 0, 0, 0],
                                  [1, 0, 0, 0],
                                  [2, 0, 0, 0],
                                  [2, 1, 0, 0],
                                  [2, 2, 1, 0],
                                  [2, 2, 2, 1],
                                  [2, 2, 2, 2]])
    mountain_2_walls_img = ["snow_tile_2.png", "stone_tile_0.png"]
    mountain_2 = Building(WORLD_Y, 41, mountain_2_struct, [], mountain_2_walls_img)
    fourth_level.buildings.append(mountain_2)

    mountain_3_struct = np.array([[0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 4, 3, 3, 1, 3, 3, 4, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 4, 3, 1, 1, 1, 1, 3, 3, 4, 0, 0],
                                  [0, 0, 0, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0],
                                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0],
                                  [0, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                  [4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    mountain_3_walls_img = ["stone_tile_0.png", "snow_tile_2.png", "dirt_tile_1.png", "snow_tile_1.png"]
    mountain_3 = Building(WORLD_Y, 60, mountain_3_struct, [], mountain_3_walls_img)
    fourth_level.buildings.append(mountain_3)

    mountain_4_struct = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 2, 2, 2, 2, 4, 0],
                                  [0, 2, 1, 1, 1, 3, 3, 4],
                                  [2, 1, 1, 3, 3, 3, 3, 3]])
    mountain_4_walls_img = ["dirt_tile_1.png", "snow_tile_1.png", "stone_tile_0.png", "snow_tile_2.png"]
    mountain_4 = Building(WORLD_Y, 86, mountain_4_struct, [], mountain_4_walls_img)
    fourth_level.buildings.append(mountain_4)

    building_struct = np.array([[ 1,  1,  1,  1,  1],
                                [ 1, -2, -2, -2,  1],
                                [-1, -3, -2, -3, -1],
                                [-1, -2, -2, -2, -1],
                                [ 0,  0,  0,  0,  0],
                                [ 0,  0,  0,  0,  0],
                                [ 0,  0,  0,  0,  0],
                                [ 0,  0,  0,  0,  0],
                                [ 0,  0,  0,  0,  0],
                                [ 0,  0,  0,  0,  0],
                                [ 0,  0,  0,  0,  0]])
    building_walls_img = ["wood_tile_5.png"]
    building_back_img = ["wood_tile_5.png", "wood_tile_3.png", "window_wood.png"]
    building = Building(WORLD_Y, 67, building_struct, building_back_img, building_walls_img)
    building.add_decoration(2, 1.2, "pennant_swords.png")
    building.add_decoration(0.3, 2.9, "torch_2.png")
    building.add_decoration(3.7, 2.9, "torch_2.png")
    fourth_level.buildings.append(building)

    warehouse_struct = np.array([[ 1,  1,  1,  1, -1],
                                 [-1, -2, -2, -2, -1],
                                 [-1, -2, -2, -2, -1]])
    warehouse_walls_img = ["wood_tile_5.png"]
    warehouse_back_img = ["wood_tile_5.png", "wood_tile_3.png", "wooden_box_crate.png"]
    warehouse = Building(WORLD_Y, 55, warehouse_struct, warehouse_back_img, warehouse_walls_img)
    warehouse.add_decoration(0, 1, "torch.png")
    warehouse.add_decoration(4, 1, "torch.png")
    warehouse.add_decoration(1, 0, "chain.png")
    warehouse.add_decoration(1, 1, "chain.png")
    warehouse.add_decoration(2, 2, "wooden_box_crate.png")
    warehouse.add_decoration(3, 1, "wooden_box_crate.png")
    warehouse.add_decoration(3, 2, "wooden_box_crate.png")
    fourth_level.buildings.append(warehouse)

    spikes_1 = Trap(TX * 35, WORLD_Y - TY * 11, "spikes.png", 1)
    spikes_2 = Trap(TX * 55, WORLD_Y - TY * 5, "spikes.png", 1)
    spikes_3 = Trap(TX * 74, WORLD_Y - TY * 5, "spikes.png", 1)
    spikes_4 = Trap(TX * 88, WORLD_Y - TY * 11, "spikes.png", 1)
    armament.add(spikes_1)
    armament.add(spikes_2)
    armament.add(spikes_3)
    armament.add(spikes_4)

    blue_fish_img = ["fishBlue.png"]
    blue_fish_1 = Fish(blue_fish_img, WORLD_Y)
    blue_fish_1.set_enemy_location(TX * 27.5, WORLD_Y - TY * 1, 100)
    blue_fish_2 = Fish(blue_fish_img, WORLD_Y)
    blue_fish_2.set_enemy_location(TX * 36.2, WORLD_Y - TY * 1, 160)
    blue_fish_3 = Fish(blue_fish_img, WORLD_Y)
    blue_fish_3.set_enemy_location(TX * 38, WORLD_Y - TY * 1, 130)
    blue_fish_4 = Fish(blue_fish_img, WORLD_Y)
    blue_fish_4.set_enemy_location(TX * 51.5, WORLD_Y - TY * 1, 100)
    blue_fish_5 = Fish(blue_fish_img, WORLD_Y)
    blue_fish_5.set_enemy_location(TX * 52.5, WORLD_Y - TY * 1, 180)
    blue_fish_6 = Fish(blue_fish_img, WORLD_Y)
    blue_fish_6.set_enemy_location(TX * 54, WORLD_Y - TY * 1, 120)
    blue_fish_7 = Fish(blue_fish_img, WORLD_Y)
    blue_fish_7.set_enemy_location(TX * 84, WORLD_Y - TY * 1, 150)

    viking_1 = Viking(viking_img, viking_attack_img, 3)
    viking_1.set_enemy_location(TX * 23, WORLD_Y - TY * 2.5, 100)
    viking_2 = Viking(viking_img, viking_attack_img, 3)
    viking_2.set_enemy_location(TX * 56.5, WORLD_Y - TY * 2.5, 50)
    viking_3 = Viking(viking_img, viking_attack_img, 3)
    viking_3.set_enemy_location(TX * 48, WORLD_Y - TY * 11.5, 80)
    viking_4 = Viking(viking_img, viking_attack_img, 3)
    viking_4.set_enemy_location(TX * 48, WORLD_Y - TY * 2.5, 60)
    viking_5 = Viking(viking_img, viking_attack_img, 3)
    viking_5.set_enemy_location(TX * 68.4, WORLD_Y - TY * 9.5, 55)
    axe_thrower_1 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 10, 5)
    axe_thrower_1.set_enemy_location(TX * 30, WORLD_Y - TY * 9.05)
    axe_thrower_2 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 10, 4, 2)
    axe_thrower_2.set_enemy_location(TX * 32.5, WORLD_Y - TY * 2.05)
    axe_thrower_3 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 15, 6)
    axe_thrower_3.set_enemy_location(TX * 58, WORLD_Y - TY * 11.05)
    axe_thrower_4 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 30, 7)
    axe_thrower_4.set_enemy_location(TX * 70, WORLD_Y - TY * 9.05)
    axe_thrower_5 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 20, 4)
    axe_thrower_5.set_enemy_location(TX * 57, WORLD_Y - TY * 5.05)

    enemies.add(blue_fish_1)
    enemies.add(blue_fish_2)
    enemies.add(blue_fish_3)
    enemies.add(blue_fish_4)
    enemies.add(blue_fish_5)
    enemies.add(blue_fish_6)
    enemies.add(blue_fish_7)
    enemies.add(viking_1)
    enemies.add(viking_2)
    enemies.add(viking_3)
    enemies.add(viking_4)
    enemies.add(viking_5)
    enemies.add(axe_thrower_1)
    enemies.add(axe_thrower_2)
    enemies.add(axe_thrower_3)
    enemies.add(axe_thrower_4)
    enemies.add(axe_thrower_5)
    return fourth_level


def decoration_level_4():
    """
    Setup decorations for 4th level
    :return: list of back_decorations and front_decorations
    """
    back_decorations = pygame.sprite.Group()
    back_decorations.add(Decoration(0, WORLD_Y - TY * 5.5, "spruce.png", True))
    back_decorations.add(Decoration(3, WORLD_Y - TY * 1.8, "big_bush.png"))
    back_decorations.add(Decoration(2.7, WORLD_Y - TY * 1.7, "mountain_bush.png"))
    back_decorations.add(Decoration(4.2, WORLD_Y - TY * 2, "mushroom_red.png"))
    back_decorations.add(Decoration(13.5, WORLD_Y - TY * 5.9, "blue_flower.png", True))
    back_decorations.add(Decoration(15.4, WORLD_Y - TY * 6.9, "spruce.png"))
    back_decorations.add(Decoration(25, WORLD_Y - TY * 1.9, "big_rock.png", True))
    back_decorations.add(Decoration(17.9, WORLD_Y - TY * 3, "grass.png", True))
    back_decorations.add(Decoration(18.1, WORLD_Y - TY * 3, "grass.png", True))
    back_decorations.add(Decoration(18.2, WORLD_Y - TY * 3, "grass.png"))
    back_decorations.add(Decoration(20.2, WORLD_Y - TY * 3.9, "spruce_2.png"))
    back_decorations.add(Decoration(31.5, WORLD_Y - TY * 3.75, "spruce_3.png"))
    back_decorations.add(Decoration(33, WORLD_Y - TY * 3.9, "spruce_2.png"))
    back_decorations.add(Decoration(34.5, WORLD_Y - TY * 3.75, "spruce_3.png"))
    back_decorations.add(Decoration(34.5, WORLD_Y - TY * 2, "mushroom_red.png"))
    back_decorations.add(Decoration(47, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(48, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(49, WORLD_Y - TY * 11, "fence.png"))
    back_decorations.add(Decoration(48, WORLD_Y - TY * 3.9, "spruce_2.png"))
    back_decorations.add(Decoration(49.4, WORLD_Y - TY * 1.9, "mushroom_brown.png"))
    back_decorations.add(Decoration(50, WORLD_Y - TY * 5.5, "spruce.png", True))
    back_decorations.add(Decoration(46, WORLD_Y - TY * 1.9, "big_rock.png", True))
    back_decorations.add(Decoration(56.5, WORLD_Y - TY * 9.5, "green_tree.png"))
    back_decorations.add(Decoration(61.2, WORLD_Y - TY * 7, "spruce.png", True))
    back_decorations.add(Decoration(62, WORLD_Y - TY * 4, "bush.png", True))
    back_decorations.add(Decoration(66, WORLD_Y - TY * 7, "rock.png"))
    back_decorations.add(Decoration(65.5, WORLD_Y - TY * 9, "spruce_3.png"))
    back_decorations.add(Decoration(74.7, WORLD_Y - TY * 3.9, "big_rock_2.png"))
    back_decorations.add(Decoration(85, WORLD_Y - TY * 1.9, "big_rock_2.png", True))
    back_decorations.add(Decoration(86.7, WORLD_Y - TY * 7, "spruce.png"))
    back_decorations.add(Decoration(88, WORLD_Y - TY * 10.7, "tree_without_leaves.png", True))
    back_decorations.add(Decoration(92.9, WORLD_Y - TY * 4, "mushroom_red.png"))
    back_decorations.add(Decoration(89, WORLD_Y - TY * 5, "wood_tile_4.png"))
    back_decorations.add(Decoration(90, WORLD_Y - TY * 5, "wood_tile_3.png"))
    back_decorations.add(Decoration(91, WORLD_Y - TY * 5, "wood_tile_3.png"))
    back_decorations.add(Decoration(92, WORLD_Y - TY * 5, "wood_tile_4.png", True))
    back_decorations.add(Decoration(89, WORLD_Y - TY * 6, "wood_tile_4.png"))
    back_decorations.add(Decoration(90, WORLD_Y - TY * 6, "window_wood.png"))
    back_decorations.add(Decoration(91, WORLD_Y - TY * 6, "wood_tile_3.png"))
    back_decorations.add(Decoration(92, WORLD_Y - TY * 6, "wood_tile_4.png", True))
    back_decorations.add(Decoration(89, WORLD_Y - TY * 7, "wood_tile_2.png"))
    back_decorations.add(Decoration(90, WORLD_Y - TY * 7, "wood_tile_1.png"))
    back_decorations.add(Decoration(91, WORLD_Y - TY * 7, "wood_tile_1.png"))
    back_decorations.add(Decoration(92, WORLD_Y - TY * 7, "wood_tile_2.png", True))
    back_decorations.add(Decoration(91.2, WORLD_Y - TY * 6.8, "pennant_horse.png", True))
    back_decorations.add(Decoration(90, WORLD_Y - TY * 4.9, "blue_flower.png"))
    back_decorations.add(Decoration(88, WORLD_Y - TY * 5, "wooden_stick_1.png"))
    back_decorations.add(Decoration(88, WORLD_Y - TY * 6, "wooden_stick_2.png"))
    back_decorations.add(Decoration(88, WORLD_Y - TY * 7, "torch_2.png"))
    front_decorations = pygame.sprite.Group()
    front_decorations.add(Decoration(-0.5, WORLD_Y - TY * 8.7, "tree_without_leaves.png"))
    front_decorations.add(Decoration(11, WORLD_Y - TY * 3, "rock.png"))
    front_decorations.add(Decoration(14, WORLD_Y - TY * 6, "way_sign_right.png"))
    front_decorations.add(Decoration(21, WORLD_Y - TY * 1.7, "mountain_bush.png"))
    front_decorations.add(Decoration(23.5, WORLD_Y - TY * 3.8, "spruce_3.png"))
    front_decorations.add(Decoration(27, WORLD_Y - TY * 9, "fence.png"))
    front_decorations.add(Decoration(30, WORLD_Y - TY * 9, "fence.png"))
    front_decorations.add(Decoration(30.5, WORLD_Y - TY * 5.52, "spruce.png", True))
    front_decorations.add(Decoration(32.15, WORLD_Y - TY * 4.60, "frozen_tree.png"))
    front_decorations.add(Decoration(40, WORLD_Y - TY * 1.9, "big_rock_2.png"))
    front_decorations.add(Decoration(43, WORLD_Y - TY * 5, "rock.png"))
    front_decorations.add(Decoration(49, WORLD_Y - TY * 2, "mushroom_brown.png"))
    front_decorations.add(Decoration(62, WORLD_Y - TY * 8.7, "tree_without_leaves.png", True))
    front_decorations.add(Decoration(63.5, WORLD_Y - TY * 2, "mushroom_brown.png"))
    front_decorations.add(Decoration(73.5, WORLD_Y - TY * 6.9, "blue_flower.png"))
    front_decorations.add(Decoration(80, WORLD_Y - TY * 2, "mushroom_brown.png"))
    front_decorations.add(Decoration(85.3, WORLD_Y - TY * 1.7, "mountain_bush.png"))
    front_decorations.add(Decoration(88.5, WORLD_Y - TY * 3.8, "spruce_3.png"))
    return back_decorations, front_decorations


def design_fifth_level(enemies, armament) -> Level:
    """
    Function for designing and creating fifth level.
    :return: 5th level object
    """
    p_loc = [(TX * -1, WORLD_Y - 64 * 7, 0),
             (TX * 4, WORLD_Y - 64 * 5, 1),
             (TX * 4, WORLD_Y - 64 * 10, 1),
             (TX * 9, WORLD_Y - 64 * 10, 0),
             (TX * 13, WORLD_Y - 64 * 10, 2),
             (TX * 38, WORLD_Y - 64 * 10, 3),
             (TX * 45, WORLD_Y - 64 * 10, 0),
             (TX * 58, WORLD_Y - 64 * 10, 1)]
    water_points = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
                    5, 6, 7, 8, 9,
                    20, 21, 22, 23, 24, 25, 26, 27,
                    73, 74, 75, 76, 77, 78]
    fifth_level = Level(5, TX, TY, WORLD_Y, water_points, 82, p_loc, "snow_tile_2.png", "blue_tile_1.png")
    bridges_loc = [(TX * 20, WORLD_Y - 64 * 3, 7),
                   (TX * 73, WORLD_Y - 64 * 4, 5)]
    fifth_level.build_bridges(bridges_loc)

    coins_locations = [(12, WORLD_Y - TY * 12),
                       (27.1, WORLD_Y - TY * 11.5),
                       (33.5, WORLD_Y - TY * 8.5),
                       (42.5, WORLD_Y - TY * 2.5),
                       (49, WORLD_Y - TY * 11),
                       (52.5, WORLD_Y - TY * 1.5),
                       (53, WORLD_Y - TY * 4.5),
                       (71.5, WORLD_Y - TY * 8.5),
                       (77.5, WORLD_Y - TY * 9)]
    fifth_level.set_coins(coins_locations)
    fifth_level.set_key((65.5, WORLD_Y - TY * 5.2))
    fifth_level.set_doors((80.4, WORLD_Y - TY * 6))

    mountain_1_struct = np.array([[0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
                                  [0, 0, 2, 2, 2, 1, 1, 1, 1, 1]])
    mountain_1_walls_img = ["stone_tile_0.png", "snow_tile_2.png"]
    mountain_1 = Building(WORLD_Y, 10, mountain_1_struct, [], mountain_1_walls_img)
    fifth_level.buildings.append(mountain_1)

    mountain_2_struct = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 2, 0],
                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]])
    mountain_2_walls_img = ["stone_tile_0.png", "snow_tile_2.png"]
    mountain_2 = Building(WORLD_Y, 28, mountain_2_struct, [], mountain_2_walls_img)
    fifth_level.buildings.append(mountain_2)

    mountain_3_struct = np.array([[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                  [0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                  [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    mountain_3_walls_img = ["stone_tile_0.png", "snow_tile_2.png"]
    mountain_3 = Building(WORLD_Y, 58, mountain_3_struct, [], mountain_3_walls_img)
    fifth_level.buildings.append(mountain_3)

    mountain_4_struct = np.array([[2, 2, 1],
                                  [1, 1, 1],
                                  [1, 1, 1]])
    mountain_4_walls_img = ["stone_tile_0.png", "snow_tile_2.png"]
    mountain_4 = Building(WORLD_Y, 79, mountain_4_struct, [], mountain_4_walls_img)
    fifth_level.buildings.append(mountain_4)

    tower_struct = np.array([[0, -2,  0, -2,  0, -2,  0, -2, 0],
                             [0,  1,  1, -1,  1, -1, -1,  1, 0],
                             [0,  2, -1, -1, -1, -1, -1,  3, 0],
                             [0,  2, -1, -1, -1, -1, -1,  3, 0],
                             [0,  2, -1, -1, -1, -1, -1,  3, 0],
                             [0,  2,  1,  1, -1, -1,  1,  3, 0],
                             [0,  2, -1, -1, -1, -1, -1,  3, 0],
                             [0, -3, -1, -1, -1, -1, -1, -4, 0],
                             [0, -3, -1, -1, -1, -1, -1, -4, 0],
                             [0,  0,  0,  0,  0,  0,  0,  0, 0],
                             [0,  0,  0,  0,  0,  0,  0,  0, 0]])
    tower_walls_img = ["stone_tile_1.png", "stone_tile_6.png", "stone_tile_7.png"]
    tower_back_img = ["stone_tile_1.png", "stone_tile_5.png", "stone_tile_6.png", "stone_tile_7.png"]
    tower = Building(WORLD_Y, 27, tower_struct, tower_back_img, tower_walls_img)
    tower.add_front(0, 0, "stone_tile_5.png")
    tower.add_front(2, 0, "stone_tile_5.png")
    tower.add_front(4, 0, "stone_tile_5.png")
    tower.add_front(6, 0, "stone_tile_5.png")
    tower.add_front(8, 0, "stone_tile_5.png")
    tower.add_front(0, 1, "stone_tile_2.png", False, True)
    tower.add_front(8, 1, "stone_tile_2.png", True, True)
    tower.add_decoration(3.95, 3.2, "pennant_swords.png")
    tower.add_decoration(1.5, 7.9, "torch_2.png")
    tower.add_decoration(3, 3.9, "torch_2.png")
    tower.add_decoration(2.2, 3, "window.png")
    tower.add_decoration(5.8, 3, "window.png")
    tower.add_decoration(6.5, 7.9, "torch_2.png")
    fifth_level.buildings.append(tower)

    building_struct = np.array([[0,  2,  2,  2,  2,  2, 0],
                                [0,  1, -2, -2, -2,  1, 0],
                                [0, -1, -3, -2, -3, -1, 0],
                                [0, -1, -2, -2, -2, -1, 0]])
    building_walls_img = ["wood_tile_5.png", "orange_tile_3.png"]
    building_back_img = ["wood_tile_5.png", "wood_tile_3.png", "window_wood.png"]
    building = Building(WORLD_Y, 39, building_struct, building_back_img, building_walls_img)
    building.add_front(0, 0, "orange_tile_2.png", False)
    building.add_front(6, 0, "orange_tile_2.png", True)
    fifth_level.buildings.append(building)

    warehouse_struct = np.array([[0,  5,  5,  5,  5,  5,  5,  5, 0],
                                 [0,  2, -1, -1, -4, -1, -1, -3, 0],
                                 [0,  2, -1, -1, -4, -1, -1, -3, 0],
                                 [0,  2,  4,  4,  4,  4,  4,  3, 0],
                                 [0, -2, -1, -1, -1, -1, -1, -3, 0],
                                 [0, -2, -1, -1, -1, -1, -1, -3, 0]])
    warehouse_walls_img = ["stone_tile_1.png", "stone_tile_6.png", "stone_tile_7.png", "wood_tile_5.png", "orange_tile_3.png"]
    warehouse_back_img = ["stone_tile_1.png", "stone_tile_6.png", "stone_tile_7.png", "wood_tile_5.png"]
    warehouse = Building(WORLD_Y, 47, warehouse_struct, warehouse_back_img, warehouse_walls_img)
    warehouse.add_front(0, 0, "orange_tile_2.png", False)
    warehouse.add_front(8, 0, "orange_tile_2.png", True)
    warehouse.add_front(4, 4, "wood_tile_5.png")
    warehouse.add_front(4, 5, "wood_tile_5.png")
    warehouse.add_decoration(2.5, 1.5, "window.png")
    warehouse.add_decoration(5.5, 1.5, "window.png")
    warehouse.add_decoration(2, 4, "chain.png")
    warehouse.add_decoration(3, 4, "chain.png")
    warehouse.add_decoration(0, 5, "wooden_box_crate.png")
    warehouse.add_decoration(5, 5, "wooden_box_crate.png")
    warehouse.add_decoration(6, 5, "wooden_box_crate.png")
    warehouse.add_decoration(2, 1, "wooden_box_crate.png")
    warehouse.add_decoration(2, 2, "wooden_box_crate.png")
    warehouse.add_decoration(3, 2, "wooden_box_crate.png")
    fifth_level.buildings.append(warehouse)

    tavern_walls_img = ["sandstone_1.png", "orange_tile_3.png", "sandstone_3.png", "sandstone_4.png", "sandstone_5.png",
                        "sandstone_6.png", "sandstone_7.png"]
    tavern_back_img = ["sandstone_1.png", "sandstone_2.png", "sandstone_3.png", "sandstone_4.png", "window_wood.png",
                       "sandstone_6.png", "sandstone_7.png", "orange_tile_3.png", "stone_tile_0.png"]
    tavern_struct = np.array([[0,  0,  0,  0, -9,  0,  0,  0,  0,  0, 0,  0,  0],
                              [0,  2,  2, -8, -9, -8,  2,  2,  2,  2,  2,  2, 0],
                              [0,  7, -1, -1, -9, -1, -1, -1, -1, -1, -1,  7, 0],
                              [0,  7, -1, -5, -9, -1, -5, -1, -1, -5, -1,  7, 0],
                              [0,  7, -1, -1, -9, -1, -1, -1, -1, -1, -1,  7, 0],
                              [0,  5,  4,  6,  4,  6,  4, -6, -4,  6,  4,  5, 0],
                              [0,  7, -1, -1, -9, -1,  1, -1, -1, -1, -1,  7, 0],
                              [0, -7, -1, -5, -9, -1,  1, -1, -1, -5, -1,  0, 0],
                              [0, -2, -3, -3, -3, -3,  3, -3, -3, -3, -3,  0, 0],
                              [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0],
                              [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0],
                              [0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0]])
    tavern = Building(WORLD_Y, 61, tavern_struct, tavern_back_img, tavern_walls_img)
    tavern.add_front(0, 1, "orange_tile_2.png", False)
    tavern.add_front(12, 1, "orange_tile_2.png", True)
    tavern.add_front(0, 5, "signboard_tavern.png", True)
    tavern.add_front(6, 6, "sandstone_6.png", to_y_flip=True)
    tavern.add_front(6, 7, "sandstone_6.png", to_y_flip=True)
    tavern.add_front(6, 8, "sandstone_6.png", to_y_flip=True)
    tavern.add_front(11, 2, "sandstone_7.png", True)
    tavern.add_front(11, 3, "sandstone_7.png", True)
    tavern.add_front(11, 4, "sandstone_7.png", True)
    tavern.add_front(11, 5, "sandstone_5.png", True)
    tavern.add_front(11, 6, "sandstone_7.png", True)
    tavern.add_front(11, 7, "sandstone_7.png", True)
    tavern.add_front(11, 8, "sandstone_2.png", True)
    fifth_level.buildings.append(tavern)

    building_1_struct = np.array([[0, 0, 0],
                                  [4, 3, 3],
                                  [0, 2, 1],
                                  [0, 2, 1],
                                  [0, 0, 0],
                                  [0, 0, 0],
                                  [0, 0, 0],
                                  [0, 0, 0],
                                  [0, 0, 0],
                                  [0, 0, 0],
                                  [0, 0, 0],
                                  [0, 0, 0]])
    building_1_walls_img = ["stone_tile_1.png", "stone_tile_6.png", "stone_tile_5.png", "stone_tile_4.png"]
    building_1 = Building(WORLD_Y, 79, building_1_struct, [], building_1_walls_img)
    fifth_level.buildings.append(building_1)

    spikes_1 = Trap(TX * 79, WORLD_Y - TY * 5, "spikes.png", 1)
    armament.add(spikes_1)

    blue_slime_imgs = ["slimeBlue.png"]
    blue_slime_1 = Slime(blue_slime_imgs)
    blue_slime_1.set_enemy_location(TX * 13, WORLD_Y - TY * 3, 40)
    blue_slime_2 = Slime(blue_slime_imgs)
    blue_slime_2.set_enemy_location(TX * 17, WORLD_Y - TY * 4, 60)

    viking_1 = Viking(viking_img, viking_attack_img, 6)
    viking_1.set_enemy_location(TX * 28, WORLD_Y - TY * 4.5, 250)
    viking_2 = Viking(viking_img, viking_attack_img, 5)
    viking_2.set_enemy_location(TX * 30, WORLD_Y - TY * 4.5, 110)
    viking_3 = Viking(viking_img, viking_attack_img, 3)
    viking_3.set_enemy_location(TX * 42, WORLD_Y - TY * 2.5, 130)
    viking_4 = Viking(viking_img, viking_attack_img, 3)
    viking_4.set_enemy_location(TX * 55, WORLD_Y - TY * 2.5, 80)
    viking_5 = Viking(viking_img, viking_attack_img, 3)
    viking_5.set_enemy_location(TX * 65, WORLD_Y - TY * 9.5, 60)
    viking_6 = Viking(viking_img, viking_attack_img, 3)
    viking_6.set_enemy_location(TX * 64, WORLD_Y - TY * 5.5, 60)
    viking_7 = Viking(viking_img, viking_attack_img, 5)
    viking_7.set_enemy_location(TX * 76, WORLD_Y - TY * 5.5, 110)

    axe_thrower_1 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 25, 5)
    axe_thrower_1.set_enemy_location(TX * 28, WORLD_Y - TY * 12.05)
    axe_thrower_2 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 7, 4, 2)
    axe_thrower_2.set_enemy_location(TX * 29, WORLD_Y - TY * 8.05)
    axe_thrower_3 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 10, 6, 2)
    axe_thrower_3.set_enemy_location(TX * 51, WORLD_Y - TY * 5.05)
    axe_thrower_4 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 10, 6)
    axe_thrower_4.set_enemy_location(TX * 53, WORLD_Y - TY * 8.05)
    axe_thrower_5 = VikingAxeThrower(axe_thrower_img, axe_thrower_attack_img, 20, 6)
    axe_thrower_5.set_enemy_location(TX * 80, WORLD_Y - TY * 12.7)

    enemies.add(blue_slime_1)
    enemies.add(blue_slime_2)
    enemies.add(viking_1)
    enemies.add(viking_2)
    enemies.add(viking_3)
    enemies.add(viking_4)
    enemies.add(viking_5)
    enemies.add(viking_6)
    enemies.add(viking_7)
    enemies.add(axe_thrower_1)
    enemies.add(axe_thrower_2)
    enemies.add(axe_thrower_3)
    enemies.add(axe_thrower_4)
    enemies.add(axe_thrower_5)

    return fifth_level


def decoration_level_5():
    """
    Setup decorations for 5th level
    :return: list of back_decorations and front_decorations
    """
    back_decorations = pygame.sprite.Group()
    back_decorations.add(Decoration(0, WORLD_Y - TY * 5.5, "spruce.png", True))
    back_decorations.add(Decoration(10, WORLD_Y - TY * 1.9, "big_rock.png", True))
    back_decorations.add(Decoration(11, WORLD_Y - TY * 3.9, "spruce_2.png"))
    back_decorations.add(Decoration(12.4, WORLD_Y - TY * 1.9, "mushroom_brown.png"))
    back_decorations.add(Decoration(13, WORLD_Y - TY * 5.5, "spruce.png", True))
    back_decorations.add(Decoration(14.5, WORLD_Y - TY * 7, "spruce.png", True))
    back_decorations.add(Decoration(15.5, WORLD_Y - TY * 9.2, "green_tree.png"))
    back_decorations.add(Decoration(17, WORLD_Y - TY * 4, "bush.png", True))
    back_decorations.add(Decoration(18, WORLD_Y - TY * 5.5, "spruce_3.png"))
    back_decorations.add(Decoration(18.5, WORLD_Y - TY * 3.9, "big_rock_2.png"))
    back_decorations.add(Decoration(36, WORLD_Y - TY * 4, "wooden_stick_1.png"))
    back_decorations.add(Decoration(36, WORLD_Y - TY * 5, "wooden_stick_2.png"))
    back_decorations.add(Decoration(36, WORLD_Y - TY * 6, "torch_2.png"))
    back_decorations.add(Decoration(35.8, WORLD_Y - TY * 4, "rock.png"))
    back_decorations.add(Decoration(40, WORLD_Y - TY * 3, "torch.png"))
    back_decorations.add(Decoration(42, WORLD_Y - TY * 3.8, "pennant_swords.png"))
    back_decorations.add(Decoration(44, WORLD_Y - TY * 3, "torch.png"))
    back_decorations.add(Decoration(46, WORLD_Y - TY * 2, "wooden_stick_1.png"))
    back_decorations.add(Decoration(46, WORLD_Y - TY * 3, "wooden_stick_2.png"))
    back_decorations.add(Decoration(46, WORLD_Y - TY * 4, "torch_2.png"))
    back_decorations.add(Decoration(45.5, WORLD_Y - TY * 1.7, "mountain_bush.png"))
    back_decorations.add(Decoration(56, WORLD_Y - TY * 4.60, "frozen_tree.png"))
    back_decorations.add(Decoration(59, WORLD_Y - TY * 5.9, "spruce_2.png"))
    back_decorations.add(Decoration(63, WORLD_Y - TY * 7, "torch.png", True))
    back_decorations.add(Decoration(63, WORLD_Y - TY * 11, "torch.png"))
    back_decorations.add(Decoration(66, WORLD_Y - TY * 7, "torch.png"))
    back_decorations.add(Decoration(66, WORLD_Y - TY * 11, "torch.png", True))
    back_decorations.add(Decoration(68, WORLD_Y - TY * 7, "torch.png", True))
    back_decorations.add(Decoration(68, WORLD_Y - TY * 11, "torch.png", True))
    back_decorations.add(Decoration(71, WORLD_Y - TY * 7, "torch.png"))
    back_decorations.add(Decoration(71, WORLD_Y - TY * 11, "torch.png"))
    back_decorations.add(Decoration(63, WORLD_Y - TY * 9, "wooden_box_crate.png"))
    back_decorations.add(Decoration(68, WORLD_Y - TY * 5, "wooden_box_crate.png"))
    back_decorations.add(Decoration(68, WORLD_Y - TY * 6, "wooden_box_crate.png"))
    back_decorations.add(Decoration(69, WORLD_Y - TY * 5, "wooden_box_crate.png"))
    back_decorations.add(Decoration(64.95, WORLD_Y - TY * 6.7, "pennant_swords.png"))
    back_decorations.add(Decoration(68.9, WORLD_Y - TY * 9.7, "pennant_swords.png"))
    back_decorations.add(Decoration(65, WORLD_Y - TY * 5, "stone_tile_0.png"))
    back_decorations.add(Decoration(65, WORLD_Y - TY * 5, "window.png"))
    back_decorations.add(Decoration(65, WORLD_Y - TY * 5, "fireplace.png"))
    back_decorations.add(Decoration(79, WORLD_Y - TY * 5, "bush.png"))
    back_decorations.add(Decoration(80, WORLD_Y - TY * 5, "stone_tile_6.png"))
    back_decorations.add(Decoration(80, WORLD_Y - TY * 6, "stone_tile_6.png"))
    back_decorations.add(Decoration(80, WORLD_Y - TY * 7, "stone_tile_6.png"))
    back_decorations.add(Decoration(80, WORLD_Y - TY * 8, "stone_tile_6.png"))
    back_decorations.add(Decoration(80, WORLD_Y - TY * 9, "stone_tile_6.png"))
    back_decorations.add(Decoration(81, WORLD_Y - TY * 5, "stone_tile_1.png"))
    back_decorations.add(Decoration(81, WORLD_Y - TY * 6, "stone_tile_1.png"))
    back_decorations.add(Decoration(81, WORLD_Y - TY * 7, "stone_tile_1.png"))
    back_decorations.add(Decoration(81, WORLD_Y - TY * 8, "stone_tile_1.png"))
    back_decorations.add(Decoration(81, WORLD_Y - TY * 9, "stone_tile_1.png"))
    front_decorations = pygame.sprite.Group()
    front_decorations.add(Decoration(2.5, WORLD_Y - TY * 1.7, "mountain_bush.png"))
    front_decorations.add(Decoration(4, WORLD_Y - TY * 2, "way_sign_right.png"))
    front_decorations.add(Decoration(10.8, WORLD_Y - TY * 2, "mushroom_red.png", True))
    front_decorations.add(Decoration(16, WORLD_Y - TY * 4, "fence.png"))
    front_decorations.add(Decoration(17, WORLD_Y - TY * 4, "fence.png"))
    front_decorations.add(Decoration(18, WORLD_Y - TY * 4, "fence.png"))
    front_decorations.add(Decoration(15.5, WORLD_Y - TY * 4, "rock.png", True))
    front_decorations.add(Decoration(27, WORLD_Y - TY * 12, "stone_tile_5.png"))
    front_decorations.add(Decoration(34.5, WORLD_Y - TY * 8.7, "tree_without_leaves.png"))
    front_decorations.add(Decoration(51, WORLD_Y - TY * 3, "torch.png"))
    front_decorations.add(Decoration(52, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    front_decorations.add(Decoration(55, WORLD_Y - TY * 2, "wooden_box_crate.png"))
    front_decorations.add(Decoration(54.5, WORLD_Y - TY * 1.7, "mountain_bush.png"))
    front_decorations.add(Decoration(58, WORLD_Y - TY * 2.9, "blue_flower.png"))
    front_decorations.add(Decoration(59, WORLD_Y - TY * 4.1, "wooden_stick_1.png"))
    front_decorations.add(Decoration(59, WORLD_Y - TY * 5, "wooden_stick_2.png"))
    front_decorations.add(Decoration(59, WORLD_Y - TY * 6, "torch_2.png"))
    front_decorations.add(Decoration(59, WORLD_Y - TY * 4, "fence.png"))
    front_decorations.add(Decoration(60, WORLD_Y - TY * 4, "fence.png"))
    front_decorations.add(Decoration(78, WORLD_Y - TY * 10.5, "pennant_1.png"))
    front_decorations.add(Decoration(79, WORLD_Y - TY * 10.5, "pennant_2.png"))
    front_decorations.add(Decoration(79, WORLD_Y - TY * 9.5, "pennant_3.png"))
    front_decorations.add(Decoration(79, WORLD_Y - TY * 8.5, "pennant_4.png"))
    front_decorations.add(Decoration(80.4, WORLD_Y - TY * 7.5, "window.png"))
    front_decorations.add(Decoration(80.4, WORLD_Y - TY * 10.2, "window.png"))
    front_decorations.add(Decoration(80, WORLD_Y - TY * 12, "stone_tile_5.png"))
    front_decorations.add(Decoration(81, WORLD_Y - TY * 12, "stone_tile_5.png"))
    return back_decorations, front_decorations


def design_level(level_id, enemies, armament):
    """
    Design level and return all needed things.
    :param level_id: which level should be created
    :param enemies: global list of enemies
    :return: level object, background, back decorations list and front decorations list
    """
    if level_id == 1:
        background = pygame.image.load(os.path.join('images', 'backgrounds', 'clouds_background.png'))
        first_level = design_first_level(enemies, armament)
        back_decorations, front_decorations = decoration_level_1()
        return first_level, background, back_decorations, front_decorations

    if level_id == 2:
        background = pygame.image.load(os.path.join('images', 'backgrounds', 'green_lands_background.png'))
        second_level = design_second_level(enemies, armament)
        back_decorations, front_decorations = decoration_level_5()
        return second_level, background, back_decorations, front_decorations

    if level_id == 3:
        background = pygame.image.load(os.path.join('images', 'backgrounds', 'orange_background.png'))
        third_level = design_third_level(enemies, armament)
        back_decorations, front_decorations = decoration_level_3()
        return third_level, background, back_decorations, front_decorations

    if level_id == 4:
        background = pygame.image.load(os.path.join('images', 'backgrounds', 'mountains_background.png'))
        fourth_level = design_fourth_level(enemies, armament)
        back_decorations, front_decorations = decoration_level_4()
        return fourth_level, background, back_decorations, front_decorations

    if level_id == 5:
        background = pygame.image.load(os.path.join('images', 'backgrounds', 'mountains_background.png'))
        fifth_level = design_fifth_level(enemies, armament)
        back_decorations, front_decorations = decoration_level_5()
        return fifth_level, background, back_decorations, front_decorations
