import pygame, sys
from settings import *
from level import *
from debug import debug


class Game:
    def __init__(self):
        # GENERAL SETUP
        pygame.init()
        self.sceen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Warhammer: Adventures")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.sceen.fill("black")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
