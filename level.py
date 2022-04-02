import pygame as pg
from block import Block
from settings import *
from mario import Mario


class Level:
    block_dic = {
        'B': 'images/Red_Brick.png',
        'X': 'images/Ground_Brick.png',
        '?': 'images/Invisible_Block.png',
        'M': 'images/Mushroom.png'
    }

    def __init__(self, level, game):
        self.settings = game.settings
        self.screen = game.screen
        self.mario = Mario(game=self, pos=(0, 32 * 14))
        self.bg = game.bg
        self.setup_level(level)

    def setup_level(self, layout):
        self.blocks = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell in Level.block_dic:
                    # print(f'{row_index}, {col_index}: {cell}')
                    x = col_index * self.settings.tile_size
                    y = row_index * self.settings.tile_size
                    block = Block((x, y), Level.block_dic[cell])
                    self.blocks.add(block)
                    # print(f'{x} {y}')

    def scroll(self):
        self.blocks.update(-1)
        self.bg.update()

    def update(self):
        self.mario.check_input()
        if self.mario.check_scroll():
            self.mario.vector.x = 0
            self.blocks.update(-1 * self.settings.mario_speed_factor)
        else:
            self.mario.update()

    def draw(self):
        self.mario.draw()
        self.blocks.draw(self.screen)
