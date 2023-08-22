import pygame
from pygame.sprite import Sprite


class Gun(Sprite):

    def __init__(self, screen):  # метод инициализации(Принимает сам графический объект)
        """инициализация пушки"""
        super(Gun, self).__init__()  # При инициализации класса подтягиваем все при помощи метода super
        self.screen = screen    # Получаем экран
        self.image = pygame.image.load('images/gun_image_1.png')  # Загружаем изображение
        self.rect = self.image.get_rect()  # Получаем изображение как прямоугольник
        self.screen_rect = screen.get_rect()  # Получаем графический объект экрана как прямоугольник
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """Отрисовка пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """Обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        """размещает пушку в нижнем центре экрана"""
        self.center = self.screen_rect.centerx
