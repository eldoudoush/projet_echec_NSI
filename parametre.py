from utilitaire import fonction_utile as fct
from utilitaire import constante as cst

class Parametre:

    def __init__(self,game):
        self.screen = cst.screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.game = game
        self.icon_image,self.icon_rect = fct.import_image_resize('image_parametre/engrenage_parametre.png',self.screen_width/8,self.screen_width/8,7*self.screen_width/8,0)
        self.interface_image,self.interface_rect  = fct.import_image_resize('image_parametre/parametre_bg.png',6*self.screen_width/8,6*self.screen_height/8,self.screen_width/8,self.screen_height/8)
        # self.choisir_couleur_noir_rect = [x,y,size_x,size_y]
        # self.choisir_couleur_blanc_rect = [x,y,size_x,size_y]
        self.est_afficher = True



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