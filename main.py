import pygame
import controls
from gun import Gun
from pygame.sprite import Group


def run():

    pygame.init()  # Инициализируем модуль pygame
    screen = pygame.display.set_mode((700, 800))  # Размер окна
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)  # цвет
    gun = Gun(screen)
    bullets = Group()

    while True:   # Бесконечный цикл
        controls.events(gun)
        gun.update_gun()  # обновляет позицию пушки
        bullets.update()  # помещаем пульки на экран
        controls.update(bg_color, screen, gun)


run()
