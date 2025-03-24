"""
класс с основой для спрайтов
"""
import pygame
from helper import resource_path
from settings import *


class GSprite(pygame.sprite.Sprite):
    def __init__(self,image_path,pos_x,pos_y,speed,size_x,size_y):
        """
        задаём необходимые переменные
        """

        self.image = pygame.transform.scale(pygame.image.load(resource_path(image_path)),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.image_path = image_path
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.speed = speed
    def reset(self, screen):
        """
        отрисовка

        """
        screen.blit(self.image,(self.rect.x,self.rect.y))
