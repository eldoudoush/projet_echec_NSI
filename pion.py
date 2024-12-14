import pygame




class Pion(pygame.sprite.Sprite):

    def __init__(self,x,y,screen):
        super().__init__()
        self.image = pygame.image.load('piece/pion.png')
        self.image = pygame.transform.scale(self.image, (screen.get_height()/8, screen.get_height()/8))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y