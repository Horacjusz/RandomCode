import random
import time

# Ustawienia gry
board_width = 20
board_height = 10
player_x = 10
player_y = 9
enemy_x = random.randint(0, board_width - 1)
enemy_y = 0
score = 0
game_over = False

# Główna pętla gry
while not game_over:
    # Czyszczenie planszy
    board = []
    for y in range(board_height):
        board.append([' '] * board_width)

    # Ustawienie gracza i przeciwnika
    board[player_y][player_x] = 'X'
    board[enemy_y][enemy_x] = 'O'

    # Wyświetlenie planszy
    print('\nSCORE:', score)
    print('-' * (board_width + 2))
    for row in board:
        print('|' + ''.join(row) + '|')
    print('-' * (board_width + 2))

    # Przemieszczenie przeciwnika w dół
    enemy_y += 1

    # Sprawdzenie kolizji z przeciwnikiem
    if enemy_x == player_x and enemy_y == player_y:
        game_over = True

    # Sprawdzenie, czy przeciwnik dotarł do końca planszy
    if enemy_y == board_height:
        enemy_x = random.randint(0, board_width - 1)
        enemy_y = 0
        score += 1
        time.sleep(0.5)

    # Odczytanie ruchu gracza
    move = input('Move (a/d): ')

    # Przemieszczenie gracza w lewo lub prawo
    if move == 'a' and player_x > 0:
        player_x -= 1
    elif move == 'd' and player_x < board_width - 1:
        player_x += 1

    # Czekanie na kolejny klatkę gry
    time.sleep(0.1)

# Wyświetlenie wyniku końcowego
print('\nGAME OVER')
print('SCORE:', score)