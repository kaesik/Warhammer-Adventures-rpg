import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type                                                                                  # ADDS TYPE TO TILE
        y_offset = HITBOX_OFFSET[sprite_type]                                                                           # CREATES A OFFSET
        self.image = surface                                                                                            # CREATES A TILE AS A SURFACE
        if sprite_type == "object":                                                                                     # IF SPRITE TYPE IS 'OBJECT'
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))                                        # SPRITE IS MOVED UP
        else:                                                                                                           # ELSE
            self.rect = self.image.get_rect(topleft=pos)                                                                # CREATES TILE AS NORMAL
        self.hitbox = self.rect.inflate(0, y_offset)                                                                    # CREATES A HITBOX WITH OFFSET
