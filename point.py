import pygame

class Point(pygame.sprite.Sprite):

    def __init__(self,x,y,screen,couleur):
        super().__init__()
        self.screen = screen
        self.screen_height = self.screen.get_height()
        self.taille_case = self.screen_height / 8
        if couleur == 'noir':
            self.image = pygame.image.load('pieces_echecs/point_noir.png')
        else:
            self.image = pygame.image.load('pieces_echecs/point_rouge.png')
        self.image = pygame.transform.scale(self.image, (self.taille_case, self.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = x*self.taille_case
        self.rect.y = y*self.taille_case
