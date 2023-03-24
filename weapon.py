import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = "weapon"                                                                                     # SPRITE TYPE IS WEAPON
        direction = player.status.split("_")[0]                                                                         # GET DIRECTION FROM PLAYER STATUS AND PRINT WEAPON IN THIS DIRECTION

        # GRAPHIC
        full_path = f"./graphic/test/weapons/{player.weapon}/{direction}.png"                                           # FIND THE FULL PATH TO THE SPRITE
        self.image = pygame.image.load(full_path).convert_alpha()                                                       # CONVERT FROM PATH TO IMAGE

        # PLACEMENT
        if direction == "right":                                                                                        # IF PLAYER IS TURNING RIGHT
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(-14, 16))                # WEAPON IS PRINTED IN THIS DIRECTION
        elif direction == "left":                                                                                       # IF PLAYER IS TURNED LEFT
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(14, 16))                 # WEAPON IS PRINTED IN THIS DIRECTION
        elif direction == "down":                                                                                       # IF PLAYER IS TURNED DOWN
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-12, -14))               # WEAPON IS PRINTED IN THIS DIRECTION
        else:                                                                                                           # IF PLAYER IS TURNED UP
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(16, 32))                 # WEAPON IS PRINTED IN THIS DIRECTION
