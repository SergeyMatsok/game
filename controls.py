import pygame
import sys


def events(gun):
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
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d:
                gun.mright = False
            # влево
            elif event.key == pygame.K_a:
                gun.mleft = False
