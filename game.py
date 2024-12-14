import pygame
from pion import Pion
from echiquier import Echiquier


class Game:
    def __init__(self,screen):
        self.all_piece = pygame.sprite.Group()
        self.echiquier = Echiquier(screen)
        self.screen = screen
        for i in range(8):
            self.ajout_pion(i,1)

    def update(self):
        self.update_echiquier()


        for elem in self.all_piece:
            self.screen.blit(elem.image,elem.rect)

    def ajout_pion(self,x,y):
        pion = Pion(x,y,self.screen)
        self.echiquier.jeu[x][y].piece = pion
        self.all_piece.add(pion)

    def update_echiquier(self):
        jeu = self.echiquier.jeu
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen,jeu[j][i].color,jeu[j][i].rect)
