import pygame
import sys
from gun import Gun


def run():

    pygame.init()  # Инициализируем модуль pygame
    screen = pygame.display.set_mode((1200, 800))  # Размер окна
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)  # цвет
    gun = Gun(screen)

    while True:   # Бесконечный цикл
        for event in pygame.event.get():  # цикл для перебоки событитий
            if event.type == pygame.QUIT:  # Событие при нажатии на закрыть окно
                sys.exit()

        screen.fill(bg_color)  # заливка окна
        gun.output()
        pygame.display.flip()  # Последний экран


run()
