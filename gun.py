import pygame


class Gun():

    def __init__(self, screen):  # метод инициализации(Принимает сам графический объект)
        """инициализация пушки"""

        self.screen = screen    # Получаем экран
        self.image = pygame.image.load('images/gun_image_1.png')  # Загружаем изображение
        self.rect = self.image.get_rect()  # Получаем изображение как прямоугольник
        self.screen_rect = screen.get_rect()  # Получаем графический объект экрана как прямоугольник
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """Отрисовка пушки"""
        self.screen.blit(self.image, self.rect)
