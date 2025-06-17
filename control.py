import pygame, sys
from bullet import Bullet
from Aliens import Ali
import time   #для создания задержки

def events(screen, scannon, bullets):
    '''обработка событий'''
    for event in pygame.event.get():                           # проверяем все действия пользователя
        if event.type == pygame.QUIT:                          # создаем условие закрытия окна
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:                     #проверка условия нажал ли пользователь на клавиатуру
            if event.key == pygame.K_RIGHT:                    #проверка нажал ли он на правую стрелку
                scannon.mright = True
            elif event.key == pygame.K_LEFT:                   #проверка нажал ли он на левую стрелку
                scannon.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, scannon)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:                       #проверка отпустил ли он клавишу
            if event.key == pygame.K_RIGHT:
                scannon.mright = False
            elif event.key == pygame.K_LEFT:
                scannon.mleft = False


def update_screen(bg_color, screen, stats, sc, scannon, aliens, bullets):
    '''обновление экрана'''
    screen.fill(bg_color)                                                         #устанавливаем фоновый цвет
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.paint()
    scannon.paint()                                            #отображаем пушку на экран
    aliens.draw(screen)
    pygame.display.flip()                                      #обновляем экран после каждого действия пользователя

def update_bullets(screen, stats, sc, aliens, bullets):
    '''обновление пуль'''
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 5 * len(aliens)
        sc.image_score()
        check_high_scores(stats, sc)
        sc.image_lifes()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


def create_army(screen, aliens):
    '''создание армии пришельцев'''
    alien = Ali(screen)
    alien_width = alien.rect.width
    alien_per_line = int((900 - 2 * alien_width) / alien_width)                 #высчитали количество пришельцев в одном ряду
    alien_height = alien.rect.height
    alien_per_y = int((600 - 100 - alien_height) / alien_height)                  #высчитали кол-во возможных рядов

    for row_number in range(alien_height - 45):
        for number_a in range(alien_per_line):                                            #цикл создания армии пришельцев
            alien = Ali(screen)
            alien.x = alien_width + (alien_width * number_a)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            aliens.add(alien)


def update_aliens(stats, scannon, sc, bullets, screen, aliens):                                 #передвижение пришельцев
    aliens.update()
    if pygame.sprite.spritecollideany(scannon, aliens):
        scannon_kill(stats, scannon, sc, bullets, screen, aliens)
    aliens_check(stats, scannon, sc, bullets, screen, aliens)


def scannon_kill(stats, scannon, sc,  bullets, screen, aliens):
    '''столкновение пушки и пришельца'''
    if stats.scannon_left > 0:
        stats.scannon_left -= 1
        sc.image_lifes()
        aliens.empty()
        bullets.empty()
        scannon.create_scannon()
        create_army(screen, aliens)
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def aliens_check(stats, scannon, sc, bullets, screen, aliens):
    '''пришел ли пришелец к цели'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            scannon_kill(stats, scannon, sc, bullets, screen, aliens)
            break

def check_high_scores(stats, sc):
    '''проверка рекорда'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
