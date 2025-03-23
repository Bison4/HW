"""
Тут класс для создания земли
"""

from GameSprite import GSprite
from settings import *


class Ground(GSprite):
    def __init__(self, image_path, pos_x, pos_y, speed, size_x, size_y):
        """
        добавляем необходимые переменные
        """
        super().__init__(image_path, pos_x, pos_y, speed, size_x, size_y)
        self.gravity = True

    def collide(self,enemy):
        """
        проверяем касание земли и гг , гравитация для гг
        """
        if self.rect.colliderect(enemy.rect):
            enemy.gravity = False
        else:
            enemy.gravity = True


