import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats_life import Stats
from score import Scores


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
    sc = Scores(screen, stats)

    while True:   # Бесконечный цикл
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()  # обновляет позицию пушки
            bullets.update()  # помещаем пульки на экран
            controls.update(bg_color, screen, stats, sc, gun, aliens, bullets)
            controls.update_bullets(screen, stats, sc, aliens, bullets)
            controls.update_aliens(stats, screen, sc, gun, aliens, bullets)


run()
