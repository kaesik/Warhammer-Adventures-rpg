import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("C:/Users/kamil/PycharmProjects/WARHAMMER_ADVENTURES/graphic/test/front_idle.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.image = pygame.image.load(
                "C:/Users/kamil/PycharmProjects/WARHAMMER_ADVENTURES/graphic/test/back_idle.png").convert_alpha()
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.image = pygame.image.load(
                "C:/Users/kamil/PycharmProjects/WARHAMMER_ADVENTURES/graphic/test/front_idle.png").convert_alpha()
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.image = pygame.image.load(
                "C:/Users/kamil/PycharmProjects/WARHAMMER_ADVENTURES/graphic/test/left_idle.png").convert_alpha()
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.image = pygame.image.load(
                "C:/Users/kamil/PycharmProjects/WARHAMMER_ADVENTURES/graphic/test/right_idle.png").convert_alpha()
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * speed

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # MOVING RIGHT
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # MOVING LEFT
                        self.rect.left = sprite.rect.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # MOVING UP
                        self.rect.up = sprite.rect.down
                    if self.direction.y < 0:  # MOVING DOWN
                        self.rect.down = sprite.rect.up

    def update(self):
        self.input()
        self.move(self.speed)
