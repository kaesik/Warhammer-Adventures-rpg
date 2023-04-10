import pygame


class Button:
    def __init__(self, pos, img_path):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load(f"{img_path}").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (pos)

    def draw(self):
        self.display_surface.blit(self.image, (self.rect.x, self.rect.y))