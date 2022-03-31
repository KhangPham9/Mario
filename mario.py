import pygame as pg
import math
from vector import Vector
from sprites import Sprites

LEFT, RIGHT, UP, DOWN, STOP = 'left', 'right', 'up', 'down', 'stop'

dirs = {LEFT: Vector(-1, 0),
        RIGHT: Vector(1, 0),
        UP: Vector(0, -1),
        DOWN: Vector(0, 1),
        STOP: Vector(0, 0)}

dir_keys = {pg.K_LEFT: LEFT, pg.K_a: LEFT,
            pg.K_RIGHT: RIGHT, pg.K_d: RIGHT,
            pg.K_UP: UP, pg.K_w: UP,
            pg.K_DOWN: DOWN, pg.K_s: DOWN}


class Mario(Sprites):

    def __init__(self, game):
        super().__init__(game)
        self.image = pg.transform.rotozoom(self.game.settings.get_sheet_image(
            self.spritesheet, self.game.settings.mario_rect), 0, 3)

        self.rect = self.image.get_rect()
        self.center = Vector(self.rect.centerx, self.rect.centery)
        self.rect.y = self.screen_rect.bottom - 170

        self.moving = False
        self.jump = False
        self.time = 0
        self.frames = 0

    def update(self):
        # print(f'self.vector: {self.vector}')
        self.check_jump()
        self.check_scroll()
        self.check_bottom()
        self.check_events()
        self.change_position(self.game.settings.mario_speed_factor)
        self.clamp()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.game.finished = True
            elif e.type == pg.KEYDOWN:
                if e.key in dir_keys:
                    self.moving = True
                    v = dirs[dir_keys[e.key]]
                    if e.key == pg.K_w:
                        self.jump = True
                    self.inc_add(v)
                elif e.key == pg.K_q:
                    self.game.finished = True
            elif e.type == pg.KEYUP:
                if e.key in dir_keys:
                    if e.key == pg.K_w:
                        return
                    self.moving = False
                    v = dirs[dir_keys[e.key]]
                    self.inc_add(-v)

    def clamp(self):
        rw, rh = self.rect.width, self.rect.height
        srw, srb = self.screen_rect.width - 50, self.screen_rect.bottom - 170
        x, y = self.center.x, self.center.y

        self.center.x = min(max(x, rw / 2), srw - rw / 2)
        self.center.y = min(max(y, rh / 2), srb - rh / 2)

    def check_jump(self):
        if self.jump:
            # if self.frames % 60 == 0:
            self.time += 0.01
            print(f'time: {self.time}')
            self.mario_jump()
            self.frames = 0
            # self.frames += 1

    def mario_jump(self):
        angle = math.sin(math.pi / 3)
        vely = -0.7 * angle
        dis = (vely * self.time + 0.9 * self.time**2 / 2) * 0.005
        vectory = Vector(0, dis)
        # print(vectory)
        self.inc_add(vectory)

    def check_bottom(self):
        if self.rect.centery + self.rect.height / 2 >= self.screen_rect.bottom - 170:
            # print('finished')
            self.time = 0
            self.jump = False
            self.vector = Vector(self.vector.x, 0)

    def check_scroll(self):
        if self.center.x + self.rect.width / 2 >= self.screen_rect.width - 50 and self.moving:
            self.game.bg.update()
