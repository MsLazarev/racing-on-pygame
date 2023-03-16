import pygame
from random import *
import time
#from player import *

pygame.init()
window = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Заезд")
window.fill((0, 0, 0))
run = True

car_sprite = pygame.transform.scale(pygame.image.load("car.png"), (50, 75))
wall = pygame.transform.scale(pygame.image.load("roadWall.jpg"), (30, 45))
sad_shumaher = pygame.transform.scale(pygame.image.load("shumaher.jpg"), (900, 700))
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

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture, x, y):
        super().__init__()
        self.image = picture
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, picture, x, y, x_speed, y_speed):
        super().__init__(picture, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        #ДРИФТ В ПРАВУЮ СТОРОНУ
        if self.x_speed > 0:
            end_time1 = time.time()
            if end_time1 - start_time >= 0.001 and end_time1 - start_time < 0.1:
                self.x_speed = 0.5
                self.y_speed = -0.5#-1.6
                self.rect.y += self.y_speed
                self.image = car_sprite_5_r
            elif end_time1 - start_time >= 0.1 and end_time1 - start_time < 0.27:
                self.x_speed = 1.2
                self.y_speed = -0.4#-1.3
                self.rect.y += self.y_speed
                self.image = car_sprite_10_r
            elif end_time1 - start_time >= 0.27 and end_time1 - start_time < 0.35:
                self.x_speed = 1.2
                self.y_speed = -0.4#-1.2
                self.rect.y += self.y_speed
                self.image = car_sprite_15_r
            elif end_time1 - start_time >= 0.35 and end_time1 - start_time < 0.42:
                self.x_speed = 1.2
                self.y_speed = -0.3#-1.1
                self.rect.y += self.y_speed
                self.image = car_sprite_20_r
            elif end_time1 - start_time >= 0.42 and end_time1 - start_time < 0.5:
                self.x_speed = 2
                self.y_speed = -0.25#-1
                self.rect.y += self.y_speed
                self.image = car_sprite_25_r
            elif end_time1 - start_time >= 0.5 and end_time1 - start_time < 0.6:
                self.x_speed = 3
                self.y_speed = -0.2#-0.9
                self.rect.y += self.y_speed
                self.image = car_sprite_30_r
            elif end_time1 - start_time >= 0.6 and end_time1 - start_time < 0.73:
                self.x_speed = 3.6
                self.y_speed = -0.2#-0.8
                self.rect.y += self.y_speed
                self.image = car_sprite_40_r
            elif end_time1 - start_time >= 0.73 and end_time1 - start_time < 0.9:
                self.x_speed = 4
                self.y_speed = -0.2#-0.7
                self.rect.y += self.y_speed
                self.image = car_sprite_47_r
            elif end_time1 - start_time >= 0.9 and end_time1 - start_time < 1.05:
                self.x_speed = 4
                self.y_speed = -0.15#-0.4
                self.rect.y += self.y_speed
                self.image = car_sprite_55_r
            elif end_time1 - start_time >= 1.05 and end_time1 - start_time < 1.2:
                self.x_speed = 3
                self.y_speed = -0.1
                self.rect.y += self.y_speed
                self.image = car_sprite_60_r
            elif end_time1 - start_time >= 1.2 and end_time1 - start_time < 1.35:
                self.x_speed = 5
                self.y_speed = -0.3
                self.rect.y += self.y_speed
                self.image = car_sprite_65_r
            elif end_time1 - start_time >= 1.35 and end_time1 - start_time < 1.5:
                self.x_speed = 5
                self.y_speed = -0.5
                self.rect.y += self.y_speed
                self.image = car_sprite_72_r
            elif end_time1 - start_time >= 1.5 and end_time1 - start_time < 1.65:
                self.x_speed = 5
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = car_sprite_80_r
            elif end_time1 - start_time >= 1.65 and end_time1 - start_time < 1.8:
                self.x_speed = 4
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = car_sprite_85_r
            elif end_time1 - start_time >= 1.8 and end_time1 - start_time < 1.95:
                self.x_speed = 5
                self.y_speed = -0.3
                self.rect.y += self.y_speed
                self.image = car_sprite_90_r
            elif end_time1 - start_time >= 1.95 and end_time1 - start_time < 2.1:
                self.x_speed = 4.6
                self.y_speed = 0.1
                self.rect.y += self.y_speed
                self.image = car_sprite_95_r
            elif end_time1 - start_time >= 2.1 and end_time1 - start_time < 2.25:
                self.x_speed = 4.7
                self.y_speed = 0.2
                self.rect.y += self.y_speed
                self.image = car_sprite_100_r
            elif end_time1 - start_time >= 2.25 and end_time1 - start_time < 2.4:
                self.x_speed = 4.8
                self.y_speed = 0.3
                self.rect.y += self.y_speed
                self.image = car_sprite_110_r
            elif end_time1 - start_time >= 2.4 and end_time1 - start_time < 2.7:
                self.x_speed = 5
                self.y_speed = 0.5
                self.rect.y += self.y_speed
                self.image = car_sprite_120_r
            elif end_time1 - start_time >= 2.7:# and end_time1 - start_time < 2.:
                self.x_speed = 5
                self.y_speed = 0.7
                self.rect.y += self.y_speed
                self.image = car_sprite_130_r
            else:
                pass
            #КОНЕЦ ДРИФТА В ПРАВУЮ СТОРОНУ
        if self.x_speed < 0:
            end_time1 = time.time()
            if end_time1 - start_time >= 0.001 and end_time1 - start_time < 0.1:
                self.x_speed = -0.5
                self.y_speed = -0.5#-1.5
                self.rect.y += self.y_speed
                self.image = car_sprite_5_l
            elif end_time1 - start_time >= 0.1 and end_time1 - start_time < 0.27:
                self.x_speed = -1.2
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = car_sprite_10_l
            elif end_time1 - start_time >= 0.27 and end_time1 - start_time < 0.35:
                self.x_speed = -1.2
                self.y_speed = -0.4#-1.2
                self.rect.y += self.y_speed
                self.image = car_sprite_15_l
            elif end_time1 - start_time >= 0.35 and end_time1 - start_time < 0.42:
                self.x_speed = -1.2
                self.y_speed = -0.3#-1.1
                self.rect.y += self.y_speed
                self.image = car_sprite_20_l
            elif end_time1 - start_time >= 0.42 and end_time1 - start_time < 0.5:
                self.x_speed = -2
                self.y_speed = -0.25#-1
                self.rect.y += self.y_speed
                self.image = car_sprite_25_l
            elif end_time1 - start_time >= 0.5 and end_time1 - start_time < 0.6:
                self.x_speed = -3
                self.y_speed = -0.2#-0.9
                self.rect.y += self.y_speed
                self.image = car_sprite_30_l
            elif end_time1 - start_time >= 0.6 and end_time1 - start_time < 0.73:
                self.x_speed = -3.6
                self.y_speed = -0.2#-0.8
                self.rect.y += self.y_speed
                self.image = car_sprite_40_l
            elif end_time1 - start_time >= 0.73 and end_time1 - start_time < 0.9:
                self.x_speed = -4
                self.y_speed = -0.15
                self.rect.y += self.y_speed
                self.image = car_sprite_47_l
            elif end_time1 - start_time >= 0.9 and end_time1 - start_time < 1.05:
                self.x_speed = -4
                self.y_speed = -0.15
                self.rect.y += self.y_speed
                self.image = car_sprite_55_l
            elif end_time1 - start_time >= 1.05 and end_time1 - start_time < 1.2:
                self.x_speed = -3
                self.y_speed = -0.1
                self.rect.y += self.y_speed
                self.image = car_sprite_60_l
            elif end_time1 - start_time >= 1.2 and end_time1 - start_time < 1.35:
                self.x_speed = -5
                self.y_speed = -0.3
                self.rect.y += self.y_speed
                self.image = car_sprite_65_l
            elif end_time1 - start_time >= 1.35 and end_time1 - start_time < 1.5:
                self.x_speed = -5
                self.y_speed = -0.5
                self.rect.y += self.y_speed
                self.image = car_sprite_72_l
            elif end_time1 - start_time >= 1.5 and end_time1 - start_time < 1.65:
                self.x_speed = -5
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = car_sprite_80_l
            elif end_time1 - start_time >= 1.65 and end_time1 - start_time < 1.8:
                self.x_speed = -4
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = car_sprite_85_l
            elif end_time1 - start_time >= 1.8 and end_time1 - start_time < 1.95:
                self.x_speed = -3.5
                self.y_speed = -0.3
                self.rect.y += self.y_speed
                self.image = car_sprite_90_l
            elif end_time1 - start_time >= 1.95 and end_time1 - start_time < 2.1:
                self.x_speed = -4.6
                self.y_speed = 0.1
                self.rect.y += self.y_speed
                self.image = car_sprite_95_l
            elif end_time1 - start_time >= 2.1 and end_time1 - start_time < 2.25:
                self.x_speed = -4.7
                self.y_speed = 0.2
                self.rect.y += self.y_speed
                self.image = car_sprite_100_l
            elif end_time1 - start_time >= 2.25 and end_time1 - start_time < 2.4:
                self.x_speed = -4.8
                self.y_speed = 0.3
                self.rect.y += self.y_speed
                self.image = car_sprite_110_l
            elif end_time1 - start_time >= 2.4 and end_time1 - start_time < 2.7:
                self.x_speed = -5
                self.y_speed = 0.5
                self.rect.y += self.y_speed
                self.image = car_sprite_120_l
            elif end_time1 - start_time >= 2.7:# and end_time1 - start_time < 2.:
                self.x_speed = -5
                self.y_speed = 0.7
                self.rect.y += self.y_speed
                self.image = car_sprite_130_l
            else:
                pass
        self.rect.x += self.x_speed
        if self.y_speed > 0:
            end_time = time.time()
            if end_time - start_time >= 0.001 and end_time - start_time < 0.3:
                self.y_speed = 1
                self.rect.y += self.y_speed
            elif end_time - start_time >= 0.3 and end_time - start_time < 0.5:
                self.y_speed = 3.5
                self.rect.y += self.y_speed
            elif end_time - start_time >= 0.5:# and end_time - start_time < 0.7:
                self.y_speed = 2.9
                self.rect.y += self.y_speed
            #elif end_time - start_time >= 1:
            #    self.y_speed = 4
            #    self.rect.y += self.y_speed
            else:
                pass

class Walls(GameSprite):
    def __init__(self, picture, x, y):
        super().__init__(picture, x, y)
    def update_wall(self, press, press_drift):
        if press_drift:
            self.rect.y += 8.5
        elif press:
            self.rect.y += 3
        else:
            self.rect.y += 6



def rot_center(image, angle):
    rot_image = pygame.transform.rotate(image, angle)
    return rot_image
press = False
press_drift = False
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
        print(last_coordinats_r)
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
last_coordinats_r.append(w1.rect.x)
last_coordinats_r.append(w1.rect.y)
finish = False
while run:
    window.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                start_time = time.time()
                hero.x_speed = -5
                press_drift = True
            if e.key == pygame.K_s:
                hero.y_speed = 5
                press = True
                start_time = time.time()
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
            i.reset()
        for i in right_walls:
            i.update_wall(press, press_drift)
            i.reset()

        if stop:
            #hero.update()
            hero.reset()
            time.sleep(1.5)
            stop = False
        else:
            hero.reset()
            hero.update()
        health_label = font.render("HEALTH:", True, (255, 255, 255))
        window.blit(health_label, (hero.rect.x + 400, hero.rect.y + 200))
        hp_list = []
        hp_list.append(str(health))
        hp = font.render(hp_list[0], True, (255, 255, 255))
        window.blit(hp, (hero.rect.x + 540, hero.rect.y + 200))
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
        shumaher.reset()
        window.blit(label_time, (1110, 750))

    pygame.time.delay(25)
    pygame.display.update()
#ad