import pygame as pg
from settings import Settings
from landing_page import LandingPage
from level import Level
from scoreboard import Scoreboard
from stats import Stats
from game_over import GameOver


class Game:
    level1 = pg.image.load('images/level1.png')

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.stats = Stats(game=self)
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.sb = Scoreboard(game=self)
        self.clock = pg.time.Clock()
        pg.display.set_caption("Super Mario")

        self.level = Level(self.settings.level_map, game=self)
        self.finished = False

    def restart(self):
        pass

    def update(self):
        self.check_events()
        self.level.update()
        self.sb.update()

    def draw(self):
        self.level.draw()
        self.sb.draw()
        pg.display.flip()

    def play(self):
        self.finished = False
        while not self.finished:
            self.update()
            self.draw()
            self.clock.tick(60)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.finished = True
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_q:
                    self.finished = True


def main():
    g = Game()
    level = LandingPage(game=g)
    level.show()
    g.play()
    game_over = GameOver(game=g)
    game_over.show()


if __name__ == '__main__':
    main()
