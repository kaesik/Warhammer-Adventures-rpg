import pygame
from settings import *


class UI:
    def __init__(self):

        # GENERAL
        self.display_surface = pygame.display.get_surface()                                                             # DISPLAYS UI
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)                                                             # GETS FONT FOR UI

        # BAR SETUP
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)                                        # DISPLAYS HEALTH BAR
        self.energy_bar_rect = pygame.Rect(10, 40, ENERGY_BAR_WIDTH, BAR_HEIGHT)                                        # DISPLAYS ENERGY BAR

        # CONVERT WEAPON DICTIONARY  # FUTURE - COMBINE CONVERTS
        self.weapon_graphics = []                                                                                       # LIST WITH ALL WEAPONS
        for weapon in weapon_data.values():                                                                             # LOOP FOR WEAPON IN DATA
            path = weapon["graphic"]                                                                                    # LOOKS FOR DESIRED WEAPON
            weapon = pygame.image.load(path).convert_alpha()                                                            # CONVERT IT TO GRAPHICS
            self.weapon_graphics.append(weapon)                                                                         # ADDS WEAPON TO THE LIST

        # CONVERT MAGIC DICTIONARY  # FUTURE - COMBINE CONVERTS
        self.magic_graphics = []                                                                                        # LIST WITH ALL MAGIC
        for magic in magic_data.values():                                                                               # LOOP FOR MAGIC IN DATA
            path = magic["graphic"]                                                                                     # LOOKS FOR DESIRED MAGIC
            magic = pygame.image.load(path).convert_alpha()                                                             # CONVERT IT TO GRAPHICS
            self.magic_graphics.append(magic)                                                                           # ADDS MAGIC TO THE LIST

    def show_bar(self, current_amount, max_amount, background_rect, color):
        """CREATES BAR RECTANGLE"""

        # DRAW BACKGROUND
        pygame.draw.rect(self.display_surface, UI_BACKGROUND_COLOR, background_rect)                                    # CREATES RECTANGLE WITH BACKGROUND COLOR

        # CONVERT STATS TO PIXEL
        ratio = current_amount / max_amount                                                                             # RATIO OF HEALTH TO MAX HEALTH
        current_width = background_rect.width * ratio                                                                   # CURRENT WIDTH IS SCREEN WIDTH TIMES RATIO
        current_rect = background_rect.copy()                                                                           #
        current_rect.width = current_width                                                                              #

        # DRAW THE BAR
        pygame.draw.rect(self.display_surface, color, current_rect)                                                     #
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, background_rect, 4)                                     #

    def show_exp(self, exp):
        """SHOWS CURRENT EXPERIENCE POINTS"""
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)                                                  #
        x = self.display_surface.get_size()[0] - 16                                                                     #
        y = self.display_surface.get_size()[1] - 16                                                                     #
        text_rect = text_surf.get_rect(bottomright=(x, y))                                                              #

        pygame.draw.rect(self.display_surface, UI_BACKGROUND_COLOR, text_rect.inflate(20, 10))                          #
        self.display_surface.blit(text_surf, text_rect)                                                                 #
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 10), 4)                           #

    def selection_box(self, left, top, has_switched):
        """CREATES SELECTION BOX"""
        background_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)                                          #
        pygame.draw.rect(self.display_surface, UI_BACKGROUND_COLOR, background_rect)                                    #
        if has_switched:                                                                                                #
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, background_rect, 4)                          #
        else:                                                                                                           #
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, background_rect, 4)                                 #
        return background_rect                                                                                          #

    def weapon_overlay(self, weapon_index, has_switched):  # FUTURE - COMBINE OVERLAYS
        """"""
        background_rect = self.selection_box(10, self.display_surface.get_size()[1] - ITEM_BOX_SIZE - 10, has_switched) #
        weapon_surf = self.weapon_graphics[weapon_index]                                                                #
        weapon_rect = weapon_surf.get_rect(center=background_rect.center)                                               #
        self.display_surface.blit(weapon_surf, weapon_rect)                                                             #

    def magic_overlay(self, magic_index, has_switched):  # FUTURE - COMBINE OVERLAYS
        """"""
        background_rect = self.selection_box(95, self.display_surface.get_size()[1] - ITEM_BOX_SIZE - 15, has_switched) #
        magic_surf = self.magic_graphics[magic_index]                                                                   #
        magic_rect = magic_surf.get_rect(center=background_rect.center)                                                 #
        self.display_surface.blit(magic_surf, magic_rect)                                                               #

    def display(self, player):
        """DISPLAYS UI"""
        self.show_bar(player.health, player.stats["health"], self.health_bar_rect, HEALTH_COLOR)                        # DISPLAYS HEALTH
        self.show_bar(player.energy, player.stats["energy"], self.energy_bar_rect, ENERGY_COLOR)                        # DISPLAYS ENERGY
        self.show_exp(player.exp)                                                                                       # DISPLAYS EXPERIENCE POINTS
        self.magic_overlay(player.magic_index, not player.can_switch_magic)   # MAGIC                                   # DISPLAYS OVERLAY WITH MAGIC
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)  # WEAPON                                # DISPLAYS OVERLAY WITH WEAPON
