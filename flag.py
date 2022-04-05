import pygame as pg


class Flag(pg.sprite.Sprite):
    def __init__(self, game, pos, image):
        super().__init__()
        self.screen = game.screen
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.original_pos = pos

    def update(self, shift=0):
        self.rect.x += shift

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def reset(self):
        self.rect = self.image.get_rect(topleft=self.original_pos)
