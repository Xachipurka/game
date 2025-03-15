import time
import pygame
speed = 100
ispeed = 100
spawn_delay = 5
class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xr = 100
        self.yr = 100
        self.color = (0, 0, 0)
        self.ac = True
        self.time1 = time.perf_counter()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.xr, self.yr))


    def update(self):
        time2 = time.perf_counter()
        self.y += (time2 - self.time1) * speed
        self.time1 = time2
        if self.y >= pygame.display.get_surface().get_size()[1]:
            self.ac = False
