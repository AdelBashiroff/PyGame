import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, scannon):
        '''инициализация пули на позиции пушки'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 1, 12)
        self.color = (29, 235, 92)
        self.speed = 5
        self.rect.centerx = scannon.rect.centerx
        self.rect.top = scannon.rect.top
        self.y = float(self.rect.y)

    def update(self):
        '''полет пули'''
        self.y -= self.speed
        self.rect.y = self.y

    def paint(self):
        '''рисовка пули'''
        pygame.draw.rect(self.screen, self.color, self.rect)



