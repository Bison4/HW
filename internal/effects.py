"""
здесь я добавил остатки зомбаков,до эффект и тд
"""
import pygame
from helper import resource_path
from settings import *


class Blud(pygame.sprite.Sprite):
    def __init__(self, image, position,size):
        """
        тут я делаю кровь
        """
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(resource_path(image)),size)
        self.rect = self.image.get_rect()
        self.rect.center = position
class Corpse(pygame.sprite.Sprite):
    def __init__(self, image, position,size):
        """
        тут я делаю трупы
        """
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(resource_path(image)),size)
        self.rect = self.image.get_rect()
        self.rect.center = position




