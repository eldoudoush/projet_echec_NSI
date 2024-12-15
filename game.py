import pygame
from echiquier import Echiquier
from point import Point
from scene_droite import SceneDroite
from accueil import Accueil

class Game:
    def __init__(self,screen):
        self.all_piece = pygame.sprite.Group()
        self.echiquier = Echiquier(screen,self)
        self.screen = screen
        self.piece_selectione = None
        self.couleur_joueur = None
        self.en_menu = True
        self.premouv = pygame.sprite.Group()
        self.scene_droite = SceneDroite(screen)
        self.ecran_accueil = Accueil(self.screen)

    def update(self):
        if self.en_menu:
            self.screen.fill((167, 4, 159))
            # pygame.draw.rect(screen,(42, 206, 166),[0,0,screen.get_width(),screen.get_height()])
            self.screen.blit(self.ecran_accueil.texte_surface, self.ecran_accueil.texte_surface_rect)
            self.screen.blit(self.ecran_accueil.play_button, self.ecran_accueil.play_button_rect)
        else:
            self.screen.fill((0, 0, 0))
            self.update_echiquier()
            self.scene_droite.update()
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
