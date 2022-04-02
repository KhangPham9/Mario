import pygame as pg
from settings import Settings
from landing_page import LandingPage
from mario import Mario
from background import Background
from block import Block
from level import Level

class Game:
    level1 = pg.image.load('images/level1.png')

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.clock = pg.time.Clock()
        pg.display.set_caption("Super Mario")

        self.bg = Background(game=self)
        self.mario = Mario(game=self)
        self.level = Level(self.settings.level_map, game=self)

    def restart(self):
        pass

    def update(self):
        self.mario.update()

    def draw(self):
        self.bg.draw()
        self.level.draw()
        self.mario.draw()
        pg.display.flip()

    def play(self):
        self.finished = False
        while not self.finished:
            self.update()
            self.draw()
            self.clock.tick(120)

def main():
    g = Game()
    l = LandingPage(game=g)
    l.show()
    g.play()


if __name__ == '__main__':
    main()
