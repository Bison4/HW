
import pygame
from helper import resource_path
from settings import *

text_map = [
    "WWWWWWWWWW",
    "W........W",
    "W........W",
    "W........W",
    "W........W",
    "W........W",
    "WWWWWWWWWW"
]

mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == "W":
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
class Ball():
    def __init__(self,image_path,pos_x, pos_y,size,speed):
        self.image = pygame.transform.scale(pygame.image.load(resource_path(image_path)),size)
        self.rect = self.image.get_rect()
        self.image_path = image_path
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.size_x = size[0]
        self.size_y = size[1]
        self.speed = speed
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))






