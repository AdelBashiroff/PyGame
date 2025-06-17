import pygame
from pygame.sprite import Sprite

class SC(Sprite):
    def __init__(self, screen):
        '''инициализация пушки'''
        super(SC, self).__init__()
        self.screen = screen                                                         #получение экрана игры
        self.image = pygame.image.load('images2/pixil-frame-0-2.png')                   #загрузка png изображения пушки
        self.rect = self.image.get_rect()                                      #получение пушки в качестве прямоугольника
        self.screen_rect = self.screen.get_rect()                                    #получение экрана в качестве прямоугольника
        self.rect.centerx = self.screen_rect.centerx                           #расположение пушки по центру экрана
        self.center = float(self.rect.centerx)                                 #для более плавного передвижения пушки переводи число в float
        self.rect.bottom = self.screen_rect.bottom                             #расположение пушки вниз экрана
        self.mright = False
        self.mleft = False
    def paint(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)                                #вывод пушки на экран

    def update_cannon(self):
        '''обновление позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:           #условие чтобы пушка не выходила за границу
            self.center += 4.5
        elif self.mleft and self.rect.left > 0:                                #условие чтобы пушка не выходила за границу
            self.center -= 4.5

        self.rect.centerx = self.center

    def create_scannon(self):
        '''создание пушки после ее уничтожения'''
        self.center = self.screen_rect.centerx











