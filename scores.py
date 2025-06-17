import pygame.font
from scannon import SC
from pygame.sprite import *
from Aliens import Ali

class Scores():
    '''вывод игровой статистики'''
    def __init__(self, screen, stats):
        '''инициализация подсчета очков'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (29, 235, 92)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_lifes()

    def image_score(self):
        '''преобразование счета в изображение'''
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 40
        self.score_rect.top = 20

    def show_score(self):
        '''вывод счета на экран'''
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lifes.draw(self.screen)

    def image_high_score(self):
        '''преобразование рекордного счета в изображение'''
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_lifes(self):
        '''кол-во жизней игрока'''
        self.lifes = Group()
        for life_num in range(self.stats.scannon_left):
            life = SC(self.screen)
            life.rect.x = self.screen_rect.right - 250 + life_num * life.rect.width
            life.rect.y = 20
            self.lifes.add(life)




