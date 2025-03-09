import random
import pygame
from o import Object
from player import Player

def add_obsticle(ob):
    obi = Obsticle(0, 0)
    obi.x  = random.randrange(0, pygame.display.get_surface().get_size()[0] - obi.xr)
    #obi = Obsticle(random.randrange(0, pygame.display.get_surface().get_size()[0] - obiiiiiii.x), 0)
    ohoho = True
    for i in range(len(ob)):
        if do_overlap((obi.x, obi.y), (obi.x + obi.xr, obi.y + obi.yr),
                    (ob[i].x, ob[i].y), (ob[i].x + ob[i].xr, ob[i].y + ob[i].yr)):
            add_obsticle(ob)
            ohoho = False
            break
    if ohoho:
        ob.append(obi)





class Obsticle(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.lives = 3
        self.live = 3
        self.color = (70, 70, 70)
        self.xrp = self.xr - 25

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
                self.live -= 1
                '''
                oh = self.live / self.lives
                l2 = oh * self.live
                self.sh = l2
                '''
                if self.live == 0:
                    self.ac = False

    def draww(self, screen):
        super().draw(screen)
        if self.live != self.lives:
            pygame.draw.rect(screen, (0, 0, 0,), (self.x, self.y - 35, self.xr, 20 + 10))
            pygame.draw.rect(screen, (255 - 255 *(self.live/self.lives), 255*(self.live/self.lives), 0),
                         (self.x + 5, self.y - 30, (self.xr - 10) * (self.live / self.lives), 20))



# написать код который рисует шкалу


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
