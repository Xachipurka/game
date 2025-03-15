import pygame
from coin import Coin
import o


class Special_coin(Coin):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (0, 255, 0)

    def collect(self):
        self.col = False
        o.ispeed *= 0.7