import pygame
from echiquier import Echiquier
from point import Point


class Game:
    def __init__(self,screen):
        self.all_piece = pygame.sprite.Group()
        self.echiquier = Echiquier(screen,self)
        self.screen = screen
        self.piece_selectione = None
        self.couleur_joueur = None
        self.en_menu = True
        self.premouv = pygame.sprite.Group()

    def update(self):
        self.update_echiquier()
        for elem in self.premouv:
            self.screen.blit(elem.image, elem.rect)

        for elem in self.all_piece:
            self.screen.blit(elem.image,elem.rect)


    def update_echiquier(self):
        jeu = self.echiquier.jeu
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen,jeu[j][i].color,jeu[j][i].rect)

    def afficher_deplacement_possible(self):
        for elem in self.piece_selectione.coup:
            x, y = elem
            if self.echiquier.jeu[y][x].piece is None:
                point = Point(x,y,self.screen,'noir')
            else:
                point = Point(x, y, self.screen,'rouge')

            self.premouv.add(point)

    def enlever_premouv(self):
        self.premouv.empty()

    def changer_piece_selectionner(self,piece):
        self.piece_selectione = piece
        self.enlever_premouv()
        if not self.piece_selectione is None :
            self.afficher_deplacement_possible()
