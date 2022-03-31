import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group


class Sprites(Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.spritesheet = pg.image.load(
            'images/allsprites.png').convert_alpha()
        self.screen_rect = self.screen.get_rect()
        self.vector = Vector()

    def move(self, velocity=Vector(0, 0), acceleration=Vector(0, 0)):
        self.vector += velocity

    def change_position(self, speed_factor=1):
        self.center += self.vector * speed_factor

    def moving(self, vector): self.vector = vector

    def inc_add(self, other):
        self.vector += other
