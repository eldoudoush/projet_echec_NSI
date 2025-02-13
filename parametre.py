import pygame.draw

from utilitaire import fonction_utile as fct
from utilitaire import constante as cst

class Parametre:

    def __init__(self,game):
        self.screen = cst.screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.game = game
        self.x = self.screen_width/8
        self.y = self.screen_height/8
        self.icon_image,self.icon_rect = fct.import_image_resize('image_parametre/engrenage_parametre.png',self.screen_width/8,self.screen_width/8,7*self.screen_width/8,-self.y/4)
        self.interface_image,self.interface_rect  = fct.import_image_resize('image_parametre/parametre_bg.png',6*self.screen_width/8,6*self.screen_height/8,self.screen_width/8,self.screen_height/8)
        self.choisir_couleur_noir_rect = [self.x*4 ,self.y*5 ,6*self.x/8,6*self.x/8]
        self.deriere_noir_rect = [self.x*4-self.x/16 ,self.y*5-self.x/16 ,7*self.x/8,7*self.x/8]
        self.choisir_couleur_blanc_rect = [self.x*5 ,self.y*5 ,6*self.x/8,6*self.x/8]
        self.deriere_blanc_rect = [self.x * 5 - self.x / 16, self.y * 5 - self.x / 16, 7 * self.x / 8, 7 * self.x / 8]
        self.est_afficher = False



    def cliquer_parametre(self,pos):
        if self.icon_rect.collidepoint(pos) :
            self.est_afficher = not self.est_afficher
        if self.est_afficher :
            self.cliquer_couleur_choisie(pos)

    def cliquer_couleur_choisie(self,pos):
        if self.game.en_menu :
            if fct.clicker(self.choisir_couleur_blanc_rect,pos) :
                self.game.couleur_joueur = 'blanc'
            elif fct.clicker(self.choisir_couleur_noir_rect,pos) :
                self.game.couleur_joueur = 'noir'

    def update(self):
        self.screen.blit(self.icon_image, self.icon_rect)
        if self.est_afficher :
            self.screen.blit(self.interface_image,self.interface_rect)
            if self.game.en_menu :
                if self.game.couleur_joueur == 'noir':
                    pygame.draw.rect(self.screen, 'green', self.deriere_noir_rect)
                else :
                    pygame.draw.rect(self.screen, 'green', self.deriere_blanc_rect)
                pygame.draw.rect(self.screen,(0,0,0),self.choisir_couleur_noir_rect)

                pygame.draw.rect(self.screen, (255,255,255), self.choisir_couleur_blanc_rect)