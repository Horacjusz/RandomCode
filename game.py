import pygame

pygame.init()
# definiowanie okna gry
win = pygame.display.set_mode((1000, 500))
# wyświetlenie okna gry
pygame.display.set_caption("Moja Gra")

run = True
KOLOR = (255, 0, 0)
x = 10
y = 30
szer = 200
wys = 100
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    # pygame.draw(win,)
    # funkcja rysująca kwadrat
    pygame.draw.rect(win, KOLOR, (x, y, szer, wys))
    pygame.draw.circle(win, (128, 0, 128), (60, 200), 50, 40)
    # linia pozioma
    pygame.draw.line(win, (100,100,100), (60, 200), (250, 250), 5)
    # linia pionowa
    pygame.draw.line(win, (200,200,200), (210, 275), (210, 375), 5)
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('tekst dolny ', 1, (255, 255, 255))
    win.blit(label, (100, 425))
    
    # opóźnienie w grze
    pygame.time.delay(50)
    # obsługa zdarzeń 
    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    krok = 5
    if keys[pygame.K_LEFT] :
        x -= krok
    if keys[pygame.K_RIGHT] :
        x += krok
    if keys[pygame.K_UP] :
        y -= krok
    if keys[pygame.K_DOWN] :
        y += krok
    pygame.draw.rect(win, (0, 255, 0), (x, y, 10, 10))
    pygame.display.update()
    # odświeżenie ekranu 
    pygame.display.update()