import pygame as pg


class Background:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.settings = game.settings
        self.rect = self.settings.level_rect
        self.bg = pg.transform.rotozoom(self.settings.get_sheet_image(
            pg.image.load('images/level_bg.png'), self.rect), 0, 2.3)

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

    def update(self):
        self.rect.x += self.settings.mario_speed_factor / 2
        self.bg = pg.transform.rotozoom(self.settings.get_sheet_image(
            pg.image.load('images/level_bg.png').convert_alpha(), self.rect), 0, 2.3)

    def reset(self):
        self.rect.x = 0
