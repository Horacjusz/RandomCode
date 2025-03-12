import pygame
import pymunk
import numpy as np
import random
import math

# Inicjalizacja Pygame
pygame.init()

# Ustawienia symulacji
size = 300  # Rozmiar planszy
radius = 2  # Promień punktów
velocity = 500  # Prędkość punktów
time_density = 10  # Ilość punktów na sekundę
display_size = size + 20
start = (display_size - size) / 2
end = display_size - start

center = (display_size // 2, display_size // 2)

density = 10

V = velocity

# Ustawienia okna
screen = pygame.display.set_mode((display_size, display_size))
pygame.display.set_caption("Symulacja punktów")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ustawienia fizyki
space = pymunk.Space()
space.gravity = (0, 0)

def add_circle(space, position, radius, velocity):
    body = pymunk.Body(1, float('inf'))
    body.position = position

    angle = random.uniform(0, 2 * math.pi)
    # angle = 0
    vel_x = velocity * math.cos(angle)
    vel_y = velocity * math.sin(angle)
    body.velocity = (vel_x, vel_y)

    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1.0
    shape.collision_type = 1  # Ustawienie typu kolizji
    shape.filter = pymunk.ShapeFilter(group=1)  # Usunięcie kolizji między kulkami

    space.add(body, shape)
    return shape

# Główna pętla
clock = pygame.time.Clock()
running = True
time_elapsed = 0

def inside(pos):
    if (start <= pos[0] < end) and (start <= pos[1] < end):
        return True
    return False

def distance(point_a, point_b=center):
    return np.sqrt(((point_a[0] - point_b[0]) ** 2) + ((point_a[1] - point_b[1]) ** 2))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    
    dt = clock.tick(60) / 1000.0
    time_elapsed += dt
    
    # Dodawanie nowych punktów zgodnie z time_density
    if time_elapsed >= 1.0 / time_density:
        time_elapsed = 0
        add_circle(space, center, radius, velocity)
    
    # Aktualizacja fizyki
    space.step(dt)
    
    # Rysowanie punktów
    for shape in space.shapes:
        pos = int(shape.body.position.x), int(shape.body.position.y)
        if not inside(pos):
            space.remove(shape)
            space.remove(shape.body)
            continue
        
        r1 = distance(pos, center)
        r2 = np.sqrt((density / np.pi) + (r1 ** 2))
        
        full = distance((0,0), shape.body.velocity)
        x = shape.body.velocity[0] / full
        y = shape.body.velocity[1] / full
        shape.body.velocity = x * V / r1, y * V / r1
        
        pygame.draw.circle(screen, RED, pos, radius)
    
    pygame.draw.line(screen, 'blue', (start, start), (start, end), 1)
    pygame.draw.line(screen, 'blue', (start, end), (end, end), 1)
    pygame.draw.line(screen, 'blue', (end, end), (end, start), 1)
    pygame.draw.line(screen, 'blue', (end, start), (start, start), 1)

    pygame.display.flip()

pygame.quit()
