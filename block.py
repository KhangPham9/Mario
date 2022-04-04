import pygame as pg


def get_image(url):
    return pg.transform.rotozoom(
        pg.image.load(url).convert_alpha(), 0, 2)


class Block(pg.sprite.Sprite):
    def __init__(self, pos, url, block_type):
        super().__init__()
        self.image = get_image(url)
        self.rect = self.image.get_rect(topleft=pos)
        self.type = block_type
        self.on_screen = False

    def update(self, shift=0):
        self.rect.x += shift

    def check_on_screen(self, game):
        if game.bg.rect.right > self.rect.right > game.bg.rect.left:
            self.on_screen = True
        else:
            self.on_screen = False
