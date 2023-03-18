import pygame
from random import *
import time

from core.GameSprite import GameSprite
from core.Player import Player
from core.walls import Walls

pygame.init()
window = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Заезд")
window.fill((0, 0, 0))
run = True

start_time =time.time()
car_sprite = pygame.transform.scale(pygame.image.load("../assets/car.png"), (50, 75))
wall = pygame.transform.scale(pygame.image.load("../assets/roadWall.jpg"), (30, 45))
sad_shumaher = pygame.transform.scale(pygame.image.load("../assets/shumaher.jpg"), (900, 700))
font = pygame.font.SysFont("Arial", 40)
whole_time = font.render("TIME:", True, (0, 0, 0))
start_timer = time.time()
last_walls = [0]
walls_way = ["l", "s", "r"]
walls_way_l = ["s", "r"]
walls_way_r = ["l", "s"]
walls_way_s = ["l", "r"]
last_coordinats_l = []
time_list = []
last_coordinats_r = []
health = 3
stop = False
cnt1 = 0

press = False
press_drift = False
differents1 = 2
differents2 = 0

cnt = 1
def make_l(last_coordinats_l, last_coordinats_r, cnt):
    for i in range(5):
        leftWall_left1 = Walls(wall, last_coordinats_l[-2] - 30, last_coordinats_l[-1] - 45)
        left_walls.add(leftWall_left1)
        last_coordinats_l.append(last_coordinats_l[-2] - 30)
        last_coordinats_l.append(last_coordinats_l[-2] - 40)
        #del last_coordinats_l[-1]
        leftWall_right2 = Walls(wall, last_coordinats_r[-2] - 30, last_coordinats_r[-1] - 45)
        right_walls.add(leftWall_right2)
        last_coordinats_r.append(last_coordinats_r[-2] - 30)
        last_coordinats_r.append(last_coordinats_r[-2] - 40)
        if cnt >= 3:
            del last_coordinats_r[0]
            del last_coordinats_r[0]
            del last_coordinats_l[0]
            del last_coordinats_l[0]
            
        #del last_coordinats_r[-1]

def make_r(last_coordinats_l, last_coordinats_r, cnt):
    for i in range(5):
        leftWall_left1 = Walls(wall, last_coordinats_l[-2] + 30, last_coordinats_l[-1] - 45)
        left_walls.add(leftWall_left1)
        last_coordinats_l.append(last_coordinats_l[-2] + 30)
        last_coordinats_l.append(last_coordinats_l[-2] - 40)
        #del last_coordinats_l[-1]
        leftWall_right1 = Walls(wall, last_coordinats_r[-2] + 30, last_coordinats_r[-1] - 45)
        right_walls.add(leftWall_right1)
        last_coordinats_r.append(last_coordinats_r[-2] + 30)
        last_coordinats_r.append(last_coordinats_r[-2] - 40)
        if cnt >= 3:
            del last_coordinats_r[0]
            del last_coordinats_r[0]
            del last_coordinats_l[0]
            del last_coordinats_l[0]
        #del last_coordinats_r[-1]
def make_s(last_coordinats_l, last_coordinats_r, cnt):
    for i in range(3):
        leftWall_left1 = Walls(wall, last_coordinats_l[-2] + 0, last_coordinats_l[-1] - 45)
        left_walls.add(leftWall_left1)
        last_coordinats_l.append(last_coordinats_l[-2] + 0)
        last_coordinats_l.append(last_coordinats_l[-2] - 40)
        #del last_coordinats_l[-1]
        leftWall_right1 = Walls(wall, last_coordinats_r[-2] + 0, last_coordinats_r[-1] - 45)
        right_walls.add(leftWall_right1)
        last_coordinats_r.append(last_coordinats_r[-2] + 0)
        last_coordinats_r.append(last_coordinats_r[-2] - 40)
        if cnt >= 3:
            del last_coordinats_r[0]
            del last_coordinats_r[0]
            del last_coordinats_l[0]
            del last_coordinats_l[0]
        #del last_coordinats_r[-1]

hero = Player(car_sprite, 750, 500, 0, 0)
shumaher = GameSprite(sad_shumaher, 100, 100)
left_walls = pygame.sprite.Group()
right_walls = pygame.sprite.Group()
#САМЫЙ НАЧАЛЬНЫЙ СТЕНЫ
start_walls = pygame.sprite.Group()
w0 = Walls(wall, 575, 0)
last_coordinats_l.append(w0.rect.x)
last_coordinats_l.append(w0.rect.y)
w1 = Walls(wall, 925, 0)
health_y = 700
last_coordinats_r.append(w1.rect.x)
last_coordinats_r.append(w1.rect.y)
finish = False
while run:
    window.fill((0, 0, 0))

    # start_time = time.time()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                hero.x_speed = -5
                start_time = time.time()
                press_drift = True
            if e.key == pygame.K_s:
                hero.y_speed = 5
                start_time = time.time()
                press = True
            if e.key == pygame.K_d:
                press_drift = True
                start_time = time.time()
                hero.x_speed = 5
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_a:
                hero.x_speed = 0
                hero.image = car_sprite
                press_drift = False
            if e.key == pygame.K_d:
                hero.x_speed = 0
                press_drift = False
                hero.image = car_sprite
            if e.key == pygame.K_s:
                hero.y_speed = 0
                press = False

    if finish == False:
        if cnt1 % 3 == 0:
            if last_walls[-1] == "s" and last_walls[-2] == "l" or last_walls[-1] == "l" and last_walls[-2] == "l" or last_walls[-1] == "s" and last_walls[-2] == "s" and last_walls[-3] == "l" or last_walls[-1] == "l" and last_walls[-2] == "r" and last_walls[-3] == "l" and last_walls[-4] == "l":
                rand = choice(walls_way_l)
                last_walls.append(rand)
            elif last_walls[-1] == "s" and last_walls[-2] == "r" or last_walls[-1] == "r" and last_walls[-2] == "r" or last_walls[-1] == "s" and last_walls[-2] == "s" and last_walls[-3] == "r" or last_walls[-1] == "r" and last_walls[-2] == "l" and last_walls[-3] == "r" and last_walls[-4] == "r":
                rand = choice(walls_way_r)
                last_walls.append(rand)
            elif last_walls[-1] == "s" and last_walls[-2] == "s":
                rand = choice(walls_way_s)
                last_walls.append(rand)
            else:
                rand = choice(walls_way_s)
                last_walls.append(rand)
            cnt1 += 1
            if last_walls[-1] == "l":
                make_l(last_coordinats_l, last_coordinats_r, cnt)
                cnt += 1
            elif last_walls[-1] == "r":
                make_r(last_coordinats_l, last_coordinats_r, cnt)
                cnt += 1
            else:
                make_s(last_coordinats_l, last_coordinats_r, cnt)
                cnt += 1
        for i in left_walls:
            i.update_wall(press, press_drift)
            i.reset(window)
        for i in right_walls:
            i.update_wall(press, press_drift)
            i.reset(window)
        else:
            cnt1 += 1
        if stop:
            #hero.update()
            hero.reset(window)
            time.sleep(1.5)
            stop = False
        else:
            hero.reset(window)
            hero.update(start_time)
        health_y -= 0.5
        health_label = font.render("HEALTH:", True, (255, 255, 255))
        window.blit(health_label, (1400, hero.rect.y + 10))
        hp_list = []
        hp_list.append(str(health))
        hp = font.render(hp_list[0], True, (255, 255, 255))
        window.blit(hp, (1550, hero.rect.y + 10))
        for i in left_walls:
            if pygame.sprite.collide_rect(hero, i) and health > 0:
                hero.rect.x += 80
                health -= 1
                stop = True
                #finish = True
                #window.blit(label_time, (1200, 600))
        for i in right_walls:
            if pygame.sprite.collide_rect(hero, i):
                hero.rect.x -= 80
                health -= 1
                stop = True
        if health == 0:
            finish = True
    else:
        window.fill((255, 255, 255))
        finish_timer = time.time()
        window.blit(whole_time, (1010, 750))
        whoole_time = int(finish_timer - start_timer)
        time_list.append(str(whoole_time))
        label_time = font.render(time_list[0], True, (0, 0, 0))
        shumaher.reset(window)
        window.blit(label_time, (1110, 750))

    pygame.time.delay(25)
    pygame.display.update()
#ad