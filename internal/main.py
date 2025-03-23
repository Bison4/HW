import pygame

from ground import Ground
from helper import resource_path

from player import Hero
from settings import *

screen = pygame.display.set_mode((WIGTH,HEIGHT),pygame.RESIZABLE)
sc_map = pygame.Surface((WIGTH // MAP_SCALE, HEIGHT // MAP_SCALE))

bg = pygame.image.load(resource_path("assets/background/fon.jpg"))
bg = pygame.transform.scale(bg,(WIGTH,HEIGHT))
pygame.display.set_caption("Niger")
screen.blit(bg,(0,0))
game = True
FPS = 60
clock = pygame.time.Clock()
hero = Hero("assets/Solider/Soldier_1/main.png", WIGTH//2,(HEIGHT//7)*4,3,WIGTH//16,HEIGHT//5, GRAVITY_SREED, FIRE)
grounds = Ground("assets/floor/floor.png", 0,(HEIGHT//7)*6,3,WIGTH,HEIGHT//5)
def collise_Z(enemy,bullet):
    if bullet.rect.colliderect(enemy.rect):
        enemy.rect.x = 0
        enemy.rect.y = 0

bullet_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
blood_group = pygame.sprite.Group()
corpse_group = pygame.sprite.Group()

zombie_event = pygame.USEREVENT + 2
pygame.time.set_timer(zombie_event, 2000)

player_center = [200,200]
def lab():
    sc_map.fill(BLACK)
    player = pygame.draw.circle(sc_map, RED, (player_center[0],player_center[1]), MAP_TILE//MAP_SCALE)
    key_presed = pygame.key.get_pressed()

    if key_presed[pygame.K_LEFT]:
        player_center[0] -= 2
    if key_presed[pygame.K_RIGHT]:
        player_center[0] += 2
    if key_presed[pygame.K_UP]:
        player_center[1] -= 2
    if key_presed[pygame.K_DOWN]:
        player_center[1] += 2

    screen.blit(sc_map, MAP_POS)
def game_bar():
    size_x = hero.helth
    pygame.draw.rect(screen, (0,hero.COLOR, 0), (10, 10, size_x, 20))
    if size_x <= 5:
        exit()
    if hero.helth < 200:
        hero.helth += 0.1
        hero.COLOR += 0.1

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
            bg = pygame.transform.scale(bg,(e.w,e.h))
        if e.type == pygame.MOUSEBUTTONDOWN:
            FIRE = True









    hero.fire_check(FIRE)
    hero.shot_anim_right()
    hero.shot_anim_left()


    bullet_group.draw(screen)
    bullet_group.update()

    blood_group.draw(screen)
    corpse_group.draw(screen)
    zombie_group.draw(screen)
    zombie_group.update()
    FIRE = False
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()