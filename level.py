import pygame
import random
from settings import *
from debug import debug
from tile import Tile
from player import Player
from support import *

class Level:
    def __init__(self):

        # GET THE DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()

        # SPRITE GROUP SETUP
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        # SPRITE SETUP
        self.create_map()

    def create_map(self):
        layouts = {
            "boundary": import_csv_layout("./map/map_FloorBlocks.csv"),
            "grass": import_csv_layout("./map/map_Grass.csv"),
            "object": import_csv_layout("./map/map_Objects.csv"),
        }
        graphics = {
            "grass": import_folder("./graphic/test/grass")
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == "boundary":
                            Tile((x, y), [self.obstacles_sprites], "invisible")
                        if style == "grass":
                            # CREATE RANDOM GRASS IMAGE FROM THE LIST
                            random_grass_img = random.choice(graphics["grass"])
                            Tile((x, y), [self.visible_sprites, self.obstacles_sprites], "grass", random_grass_img)
                        if style == "object":
                            pass
        #         if col == "x":
        #             Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
        #         if col == "p":
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)
        self.player = Player((2400, 1800), [self.visible_sprites], self.obstacles_sprites)

    def run(self):
        # UPDATE AND DRAW THE GAME
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        # debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        # GENERAL SETUP
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

        # CREATING THE FLOOR
        self.floor_surf = pygame.image.load("./graphic/test/ground.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):

        # GETTING THE OFFSET
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # DRAWING THE FLOOR
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
