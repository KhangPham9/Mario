import pygame as pg
from timer import Timer


class Mario(pg.sprite.Sprite):

    def __init__(self, game, pos):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.original_pos = pos

        self.image = pg.transform.rotozoom(self.settings.get_sheet_image(
            self.settings.sprite_sheet, self.settings.mario_rect), 0, 2)

        self.s_mario_images = game.settings.s_mario_images()

        self.b_mario_images = game.settings.b_mario_images()

        self.s_r_move_image = [self.s_mario_images[1],
                               self.s_mario_images[2], self.s_mario_images[3]]
        self.s_l_move_image = [self.s_mario_images[7],
                               self.s_mario_images[8], self.s_mario_images[9]]

        self.b_r_move_image = [self.b_mario_images[1], self.b_mario_images[2], self.b_mario_images[3],
                               self.b_mario_images[5]]
        self.b_l_move_image = [self.b_mario_images[6], self.b_mario_images[7], self.b_mario_images[8],
                               self.b_mario_images[10]]

        self.s_image_dic = {
            'D': self.s_r_move_image,
            'A': self.s_l_move_image
        }
        self.b_image_dic = {
            'D': self.b_r_move_image,
            'A': self.b_l_move_image
        }
        self.image_dic = {
            's': self.s_image_dic,
            'b': self.b_image_dic
        }

        self.rect = self.image.get_rect(topleft=pos)
        self.vector = pg.math.Vector2(0, 0)
        self.timer = Timer(image_list=self.s_mario_images)
        self.last_key_pressed = None
        self.jumping = False
        self.size = 's'

    def update(self):
        self.clamp_left()
        self.rect.x += self.vector.x
        # self.clamp()
        # self.rect.centerx, self.rect.centery = self.center.x, self.center.y

    def draw(self):
        if self.last_key_pressed:
            self.image = self.timer.image()
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect(topleft=(x, y))
        self.screen.blit(self.image, self.rect)

    def check_scroll(self):
        if self.rect.x + self.rect.width >= self.screen_rect.width - 200 and self.last_key_pressed == 'D':
            return True

    def check_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_d]:
            if self.last_key_pressed != 'D':
                self.timer = Timer(image_list=self.image_dic[self.size]['D'])
            self.vector.x = 1 * self.game.settings.mario_speed_factor
            self.last_key_pressed = 'D'
        elif keys[pg.K_a]:
            if self.last_key_pressed != 'A':
                self.timer = Timer(image_list=self.image_dic[self.size]['A'])
            self.vector.x = -1 * self.game.settings.mario_speed_factor
            self.last_key_pressed = 'A'
        else:
            self.vector.x = 0
            self.last_key_pressed = None
            if self.size == 's':
                self.image = self.s_mario_images[0]
            else:
                self.image = self.b_mario_images[0]
        if keys[pg.K_w] and not self.is_jumping():
            self.jump()

    def clamp_left(self):
        if self.rect.x <= 0 and self.last_key_pressed == 'A':
            self.rect.x = 0
            self.vector.x = 0

    def jump(self):
        if not self.jumping:
            self.vector.y = self.settings.mario_jump

    def is_jumping(self):
        if self.vector.y == 0:
            self.jumping = False
        else:
            self.jumping = True

    def change_size(self, str):
        self.size = str

    def reset(self):
        self.image = pg.transform.rotozoom(self.settings.get_sheet_image(
            self.settings.sprite_sheet, self.settings.mario_rect), 0, 2)
        self.rect = self.image.get_rect(topleft=self.original_pos)
