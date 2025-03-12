import pygame
import math
pygame.init()

width = 1300
height = 1300

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((width, height))

screen.fill(WHITE)

def f(x, p = 0, q = 0) :
    return math.sin(x**2)

start = -10
end = 10

zero = 0
if 0 >= start and 0 <= end :
    length = end - start
    zero = (-start / length) * width

POINT = (zero, height // 2)

pygame.draw.line(screen, BLACK, (POINT[0], 0), (POINT[0], height), 1)
pygame.draw.line(screen, BLACK, (0, POINT[1]), (width, POINT[1]), 1)

eps = 0.0001

def point_to_draw(point) :
    global start, end, eps, width
    mult = width / (abs(end - start))
    return ((point[0] * mult) + POINT[0], POINT[1] - (point[1] * mult))

def numerical(func = f) :
    global start, end, eps, width
    n = int(abs(end - start) / eps)
    
    prev_point = (start, func(start))
    prev_diff = None
    prev_integral = (None, 0)
    x = prev_point[0] + eps
    i = 0
    drawing = False
    counter = 0
    cum_sum = 0
    while i < n :
        if not drawing : print(x)
        point = (x, func(x))
        diff_point = (x, (point[1] - prev_point[1]) / (point[0] - prev_point[0]))
        integral_point = (x, ((prev_point[1] + point[1]) * (point[0] - prev_point[0]) / 2) + prev_integral[1])
        
        if drawing :
            pygame.draw.line(screen, RED, point_to_draw(prev_point), point_to_draw(point), 2)
            if prev_diff is not None :
                pygame.draw.line(screen, BLUE, point_to_draw(prev_diff), point_to_draw(diff_point), 2)
            if prev_integral[0] != None :
                pygame.draw.line(screen, GREEN, point_to_draw(prev_integral), point_to_draw(integral_point), 2)
                print(integral_point)
        if not drawing and abs(point[1]) <= eps :
            counter += 1
            cum_sum += integral_point[1]
        if not drawing and (i + 1 == n) :
            C = -(cum_sum) / counter
            if i + 1 == n : C = 0
            print(C)
            i = 0
            x = start + eps
            prev_point = (start, func(start))
            prev_diff = None
            prev_integral = (None, C)
            drawing = True
            
            continue
        
        i += 1
        x += eps
        prev_point = point
        prev_diff = diff_point
        prev_integral = integral_point
        
numerical(f)



pygame.display.flip()

running = True
    
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    
    