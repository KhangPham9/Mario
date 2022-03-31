import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group


class Rectangle(Sprite):

    def __init__(self, game):
        super().__init__()
