from csv import reader
from os import walk
import pygame
import pygame.image
import json


def import_csv_layout(path):
    """IMPORTS CSV LAYOUT BASED ON THE GIVEN  PATH"""
    terrain_map = []                                                                                                    # CREATES LIST WITH MAP
    with open(path) as level_map:                                                                                       #
        layout = reader(level_map, delimiter=",")                                                                       #
        for row in layout:                                                                                              #
            terrain_map.append(list(row))                                                                               #
        return terrain_map                                                                                              #


def import_folder(path):
    """IMPORTS FOLDER BASED ON THE GIVEN PATH"""
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = f"{path}/{image}"
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)
    return surface_list


def save_game(path, name, data):
    with open(f"{path}/{name}.txt", "w") as save_file:
        json.dump(data, save_file)


def load_game(path, name):
    with open(f"{path}/{name}.txt") as save_file:
        load_file = json.load(save_file)
        return load_file
