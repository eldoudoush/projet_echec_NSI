import pygame
import string
import utilitaire.constante as cst

class SceneDroite:

    def __init__(self,screen,game):

        self.game = game
        self.screen = screen
        self.screen_height = screen.get_height()
        self.origine = (self.screen_height,0)
        self.width = self.screen.get_width() - self.screen_height
        self.pos_blanc = (self.screen_height+((1/8)*self.width),self.screen_height/8)
        self.pos_noir = (self.screen_height+((5/8)*self.width),self.screen_height/8)
        self.timer_noir = cst.timer_noir
        self.timer_blanc = cst.timer_blanc
        self.timer_noir_minute = ''
        self.timer_blanc_minute = ''
        self.coup_joue_blanc = []
        self.piece_blanc_manger = AffichagePionManger(self.screen,'blanc')
        self.coup_joue_noir = []
        self.piece_noir_manger = AffichagePionManger(self.screen,'noir')
        self.font = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.width//14)
        self.all_texte = []

    def temp_timer_reduction(self):
        """

        """
        if self.game.timer_on :
            if self.game.couleur_joueur == 'noir':
                self.timer_noir -=1
                if self.timer_noir == 0 :
                    self.game.timer_on = False
                    self.game.afficher_mat = True
            else :
                self.timer_blanc -= 1
                if self.timer_blanc == 0 :
                    self.game.timer_on = False
                    self.game.afficher_mat = True


    def maj_temps_minute(self):
        self.timer_blanc_minute = str(self.timer_blanc//60)+':'+('0' if self.timer_blanc%60<10 else '') + str(self.timer_blanc%60)
        self.timer_noir_minute = str(self.timer_noir//60)+':'+('0' if self.timer_noir%60<10 else '') +str(self.timer_noir%60)

    def update(self):
        self.maj_temps_minute()
        text_blanc = self.timer_blanc_minute
        text_noir = self.timer_noir_minute
        self.screen.blit(self.font.render(text_blanc, True, (255,255,255)), self.pos_blanc)
        self.screen.blit(self.font.render(text_noir, True, (255, 255, 255)), self.pos_noir)
        self.piece_noir_manger.update()
        self.piece_blanc_manger.update()
        self.afficher_coup_texte()

    def reset_scene_droite(self):
        self.timer_noir = 30 * 60
        self.timer_blanc = 30 * 60
        self.coup_joue_blanc.clear()
        self.piece_blanc_manger.clear()
        self.coup_joue_noir.clear()
        self.piece_noir_manger.clear()
        self.all_texte.clear()

    def cree_texte(self,couleur):
        if couleur == 'blanc' :
            coup = self.coup_joue_blanc[-1]
        else :
            coup = self.coup_joue_noir[-1]
        print(self.coup_joue_noir)
        print(self.coup_joue_blanc)
        print(coup)
        texte = Texte(self.screen,coup,couleur)
        for elem in self.all_texte :
            if elem.couleur == couleur:
                elem.changer_position()
        self.all_texte.append(texte)

    def afficher_coup_texte(self):
        for elem in self.all_texte:
            if elem.pos_actuel < 12 :
                self.screen.blit(elem.texte_affichable[0],elem.texte_affichable[1])


class Texte:
    def __init__(self,screen,coup_jouer_ecrit,couleur):
        self.screen = screen
        self.screen_height = screen.get_height()
        self.origine = (self.screen_height, 0)
        self.width = self.screen.get_width() - self.screen_height
        self.pos_actuel = 0
        self.font = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.width//25)
        self.y = (self.pos_actuel+5) * self.screen_height / 25
        self.couleur = couleur
        if couleur == 'blanc' :
            self.x = self.screen_height + self.width/8
        else:
            self.x = self.screen_height + 5 * self.width / 8
        self.texte = self.creer_texte(coup_jouer_ecrit)
        self.texte_affichable = (self.font.render(self.texte, True, (255, 255, 255)), (self.x ,self.y))

    def creer_texte(self,coup):
        alphabet = string.ascii_lowercase
        texte = ''
        dic_Piece_anglais = {'p' : '','d' : 'Q','t' : 'R','r' : 'K','f' : 'B','c': 'C'}
        case = alphabet[coup[1][0]] + str(coup[1][1]+1)
        texte += dic_Piece_anglais[coup[0]] + case
        if len(coup) == 3:
            texte += 'x' + dic_Piece_anglais[coup[2]]
            print('gaming')
        return texte

    def changer_position(self):
        self.pos_actuel += 1
        self.y = (self.pos_actuel+5) * self.screen_height / 25
        self.texte_affichable = (self.font.render(self.texte, True, (255, 255, 255)), (self.x ,self.y) )



class AffichagePionManger:
    def __init__(self,screen,couleur):
        self.couleur = couleur
        self.screen = screen
        self.screen_height = screen.get_height()
        self.origine = (self.screen_height, 0)
        self.width = self.screen.get_width() - self.screen_height

        self.liste_piece_manger =[]
        self.dic_piece = {'pion':0,'cheval':0,'dame':0,'roi':0,'fou':0,'tour':0}
        self.dic_emplacement_piece = {'pion':self.pos(0,0),'cheval':self.pos(1,0),'dame':self.pos(2,0),'roi':self.pos(2,1),'fou':self.pos(0,1),'tour':self.pos(1,1)}
        self.dic_Piece_anglais = {'p' : 'P','d' : 'Q','t' : 'R','r' : 'K','f' : 'B','c': 'C'}
        self.dic_texte_piece = {'pion':None,'cheval':None,'dame':None,'roi':None,'fou':None,'tour':None}
        self.font_size =  self.width // 30
        self.font = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF',self.font_size)

    def creer_texte(self,piece):
        self.liste_piece_manger.append(piece)
        piece_nom = piece.piece
        self.dic_piece[piece_nom] += 1
        self.dic_texte_piece[piece_nom] = (self.font.render( str(self.dic_piece[piece_nom])+'x '+self.dic_Piece_anglais[piece_nom[0]], True, (255, 255, 255)), (self.dic_emplacement_piece[piece_nom]))
        print(self.dic_Piece_anglais[piece_nom[0]])

    def update(self):
        for elem in self.dic_texte_piece.values():
            if not elem is None :
                x,y = elem
                self.screen.blit(x,y)

    def pos(self,x,y):
        if self.couleur == 'blanc':
            x_return = self.screen_height + ((x / 8) * self.width) + 1 * self.width / 40
            y_return = (y+6) * self.screen_height / 8
        else:
            x_return = self.screen_height + (((x+5) / 8) * self.width)
            y_return =  (y+6) * self.screen_height / 8
        return (x_return,y_return)

    def clear(self):
        self.liste_piece_manger = []
        # self.dic_piece = {'pion': 0, 'cheval': 0, 'dame': 0, 'roi': 0, 'fou': 0, 'tour': 0}
        # self.dic_emplacement_piece = {'pion': self.pos(0, 0), 'cheval': self.pos(1, 0), 'dame': self.pos(2, 0),
        #                               'roi': self.pos(0, 1), 'fou': self.pos(1, 1), 'tour': self.pos(2, 1)}
        # self.dic_texte_piece = {'pion': None, 'cheval': None, 'dame': None, 'roi': None, 'fou': None, 'tour': None}
        self.__init__(self.screen ,self.couleur)
"""import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 20, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)"""