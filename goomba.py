import pygame as pg
import math
from vector import Vector
from timer import Timer


class Goomba(pg.sprite.Sprite):

    def __init__(self, game, pos):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.transform.rotozoom(self.settings.get_sheet_image(
            self.settings.sprite_sheet, self.settings.goomba_rect), 0, 2)

        self.rect = self.image.get_rect(topleft=pos)

        self.vector = pg.math.Vector2(-1, 0)

    def update(self):
        self.rect.x += self.vector.x * self.settings.goomba_speed_factor

    def move(self, vector=pg.math.Vector2(-1, 0)):
        self.vector = vector

    @staticmethod
    def create_goomba(game, pos):
        return Goomba(game=game, pos=pos)
    # def draw(self):
    # self.screen.blit(self.image, self.rect)
