import pygame
from pion import Pion
from echiquier import Echiquier


class Game:
    def __init__(self,screen):
        self.all_piece = pygame.sprite.Group()
        self.echiquier = Echiquier(screen,self)
        self.screen = screen
        self.piece_selectione = None
        self.couleur_joueur = None

    def update(self):
        self.update_echiquier()


        for elem in self.all_piece:
            self.screen.blit(elem.image,elem.rect)

    def ajout_pion(self,x,y):
        pion = Pion(x,y,self.screen,'noir')
        self.echiquier.jeu[x][y].piece = pion
        self.all_piece.add(pion)

    def update_echiquier(self):
        jeu = self.echiquier.jeu
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen,jeu[j][i].color,jeu[j][i].rect)
