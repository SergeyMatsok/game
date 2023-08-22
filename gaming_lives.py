import pygame
from pygame.sprite import Sprite


class Hart(Sprite):

    def __init__(self, screen):  # метод инициализации(Принимает сам графический объект)
        """инициализация игровых жизней"""
        super(Hart, self).__init__()  # При инициализации класса подтягиваем все при помощи метода super
        self.screen = screen    # Получаем экран
        self.image = pygame.image.load('images\w_hart.png')  # Загружаем изображение
        self.rect = self.image.get_rect()  # Получаем изображение как прямоугольник
        self.screen_rect = screen.get_rect()  # Получаем графический объект экрана как прямоугольник
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
