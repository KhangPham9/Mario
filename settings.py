import pygame as pg


class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (60, 60, 60)

        # font settings
        self.headingFont = pg.font.SysFont(None, 140)
        self.subheadingFont = pg.font.SysFont(None, 122)
        self.font = pg.font.SysFont(None, 48)

        # sprite settings
        self.goomba_rect = pg.Rect(0, 0, 16, 16)

        self.mario_rect = pg.Rect(57, 0, 16, 16)

        # mario settings
        self.mario_speed_factor = 0.5

        # level settings
        self.level_rect = pg.Rect(0, 0, 1200, 800)

    def get_sheet_image(self, spritesheet, rectangle, color_key=None):
        """gets an image from a sprite sheet expects a pygame rectangle
            and a spritesheet """
        rect = rectangle
        sheet = spritesheet
        image = pg.Surface(rect.size).convert()
        image.blit(sheet, (0, 0), rect)
        return image
