import pygame
from random import *
import time
from player import *

pygame.init()
window = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Заезд")
window.fill((0, 0, 0))
run = True

car_sprite = pygame.transform.scale(pygame.image.load("car.png"), (50, 75))
wall = pygame.transform.scale(pygame.image.load("roadWall.jpg"), (30, 45))
last_walls = [0]
walls_way = ["l", "s", "r"]
walls_way_l = ["s", "r"]
walls_way_r = ["l", "s"]
walls_way_s = ["l", "r"]
last_coordinats_l = []
last_coordinats_r = []






def rot_center(image, angle):
    rot_image = pygame.transform.rotate(image, angle)
    return rot_image
press = False
#СОЗДАНИЕ КАРТИНОК В ПРАВУЮ СТОРОНУ
car_sprite_5_r = rot_center(car_sprite, 355)
car_sprite_10_r = rot_center(car_sprite, 350)
car_sprite_15_r = rot_center(car_sprite, 345)
car_sprite_20_r = rot_center(car_sprite, 340)
car_sprite_25_r = rot_center(car_sprite, 335)
car_sprite_30_r = rot_center(car_sprite, 330)
car_sprite_40_r = rot_center(car_sprite, 320)
car_sprite_47_r = rot_center(car_sprite, 313)
car_sprite_55_r = rot_center(car_sprite, 305)
car_sprite_60_r = rot_center(car_sprite, 300)
car_sprite_65_r = rot_center(car_sprite, 295)
car_sprite_72_r = rot_center(car_sprite, 288)
car_sprite_80_r = rot_center(car_sprite, 280)
car_sprite_85_r = rot_center(car_sprite, 275)
car_sprite_90_r = rot_center(car_sprite, 270)
car_sprite_95_r = rot_center(car_sprite, 265)
car_sprite_100_r = rot_center(car_sprite, 260)
car_sprite_110_r = rot_center(car_sprite, 250)
car_sprite_120_r = rot_center(car_sprite, 240)
car_sprite_130_r = rot_center(car_sprite, 230)
#СОЗДАНИЕ КАРТИНОК В ЛЕВУЮ СТОРОНУ
car_sprite_5_l = rot_center(car_sprite, 5)
car_sprite_10_l = rot_center(car_sprite, 10)
car_sprite_15_l = rot_center(car_sprite, 15)
car_sprite_20_l = rot_center(car_sprite, 20)
car_sprite_25_l = rot_center(car_sprite, 25)
car_sprite_30_l = rot_center(car_sprite, 30)
car_sprite_40_l = rot_center(car_sprite, 40)
car_sprite_47_l = rot_center(car_sprite, 47)
car_sprite_55_l = rot_center(car_sprite, 55)
car_sprite_60_l = rot_center(car_sprite, 60)
car_sprite_65_l = rot_center(car_sprite, 65)
car_sprite_72_l = rot_center(car_sprite, 72)
car_sprite_80_l = rot_center(car_sprite, 80)
car_sprite_85_l = rot_center(car_sprite, 85)
car_sprite_90_l = rot_center(car_sprite, 90)
car_sprite_95_l = rot_center(car_sprite, 95)
car_sprite_100_l = rot_center(car_sprite, 100)
car_sprite_110_l = rot_center(car_sprite, 110)
car_sprite_120_l = rot_center(car_sprite, 120)
car_sprite_130_l = rot_center(car_sprite, 130)
def make_l(last_coordinats_l, last_coordinats_r):
    for i in range(5):
        leftWall_left1 = Walls(wall, last_coordinats_l[-2] - 30, last_coordinats_l[-1] - 45)
        left_walls.add(leftWall_left1)
        last_coordinats_l.append(last_coordinats_l[-2] - 30)
        last_coordinats_l.append(last_coordinats_l[-2] - 40)
        leftWall_right2 = Walls(wall, last_coordinats_r[-2] - 30, last_coordinats_r[-1] - 45)
        right_walls.add(leftWall_right2)
        last_coordinats_r.append(last_coordinats_r[-2] - 30)
        last_coordinats_r.append(last_coordinats_r[-2] - 40)
        last_coordinats_r.pop(-3)

def make_r(last_coordinats_l, last_coordinats_r):
    for i in range(5):
        leftWall_left1 = Walls(wall, last_coordinats_l[-2] + 30, last_coordinats_l[-1] - 45)
        left_walls.add(leftWall_left1)
        last_coordinats_l.append(last_coordinats_l[-2] + 30)
        last_coordinats_l.append(last_coordinats_l[-2] - 40)
        leftWall_right1 = Walls(wall, last_coordinats_r[-2] + 30, last_coordinats_r[-1] - 45)
        right_walls.add(leftWall_right1)
        last_coordinats_r.append(last_coordinats_r[-2] + 30)
        last_coordinats_r.append(last_coordinats_r[-2] - 40)
        last_coordinats_r.pop(-3)
def make_s(last_coordinats_l, last_coordinats_r):
    for i in range(3):
        leftWall_left1 = Walls(wall, last_coordinats_l[-2] + 0, last_coordinats_l[-1] - 45)
        left_walls.add(leftWall_left1)
        last_coordinats_l.append(last_coordinats_l[-2] + 0)
        last_coordinats_l.append(last_coordinats_l[-2] - 40)
        leftWall_right1 = Walls(wall, last_coordinats_r[-2] + 0, last_coordinats_r[-1] - 45)
        right_walls.add(leftWall_right1)
        last_coordinats_r.append(last_coordinats_r[-2] + 0)
        last_coordinats_r.append(last_coordinats_r[-2] - 40)
        last_coordinats_r.pop(-3)

hero = Player(car_sprite, 750, 500, 0, 0)
left_walls = pygame.sprite.Group()
right_walls = pygame.sprite.Group()
#САМЫЙ НАЧАЛЬНЫЙ СТЕНЫ
start_walls = pygame.sprite.Group()
w0 = Walls(wall, 575, 0)
last_coordinats_l.append(w0.rect.x)
last_coordinats_l.append(w0.rect.y)
w1 = Walls(wall, 925, 0)
last_coordinats_r.append(w1.rect.x)
last_coordinats_r.append(w1.rect.y)

while run:
    window.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                start_time = time.time()
                hero.x_speed = -5
            if e.key == pygame.K_s:
                hero.y_speed = 5
                press = True
                start_time = time.time()
            if e.key == pygame.K_d:
                start_time = time.time()
                hero.x_speed = 5
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_a:
                hero.x_speed = 0
                hero.image = car_sprite
            if e.key == pygame.K_d:
                hero.x_speed = 0
                hero.image = car_sprite
            if e.key == pygame.K_s:
                hero.y_speed = 0
                press = False
    if last_walls[-1] == "s" and last_walls[-2] == "l" or last_walls[-1] == "l" and last_walls[-2] == "l" or last_walls[-1] == "s" and last_walls[-2] == "s" and last_walls[-3] == "l":
        rand = choice(walls_way_l)
        last_walls.append(rand)
    elif last_walls[-1] == "s" and last_walls[-2] == "r" or last_walls[-1] == "r" and last_walls[-2] == "r" or last_walls[-1] == "s" and last_walls[-2] == "s" and last_walls[-3] == "r":
        rand = choice(walls_way_r)
        last_walls.append(rand)
    elif last_walls[-1] == "s" and last_walls[-2] == "s":
        rand = choice(walls_way_s)
        last_walls.append(rand)
    else:
        rand = choice(walls_way_s)
        last_walls.append(rand)

    if last_walls[-1] == "l":
        make_l(last_coordinats_l, last_coordinats_r)
    elif last_walls[-1] == "r":
        make_r(last_coordinats_l, last_coordinats_r)
    else:
        make_s(last_coordinats_l, last_coordinats_r)
    for i in left_walls:
        i.update_wall(press)
        i.reset()
    for i in right_walls:
        i.update_wall(press)
        i.reset()
    hero.reset()
    hero.update()
    pygame.time.delay(25)
    pygame.display.update()