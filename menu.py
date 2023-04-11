import pygame
from settings import *
from button import Button


class Menu:
    """MENU WITH RESUME, OPTIONS AND EXIT  BUTTON"""
    def __init__(self):

        # GENERAL SETUP
        self.display_surface = pygame.display.get_surface()                                                             # GETS THE SURFACE OF THE MENU PANEL WHICH IS SCREEN
        self.bg_img = pygame.image.load(f"{BACKGROUND_IMAGE}").convert_alpha()
        self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))
        self.start_button = Button((WIDTH/2-500, HEIGHT/2), START_IMAGE)
        self.resume_button = Button((WIDTH/2-500, HEIGHT/2), RESUME_IMAGE)
        self.options_button = Button((WIDTH/2, HEIGHT/2), OPTIONS_IMAGE)
        self.exit_button = Button((WIDTH/2+500, HEIGHT/2), EXIT_IMAGE)
        self.save_button = Button((WIDTH/2-250, HEIGHT/2+250), SAVE_IMAGE)
        self.load_button = Button((WIDTH/2+250, HEIGHT/2+250), LOAD_IMAGE)

    def display(self):
        self.display_surface.blit(self.bg_img, (0, 0))
        self.start_button.draw()
        self.resume_button.draw()
        self.options_button.draw()
        self.exit_button.draw()
        self.save_button.draw()
        self.load_button.draw()

    def start(self):
        pass

    def resume(self):
        pass

    def options(self):
        pass

    def exit(self):
        pass
