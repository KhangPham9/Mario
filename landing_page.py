import pygame as pg
from button import Button
import sys


class LandingPage:

    def __init__(self, game):
        # settings
        self.screen = game.screen
        self.settings = game.settings
        self.finished = False

        # text
        self.rect = pg.Rect(320, 200, 800, 400)
        self.text = self.render_font(self.settings.headingFont, msg="Super Mario", text_color=(0, 0, 0),
                                     bg_color=(255, 0, 0))

        # buttons
        self.play_button = Button(self.screen, "PLAY GAME", ul=(500, 400))
        self.hover = False

    def render_font(self, font, msg, text_color, bg_color, antialis=True):
        text = font.render(msg, antialis, text_color, bg_color)
        return text

    def update(self):
        pass

    def show(self):
        while not self.finished:
            self.update()
            self.draw()
            self.check_events()

    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.text, self.rect)
        self.play_button.draw()
        pg.display.flip()

    def mouse_on_button(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.play_button.rect.collidepoint(mouse_x, mouse_y)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit("exiting mario")
                sys.exit()
            elif e.type == pg.MOUSEBUTTONDOWN:
                if self.mouse_on_button:
                    self.finished = True
            elif e.type == pg.MOUSEMOTION:
                if self.mouse_on_button() and not self.hover:
                    self.play_button.toggle_colors()
                    self.hover = True
                elif not self.mouse_on_button() and self.hover:
                    self.play_button.toggle_colors()
                    self.hover = False
