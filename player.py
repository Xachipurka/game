import pygame


class Player:
    def __init__(self):
        self.x = 100
        self.y = 1100
        self.xr = 50
        self.yr = 100
        self.l = 1
        self.screen = pygame.display.get_surface().get_size()
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.xr, self.yr))

    def left(self):
        if self.x > 0:
            self.x -= 5

    def right(self):
        if self.x < self.screen[0] - self.xr:
            self.x += 5
