import pygame
import fonction_utile as fct

class Parametre:

    def __init__(self,screen,game):
        self.screen = screen
        self.game = game
        self.icon_image,self.icon_rect = fct.import_image_resize(...)
        self.interface_image,self.interface_rect  = fct.import_image_resize(...)
        self.choisir_couleur_noir_rect = [x,y,size_x,size_y]
        self.choisir_couleur_blanc_rect = [x,y,size_x,size_y]
        self.est_afficher = False



    def cliquer_parametre(self,pos):
        if self.icon_rect.collidepoint(pos) :
            self.est_afficher = not self.est_afficher

    def cliquer_couleur_choisie(self,pos):
        if fct.clicker(self.choisir_couleur_blanc_rect,pos) :
            self.game.couleur_joueur = 'blanc'
        elif fct.clicker(self.choisir_couleur_noir_rect,pos) :
            self.game.couleur_joueur = 'noir'

    def update(self):
        self.screen.blit(self.icon_image, self.icon_rect)
        if self.est_afficher :
            self.screen.blit(self.interface_image,self.interface_rect)