import pygame, sys
from settings import *
from level import *
from debug import debug


class Game:
    def __init__(self):
        # GENERAL SETUP
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_icon(pygame.image.load('./graphic/settings/icon.png'))
        pygame.display.set_caption("Warhammer: Adventures")
        self.clock = pygame.time.Clock()
        self.level = Level()

        # SOUND
        main_sound = pygame.mixer.Sound("./graphic/test/audio/main.ogg")
        main_sound.set_volume(0.05)
        main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
