from unittest import TestCase
from enemy import Enemy, Slime
import pygame


def initPygame():
    pygame.init()
    pygame.display.set_mode([960, 780])


class TestEnemy(TestCase):
    def setUp(self):
        initPygame()
        self.enemy = Enemy(["slimeBlue.png"])
        self.enemy.set_enemy_location(128, 128, 200)

    def test_set_enemy_location(self):
        self.enemy.set_enemy_location(64, 64, 100)
        self.assertEqual(self.enemy.rect.x, 64)
        self.assertEqual(self.enemy.rect.y, 64)
        self.assertEqual(self.enemy.distance, 100)

    def test_move(self):
        self.assertEqual(self.enemy.rect.x, 128)
        self.assertEqual(self.enemy.rect.y, 128)
        self.assertEqual(self.enemy.frame_counter, 0)
        self.enemy.move(128, 128)
        self.assertEqual(self.enemy.rect.x, 256)
        self.assertEqual(self.enemy.rect.y, 256)
        self.assertEqual(self.enemy.frame_counter, 1)


class TestSlime(TestCase):
    def setUp(self):
        initPygame()
        self.enemy = Slime(["slimeBlue.png"])
        self.enemy.set_enemy_location(128, 128, 20)

    def test_controller(self):
        self.assertEqual(self.enemy.rect.x, 128)
        self.assertEqual(self.enemy.move_counter, 0)
        self.assertEqual(self.enemy.current_direction, 2)
        self.enemy.controller()
        self.assertEqual(self.enemy.rect.x, 130)
        self.assertEqual(self.enemy.move_counter, 1)
        for i in range(21):
            self.enemy.controller()
        self.assertEqual(self.enemy.rect.x, 164)
        self.assertEqual(self.enemy.move_counter, -18)
        self.assertEqual(self.enemy.current_direction, -2)
