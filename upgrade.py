import pygame
from settings import *


class Upgrade:
    """LETS YOU UPGRADE ATTRIBUTES FOR EXPERIENCE"""
    def __init__(self, player):

        # GENERAL SETUP
        self.display_surface = pygame.display.get_surface()                                                             # GETS THE SURFACE OF THE UPGRADE PANEL WHICH IS SCREEN
        self.player = player                                                                                            # GETS THE PLAYER
        self.attribute_num = len(player.stats)                                                                          # GETS THE NUMBER OF ATTRIBUTES
        self.attribute_names = list(player.stats.keys())                                                                # GETS THE NAME OF THE ATTRIBUTES
        self.max_values = list(player.max_stats.values())                                                               # GETS THE MAX VALUES OF THE ATTRIBUTES
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)                                                             # GETS THE FONT FOR THE ATTRIBUTES

        # ITEM CREATION
        self.height = self.display_surface.get_size()[1] * 0.8                                                          # GETS HEIGHT OF THE UPGRADE PANEL
        self.width = self.display_surface.get_size()[0] // 6                                                            # GETS WIDTH OF THE ONE UPGRADE PANEL
        self.create_items()                                                                                             # CREATE ONE UPGRADE PANEL

        # SELECTION SYSTEM
        self.selection_index = 0                                                                                        # INDEX OF THE SELECTED PANEL
        self.selection_time = None                                                                                      # COOLDOWN OF SELECTION
        self.can_move = True                                                                                            # CHECK IF YOU CAN MOVE IN UPGRADE PANEL

    def input(self):
        """CHECKS WHAT THE PLAYER HAS PRESSED AND DOES IT"""
        keys = pygame.key.get_pressed()                                                                                 # GETS THE KEYS FROM KEYBOARD

        if self.can_move:                                                                                               # IF YOU CAN MOVE IN UPGRADE PANEL
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_num - 1:                                  # IF YOU PRESS 'RIGHT' KEY, AND INDEX IS NOT GREATER THAN NUMBER OF ATTRIBUTES
                self.selection_index += 1                                                                               # INCREASE THE INDEX NUMBER
                self.can_move = False                                                                                   # MAKES YOU UNABLE TO MOVE
                self.selection_time = pygame.time.get_ticks()                                                           # CHECKS TIME WHEN YOU INCREASED THE INDEX
            elif keys[pygame.K_LEFT] and self.selection_index > 0:                                                      # IF YOU PRESS 'LEFT' KEY, AND INDEX IS GREATER THAN 0
                self.selection_index -= 1                                                                               # DECREASE THE INDEX NUMBER
                self.can_move = False                                                                                   # MAKES YOU UNABLE TO MOVE
                self.selection_time = pygame.time.get_ticks()                                                           # CHECKS TIME WHEN YOU INCREASED THE INDEX
            if keys[pygame.K_SPACE]:                                                                                    # IF YOU PRESS 'SPACE' KEY
                self.can_move = False                                                                                   # MAKES YOU UNABLE TO MOVE
                self.selection_time = pygame.time.get_ticks()                                                           # CHECKS TIME WHEN YOU INCREASED THE INDEX
                self.item_list[self.selection_index].trigger(self.player)                                               # TRIGGER THE UPGRADE

    def selection_cooldown(self):
        """MAKES COOLDOWN IN SELECTION UPGRADE PANEL BASED ON TICKS"""
        if not self.can_move:                                                                                           # IF YOU CAN'T MOVE IN UPGRADE PANEL
            current_time = pygame.time.get_ticks()                                                                      # CHECKS THE CURRENT TIME
            if current_time - self.selection_time >= 300:                                                               # IF CURRENT TIME MINUS SELECTION TIME IS GREATER THAN COOLDOWN
                self.can_move = True                                                                                    # MAKES YOU ABLE TO MOVE

    def create_items(self):
        """CREATES AN ITEM BASED ON THE GIVEN PARAMETERS"""
        self.item_list = []                                                                                             # CREATES THE LIST OF THE ITEMS

        for item, index in enumerate(range(self.attribute_num)):                                                        # LOOP THROUGH THE NUMBER OF THE ATTRIBUTES
            full_width = self.display_surface.get_size()[0]                                                             # FINDS THE FULL WIDTH OF THE SCREEN
            increment = full_width // self.attribute_num                                                                # FINDS THE WIDTH OF ONE ELEMENT BASED ON THE NUMBER OF ATTRIBUTES
            left = (item * increment) + (increment - self.width) // 2                                                   # FINDS THE LEFT SIDE OF THE ELEMENT
            top = self.display_surface.get_size()[1] * 0.1                                                              # FINDS THE TOP SIDE OF THE ELEMENT
            item = Item(left, top, self.width, self.height, index, self.font)                                           # CHANGES THE ITEM TO THE ITEM OBJECT
            self.item_list.append(item)                                                                                 # ADDS THE ITEM TO THE LIST

    def display(self):
        """DISPLAYS WHAT THE PLAYER WANTS TO DO IN THE UPGRADE PANEL"""
        self.input()                                                                                                    # GETS THE INPUT OF PLAYER
        self.selection_cooldown()                                                                                       # CHECK THE COOLDOWN

        for index, item in enumerate(self.item_list):                                                                   # LOOP THROUGH THE ITEM LIST

            # GET ATTRIBUTES
            name = self.attribute_names[index]                                                                          # GETS THE NAME OF ATTRIBUTE BASED ON INDEX
            value = self.player.get_value_by_index(index)                                                               # GETS THE VALUE OF ATTRIBUTE BASED ON INDEX
            max_value = self.max_values[index]                                                                          # GETS THE MAX VALUE OF ATTRIBUTE BASED ON INDEX
            cost = self.player.get_cost_by_index(index)                                                                 # GETS THE COST OF THE UPGRADE OF THE ATTRIBUTE BASED ON INDEX
            item.display(self.display_surface, self.selection_index, name, value, max_value, cost)                      # DISPLAYS ALL THE INFORMATION ON THE UPGRADE PANEL


class Item:
    """WINDOW WITH ATTRIBUTE AND ALL INFORMATION"""
    def __init__(self, left, top, width, height, index, font):
        self.rect = pygame.Rect(left, top, width, height)                                                               # CREATES THE RECTANGLE
        self.index = index                                                                                              # CREATES INDEX
        self.font = font                                                                                                # FINDS THE FONT

    def display_names(self, surface, name, cost, selected):
        """DISPLAY TITLE AND COS OF THE ITEM"""
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR                                                         # GETS A COLOR DEPENDING ON WHETHER THE SELECTED OR NOT

        # TITLE
        title_surface = self.font.render(name, False, color)                                                            # CREATE THE SURFACE OF THE TITLE
        title_rect = title_surface.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 20))                       # CREATE A RECTANGLE WITH THE TITLE AND THE PLACE OF IT

        # COST
        cost_surface = self.font.render(f"{int(cost)}", False, color)                                                   # CREATE THE SURFACE OF THE COST
        cost_rect = cost_surface.get_rect(midbottom=self.rect.midbottom - pygame.math.Vector2(0, 20))                   # CREATE A RECTANGLE WITH THE COST AND THE PLACE OF IT

        # DRAW
        surface.blit(title_surface, title_rect)                                                                         # PLACE THE TITLE RECTANGLE
        surface.blit(cost_surface, cost_rect)                                                                           # PLACE THE COST RECTANGLE

    def display_bar(self, surface, value, max_value, selected):
        """DISPLAYS BAR WITH SLIDER"""

        # DRAWING SETUP
        top = self.rect.midtop + pygame.math.Vector2(0, 100)                                                            # FINDS TOP OF THE BAR
        bottom = self.rect.midbottom - pygame.math.Vector2(0, 100)                                                      # FINDS BOTTOM IF THE BAR
        color = BAR_COLOR_SELECTED if selected else BAR_COLOR                                                           # GETS A COLOR DEPENDING ON WHETHER THE SELECTED OR NOT

        # BAR SETUP
        full_height = bottom[1] - top[1]                                                                                # GETS THE HEIGHT OF THE BAR BASED ON THE TOP AND BOTTOM
        relative_number = (value / max_value) * full_height                                                             # CHANGES VALUES TO PIXELS ON BAR
        value_rect = pygame.Rect(top[0]-15, bottom[1]-relative_number, 30, 10)                                          # SLIDER ON BAR

        # DRAW ELEMENTS
        pygame.draw.line(surface, color, top, bottom, 5)                                                                # PLACE THE BAR AS THE LINE
        pygame.draw.rect(surface, color, value_rect)                                                                    # PLACE THE SLIDER AS THE RECTANGLE

    def trigger(self, player):
        """ALLOWS YOU TO UPGRADE A ATTRIBUTE AND INCREASE THE COST OF THE UPGRADE"""
        upgrade_attribute = list(player.stats.keys())[self.index]                                                       # FINDS THE ATTRIBUTE BASED ON INDEX

        if player.exp >= player.upgrade_cost[upgrade_attribute] \
                and player.stats[upgrade_attribute] < player.max_stats[upgrade_attribute]:                              # IF PLAYER EXP IS GREATER THAN UPGRADE COST ATTRIBUTE AND ATTRIBUTE IS NOT GREATER THAN MAX VALUE
            player.exp -= player.upgrade_cost[upgrade_attribute]                                                        # SUBTRACT EXPERIENCE EQUAL TO THE COST OF ATTRIBUTE
            player.stats[upgrade_attribute] *= 1.2                                                                      # MULTIPLIES AN ATTRIBUTE BY A GIVEN VALUE
            player.upgrade_cost[upgrade_attribute] *= 1.4                                                               # MULTIPLIES AN COST OF THE ATTRIBUTE BY A GIVEN VALUE

        if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:                                       # IF PLAYER ATTRIBUTE IS GREATER THAN MAX VALUE
            player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]                                       # THEN PLAYER ATTRIBUTE IS EQUAL TO MAX VALUE

    def display(self, surface, selection_num, name, value, max_value, cost):
        """HIGHLIGHTS THE SELECTED ITEM"""
        if self.index == selection_num:                                                                                 # IF INDEX IS EQUAL TO SELECTED NUMBER
            pygame.draw.rect(surface, UPGRADE_BACKGROUND_COLOR_SELECTED, self.rect)                                     # CHANGES BACKGROUND COLOR
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)                                                    # CHANGES BORDER COLO
        else:                                                                                                           # ELSE
            pygame.draw.rect(surface, UI_BACKGROUND_COLOR, self.rect)                                                   # COLOR IS NORMAL
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)                                                    # BORDER COLOR IS NORMAL

        self.display_names(surface, name.title(), cost, self.index == selection_num)                                    # DISPLAYS HIGHLIGHTED NAMES
        self.display_bar(surface, value, max_value, self.index == selection_num)                                        # DISPLAYS HIGHLIGHTED BAR
