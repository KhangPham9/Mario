import pygame as pg
from block import Block
from settings import *

class Level:
    block_dic = {
        'B': 'images/Red_Brick.png',
        'X': 'images/Ground_Brick.png',
        '?': 'images/Invisible_Block.png',
        'M': 'images/Mushroom.png'
    }
    def __init__(self, level, game):
        self.screen = game.screen
        self.mario = game.mario
        self.setup_level(level)


    def setup_level(self, layout):
        self.blocks = pg.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell in Level.block_dic:
                    # print(f'{row_index}, {col_index}: {cell}')
                    x = col_index * 32
                    y = row_index * 32
                    block = Block((x,y), Level.block_dic[cell])
                    self.blocks.add(block)
                    # print(f'{x} {y}')

    def scroll(self):
        self.blocks.update(1)

    def update(self):
        if self.mario.check_scroll():
            self.scroll()

    def draw(self):
        self.blocks.draw(self.screen)
