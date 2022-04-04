import pygame as pg
from button import Button
import sys


class GameOver:

    def __init__(self, game):
        # settings
        self.screen = game.screen
        self.settings = game.settings
        self.finished = False
        self.stats = game.stats



        # text
        self.rect = pg.Rect(320, 0, 800, 200)
        self.rect1 = pg.Rect(320, 200, 800, 100)
        self.rect2 = pg.Rect(320, 300, 800, 100)
        self.text = self.render_font(self.settings.headingFont, msg="Game Over", text_color='black',
                                     bg_color=(255, 0, 0))
        self.text1 = self.render_font(self.settings.subheadingFont, msg=f'Score: {self.stats.score}', text_color='black',
                                      bg_color='red')
        self.text2 = self.render_font(self.settings.subheadingFont, msg=f'Highscore: {self.stats.highscore}',
                                      text_color='black', bg_color='red')

        # buttons
        self.play_button = Button(self.screen, "QUIT GAME", ul=(500, 400))
        self.hover = False

        if self.stats.score > self.stats.highscore:
            self.stats.high_score = self.stats.score
            self.stats.save_high_score()


    @staticmethod
    def render_font(font, msg, text_color, bg_color, antialis=True):
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
        self.screen.blit(self.text1, self.rect1)
        self.screen.blit(self.text2, self.rect2)
        self.play_button.draw()
        pg.display.flip()

    def mouse_on_button(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.play_button.rect.collidepoint(mouse_x, mouse_y)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit("exiting mario")
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
