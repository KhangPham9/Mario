import pygame as pg


class Flag(pg.sprite.Sprite):
    def __init__(self, game, pos, image):
        super().__init__()
        self.screen = game.screen
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, shift=0):
        self.rect.x += shift

    def draw(self):
        self.screen.blit(self.image, self.rect)
