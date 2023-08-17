import pygame
import sys
from bullet import Bullet


def events(screen, gun, bullets):
    """Обработа событий"""
    for event in pygame.event.get():  # цикл для перебоки событитий
        if event.type == pygame.QUIT:  # Событие при нажатии на закрыть окно
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = True
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, gun, bullets ):
    """обновление экрана"""
    screen.fill(bg_color)  # заливка окна
    gun.output()
    pygame.display.flip()  # Последний экран