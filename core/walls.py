import pygame
from core.GameSprite import GameSprite

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