import pygame as pg


DARK_GREY = (30, 30, 30)


class SbElement:
    def __init__(self, screen, bg_color, ul, font, get_score, element_type=None):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_color = bg_color
        self.ul = ul
        self.font = font
        self.text_color = DARK_GREY
        self.score_image, self.score_rect = None, None
        self.get_score = get_score
        self.last_score = self.get_score()
        self.first_update = True
        self.element_type = element_type
        self.update()

    def update(self): 
        score = self.get_score()
        if not self.first_update and self.last_score == score:
            return

        self.first_update = False
        self.last_score = score
        if self.element_type == 'lives':
            score_str = f'Lives left: {str(score)}'
        else:
            score_str = str(score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        r = self.score_rect 
        if self.ul[0] + r.width > self.screen_rect.right:
            self.score_rect.right = self.screen_rect.right - 20
        else:
            self.score_rect.left = self.ul[0]
        self.score_rect.top = self.ul[1]

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)


class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.stats = game.stats
        screen = game.screen
        sr = screen.get_rect()
        self.bg_color = (255, 255, 255)
        font = pg.font.SysFont('', 48)

        self.score = SbElement(screen=screen, bg_color=self.bg_color,
                               ul=(sr.right - 40, 20), font=font, 
                               get_score=self.stats.get_score)
        self.highscore = SbElement(screen=screen, bg_color=self.bg_color,
                                   ul=(sr.centerx, 20), font=font, 
                                   get_score=self.stats.get_highscore)

        self.lives = SbElement(screen=screen, bg_color=self.bg_color,
                               ul=(sr.left, 20), font=font,
                               get_score=self.stats.get_lives_left, element_type='lives')

        self.update()

    def update(self):
        self.lives.update()
        self.score.update()
        self.highscore.update()

    def draw(self): 
        self.score.draw()
        self.lives.draw()
