from race import *

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
                self.y_speed = -2.4
                self.rect.y += self.y_speed
                self.image = car_sprite_5_r
            elif end_time1 - start_time >= 0.1 and end_time1 - start_time < 0.27:
                self.x_speed = 1.2
                self.y_speed = -1.8
                self.rect.y += self.y_speed
                self.image = car_sprite_10_r
            elif end_time1 - start_time >= 0.27 and end_time1 - start_time < 0.35:
                self.x_speed = 1.2
                self.y_speed = -1.7
                self.rect.y += self.y_speed
                self.image = car_sprite_15_r
            elif end_time1 - start_time >= 0.35 and end_time1 - start_time < 0.42:
                self.x_speed = 1.2
                self.y_speed = -1.6
                self.rect.y += self.y_speed
                self.image = car_sprite_20_r
            elif end_time1 - start_time >= 0.42 and end_time1 - start_time < 0.5:
                self.x_speed = 2
                self.y_speed = -1.5
                self.rect.y += self.y_speed
                self.image = car_sprite_25_r
            elif end_time1 - start_time >= 0.5 and end_time1 - start_time < 0.6:
                self.x_speed = 3
                self.y_speed = -1.4
                self.rect.y += self.y_speed
                self.image = car_sprite_30_r
            elif end_time1 - start_time >= 0.6 and end_time1 - start_time < 0.73:
                self.x_speed = 3.6
                self.y_speed = -1.3
                self.rect.y += self.y_speed
                self.image = car_sprite_40_r
            elif end_time1 - start_time >= 0.73 and end_time1 - start_time < 0.9:
                self.x_speed = 4
                self.y_speed = -1.2
                self.rect.y += self.y_speed
                self.image = car_sprite_47_r
            elif end_time1 - start_time >= 0.9 and end_time1 - start_time < 1.05:
                self.x_speed = 4
                self.y_speed = -1
                self.rect.y += self.y_speed
                self.image = car_sprite_55_r
            elif end_time1 - start_time >= 1.05 and end_time1 - start_time < 1.2:
                self.x_speed = 3
                self.y_speed = -0.5
                self.rect.y += self.y_speed
                self.image = car_sprite_60_r
            elif end_time1 - start_time >= 1.2 and end_time1 - start_time < 1.35:
                self.x_speed = 5
                self.y_speed = -0.7
                self.rect.y += self.y_speed
                self.image = car_sprite_65_r
            elif end_time1 - start_time >= 1.35 and end_time1 - start_time < 1.5:
                self.x_speed = 5
                self.y_speed = -0.9
                self.rect.y += self.y_speed
                self.image = car_sprite_72_r
            elif end_time1 - start_time >= 1.5 and end_time1 - start_time < 1.65:
                self.x_speed = 1.2
                self.y_speed = -0.8
                self.rect.y += self.y_speed
                self.image = car_sprite_80_r
            elif end_time1 - start_time >= 1.65 and end_time1 - start_time < 1.8:
                self.x_speed = 1.4
                self.y_speed = -0.8
                self.rect.y += self.y_speed
                self.image = car_sprite_85_r
            elif end_time1 - start_time >= 1.8 and end_time1 - start_time < 1.95:
                self.x_speed = 1.5
                self.y_speed = -0.7
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
                self.y_speed = -2.4
                self.rect.y += self.y_speed
                self.image = car_sprite_5_l
            elif end_time1 - start_time >= 0.1 and end_time1 - start_time < 0.27:
                self.x_speed = -1.2
                self.y_speed = -1.8
                self.rect.y += self.y_speed
                self.image = car_sprite_10_l
            elif end_time1 - start_time >= 0.27 and end_time1 - start_time < 0.35:
                self.x_speed = -1.2
                self.y_speed = -1.7
                self.rect.y += self.y_speed
                self.image = car_sprite_15_l
            elif end_time1 - start_time >= 0.35 and end_time1 - start_time < 0.42:
                self.x_speed = -1.2
                self.y_speed = -1.6
                self.rect.y += self.y_speed
                self.image = car_sprite_20_l
            elif end_time1 - start_time >= 0.42 and end_time1 - start_time < 0.5:
                self.x_speed = -2
                self.y_speed = -1.5
                self.rect.y += self.y_speed
                self.image = car_sprite_25_l
            elif end_time1 - start_time >= 0.5 and end_time1 - start_time < 0.6:
                self.x_speed = -3
                self.y_speed = -1.4
                self.rect.y += self.y_speed
                self.image = car_sprite_30_l
            elif end_time1 - start_time >= 0.6 and end_time1 - start_time < 0.73:
                self.x_speed = -3.6
                self.y_speed = -1.3
                self.rect.y += self.y_speed
                self.image = car_sprite_40_l
            elif end_time1 - start_time >= 0.73 and end_time1 - start_time < 0.9:
                self.x_speed = -4
                self.y_speed = -1.2
                self.rect.y += self.y_speed
                self.image = car_sprite_47_l
            elif end_time1 - start_time >= 0.9 and end_time1 - start_time < 1.05:
                self.x_speed = -4
                self.y_speed = -1
                self.rect.y += self.y_speed
                self.image = car_sprite_55_l
            elif end_time1 - start_time >= 1.05 and end_time1 - start_time < 1.2:
                self.x_speed = -3
                self.y_speed = -0.5
                self.rect.y += self.y_speed
                self.image = car_sprite_60_l
            elif end_time1 - start_time >= 1.2 and end_time1 - start_time < 1.35:
                self.x_speed = -5
                self.y_speed = -0.7
                self.rect.y += self.y_speed
                self.image = car_sprite_65_l
            elif end_time1 - start_time >= 1.35 and end_time1 - start_time < 1.5:
                self.x_speed = -5
                self.y_speed = -0.9
                self.rect.y += self.y_speed
                self.image = car_sprite_72_l
            elif end_time1 - start_time >= 1.5 and end_time1 - start_time < 1.65:
                self.x_speed = -1.2
                self.y_speed = -0.8
                self.rect.y += self.y_speed
                self.image = car_sprite_80_l
            elif end_time1 - start_time >= 1.65 and end_time1 - start_time < 1.8:
                self.x_speed = -1.4
                self.y_speed = -0.8
                self.rect.y += self.y_speed
                self.image = car_sprite_85_l
            elif end_time1 - start_time >= 1.8 and end_time1 - start_time < 1.95:
                self.x_speed = -1.5
                self.y_speed = -0.7
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
                self.y_speed = 2
                self.rect.y += self.y_speed
            elif end_time - start_time >= 0.5:# and end_time - start_time < 0.7:
                self.y_speed = 3
                self.rect.y += self.y_speed
            #elif end_time - start_time >= 1:
            #    self.y_speed = 4
            #    self.rect.y += self.y_speed
            else:
                pass

class Walls(GameSprite):
    def __init__(self, picture, x, y):
        super().__init__(picture, x, y)
    def update_wall(self, press):
        if press:
            self.rect.y += 4
        else:
            self.rect.y += 5