import pygame
import sys
from bullet import Bullet
from alien import Alien


def events(screen, gun, bullets):
    """Обработка событий"""
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


def update(bg_color, screen, gun, aliens, bullets):
    """обновление экрана"""
    screen.fill(bg_color)  # заливка окна
    for bullet in bullets.sprites():
        bullet.drop_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()  # Последний экран


def update_bullets(bullets):
    """"Обновляет позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # Удаляем пули из контейнера


def update_aliens(aliens):
    """обновляет позицию инопланитян"""
    aliens.update()


def create_army(screen, aliens):
    """создание армии пришельцев"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            aliens.add(alien)
