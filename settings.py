# GAME SETUP
WIDTH = 1920
HEIGHT = 1080
FPS = 60
TILESIZE = 64

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 150
ITEM_BOX_SIZE = 100
UI_FONT = "./graphic/font/KINGTHINGS-PETROCK.TTF"
UI_FONT_SIZE = 36

# GENERAL COLORS
WATER_COLOR = "#71ddee"
UI_BACKGROUND_COLOR = "#222222"
UI_BORDER_COLOR = "#111111"
TEXT_COLOR = "#EEEEEE"

#UI COLORS
HEALTH_COLOR = "red"
ENERGY_COLOR = "blue"
UI_BORDER_COLOR_ACTIVE = "gold"

# WEAPONS DATA
weapon_data = {
    "sword": {"cooldown": 100, "damage": 15, "graphic": "./graphic/test/weapons/sword/full.png"},
    "lance": {"cooldown": 400, "damage": 30, "graphic": "./graphic/test/weapons/lance/full.png"},
    "axe": {"cooldown": 300, "damage": 20, "graphic": "./graphic/test/weapons/axe/full.png"},
    "rapier": {"cooldown": 50, "damage": 8, "graphic": "./graphic/test/weapons/rapier/full.png"},
    "sai": {"cooldown": 80, "damage": 10, "graphic": "./graphic/test/weapons/sai/full.png"},
}

# MAGIC DATA
magic_data = {
    "flame": {"strength": 5, "cost": 20, "graphic": "./graphic/test/magic/flame/fire.png"},
    "heal": {"strength": 20, "cost": 10, "graphic": "./graphic/test/magic/heal/heal.png"},
}

# STATS DATA
stats_data = {
    "health": 100,
    "energy": 60,
    "attack": 10,
    "magic": 4,
    "speed": 6,
}

