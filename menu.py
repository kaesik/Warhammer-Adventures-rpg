import pygame
from settings import *
from button import Button


class Menu:
    """MENU WITH RESUME, OPTIONS AND EXIT  BUTTON"""
    def __init__(self):

        # GENERAL SETUP
        self.display_surface = pygame.display.get_surface()                                                             # GETS THE SURFACE OF THE MENU PANEL WHICH IS SCREEN
        self.bg_img = pygame.image.load(f"{BACKGROUND_IMAGE}").convert_alpha()
        self.start_button = Button((WIDTH/2-500, HEIGHT/2), START_IMAGE)
        self.resume_button = Button((WIDTH/2-500, HEIGHT/2), RESUME_IMAGE)
        self.option_button = Button((WIDTH/2, HEIGHT/2), OPTION_IMAGE)
        self.exit_button = Button((WIDTH/2+500, HEIGHT/2), EXIT_IMAGE)

    def display(self):
        self.display_surface.blit(self.bg_img, (0, 0))
        self.start_button.draw()
        self.resume_button.draw()
        self.option_button.draw()
        self.exit_button.draw()

    def start(self):
        pass

    def resume(self):
        pass

    def option(self):
        pass

    def exit(self):
        pass