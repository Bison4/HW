from collections import deque

import pygame
from helper import resource_path
from settings import *


class Enemy(pygame.sprite.Sprite):



    def __init__(self, image, position, size, hero, helth,ground, gravity_speed, blud, blood_group, corpse, corpse_group, color = 255):
        super().__init__()
        self.hero = hero
        self.helth = helth
        self.blud = blud
        self.corpse = corpse
        self.color = color
        self.corpse_group = corpse_group
        self.blood_group = blood_group
        self.gravity_speed = gravity_speed
        self.image = pygame.transform.scale(pygame.image.load(resource_path(image)), size)
        self.rect = self.image.get_rect()
        self.animation_count_walk = 0
        self.rect.center = position
        self.speed = 1
        self.size = size
        self.ground = ground
        self.enemy_r = hero.fire_walk_r
        self.dead_event = False
        self.animation_count_dead = 0
        self.score_dead = 0


        self.gravity = True
        self.anim_walk = deque(
        [pygame.transform.scale(pygame.image.load(resource_path(f"assets/zombie/run/{i}.png")), size).convert_alpha() for
             i in range(7)])
        self.anim_dead = deque(
        [pygame.transform.scale(pygame.image.load(resource_path(f"assets/zombie/dead/{i}.png")), size).convert_alpha() for
             i in range(4)])

        self.anim_speed = 10
    def walk(self):
        if self.hero.rect.x < self.rect.x:
            self.rect.x -= self.speed
        if self.hero.rect.x > self.rect.x:
            self.rect.x += self.speed


    def walk_anim(self):
        self.image = self.anim_walk[0]
        if self.animation_count_walk < self.anim_speed:
            self.animation_count_walk += 1
        else:
            self.anim_walk.rotate()
            self.animation_count_walk = 0
    def dead_anim(self):
        if self.dead_event:
            self.image = self.anim_dead[0]
            if self.animation_count_dead < self.anim_speed:
                self.animation_count_dead += 1
            else:
                self.anim_dead.rotate()
                self.score_dead += 1
                self.animation_count_dead = 0
    def gravity_z(self):
        if self.gravity:
            self.rect.y += self.gravity_speed
        if self.rect.colliderect(self.ground.rect):
            self.gravity = False
    def colide_hero(self):
        if self.helth <= 0:
            self.dead_event = True
            self.helth = 10
        if self.score_dead == 3:
            self.dead_event = False
            self.score_dead =0


            blood = self.blud("assets/image/blood.png",((self.rect.x  ),self.rect.y + self.size[1]),(200,50))
            self.blood_group.add(blood)
            corpse = self.corpse("assets/zombie/dead/4.png",(self.rect.x//2 ,(self.rect.y + self.size[1]) - 100),(400,200))
            self.corpse_group.add(corpse)
            if len(self.blood_group) >= 3:
                b_list = self.blood_group.sprites()
                c_list = self.corpse_group.sprites()
                b_list[0].kill()
                c_list[0].kill()


            self.kill()
        if self.rect.colliderect(self.hero.rect):
            self.hero.helth -= 1
            self.hero.COLOR -= 1

    def update(self):
        self.walk()
        self.walk_anim()
        self.dead_anim()

        self.gravity_z()
        self.colide_hero()

