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

font = pygame.font.Font('freesansbold.ttf', 14)

rotation_angle = 0
white, black = (240, 240, 240), (15, 15, 15)
hue = 0

n = 0
c = 20
cube_position = [width//2, height//2]
scale = 20
points = []
counter = False
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.points= [[x], [y], [1]]
        self.color = color

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def fibonnaci_numbers(r):
    fib_list = []
    i, j = 1, 1
    for _ in range(r):
        fib_list.append(i)
        i, j = j, i + j
    return fib_list

def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        return result_matrix
    else:
        print("error! the columns of the first matrix must be equal with the rows of the second matrix")
        return None

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

    rotation_z =[[cos(rotation_angle), -sin(rotation_angle), 0],
                     [sin(rotation_angle), cos(rotation_angle), 0 ],
                      [0, 0, 1]]
    if n < 700:
        # coloring type hsv2rgb(hue, 1, 1) for a rainbow pattern
        # hsv2rgb(angle/255, 1, 1) for a spiral rainbow pattern
        p = Point(int(x), int(y), hsv2rgb(angle/255, 1, 1))
        points.append(p)

    for point in points:
        rotated_2d = matrix_multiplication(rotation_z, point.points)

        distance = 20
        z = 1/(distance - rotated_2d[2][0])
        projection_matrix = [[z, 0, 0],
                             [0, z, 0]]
        projected2d = matrix_multiplication(projection_matrix, rotated_2d)
        x_pos = int(projected2d[0][0] * scale) + cube_position[0]
        y_pos = int(projected2d[1][0] * scale) + cube_position[1]
        pygame.draw.circle(screen, point.color, (x_pos, y_pos), 8)

    text = font.render(str(int(r)), True, white)
    textRect = text.get_rect()
    textRect.center = (50, 100)
    screen.blit(text, textRect)
    pygame.display.update()

    n += 1
    hue += 0.003
    rotation_angle += 0.01
pygame.quit()
