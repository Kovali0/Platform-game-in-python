from unittest import TestCase
from Level import Level
import pygame


def initPygame():
    pygame.init()
    pygame.display.set_mode([960, 780])


class TestLevel(TestCase):
    def setUp(self):
        initPygame()
        p_loc = [(64 * 3, 780 - 64 * 4, 3)]
        water_points = [-10, -9, -8, -7, -6, 6, 7, 8, 9, 10]
        self.level = Level(1, 64, 64, 780, water_points, 20, p_loc)

    def test_ground(self):
        self.assertEqual(len(self.level.ground_list), 20)
        self.assertEqual(len(self.level.water_list), 10)

    def test_platforms(self):
        self.assertEqual(len(self.level.plat_list), 3 + 1)
        platform = self.level.plat_list.sprites()[0]
        self.assertEqual(platform.rect.x, 64 * 3)
        self.assertEqual(platform.rect.y, 780 - 64 * 4)
        self.assertEqual(platform.is_water, False)

    def test_set_coins(self):
        self.assertEqual(len(self.level.coins_list), 0)
        self.level.set_coins([(5, 780 - 64 * 2)])
        self.assertEqual(len(self.level.coins_list), 1)
        coin = self.level.coins_list.sprites()[0]
        self.assertEqual(coin.rect.center, (5 * 64, 780 - 64 * 2))

    def test_set_key(self):
        self.assertEqual(len(self.level.key), 0)
        self.level.set_key((4, 780 - 64 * 5))
        self.assertEqual(len(self.level.key), 1)
        key = self.level.key.sprites()[0]
        self.assertEqual(key.rect.center, (4 * 64, 780 - 64 * 5))

    def test_set_doors(self):
        self.assertEqual(len(self.level.doors), 0)
        self.level.set_doors((1, 780 - 64 * 2))
        self.assertEqual(len(self.level.doors), 1)
        doors = self.level.doors.sprites()[0]
        self.assertEqual(doors.image, doors.doors[0])
