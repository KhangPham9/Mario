import pygame as pg


class Block(pg.sprite.Sprite):
    def __init__(self, pos, url):
        super().__init__()
        self.image = self.get_image(url)
        self.rect = self.image.get_rect(topleft=pos)

    def get_image(self, url):
        return pg.transform.rotozoom(
            pg.image.load(url).convert_alpha(), 0, 2)

    def update(self, shift=0):
        self.rect.x += shift
