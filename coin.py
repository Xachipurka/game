from o import Object
import pygame
from player import Player


class Coin(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.xr = 30
        self.yr = 30
        self.col = True
        self.color = (255, 255, 20)


        # should be called in main
    def update(self, player):
        super().update()
        if do_overlap((self.x, self.y), (self.x + self.xr, self.y + self.yr),
                      (player.x, player.y), (player.x + player.xr, player.y + player.yr)):
            self.collect()

    def collect(self):
        self.col = False


def do_overlap(l1, r1, l2, r2):
    """
    Определяет, пересекаются ли два прямоугольника.

    :param l1: координаты левого верхнего угла первого прямоугольника (x, y)
    :param r1: координаты правого нижнего угла первого прямоугольника (x, y)
    :param l2: координаты левого верхнего угла второго прямоугольника (x, y)
    :param r2: координаты правого нижнего угла второго прямоугольника (x, y)
    :return: True, если прямоугольники пересекаются, иначе False.
    """
    # Если один прямоугольник находится левее другого:
    if r1[0] < l2[0] or r2[0] < l1[0]:
        return False

    # Если один прямоугольник находится выше другого:
    if l1[1] > r2[1] or l2[1] > r1[1]:
        return False

    return True
