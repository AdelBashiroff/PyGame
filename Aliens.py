import pygame

class Ali(pygame.sprite.Sprite):
    '''класс, отвечающий за пришельцев на экране'''

    def __init__(self, screen):
        '''создание начальной позиции пришельцев'''
        super(Ali, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw(self):
        '''вывод пришельца на экран'''
        self.screen.blit(self.image, self.rect)


    def update(self):
        '''перемещение пришельцев'''
        self.y += 0.4
        self.rect.y = self.y





