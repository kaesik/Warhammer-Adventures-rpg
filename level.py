import pygame
import random
from settings import *
from debug import debug
from tile import Tile
from player import Player
from support import *
from weapon import Weapon
from ui import UI
from enemy import Enemy


class Level:
    def __init__(self):

        # GET THE DISPLAY SURFACE
        self.display_surface = pygame.display.get_surface()

        # SPRITE GROUP SETUP
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # ATTACK SPRITES
        self.current_attack = None

        # SPRITE SETUP
        self.create_map()

        # USER INTERFACE
        self.ui = UI()

    def create_map(self):
        layouts = {
            "boundary": import_csv_layout("./map/map_FloorBlocks.csv"),
            "grass": import_csv_layout("./map/map_Grass.csv"),
            "object": import_csv_layout("./map/map_Objects.csv"),
            "entities": import_csv_layout("./map/map_Entities.csv"),
        }
        graphics = {
            "grass": import_folder("./graphic/test/grass"),
            "objects": import_folder("./graphic/test/objects"),
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == "boundary":
                            Tile((x, y), [self.obstacle_sprites], "invisible")
                        if style == "grass":
                            # CREATE RANDOM GRASS IMAGE FROM THE LIST
                            random_grass_img = random.choice(graphics["grass"])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], "grass", random_grass_img)
                        if style == "object":
                            # CREATE RANDOM OBJECTS IMAGE FROM THE LIST
                            surf = graphics["objects"][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], "object", surf)
                        if style == "entities":
                            if col == "394":
                                self.player = Player(
                                    (x, y),  # WHERE PLAYER IS PLACED
                                    [self.visible_sprites],  # PLAYER GROUPS
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic,
                                )
                            else:
                                if col == "390":
                                    monster_name = "bamboo"
                                elif col == "391":
                                    monster_name = "spirit"
                                elif col == "392":
                                    monster_name = "raccoon"
                                elif col == "393":
                                    monster_name = "squid"
                                else:
                                    monster_name = "blank"
                                Enemy(monster_name, (x, y), [self.visible_sprites], self.obstacle_sprites)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def create_magic(self, style, strength, cost):
        print(style)
        print(strength)
        print(cost)

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        # UPDATE AND DRAW THE GAME
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)
        # debug(self.player.status)


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

    def enemy_update(self, player):
        enemy_sprites = \
            [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "enemy"]
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
