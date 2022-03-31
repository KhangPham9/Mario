import pygame as pg
from settings import Settings
from landing_page import LandingPage
from mario import Mario
from background import Background
from block import Block


class Game:
    level1 = pg.image.load('images/level1.png')

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pg.display.set_caption("Super Mario")

        self.bg = Background(game=self)
        self.mario = Mario(game=self)
        self.block = Block(game=self, image_url='images/Blue_Brick.png')

    def restart(self):
        pass

    def update(self):
        self.mario.update()

    def draw(self):
        self.bg.draw()
        self.block.draw()
        self.mario.draw()
        pg.display.flip()

    def play(self):
        self.finished = False
        while not self.finished:
            self.update()
            self.draw()


def main():
    g = Game()
    l = LandingPage(game=g)
    l.show()
    g.play()


if __name__ == '__main__':
    main()
