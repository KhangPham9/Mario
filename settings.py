import pygame as pg


class Settings:
    file1 = open('images/level_loc.txt', 'r')
    level = file1.readlines()

    level_map = []
    for line in level:
        level_map.append(line)

    def __init__(self):
        # screen settings
        self.level_map = Settings.level_map
        self.tile_size = 32
        self.screen_width = 1200
        self.screen_height = (len(self.level_map) - 15) * self.tile_size
        self.bg_color = (60, 60, 60)

        self.sprite_sheet = pg.image.load('images/allsprites.png')

        # font settings
        self.headingFont = pg.font.SysFont('', 140)
        self.subheadingFont = pg.font.SysFont('', 122)
        self.font = pg.font.SysFont('', 48)

        # sprite settings
        self.goomba_rect = pg.Rect(0, 0, 16, 16)
        self.goomba_speed_factor = 4
        self.goomba_points = 100

        # mario settings
        self.mario_rect = pg.Rect(57, 0, 16, 16)
        self.mario_speed_factor = 12
        self.mario_jump = -12
        self.mario_lives = 3

        # level settings
        self.level_rect = pg.Rect(0, 0, 1200, 800)

        self.gravity = 0.4

    def s_mario_images(self):
        return [pg.transform.rotozoom(self.get_sheet_image(self.sprite_sheet,
                                                           pg.Rect(57, x, 16,
                                                                   16)), 0, 2)
                for x in range(0, 16 * 15, 20)]

    def b_mario_images(self):
        return [pg.transform.rotozoom(self.get_sheet_image(self.sprite_sheet,
                                                           pg.Rect(120, x, 16,
                                                                   32)), 0, 2)
                for x in range(0, 40 * 11, 40)]

    def goomba_images(self):
        return [pg.transform.rotozoom(self.get_sheet_image(self.sprite_sheet,
                                                           pg.Rect(0, x, 16, 16)), 0, 2)
                for x in range(0, 22 * 3, 22)]

    def get_flag(self):
        return pg.transform.rotozoom(self.get_sheet_image(self.sprite_sheet,
                                                          pg.Rect(318, 0, 16, 128)), 0, 2)

    @staticmethod
    def get_sheet_image(spritesheet, rectangle, color_key=None):
        rect = rectangle
        sheet = spritesheet
        image = pg.Surface(rect.size).convert_alpha()
        image.blit(sheet, (0, 0), rect)
        return image
