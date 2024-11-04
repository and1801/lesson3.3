import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра тир')
icon = pygame.image.load('image/avatar vault boy chips.png')
pygame.display.set_icon(icon)

# Загрузка изображения цели
target_img = pygame.image.load('image/target.png')
target_width = 80
target_height = 80

# Начальные координаты и скорость цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = random.choice([-5, 5])
target_speed_y = random.choice([-5, 5])

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счетчик попаданий и уровень
hits = 0
level = 1
SPEED_INCREMENT = 1  # Увеличение скорости при повышении уровня
LEVEL_UP_HITS = 5  # Количество попаданий для повышения уровня

# Шрифт для отображения счетчика и уровня
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Перемещение цели на случайные координаты
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Увеличение счетчика попаданий
                hits += 1

                # Проверка на повышение уровня
                if hits % LEVEL_UP_HITS == 0:
                    level += 1
                    # Увеличение скорости
                    target_speed_x += SPEED_INCREMENT if target_speed_x > 0 else -SPEED_INCREMENT
                    target_speed_y += SPEED_INCREMENT if target_speed_y > 0 else -SPEED_INCREMENT
                    print(f"Level Up! Current level: {level}")

    # Обновление позиции цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на столкновение с границами экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    # Отображение цели на экране
    screen.blit(target_img, (target_x, target_y))

    # Отображение счетчика попаданий и уровня
    hit_text = font.render(f'Попадания: {hits}', True, (255, 255, 255))
    screen.blit(hit_text, (10, 10))

    level_text = font.render(f'Уровень: {level}', True, (255, 255, 255))
    screen.blit(level_text, (10, 50))

    pygame.display.update()
    clock.tick(60)  # Ограничение FPS

pygame.quit()