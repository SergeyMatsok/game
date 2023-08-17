import pygame
import controls
from gun import Gun


def run():

    pygame.init()  # Инициализируем модуль pygame
    screen = pygame.display.set_mode((700, 800))  # Размер окна
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)  # цвет
    gun = Gun(screen)

    while True:   # Бесконечный цикл
        controls.events(gun)
        gun.update_gun()  # обновляет позицию пушки
        screen.fill(bg_color)  # заливка окна
        gun.output()
        pygame.display.flip()  # Последний экран


run()
