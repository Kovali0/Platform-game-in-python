from unittest import TestCase
from player import Player
import pygame


def initPygame():
    pygame.init()
    pygame.display.set_mode([960, 780])


class TestPlayer(TestCase):

    def setUp(self):
        initPygame()
        self.player = Player(0, 0)

    def test_init(self):
        self.assertEqual(self.player.rect.x, 0)
        self.assertEqual(self.player.rect.y, 0)

    def test_move(self):
        self.player.move(20, 20)
        self.assertEqual(self.player.rect.x, 20)
        self.assertEqual(self.player.rect.y, 20)
        self.player.move(-15, -15)
        self.assertEqual(self.player.rect.x, 5)
        self.assertEqual(self.player.rect.y, 5)

    def test_gravity(self):
        self.player.vel_y = 7
        self.player.gravity()
        self.player.gravity()
        self.assertEqual(self.player.vel_y, 9)
        self.player.gravity()
        self.player.gravity()
        self.assertEqual(self.player.vel_y, 10)

    def test_fall_off_the_world(self):
        self.player.move(20, 20)
        self.player.fall_off_the_world()
        self.assertEqual(self.player.life, 1)
        self.assertEqual(self.player.rect.x, 0)
        self.assertEqual(self.player.rect.y, -64 * 3)

    def test_reset(self):
        self.player.frame_counter = 2
        self.player.direction = "left"
        self.player.gravity()
        self.player.reset(200)
        self.assertEqual(self.player.frame_counter, 0)
        self.assertEqual(self.player.direction, "right")
        self.assertEqual(self.player.vel_y, 0)
        self.assertEqual(self.player.rect.x, 200)
        self.assertEqual(self.player.rect.y, -64 * 3)
