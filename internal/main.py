"""
здесь я запускаю игру
"""

import pygame
from ground import Ground
from helper import resource_path
from player import Hero
from settings import (
    FIRE,
    GRAVITY_SREED,
    HEIGHT,
    MAP_SCALE,
    WIGTH,
)
def game_bar():
    size_x = hero.helth
    pygame.draw.rect(screen, (0, hero.COLOR, 0), (10, 10, size_x, 20))
    if size_x <= 5:
        exit()
    if hero.helth < 200:
        hero.helth += 0.1
        hero.COLOR += 0.1
screen = pygame.display.set_mode((WIGTH, HEIGHT), pygame.RESIZABLE)
sc_map = pygame.Surface((WIGTH // MAP_SCALE, HEIGHT // MAP_SCALE))

bg = pygame.image.load(resource_path("assets/background/fon.jpg"))
bg = pygame.transform.scale(bg, (WIGTH, HEIGHT))
pygame.display.set_caption("Niger")
screen.blit(bg, (0, 0))
game = True
FPS = 60
clock = pygame.time.Clock()
hero = Hero(
    "assets/Solider/Soldier_1/main.png",
    WIGTH // 2,
    (HEIGHT // 7) * 4,
    3,
    WIGTH // 16,
    HEIGHT // 5,
    GRAVITY_SREED,
    FIRE,
)
grounds = Ground(
    "assets/floor/floor.png", 0, (HEIGHT // 7) * 6, 3, WIGTH, HEIGHT // 5
)



player_center = [200, 200]





running = True
while running:
    screen.blit(bg, (0, 0))
    grounds.reset(screen)
    grounds.collide(hero)
    HERO_GRAVITY = grounds.gravity
    hero.reset(screen)

    game_bar()
    hero.walk()

    hero.gravity_hero()
    hero.walk_anim_right()
    hero.walk_anim_left()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.VIDEORESIZE:
            HEIGHT = e.w
            bg = pygame.transform.scale(bg, (e.w, e.h))
        if e.type == pygame.MOUSEBUTTONDOWN:
            FIRE = True

    hero.fire_check(FIRE)
    hero.shot_anim_right()
    hero.shot_anim_left()


    FIRE = False
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
