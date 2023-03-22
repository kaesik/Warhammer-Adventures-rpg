import pygame
from support import import_folder
from random import choice


class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # MAGIC
            "flame": import_folder("./graphic/test/particles/flame/frames"),
            "aura": import_folder("./graphic/test/particles/aura"),
            "heal": import_folder("./graphic/test/particles/heal/frames"),

            # ATTACKS
            "claw": import_folder("./graphic/test/particles/claw"),
            "slash": import_folder("./graphic/test/particles/slash"),
            "sparkle": import_folder("./graphic/test/particles/sparkle"),
            "leaf_attack": import_folder("./graphic/test/particles/leaf_attack"),
            "thunder": import_folder("./graphic/test/particles/thunder"),

            # MONSTER DEATHS
            "squid": import_folder("./graphic/test/particles/smoke_orange"),
            "raccoon": import_folder("./graphic/test/particles/raccoon"),
            "spirit": import_folder("./graphic/test/particles/nova"),
            "bamboo": import_folder("./graphic/test/particles/bamboo"),

            # LEAFS
            "leaf": (
                import_folder("./graphic/test/particles/leaf1"),
                import_folder("./graphic/test/particles/leaf2"),
                import_folder("./graphic/test/particles/leaf3"),
                import_folder("./graphic/test/particles/leaf4"),
                import_folder("./graphic/test/particles/leaf5"),
                import_folder("./graphic/test/particles/leaf6"),
                self.reflect_images(import_folder("./graphic/test/particles/leaf1")),
                self.reflect_images(import_folder("./graphic/test/particles/leaf2")),
                self.reflect_images(import_folder("./graphic/test/particles/leaf3")),
                self.reflect_images(import_folder("./graphic/test/particles/leaf4")),
                self.reflect_images(import_folder("./graphic/test/particles/leaf5")),
                self.reflect_images(import_folder("./graphic/test/particles/leaf6"))
            )
        }

    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames["leaf"])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = "magic"
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
