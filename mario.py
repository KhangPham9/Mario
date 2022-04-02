import pygame as pg
import math
from vector import Vector
from sprites import Sprites
from timer import Timer


class Mario(Sprites):

    def __init__(self, game, pos):
        super().__init__(game)
        self.image = pg.transform.rotozoom(self.game.settings.get_sheet_image(
            self.game.settings.sprite_sheet, self.game.settings.mario_rect), 0, 2)

        self.s_mario_images = game.settings.s_mario_images()

        self.r_move_image = [self.s_mario_images[1],
                             self.s_mario_images[2], self.s_mario_images[3]]
        self.l_move_image = [self.s_mario_images[7],
                             self.s_mario_images[8], self.s_mario_images[9]]
        self.image_dic = {
            'D': self.r_move_image,
            'A': self.l_move_image
        }

        self.rect = self.image.get_rect(topleft=pos)
        self.vector = pg.math.Vector2(0, 0)
        self.timer = Timer(image_list=self.s_mario_images)
        self.last_key_pressed = None

    def update(self):
        self.rect.x += self.vector.x
        # self.clamp()
        # self.rect.centerx, self.rect.centery = self.center.x, self.center.y

    def draw(self):
        if self.last_key_pressed != None:
            self.image = self.timer.image()
        self.screen.blit(self.image, self.rect)

    def clamp(self):
        rw, rh = self.rect.width, self.rect.height
        srw, srb = self.screen_rect.width - 50, self.screen_rect.bottom
        x, y = self.center.x, self.center.y

        self.center.x = min(max(x, rw / 2), srw - rw / 2)
        self.center.y = min(max(y, rh / 2), srb - rh / 2)

    def check_scroll(self):
        if self.rect.x + self.rect.width >= self.screen_rect.width - 50 and self.last_key_pressed == 'D':
            return True

    def check_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_d]:
            if self.last_key_pressed != 'D':
                self.timer = Timer(image_list=self.image_dic['D'])
            self.vector.x = 1 * self.game.settings.mario_speed_factor
            self.last_key_pressed = 'D'
        elif keys[pg.K_a]:
            if self.last_key_pressed != 'A':
                self.timer = Timer(image_list=self.image_dic['A'])
            self.vector.x = -1 * self.game.settings.mario_speed_factor
            self.last_key_pressed = 'A'
        else:
            self.vector.x = 0
            self.last_key_pressed = None
            self.image = self.s_mario_images[0]
