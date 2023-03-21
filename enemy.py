import pygame
from settings import *
from entity import Entity
from support import *


class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites):

        # GENERAL SETUP
        super().__init__(groups)
        self.sprite_type = "enemy"

        # GRAPHICS SETUP
        self.import_graphics(monster_name)
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]

        # MOVEMENT
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # STATS
        self.monster_name = monster_name  # GIVE NAME OF THE MONSTER
        monster_info = monster_data[self.monster_name]  # TAKE DATA FROM SETTINGS
        self.health = monster_info['health']  # GET HEALTH OF THE MONSTER
        self.exp = monster_info['exp']  # GET EXP FOR THE MONSTER
        self.speed = monster_info['speed']  # SPEED OF THE MONSTER
        self.attack_damage = monster_info['damage']  # DAMAGE THAT MONSTER DEAL
        self.resistance = monster_info['resistance']  # KNOCK BACK OF MONSTER
        self.attack_radius = monster_info['attack_radius']  # RADIUS FROM HE IS ABLE TO ATTACK
        self.notice_radius = monster_info['notice_radius']  # RADIUS FROM HE IS ABLE TO NOTICE PLAYER
        self.attack_type = monster_info['attack_type']  # TYPE OF THE ATTACK

        # PLAYER INTERACTION
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

    def import_graphics(self, name):
        self.animations = {"idle": [], "move": [], "attack": []}
        main_path = f"./graphic/test/monsters/{name}"
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(f"{main_path}/{animation}")

    def get_player_distance_direction(self, player):
        enemy_vector = pygame.math.Vector2(self.rect.center)  # GET VECTOR OF THE ENEMY FROM LEFT TOP CORNER
        player_vector = pygame.math.Vector2(player.rect.center)  # GET VECTOR OF PLAYER FROM LEFT TOP CORNER
        distance = (player_vector - enemy_vector).magnitude()  # GET VECTOR FROM PLAYER TO ENEMY AND CHANGE TO DISTANCE

        if distance > 0:  # IF DISTANCE IS GREATER THAN 0
            direction = (player_vector - enemy_vector).normalize()  # GET VECTOR AND CHANGE TO DIRECTION
        else:  # IF DISTANCE IS 0
            direction = pygame.math.Vector2()  # DIRECTION IS NOWHERE, MONSTER NOT MOVE

        return distance, direction

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:  # IF PLAYER IS IN ATTACK_RADIUS
            if self.status != "attack":  # IF STATUS IS DIFFERENT FROM ATTACK
                self.frame_index = 0  # RESET ANIMATION
            self.status = "attack"  # MONSTER ATTACK
        elif distance <= self.notice_radius:  # IF PLAYER IS IN NOTICE_RADIUS
            self.status = "move"  # MONSTER MOVE
        else:  # ELSE
            self.status = "idle"  # MONSTER JUST IDLE

    def actions(self, player):
        if self.status == "attack":
            self.attack_time = pygame.time.get_ticks()
        elif self.status == "move":
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == "attack":
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def update(self):
        self.move(self.speed)
        self.animate()
        self.cooldown()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)
