from time import sleep

import pygame
from echiquier import Echiquier
from point import Point
from scene_droite import SceneDroite
from accueil import Accueil
from bot import Bot
from parametre import Parametre

class Game:
    def __init__(self,screen):
        self.all_piece = pygame.sprite.Group() #stock toute les pieces
        self.piece_blanc = [] #stock toute les pieces blanches
        self.piece_noir = [] #stock toute les pieces noires
        self.roi_blanc = None #stock le roi blanc
        self.roi_noir = None #stock le roi noir
        self.bot = Bot(self) #crée une class bot
        self.echiquier = Echiquier(screen,self) # crée l'échiquier
        self.screen = screen #récupère le screen
        self.piece_selectione = None #stock la piece selectioné
        self.couleur_joueur = 'blanc' #stock la couleur du joueur actuelle
        self.en_menu = True #variable pour savoir l'état du jeu : menu / en partie
        self.premouv = pygame.sprite.Group() #stock tous les mouvements possibles de la piece selectionner à afficher sur le moment
        self.scene_droite = SceneDroite(screen,self) #crée l'affichage à droite du jeu
        self.ecran_accueil = Accueil(self.screen) #crée l'écran d'acceuil
        self.rgb = (100,150,50) #stock la couleur du fond d'écran pour le menu
        self.coup_noir = {} #stock tous les coups disponibles pour les noirs
        self.coup_blanc = {} #stock tous les coups disponibles pour les blancs
        self.afficher_mat = False #variable qui gère l'échec et mat
        self.taille_case = self.screen.get_height() / 8 #variable de la taille des case
        self.timer_on = False #permet de stopper les timer si True
        self.select_bot = None #permet se savoir quel bot lancer devient alors un int
        self.bouton_restart = None #stock le bouton restart qui apparait à la fin de la partie
        self.bouton_restart_rect = None #stock le rectangle bouton restart qui apparait à la fin de la partie
        self.parametre = Parametre(self) #crée les paramètres du jeu
        self.couleur_bot = 'noir' #gère la couleur du bot
        self.draw = False #gère l'égalité

    def update(self):
        """
        :return: crée l'image à afficher celon l'état du jeu
        """
        if self.en_menu :
            self.screen.fill(self.rgb)
            # pygame.draw.rect(screen,(42, 206, 166),[0,0,screen.get_width(),screen.get_height()])
            self.ecran_accueil.update()
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
        self.parametre.update()

    def changer_couleur(self):
        """
        change la couleur du joueur qui joue et fait jouer le bot
        """
        if self.couleur_joueur == 'blanc':
            self.couleur_joueur = 'noir'
            self.coup_blanc = self.calcul_coup_blanc()
            self.coup_noir = self.calcul_coup_noir(True)
            self.check_mate(self.coup_noir)


        elif self.couleur_joueur == 'noir':
            self.couleur_joueur = 'blanc'
            self.coup_noir = self.calcul_coup_noir()
            self.coup_blanc = self.calcul_coup_blanc()
            self.check_mate(self.coup_blanc)

        else:
            print('probleme couleur !!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        self.afficher_echec()
        self.enlever_echec()

        if self.couleur_joueur == self.couleur_bot:
            if self.select_bot is None:
                return
            elif self.select_bot == 1 :
                self.bot.calcule_coup_aleatoire()
            elif self.select_bot == 2:
                print(self.bot.calcule_meilleur_coup(self.couleur_joueur))
            elif self.select_bot == 3 :
                #self.bot.coup_joue_min_max( 3, self.couleur_joueur)
                print(self.bot.jouer_min_max(3,True,self.couleur_joueur))


    def update_echiquier(self):
        """
        :return: affiche toute les cases de l'echiquier
        """
        jeu = self.echiquier.jeu
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(self.screen,jeu[j][i].color,jeu[j][i].rect)

    def afficher_deplacement_possible(self):
        """
        :return: affiche tout les delacement possible d'une piece calculer au préalable
        """
        for elem in self.piece_selectione.coup:
            # print(elem)
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
        """
        :return: enlève tout les affichage charcher
        """
        self.premouv.empty()

    def changer_piece_selectionner(self,piece):
        """
        :param piece: piece de l'echiquier ou None
        :return: met la piece en piece selectionner et affiche les coup de celle-ci
        """
        self.piece_selectione = piece
        self.enlever_premouv()
        if not self.piece_selectione is None :
            self.afficher_deplacement_possible()

    def calcul_coup_blanc(self,roi_mouv=True,calcul=True):
        """
        :param roi_mouv: bool
        :param calcul: bool
        :return: calcule les coup de toute les pieces blanches si calcul est True
                 alors il verifie que les coup ne mette pas le roi en echec
                 la fonction renvoie un set de tout les coups
        """
        l = []
        for elem in self.piece_blanc:
            if elem.piece != 'roi' and elem.peut_jouer:
                elem.coup_possible(detect_echec = calcul)
                l += elem.coup

            elif elem.piece == 'roi' and roi_mouv and elem.peut_jouer:
                elem.coup_possible(detect_echec = calcul)
                l += elem.coup

        return set(l)

    def calcul_coup_noir(self,roi_mouv=True,calcul=True):
        """
            :param roi_mouv: bool
            :param calcul: bool
            :return: calcule les coup de toute les pieces noires si calcul est True
                     alors il verifie que les coup ne mette pas le roi en echec
                     la fonction renvoie un set de tout les coups
        """
        l = []
        for elem in self.piece_noir:
            if elem.piece != 'roi' and elem.peut_jouer :
                elem.coup_possible(detect_echec = calcul)
                l += elem.coup
            elif elem.piece == 'roi' and roi_mouv and elem.peut_jouer :
                elem.coup_possible(detect_echec = calcul)
                l += elem.coup
        return set(l)


    def afficher_echec(self):
        """
        :return: rend le roi du joueur actuelle rouge
        """
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
        """
        :return:  rend au roi de l'adversaire du joueur actuelle sa couleur original
        """
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
        """
        :param liste: list des coups d'un joueur
        :return: si aucun coup est possible self.afficher_mat = True et le timer s'arrete
        """
        if len(liste) == 0 :
            if self.couleur_joueur == 'blanc':
                if not self.roi_blanc.coordone in self.coup_noir:
                    self.draw = True
            else:
                if not self.roi_noir.coordone in self.coup_blanc:
                    self.draw = True
            self.afficher_mat = True
            self.timer_on = False

    def afficher_echec_et_mat(self):
        """
        affiche un texte qui dit le gagnent et affiche un boutton qui si cliquer renvoie au menu
        """
        if self.couleur_joueur == 'blanc':
            couleur_gagnant = 'noir'
        else:
            couleur_gagnant = 'blanc'
        if self.draw :
            mot_afficher = '  il y a egalite'
        else:
            mot_afficher = "les "+couleur_gagnant+" ont gagne"
        font = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.screen.get_width() // 25)
        texte_surface = font.render(mot_afficher, True, self.rgb)
        texte_surface_rect = texte_surface.get_rect()
        texte_surface_rect.x = self.screen.get_width() / 5
        texte_surface_rect.y = self.screen.get_height() / 3


        play_button0 = pygame.image.load('pieces_echecs/bouton_vierge.png')
        play_button0 = pygame.transform.scale(play_button0, (self.screen.get_width() / 3, self.screen.get_height() / 6))
        play_button0_rect = play_button0.get_rect()
        play_button0_rect[0] = self.screen.get_width() / 4
        play_button0_rect[1] = 3 * self.screen.get_height() / 5


        font1 = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.screen.get_width() // 40)

        texte1_surface = font1.render("retour au menu", True, (0, 0, 0))
        texte1_surface_rect = texte1_surface.get_rect()
        texte1_surface_rect.x = 1.15 * self.screen.get_width() / 4
        texte1_surface_rect.y = 2 * self.screen.get_height() / 3

        self.bouton_restart_rect = play_button0_rect
        self.bouton_restart = play_button0
        self.screen.blit(texte_surface, texte_surface_rect)
        self.screen.blit(play_button0, play_button0_rect)
        self.screen.blit(texte1_surface, texte1_surface_rect)


    def reset(self):
        """
        remet permet de remettre à zero le jeu
        """
        del self.echiquier
        del self.all_piece
        self.all_piece = pygame.sprite.Group()
        self.piece_noir.clear()
        self.piece_blanc.clear()
        self.roi_blanc = None
        self.roi_noir = None
        self.echiquier = Echiquier(self.screen, self)
        self.couleur_joueur = 'blanc'
        self.afficher_mat = False
        self.piece_selectione = None
        self.couleur_joueur = 'blanc'
        self.premouv = pygame.sprite.Group()
        self.coup_noir.clear()
        self.coup_blanc.clear()
        self.afficher_mat = False
        self.timer_on = False
        self.select_bot = None
        self.parametre.est_afficher = False
        self.scene_droite.reset_scene_droite()
        self.en_menu = True


    def choix_mode_jeu(self,var):
        """
        :param var: int
        lance le mode de jeu attribuet a var
        """
        self.select_bot = var
        print('je suis une var : ',var)
        self.en_menu = False
        self.timer_on = True
        self.calcul_coup_blanc()

        if self.couleur_bot == 'blanc' :
            if self.select_bot is None:
                return
            elif self.select_bot == 1:
                self.bot.calcule_coup_aleatoire()
            elif self.select_bot == 2:
                print(self.bot.calcule_meilleur_coup(self.couleur_joueur))
            elif self.select_bot == 3:
                # self.bot.coup_joue_min_max( 3, self.couleur_joueur)
                print(self.bot.jouer_min_max(3, True, self.couleur_joueur))
