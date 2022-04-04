import pygame as pg
from timer import Timer


class Goomba(pg.sprite.Sprite):

    def __init__(self, game, pos):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image_list = self.game.settings.goomba_images()
        self.image = self.image_list[0]
        self.move_images = [self.image_list[0], self.image_list[1]]
        self.death_image = [self.image_list[2], self.image_list[2]]
        self.rect = self.image.get_rect(topleft=pos)
        self.vector = pg.math.Vector2(-1, 0)

        self.timer = Timer(image_list=self.move_images)
        self.dying = False

    def update(self):
        if not self.dying:
            self.rect.x += self.vector.x * self.settings.goomba_speed_factor
        if self.timer.is_expired():
            self.kill()

    def turn(self):
        self.vector *= -1

    def draw(self):
        self.image = self.timer.image()
        self.screen.blit(self.image, self.rect)

    def switch_timer(self):
        self.timer = Timer(image_list=self.death_image, is_loop=False, delay=300)

    @staticmethod
    def create_goomba(game, pos):
        return Goomba(game=game, pos=pos)


