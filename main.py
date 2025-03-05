import random
import time
import pygame
from player import Player
from obsticle import Obsticle
from coin import Coin
from o import speed
import o

pygame.init()


screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
background_color = (255, 255, 255)  # Белый цвет

p = Player()
#o = Obsticle()
ob = [Obsticle(random.randrange(0, pygame.display.get_surface().get_size()[0]), 0) for i in range(10)]
co = []
coin = 0
font = pygame.font.Font(None, 40)
time_start = time.perf_counter()
running = True
while running:
    n = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for i in range(len(ob) - 1, -1, -1):
            ob[i].touch(event)
            if not ob[i].ac:
                xo = ob[i].x
                yo = ob[i].y
                del ob[i]
                #                if random.randrange(1, 4) == 3:
                co.append(Coin(xo, yo))


    keys = pygame.key.get_pressed()

    # Check for specific keys
    if keys[pygame.K_a]:
        p.left()
        # Add your logic for moving left here
    if keys[pygame.K_d]:
        p.right()
        # Add your logic for moving right here
    screen.fill((255, 255, 255))

    p.draw(screen)
    time_update = time.perf_counter()

    for i in range(len(co) - 1, -1, -1):
        co[i].draw(screen)
        if not co[i].col:
            del co[i]
            coin += 1
        elif not co[i].ac:
            del co[i]

    for i in range(len(co)):
        co[i].update(p)

    for i in range(len(ob)):
        ob[i].update(p)

    if time_update - time_start > o.time0:
        for _ in range(3):
            ob.append(Obsticle(random.randrange(0, pygame.display.get_surface().get_size()[0]), 0))
        time_start += o.time0
        o.speed += 250
        o.time0 *= 0.98

    if p.l <= 0:
        running = False

    for i in range(len(ob)):
        ob[i].draw(screen)



    text = font.render(f'coins: {coin}', True, (0, 0, 0))
    screen.blit(text, (20, 10))
    print(len(ob))
    pygame.display.flip()