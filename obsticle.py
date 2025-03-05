import random
import pygame
from o import Object
from player import Player

class Obsticle(Object):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.color = (70, 70, 70)

    def update(self, player):
        # should be called in main
        super().update()
        if do_overlap((self.x, self.y), (self.x + self.xr, self.y + self.yr),
                      (player.x, player.y), (player.x + player.xr, player.y + player.yr)):
            print("Life --")
            player.l -= 1

    def touch(self, event):
        if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN for presses
            x, y = event.pos
            if pygame.Rect(self.x, self.y, self.xr, self.yr).collidepoint(x, y):
                self.ac = False




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
