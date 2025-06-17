import pygame
import sys                                               #импортируем модуль для обработки событий и закрытия окна игры
import control                                           #импортируем управление пушкой
from scannon import SC                                   #импортируем class по созданию пушки на экране
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():                                               #создаем функцию запуска игры
    pygame.init()                                        #инициализируем игру
    FPS = 30                                             #настраиваем частоту кадров в секунду
    FramePerSec = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 600))         #устанавливаем размер окна игры
    pygame.display.set_caption('SPACE INVADERS')         #устанавливаем название для игры
    bg_color = (0, 0, 0)                                 #устанавливаем фоновый цвет по модели RGB, получается черный цвет
    scannon = SC(screen)
    bullets = Group()
    aliens = Group()
    control.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:                                          #создаем главный цикл игры
        control.events(screen, scannon, bullets)         #проверяем события пользователя
        if stats.run_game:
            scannon.update_cannon()                          #обновляем позицию пушки
            bullets.update()
            control.update_screen(bg_color, screen, stats, sc, scannon, aliens, bullets)  #функция обновления экрана
            control.update_bullets(screen, stats, sc, aliens, bullets)
            control.update_aliens(stats, scannon, sc, bullets, screen, aliens)



run()