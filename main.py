import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats_life import Stats


def run():

    pygame.init()  # Инициализируем модуль pygame
    screen = pygame.display.set_mode((700, 800))  # Размер окна
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)  # цвет
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()

    while True:   # Бесконечный цикл
        controls.events(screen, gun, bullets)
        gun.update_gun()  # обновляет позицию пушки
        bullets.update()  # помещаем пульки на экран
        controls.update(bg_color, screen, gun, aliens, bullets)
        controls.update_bullets(aliens, bullets)
        controls.update_aliens(stats, screen, gun, aliens, bullets)


run()
