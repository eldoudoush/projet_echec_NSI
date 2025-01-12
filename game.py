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
        self.afficher_mat = False
        self.taille_case = self.screen.get_height() / 8

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
        if self.afficher_mat :
            self.afficher_echec_et_mat()

    def changer_couleur(self):
        if self.couleur_joueur == 'blanc':
            self.couleur_joueur = 'noir'
            self.coup_blanc = self.calcul_coup_blanc()
            self.coup_noir = self.calcul_coup_noir(True)
            self.check_mate(self.coup_noir)


        elif self.couleur_joueur == 'noir':
            self.couleur_joueur = 'blanc'
            self.coup_noir = self.calcul_coup_noir()
            self.coup_blanc = self.calcul_coup_blanc(True)
            self.check_mate(self.coup_blanc)

        else:
            print('probleme !!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        self.afficher_echec()
        self.enlever_echec()

        if self.couleur_joueur == 'noir':
            print('bot jou')
            #self.bot.calcule_coup_aleatoire()
            self.bot.calcule_meilleur_coup(self.couleur_joueur)

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
        x,y = self.piece_selectione.coordone
        point = Point(x, y, self.screen, 'selectione')
        self.premouv.add(point)

    def enlever_premouv(self):
        self.premouv.empty()

    def changer_piece_selectionner(self,piece):
        self.piece_selectione = piece
        self.enlever_premouv()
        if not self.piece_selectione is None :
            self.afficher_deplacement_possible()

    def calcul_coup_blanc(self,roi_mouv=False,calcul=True):
        l = []
        for elem in self.piece_blanc:
            if elem.piece != 'roi' and elem.peut_jouer:
                elem.coup_possible(detect_echec = calcul)
                l += elem.coup

            elif elem.piece == 'roi' and roi_mouv and elem.peut_jouer:
                elem.coup_possible(detect_echec = True)
        return set(l)

    def calcul_coup_noir(self,roi_mouv=False,calcul=True):
        l = []
        for elem in self.piece_noir:
            if elem.piece != 'roi' and elem.peut_jouer :
                elem.coup_possible(detect_echec = calcul)
                l += elem.coup
            elif elem.piece == 'roi' and roi_mouv and elem.peut_jouer :
                elem.coup_possible(detect_echec = True)
                l += elem.coup
        return set(l)


    def afficher_echec(self):
        if self.couleur_joueur == 'blanc' :
            if self.roi_blanc.coordone in self.coup_noir:
                self.roi_blanc.image = pygame.image.load('pieces_echecs/roi_rouge.png')
                self.roi_blanc.image = pygame.transform.scale(self.roi_blanc.image,(self.taille_case, self.taille_case))
                self.roi_blanc.echec = True
        else:
            if self.roi_noir.coordone in self.coup_blanc:
                self.roi_noir.image = pygame.image.load('pieces_echecs/roi_rouge.png')
                self.roi_noir.image = pygame.transform.scale(self.roi_noir.image,(self.taille_case, self.taille_case))
                self.roi_noir.echec = True

    def enlever_echec(self):
        if self.couleur_joueur == 'blanc':
            if self.roi_noir.echec:
                self.roi_noir.image = pygame.image.load('pieces_echecs/roi_noir.png')
                self.roi_noir.image = pygame.transform.scale(self.roi_noir.image, (self.taille_case, self.taille_case))
                self.roi_noir.echec = False
        else :
            if self.roi_blanc.echec:
                self.roi_blanc.image = pygame.image.load('pieces_echecs/roi_blanc.png')
                self.roi_blanc.image = pygame.transform.scale(self.roi_blanc.image, (self.taille_case, self.taille_case))
                self.roi_blanc.echec = False



    def check_mate(self,liste):
        if len(liste) == 0 :
            self.afficher_mat = True

    def afficher_echec_et_mat(self):
        if self.couleur_joueur == 'blanc':
            couleur_gagnant = 'noir'
        else:
            couleur_gagnant = 'blanc'
        font = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.screen.get_width() // 25)
        texte_surface = font.render("les "+couleur_gagnant+' ont gagne', True, self.rgb)
        texte_surface_rect = texte_surface.get_rect()
        texte_surface_rect.x = self.screen.get_width() / 5
        texte_surface_rect.y = self.screen.get_height() / 3
        self.screen.blit(texte_surface,texte_surface_rect)


    def reset(self):
        self.en_menu = True
        del self.echiquier
        del self.all_piece
        self.all_piece = pygame.sprite.Group()
        self.piece_noir.clear()
        self.piece_blanc.clear()
        self.echiquier = Echiquier(self.screen, self)
        self.couleur_joueur = 'blanc'
        self.afficher_mat = False
