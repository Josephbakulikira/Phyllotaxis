import pygame
import os
import colorsys
from math import sqrt, cos, sin

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920, 1080
size = (width, height)
pygame.init()
pygame.display.set_caption("Phyllotaxis")
screen = pygame.display.set_mode(size)
fps = 30
clock = pygame.time.Clock()


white, black = (240, 240, 240), (15, 15, 15)
hue = 0

n = 0
c = 18
points = []
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    angle = n * 137.5
    r = c * sqrt(n)

    x = r * cos(angle)
    y = r * sin(angle)

    p = Point(int(x) + width//2, int(y)+ height//2, hsv2rgb(hue, 1, 1))
    points.append(p)

    for point in points:
        pygame.draw.circle(screen, point.color, (point.x, point.y), 8)
    n += 1
    hue += 0.005
    pygame.display.update()
pygame.quit()
