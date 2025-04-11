"""
тут добавляем пули
"""
import pygame
from helper import resource_path
from player import *
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, position,size, hero, enemy,zombie_group):
        """
        добавляем необходимые переменные
        """
        super().__init__()
        self.enemy = enemy
        self.size = size
        self.image = pygame.transform.scale(pygame.image.load(resource_path(image)),self.size)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 3
        self.hero = hero
        self.zombie_group = zombie_group
        self.enemy_r = self.hero.fire_walk_r

        self.enemy_l = hero.fire_walk_l
    def update(self):
        """
        проверяем касание пули и зомби , полет пули и тд
        """
        zombie_list = self.zombie_group.sprites()
        if self.rect.colliderect(self.enemy):
            zombie_list[0] .helth -= 1
            self.kill()
        if self.enemy_l:
            self.rect.x -= self.speed

        if self.enemy_r:
            self.image = pygame.transform.rotate(self.image,180)
            self.rect.x += self.speed
        if self.rect.x < 0:
            self.kill()
        if self.rect.x > 1000:
            self.kill()
