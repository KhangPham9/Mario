import pygame as pg
from block import Block
from settings import *
from mario import Mario
from goomba import Goomba


class Level:
    block_dic = {
        'B': 'images/Red_Brick.png',
        'X': 'images/Ground_Brick.png',
        '?': 'images/Item_Brick.png',
        'M': 'images/Mushroom.png',
        'R': 'images/Stair_Brick.png'
    }
    mob_dic = {
        'G': Goomba.create_goomba
    }

    def __init__(self, level, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.mario = Mario(game=self.game, pos=(0, 32 * 14))
        self.bg = game.bg
        self.setup_level(level)

    def setup_level(self, layout):
        self.blocks = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * self.settings.tile_size
                y = row_index * self.settings.tile_size
                if cell in Level.block_dic:
                    # print(f'{row_index}, {col_index}: {cell}')
                    block = Block((x, y), Level.block_dic[cell])
                    self.blocks.add(block)
                elif cell in Level.mob_dic:
                    mob = Level.mob_dic[cell](game=self.game, pos=(x, y))
                    self.mobs.add(mob)

    def scroll(self):
        self.blocks.update(-1 * self.settings.mario_speed_factor)
        self.bg.update()

    def update(self):
        self.mario.check_input()
        self.vertical_collision()
        self.horizontal_collision()
        if self.mario.check_scroll():
            self.mario.vector.x = 0
            self.scroll()
        else:
            self.mario.update()
        self.mobs.update()

    def draw(self):
        self.mario.draw()
        self.blocks.draw(self.screen)
        self.mobs.draw(self.screen)

    def horizontal_collision(self):
        for sprite in self.blocks.sprites():
            if sprite.rect.colliderect(self.mario.rect):
                if self.mario.vector.x < 0:
                    self.mario.rect.left = sprite.rect.right
                elif self.mario.vector.x > 0:
                    self.mario.rect.right = sprite.rect.left

    def vertical_collision(self):
        self.apply_gravity(self.mario)
        for mob in self.mobs:
            self.apply_gravity(mob)

        for block in self.blocks.sprites():
            if block.rect.colliderect(self.mario.rect):
                if self.mario.vector.y < 0:
                    self.mario.rect.top = block.rect.bottom
                elif self.mario.vector.y > 0:
                    self.mario.rect.bottom = block.rect.top
                    self.mario.vector.y = 0

        for blocks in self.blocks.sprites():
            for mob in self.mobs.sprites():
                if blocks.rect.colliderect(mob.rect):
                    if mob.vector.y < 0:
                        mob.rect.top = blocks.rect.bottom
                    elif mob.vector.y > 0:
                        mob.rect.bottom = blocks.rect.top
                        mob.vector.y = 0

    def apply_gravity(self, sprite):
        sprite.vector.y += self.settings.gravity
        sprite.rect.y += sprite.vector.y
