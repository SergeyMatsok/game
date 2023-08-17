import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Создаем пулю в текущей позиции пушки"""
        super(Bullet, self).__init__()  # позволяет наследовать базовые классы
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)  # размер пули(0, 0 - координаты 2, 12 размер)
        self.color = 237, 28, 35  # цвет пули
        self.speed = 1
        self.rect.centerx = gun.rect.centerx  # определяем верх пушки
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def drop_bullet(self):
        """рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)