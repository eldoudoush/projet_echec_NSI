import pygame
from echiquier import Echiquier
from point import Point
from scene_droite import SceneDroite
from accueil import Accueil
from bot import Bot

class Game:
    def __init__(self,screen):
        self.all_piece = pygame.sprite.Group()
        self.piece_blanc = []
        self.piece_noir = []
        self.roi_blanc = None
        self.roi_noir = None
        self.bot = Bot(self)
        self.echiquier = Echiquier(screen,self)
        self.screen = screen
        self.piece_selectione = None
        self.couleur_joueur = 'blanc'
        self.en_menu = True
        self.premouv = pygame.sprite.Group()
        self.scene_droite = SceneDroite(screen,self)
        self.ecran_accueil = Accueil(self.screen)
        self.rgb = (0,0,0)
        self.coup_noir = {}
        self.coup_blanc = {} 

    def update(self):
        if self.en_menu:
            self.screen.fill(self.rgb)
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

    def changer_couleur(self):
        if self.couleur_joueur == 'blanc':
            self.couleur_joueur = 'noir'
            self.coup_blanc = self.calcul_coup_blanc()
            self.coup_noir = self.calcul_coup_noir(True)
            self.check_mate(self.coup_noir)
            self.bot.calcule_coup_aleatoire()


        elif self.couleur_joueur == 'noir':
            self.couleur_joueur = 'blanc'
            self.coup_noir = self.calcul_coup_noir()
            self.coup_blanc = self.calcul_coup_blanc(True)
            self.check_mate(self.coup_blanc)


        else:
            print('quelque chose est arrivé')

    def update_echiquier(self):
        jeu = self.echiquier.jeu
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen,jeu[j][i].color,jeu[j][i].rect)

    def afficher_deplacement_possible(self):
        for elem in self.piece_selectione.coup:
            print(elem)
            x, y = elem
            if self.echiquier.jeu[x][y].piece is None:
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

    def calcul_coup_blanc(self,roi_mouv=False,calcul=True):
        L = []
        for elem in self.piece_blanc:
            if elem.piece != 'roi' and elem.peut_jouer:
                elem.coup_possible(detect_echec = calcul)
                L += elem.coup

            elif elem.piece == 'roi' and roi_mouv and elem.peut_jouer:
                elem.coup_possible(detect_echec = True)
        return set(L)

    def calcul_coup_noir(self,roi_mouv=False,calcul=True):
        L = []
        for elem in self.piece_noir:
            if elem.piece != 'roi' and elem.peut_jouer :
                elem.coup_possible(detect_echec = calcul)
                L += elem.coup
            elif elem.piece == 'roi' and roi_mouv and elem.peut_jouer :
                elem.coup_possible(detect_echec = True)
                L += elem.coup
        return set(L)

    def check_mate(self,liste):
        if len(liste) == 0 :
            self.en_menu = True
            del(self.echiquier)
            del(self.all_piece)
            self.all_piece = pygame.sprite.Group()
            self.piece_noir.clear()
            self.piece_blanc.clear()
            self.echiquier = Echiquier(self.screen, self)
            self.couleur_joueur = 'blanc'