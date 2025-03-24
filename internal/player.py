"""
Тут класс для создания игрока
"""

from collections import deque

import pygame
from GameSprite import GSprite
from helper import resource_path
from settings import WIGTH


class Hero(GSprite):
    def __init__(
        self,
        image_path,
        pos_x,
        pos_y,
        speed,
        size_x,
        size_y,
        gravity_speed,
        fire,
    ):
        """
        добавляем необходимые переменные
        """
        super().__init__(image_path, pos_x, pos_y, speed, size_x, size_y)

        self.WIGTH = WIGTH
        self.gravity = True
        self.fire = fire
        self.gravity_speed = gravity_speed
        self.anim_walk_right = deque(
            [
                pygame.transform.scale(
                    pygame.image.load(
                        resource_path(
                            f"assets/Solider/Soldier_1/walk/right/{i}.png"
                        )
                    ),
                    (self.size_x, self.size_y),
                ).convert_alpha()
                for i in range(7)
            ]
        )
        self.anim_walk_left = deque(
            [
                pygame.transform.scale(
                    pygame.image.load(
                        resource_path(
                            f"assets/Solider/Soldier_1/walk/left/{i}.png"
                        )
                    ),
                    (self.size_x, self.size_y),
                ).convert_alpha()
                for i in range(7)
            ]
        )
        self.anim_shot_right = deque(
            [
                pygame.transform.scale(
                    pygame.image.load(
                        resource_path(
                            f"assets/Solider/Soldier_1/shots/right/{i}.png"
                        )
                    ),
                    (self.size_x, self.size_y),
                ).convert_alpha()
                for i in range(4)
            ]
        )
        self.anim_shot_left = deque(
            [
                pygame.transform.scale(
                    pygame.image.load(
                        resource_path(
                            f"assets/Solider/Soldier_1/shots/left/{i}.png"
                        )
                    ),
                    (self.size_x, self.size_y),
                ).convert_alpha()
                for i in range(4)
            ]
        )
        self.helth = 200
        self.COLOR = 255
        self.animation_count_walk_l = 0
        self.animation_count_shot = 0
        self.animation_count_walk = 0
        self.anim_walk_p_r = False
        self.anim_walk_p_l = False
        self.fire_walk_r = False
        self.fire_walk_l = False
        self.shot_r = False
        self.shot_l = False
        self.score_anim_shot = 0

        self.anim_speed = 10

    def walk(self):
        """
        управление спрайтом
        """
        self.anim_walk_p_r = False
        self.anim_walk_p_l = False

        key_presed = pygame.key.get_pressed()

        if key_presed[pygame.K_d] and self.rect.x + self.size_x <= self.WIGTH:
            self.rect.x += self.speed
            self.anim_walk_p_r = True
            self.fire_walk_r = True
            self.fire_walk_l = False

        if key_presed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.anim_walk_p_l = True
            self.fire_walk_r = False
            self.fire_walk_l = True

    def walk_anim_right(self):
        """
        анимация хотьбы на право спрайт
        """
        if self.anim_walk_p_r:
            self.image = self.anim_walk_right[0]
            if self.animation_count_walk < self.anim_speed:
                self.animation_count_walk += 1
            else:
                self.anim_walk_right.rotate()
                self.animation_count_walk = 0

    def shot_anim_right(self):
        """
        анимация стрельба на право спрайт
        """
        if self.shot_r:
            self.image = self.anim_shot_right[0]
            if self.animation_count_shot < self.anim_speed:
                self.animation_count_shot += 1
            else:
                self.anim_shot_right.rotate()
                self.score_anim_shot += 1
                self.animation_count_shot = 0

    def fire_check(self, fire):
        """
        проверка в какую сторону стреляет спрайт
        """
        if fire and self.fire_walk_l:
            self.shot_l = True
        if fire and self.fire_walk_r:
            self.shot_r = True
        if self.score_anim_shot == 4:
            self.shot_l = False
            self.shot_r = False

            self.score_anim_shot = 0

    def shot_anim_left(self):
        """
        анимация стрельба на лево спрайт
        """
        if self.shot_l:
            self.image = self.anim_shot_left[0]
            if self.animation_count_shot < self.anim_speed:
                self.animation_count_shot += 1
            else:
                self.anim_shot_left.rotate()
                self.score_anim_shot += 1

                self.animation_count_shot = 0

    def walk_anim_left(self):
        """
        анимация хотьбы на лево спрайт
        """
        if self.anim_walk_p_l:
            self.image = self.anim_walk_left[0]
            if self.animation_count_walk_l < self.anim_speed:
                self.animation_count_walk_l += 1
            else:
                self.anim_walk_left.rotate()
                self.animation_count_walk_l = 0

    def gravity_hero(self):
        """
        гравитация спрайта
        """
        if self.gravity:
            self.rect.y += self.gravity_speed
