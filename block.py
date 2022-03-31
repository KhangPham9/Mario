import pygame as pg
from pygame.sprite import Sprite, Group


class Block(Sprite):

    def __init__(self, game, image_url):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.image = pg.transform.rotozoom(
            pg.image.load(image_url).convert_alpha(), 0, 3)
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, (50, 50))
