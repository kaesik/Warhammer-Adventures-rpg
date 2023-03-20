import pygame
from settings import *
from entity import Entity

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups):

        # GENERAL SETUP
        super().__init__(groups)
        self.sprite_type = "enemy"
