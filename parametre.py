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
        self.icon_image,self.icon_rect = fct.import_image_resize('image_parametre/engrenage_parametre.png',self.screen_width//11,self.screen_width//11,14.5*self.screen_width//16,self.y//16)
        self.interface_image,self.interface_rect  = fct.import_image_resize('image_parametre/parametre_bg.png',6*self.screen_width//8,6*self.screen_height//8,self.screen_width//8,self.screen_height//8)
        self.choisir_couleur_noir_rect = [self.x*4 ,self.y*5 ,6*self.x/8,6*self.x/8]
        self.deriere_noir_rect = [self.x*4-self.x/16 ,self.y*5-self.x/16 ,7*self.x/8,7*self.x/8]
        self.choisir_couleur_blanc_rect = [self.x*5 ,self.y*5 ,6*self.x/8,6*self.x/8]
        self.deriere_blanc_rect = [self.x * 5 - self.x / 16, self.y * 5 - self.x / 16, 7 * self.x / 8, 7 * self.x / 8]
        self.redemarer_rect = [self.x *3/2 , self.y * 4.5 , 2 * self.x ,  self.x ]
        self.font = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.screen_width//30)
        self.redemarer_texte = self.font.render("retourner", True, (0, 0, 0))
        self.redemarer_textedessous = self.font.render("au menu", True, (0, 0, 0))
        self.appliquer_timer_rect = [self.x*5.25,self.y*3.6,self.x,self.y/2]
        self.font2 = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.screen_width//50)
        self.texte_appliquer,self.texte_appliquer_pos = self.font2.render("appliquer", True, (0, 0, 0)),(self.x*5.25,self.y*3.7)
        self.gestionnaire_de_boite_texte = fct.GestionnaireDeBoiteTexte()
        self.boitetexte_minute_blanc = fct.BoiteTexte(self.screen,'0123456789',2,[self.x*4,self.y*3,self.x/2,self.y/2],texte_originel=str(cst.timer_blanc//60))
        self.boitetexte_seconde_blanc = fct.BoiteTexte(self.screen,'0123456789',2,[self.x*4.6,self.y*3,self.x/2,self.y/2],texte_originel=('0' if cst.timer_blanc % 60 < 10 else '') +str(cst.timer_blanc % 60) )
        self.boitetexte_minute_noir = fct.BoiteTexte(self.screen, '0123456789', 2,[self.x * 5.4, self.y * 3, self.x / 2, self.y / 2],texte_originel=str(cst.timer_noir//60))
        self.boitetexte_seconde_noir = fct.BoiteTexte(self.screen, '0123456789', 2,[self.x * 6, self.y * 3, self.x / 2, self.y / 2],texte_originel=('0' if cst.timer_noir % 60 < 10 else '') +str(cst.timer_noir % 60))
        self.gestionnaire_de_boite_texte.append(self.boitetexte_seconde_blanc)
        self.gestionnaire_de_boite_texte.append(self.boitetexte_minute_blanc)
        self.gestionnaire_de_boite_texte.append(self.boitetexte_seconde_noir)
        self.gestionnaire_de_boite_texte.append(self.boitetexte_minute_noir)
        self.est_afficher = False



    def cliquer_parametre(self,pos):
        if self.icon_rect.collidepoint(pos) :
            self.est_afficher = not self.est_afficher
            self.boitetexte_minute_blanc.changer_texte( str(cst.timer_blanc // 60))
            self.boitetexte_seconde_blanc.changer_texte(('0' if cst.timer_blanc % 60 < 10 else '') +str(cst.timer_blanc % 60) )
            self.boitetexte_minute_noir.changer_texte( str(cst.timer_noir // 60))
            self.boitetexte_seconde_noir.changer_texte( ('0' if cst.timer_noir % 60 < 10 else '') +str(cst.timer_noir % 60) )
        if self.est_afficher :
            self.cliquer_couleur_choisie(pos)
            if not self.game.en_menu :
                if fct.clicker(self.redemarer_rect,pos) :
                    self.game.reset()
                    print('reset')
            else:
                self.gestionnaire_de_boite_texte.activer_boitetexte(pos)
                if fct.clicker(self.appliquer_timer_rect,pos):
                    cst.timer_blanc = int(self.boitetexte_seconde_blanc.texte)+int(self.boitetexte_minute_blanc.texte)*60
                    cst.timer_noir = int(self.boitetexte_seconde_noir.texte) + int(
                        self.boitetexte_minute_noir.texte) * 60
                    self.boitetexte_minute_blanc.changer_texte( str(cst.timer_blanc // 60))
                    self.boitetexte_seconde_blanc.changer_texte(('0' if cst.timer_blanc % 60 < 10 else '') +str(cst.timer_blanc % 60) )
                    self.boitetexte_minute_noir.changer_texte( str(cst.timer_noir // 60))
                    self.boitetexte_seconde_noir.changer_texte( ('0' if cst.timer_noir % 60 < 10 else '') +str(cst.timer_noir % 60) )
                    self.game.scene_droite.timer_blanc = cst.timer_blanc
                    self.game.scene_droite.timer_noir = cst.timer_noir


    def cliquer_couleur_choisie(self,pos):
        if self.game.en_menu :
            if fct.clicker(self.choisir_couleur_blanc_rect,pos) :
                self.game.couleur_bot = 'noir'
            elif fct.clicker(self.choisir_couleur_noir_rect,pos) :
                self.game.couleur_bot = 'blanc'

    def update(self):
        self.screen.blit(self.icon_image, self.icon_rect)
        if self.est_afficher :
            self.screen.blit(self.interface_image,self.interface_rect)
            if self.game.en_menu :
                if self.game.couleur_bot == 'noir':
                    pygame.draw.rect(self.screen, 'green', self.deriere_blanc_rect)
                else :
                    pygame.draw.rect(self.screen, 'green', self.deriere_noir_rect)
                pygame.draw.rect(self.screen,(0,0,0),self.choisir_couleur_noir_rect)

                pygame.draw.rect(self.screen, (255,255,255), self.choisir_couleur_blanc_rect)
                self.gestionnaire_de_boite_texte.uptdate()
                pygame.draw.rect(self.screen,'blue',self.appliquer_timer_rect,)
                self.screen.blit(self.texte_appliquer,self.texte_appliquer_pos)
            else:
                pygame.draw.rect(self.screen,(58,34,10), self.redemarer_rect)
                self.screen.blit(self.redemarer_texte,(self.redemarer_rect[0]+self.x/5, self.redemarer_rect[1]+self.x/5 ))
                self.screen.blit(self.redemarer_textedessous,
                                 (self.redemarer_rect[0] + self.x / 5, self.redemarer_rect[1] + self.x / 5 + 5 *self.redemarer_texte.get_rect()[3]/4))
