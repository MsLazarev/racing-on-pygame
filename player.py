import pygame
import time

car_sprite = pygame.transform.scale(pygame.image.load("car.png"), (50, 75))

def rot_center(image, angle):
    rot_image = pygame.transform.rotate(image, angle)
    return rot_image
#СОЗДАНИЕ КАРТИНОК В ПРАВУЮ СТОРОНУ
# car_sprite_5_r = rot_center(car_sprite, 355)
# car_sprite_10_r = rot_center(car_sprite, 350)
# car_sprite_15_r = rot_center(car_sprite, 345)
# car_sprite_20_r = rot_center(car_sprite, 340)
# car_sprite_25_r = rot_center(car_sprite, 335)
# car_sprite_30_r = rot_center(car_sprite, 330)
# car_sprite_40_r = rot_center(car_sprite, 320)
# car_sprite_47_r = rot_center(car_sprite, 313)
# car_sprite_55_r = rot_center(car_sprite, 305)
# car_sprite_60_r = rot_center(car_sprite, 300)
# car_sprite_65_r = rot_center(car_sprite, 295)
# car_sprite_72_r = rot_center(car_sprite, 288)
# car_sprite_80_r = rot_center(car_sprite, 280)
# car_sprite_85_r = rot_center(car_sprite, 275)
# car_sprite_90_r = rot_center(car_sprite, 270)
# car_sprite_95_r = rot_center(car_sprite, 265)
# car_sprite_100_r = rot_center(car_sprite, 260)
# car_sprite_110_r = rot_center(car_sprite, 250)
# car_sprite_120_r = rot_center(car_sprite, 240)
# car_sprite_130_r = rot_center(car_sprite, 230)
# #СОЗДАНИЕ КАРТИНОК В ЛЕВУЮ СТОРОНУ
# car_sprite_5_l = rot_center(car_sprite, 5)
# car_sprite_10_l = rot_center(car_sprite, 10)
# car_sprite_15_l = rot_center(car_sprite, 15)
# car_sprite_20_l = rot_center(car_sprite, 20)
# car_sprite_25_l = rot_center(car_sprite, 25)
# car_sprite_30_l = rot_center(car_sprite, 30)
# car_sprite_40_l = rot_center(car_sprite, 40)
# car_sprite_47_l = rot_center(car_sprite, 47)
# car_sprite_55_l = rot_center(car_sprite, 55)
# car_sprite_60_l = rot_center(car_sprite, 60)
# car_sprite_65_l = rot_center(car_sprite, 65)
# car_sprite_72_l = rot_center(car_sprite, 72)
# car_sprite_80_l = rot_center(car_sprite, 80)
# car_sprite_85_l = rot_center(car_sprite, 85)
# car_sprite_90_l = rot_center(car_sprite, 90)
# car_sprite_95_l = rot_center(car_sprite, 95)
# car_sprite_100_l = rot_center(car_sprite, 100)
# car_sprite_110_l = rot_center(car_sprite, 110)
# car_sprite_120_l = rot_center(car_sprite, 120)
# car_sprite_130_l = rot_center(car_sprite, 130)
#
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture, x, y, win):
        super().__init__()
        self.image = picture
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.window = win
    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def __init__(self, picture, x, y, x_speed, y_speed, win):
        super().__init__(picture, x, y, win)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self, start_time):
        #ДРИФТ В ПРАВУЮ СТОРОНУ
        if self.x_speed > 0:
            end_time1 = time.time()
            # self.rect.y -= 1*(self.rect.x**0.2)
            if end_time1 - start_time >= 0.001 and end_time1 - start_time < 0.1:
                self.x_speed = 0.5
                self.y_speed = -0.5#-1.6
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 355)
            elif end_time1 - start_time >= 0.1 and end_time1 - start_time < 0.27:
                self.x_speed = 1.2
                self.y_speed = -0.4#-1.3
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 350)
            elif end_time1 - start_time >= 0.27 and end_time1 - start_time < 0.35:
                self.x_speed = 1.2
                self.y_speed = -0.4#-1.2
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 345)
            elif end_time1 - start_time >= 0.35 and end_time1 - start_time < 0.42:
                self.x_speed = 1.2
                self.y_speed = -0.3#-1.1
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 340)
            elif end_time1 - start_time >= 0.42 and end_time1 - start_time < 0.5:
                self.x_speed = 2
                self.y_speed = -0.25#-1
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 335)
            elif end_time1 - start_time >= 0.5 and end_time1 - start_time < 0.6:
                self.x_speed = 3
                self.y_speed = -0.2#-0.9
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 330)
            elif end_time1 - start_time >= 0.6 and end_time1 - start_time < 0.73:
                self.x_speed = 3.6
                self.y_speed = -0.2#-0.8
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 320)
            elif end_time1 - start_time >= 0.73 and end_time1 - start_time < 0.9:
                self.x_speed = 4
                self.y_speed = -0.2#-0.7
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 313)
            elif end_time1 - start_time >= 0.9 and end_time1 - start_time < 1.05:
                self.x_speed = 4
                self.y_speed = -0.15#-0.4
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 305)
            elif end_time1 - start_time >= 1.05 and end_time1 - start_time < 1.2:
                self.x_speed = 3
                self.y_speed = -0.1
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 300)
            elif end_time1 - start_time >= 1.2 and end_time1 - start_time < 1.35:
                self.x_speed = 5
                self.y_speed = -0.3
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 295)
            elif end_time1 - start_time >= 1.35 and end_time1 - start_time < 1.5:
                self.x_speed = 5
                self.y_speed = -0.5
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 288)
            elif end_time1 - start_time >= 1.5 and end_time1 - start_time < 1.65:
                self.x_speed = 5
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 280)
            elif end_time1 - start_time >= 1.65 and end_time1 - start_time < 1.8:
                self.x_speed = 4
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 275)
            elif end_time1 - start_time >= 1.8 and end_time1 - start_time < 1.95:
                self.x_speed = 5
                self.y_speed = -0.3
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 270)
            elif end_time1 - start_time >= 1.95 and end_time1 - start_time < 2.1:
                self.x_speed = 4.6
                self.y_speed = 0.1
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 265)
            elif end_time1 - start_time >= 2.1 and end_time1 - start_time < 2.25:
                self.x_speed = 4.7
                self.y_speed = 0.2
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 260)
            elif end_time1 - start_time >= 2.25 and end_time1 - start_time < 2.4:
                self.x_speed = 4.8
                self.y_speed = 0.3
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 250)
            elif end_time1 - start_time >= 2.4 and end_time1 - start_time < 2.7:
                self.x_speed = 5
                self.y_speed = 0.5
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 240)
            elif end_time1 - start_time >= 2.7:# and end_time1 - start_time < 2.:
                self.x_speed = 5
                self.y_speed = 0.7
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 230)
            else:
                pass
            #КОНЕЦ ДРИФТА В ПРАВУЮ СТОРОНУ
        if self.x_speed < 0:
            end_time1 = time.time()
            if end_time1 - start_time >= 0.001 and end_time1 - start_time < 0.1:
                self.x_speed = -0.5
                self.y_speed = -0.5#-1.5
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 5)
            elif end_time1 - start_time >= 0.1 and end_time1 - start_time < 0.27:
                self.x_speed = -1.2
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 10)
            elif end_time1 - start_time >= 0.27 and end_time1 - start_time < 0.35:
                self.x_speed = -1.2
                self.y_speed = -0.4#-1.2
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 15)
            elif end_time1 - start_time >= 0.35 and end_time1 - start_time < 0.42:
                self.x_speed = -1.2
                self.y_speed = -0.3#-1.1
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 20)
            elif end_time1 - start_time >= 0.42 and end_time1 - start_time < 0.5:
                self.x_speed = -2
                self.y_speed = -0.25#-1
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 25)
            elif end_time1 - start_time >= 0.5 and end_time1 - start_time < 0.6:
                self.x_speed = -3
                self.y_speed = -0.2#-0.9
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 30)
            elif end_time1 - start_time >= 0.6 and end_time1 - start_time < 0.73:
                self.x_speed = -3.6
                self.y_speed = -0.2#-0.8
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 40)
            elif end_time1 - start_time >= 0.73 and end_time1 - start_time < 0.9:
                self.x_speed = -4
                self.y_speed = -0.15
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 47)
            elif end_time1 - start_time >= 0.9 and end_time1 - start_time < 1.05:
                self.x_speed = -4
                self.y_speed = -0.15
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 55)
            elif end_time1 - start_time >= 1.05 and end_time1 - start_time < 1.2:
                self.x_speed = -3
                self.y_speed = -0.1
                self.rect.y += self.y_speed
                self.image =rot_center(self.image, 60)
            elif end_time1 - start_time >= 1.2 and end_time1 - start_time < 1.35:
                self.x_speed = -5
                self.y_speed = -0.3
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 65)
            elif end_time1 - start_time >= 1.35 and end_time1 - start_time < 1.5:
                self.x_speed = -5
                self.y_speed = -0.5
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 72)
            elif end_time1 - start_time >= 1.5 and end_time1 - start_time < 1.65:
                self.x_speed = -5
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 80)
            elif end_time1 - start_time >= 1.65 and end_time1 - start_time < 1.8:
                self.x_speed = -4
                self.y_speed = -0.4
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 85)
            elif end_time1 - start_time >= 1.8 and end_time1 - start_time < 1.95:
                self.x_speed = -3.5
                self.y_speed = -0.3
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 90)
            elif end_time1 - start_time >= 1.95 and end_time1 - start_time < 2.1:
                self.x_speed = -4.6
                self.y_speed = 0.1
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 95)
            elif end_time1 - start_time >= 2.1 and end_time1 - start_time < 2.25:
                self.x_speed = -4.7
                self.y_speed = 0.2
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 100)
            elif end_time1 - start_time >= 2.25 and end_time1 - start_time < 2.4:
                self.x_speed = -4.8
                self.y_speed = 0.3
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 110)
            elif end_time1 - start_time >= 2.4 and end_time1 - start_time < 2.7:
                self.x_speed = -5
                self.y_speed = 0.5
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 120)
            elif end_time1 - start_time >= 2.7:# and end_time1 - start_time < 2.:
                self.x_speed = -5
                self.y_speed = 0.7
                self.rect.y += self.y_speed
                self.image = rot_center(self.image, 130)
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
    def __init__(self, picture, x, y, win):
        super().__init__(picture, x, y, win)
    def update_wall(self, press, press_drift):
        if press_drift:
            self.rect.y += 8.5
        elif press:
            self.rect.y += 3
        else:
            self.rect.y += 6