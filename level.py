from block import Block
from background import Background
from goomba import Goomba
from mario import Mario
from flag import Flag
from settings import *


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
        self.mario = Mario(game=self.game, pos=(0, 32 * 15))
        self.level = level

        self.blocks = None
        self.mobs = None
        self.flag = None
        self.setup_level(self.level)

    def reset(self):
        for block in self.blocks:
            block.kill()

        for mob in self.mobs:
            mob.kill()

        self.mario.reset()
        self.bg.reset()

    def setup_level(self, layout):
        self.bg = Background(game=self.game)
        self.blocks = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * self.settings.tile_size
                y = row_index * self.settings.tile_size
                if cell in Level.block_dic:
                    # print(f'{row_index}, {col_index}: {cell}')
                    block = Block(
                        (x, y), Level.block_dic[cell])
                    self.blocks.add(block)
                elif cell in Level.mob_dic:
                    mob = Level.mob_dic[cell](game=self.game, pos=(x, y))
                    self.mobs.add(mob)
                elif cell == 'F':
                    image = self.settings.get_flag()
                    flag = Flag(self.game, (x, y), image)
                    self.flag = flag

    def scroll(self):
        self.blocks.update(-1 * self.settings.mario_speed_factor)
        self.bg.update()
        self.flag.update(-1 * self.settings.mario_speed_factor)
        self.settings.goomba_speed_factor = 16
        self.game.stats.score += 10

    def update(self):
        self.mario.check_input()
        self.horizontal_collision()
        self.vertical_collision()
        self.mobs.update()
        if self.mario.check_scroll():
            self.mario.vector.x = 0
            self.scroll()
        else:
            self.mario.update()
            self.settings.goomba_speed_factor = 4

        self.game.stats.highscore = max(
            self.game.stats.score, self.game.stats.highscore)

    def draw(self):
        self.bg.draw()
        self.mario.draw()
        self.blocks.draw(self.screen)
        for mob in self.mobs:
            mob.draw()

        self.flag.draw()

    def horizontal_collision(self):
        for blocks in self.blocks.sprites():
            if blocks.rect.colliderect(self.mario.rect):
                if self.mario.vector.x < 0:
                    self.mario.rect.left = blocks.rect.right
                elif self.mario.vector.x > 0:
                    self.mario.rect.right = blocks.rect.left

        for blocks in self.blocks.sprites():
            for mob in self.mobs.sprites():
                if not mob.dying:
                    if blocks.rect.colliderect(mob.rect):
                        if mob.vector.x < 0:
                            mob.rect.left = blocks.rect.right
                        elif mob.vector.x > 0:
                            mob.rect.right = blocks.rect.left
                        mob.turn()

        for mob in self.mobs.sprites():
            if not mob.dying:
                if mob.rect.colliderect(self.mario.rect):
                    self.game.stats.mario_hit()
                    self.reset()
                    self.setup_level(self.level)

        if self.flag.rect.colliderect(self.mario.rect):
            self.game.finished = True

    def vertical_collision(self):
        self.apply_gravity(self.mario)
        for mob in self.mobs:
            if not mob.dying:
                self.apply_gravity(mob)

        for block in self.blocks.sprites():
            if block.rect.colliderect(self.mario.rect):
                if self.mario.vector.y < 0:
                    self.mario.rect.top = block.rect.bottom
                elif self.mario.vector.y > 0:
                    self.mario.vector.y = 0
                    self.mario.rect.bottom = block.rect.top

        for blocks in self.blocks.sprites():
            for mob in self.mobs.sprites():
                if not mob.dying:
                    if blocks.rect.colliderect(mob.rect):
                        if mob.vector.y < 0:
                            mob.rect.top = blocks.rect.bottom
                        elif mob.vector.y > 0:
                            mob.rect.bottom = blocks.rect.top
                            mob.vector.y = 0

        for mob in self.mobs.sprites():
            if not mob.dying:
                if mob.rect.colliderect(self.mario.rect):
                    if self.mario.vector.y > 0:
                        self.mario.jumping = False
                        self.mario.jump()
                        self.game.stats.goomba_hit(mob)
                        mob.switch_timer()

    def apply_gravity(self, sprite):
        sprite.vector.y += self.settings.gravity
        sprite.rect.y += sprite.vector.y
