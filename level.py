import pygame
from settings import *
from debug import debug
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # GET THE DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()

        # SPRITE GROUP SETUP
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # SPRITE SETUP
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                if col == "p":
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

            # print(row_index)
            # print(row)

    def run(self):
        # UPDATE AND DRAW THE GAME
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)