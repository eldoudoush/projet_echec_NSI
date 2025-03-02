import pygame
from utilitaire.fonction_utile import import_image_resize

class Pion(pygame.sprite.Sprite):

    def __init__(self,x,y,screen,color,echiquier):
        super().__init__()
        self.piece = 'pion'
        self.peut_jouer = True
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height / 8
        self.color = color
        self.coup = []
        self.val = 10
        if color == 'blanc':
            image = 'pieces_echecs/pion_blanc.png'
        else:
            image = 'pieces_echecs/pion_noir.png'
        self.image,self.rect = import_image_resize(image,self.taille_case, self.taille_case,self.taille_case*x,self.taille_case*y)

        self.coordone = (x,y)
        self.premier_coup = True
        self.echiquier = echiquier
        self.visible = True

    def maj_position(self):
        """
        met a jour la position de la piece en fonction de la case où elle est
        """
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]

    def coup_possible(self,detect_echec=False):
        """
        :param detect_echec: bool
        met dans self.coup tout les coup possible de la piece avec un empechement d'echec si detect_echec = True
        tous sinon
        """
        self.coup.clear()
        x = self.coordone[0]
        y = self.coordone[1]
        if self.color == 'blanc':
            if self.premier_coup :
                for i in range(1,3):
                    if not self.echiquier.jeu[x][y - i].piece is None :
                        break
                    else :
                        ajoute_coup_pas_echec(self, (x,y - i), self.echiquier, roi=False,calcul=detect_echec)
            else:
                if out_of_board((x,y - 1)) and self.echiquier.jeu[x][y -1].piece is None:
                    ajoute_coup_pas_echec(self, (x, y-1), self.echiquier, roi=False,calcul=detect_echec)
            if out_of_board((x+1,y -1)) and not self.echiquier.jeu[x+1][y -1].piece is None and self.echiquier.jeu[x+1][y -1].piece.color != self.color :
                ajoute_coup_pas_echec(self, (x+1, y - 1), self.echiquier, roi=False,calcul=detect_echec)
            if out_of_board((x-1,y -1)) and not self.echiquier.jeu[x-1][y -1].piece is None and self.echiquier.jeu[x-1][y -1].piece.color != self.color:
                ajoute_coup_pas_echec(self, (x-1, y - 1), self.echiquier, roi=False,calcul=detect_echec)

        else :
            if self.premier_coup:
                for i in range(1,3):
                    if out_of_board((x,y + i)) and not self.echiquier.jeu[x][y + i].piece is None :
                        break
                    else :
                        ajoute_coup_pas_echec(self, (x,y + i), self.echiquier, roi=False,calcul=detect_echec)
            else:
                if out_of_board((x,y + 1)) and self.echiquier.jeu[x][y +1].piece is None:
                    ajoute_coup_pas_echec(self, (x, y+1), self.echiquier, roi=False,calcul=detect_echec)
            if out_of_board((x+1,y +1)) and not self.echiquier.jeu[x+1][y +1].piece is None and self.echiquier.jeu[x+1][y +1].piece.color != self.color :
                ajoute_coup_pas_echec(self, (x+1, y +1), self.echiquier, roi=False,calcul=detect_echec)
            if out_of_board((x-1,y +1)) and not self.echiquier.jeu[x-1][y +1].piece is None and self.echiquier.jeu[x-1][y +1].piece.color != self.color:
                ajoute_coup_pas_echec(self, (x-1, y +1), self.echiquier, roi=False,calcul=detect_echec)


    def promo_pion(self):
        x, y = self.coordone
        couleur = self.color
        truc=Reine(x,y,self.screen,couleur,self.echiquier)
        new_piece=truc
        if couleur == 'blanc' and y == 0:
            self.echiquier.game.all_piece.remove(self)
            self.echiquier.game.piece_blanc.remove(self)
            self.echiquier.game.all_piece.add(new_piece)
            self.echiquier.game.piece_blanc.append(new_piece)
            self.echiquier.jeu[x][y].piece = new_piece
        if couleur == 'noir' and y == 7:
            self.echiquier.game.all_piece.remove(self)
            self.echiquier.game.piece_noir.remove(self)
            self.echiquier.game.all_piece.add(new_piece)
            self.echiquier.game.piece_noir.append(new_piece)
            self.echiquier.jeu[x][y].piece = new_piece

class Cheval(pygame.sprite.Sprite):

    def __init__(self,x,y,screen,color,echiquier):
        super().__init__()
        self.piece = 'cheval'
        self.peut_jouer = True
        self.echiquier = echiquier
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height / 8
        self.color = color
        self.val = 30
        if color == 'blanc':
            self.image = pygame.image.load('pieces_echecs/cheval_blanc.png')
        else:
            self.image = pygame.image.load('pieces_echecs/cheval_noir.png')
        self.image = pygame.transform.scale(self.image, (self.taille_case, self.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.taille_case*x
        self.rect.y = self.taille_case*y
        self.coordone = (x,y)
        self.coup = []
        self.premier_coup = True
        self.visible = True

    def maj_position(self):
        """
        met a jour la position de la piece en fonction de la case où elle est
        """
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]

    def coup_possible(self,detect_echec = False):
        """
        :param detect_echec: bool
        met dans self.coup tout les coup possible de la piece avec un empechement d'echec si detect_echec = True
        tous sinon
                """
        self.coup.clear()
        x = self.coordone[0]
        y = self.coordone[1]
        for elem in [(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2),(x+2,y-1),(x+2,y+1),(x-2,y-1),(x-2,y+1)]:
            a,b = elem
            if out_of_board(elem) and self.echiquier.jeu[a][b].piece is None :
                ajoute_coup_pas_echec(self, (a,b), self.echiquier, roi=False,calcul=detect_echec)
            elif out_of_board(elem) and not self.echiquier.jeu[a][b].piece is None and self.echiquier.jeu[a][b].piece.color != self.color :
                ajoute_coup_pas_echec(self, (a,b), self.echiquier, roi=False,calcul=detect_echec)



class Fou(pygame.sprite.Sprite):

    def __init__(self,x,y, screen, color,echiquier):
        super().__init__()
        self.piece = 'fou'
        self.peut_jouer = True
        self.echiquier = echiquier
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height / 8
        self.color = color
        self.val = 30
        if color == 'blanc':
            self.image = pygame.image.load('pieces_echecs/fou_blanc.png')
        else:
            self.image = pygame.image.load('pieces_echecs/fou_noir.png')
        self.image = pygame.transform.scale(self.image, (self.taille_case, self.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.taille_case * x
        self.rect.y = self.taille_case * y
        self.coordone = (x, y)
        self.coup = []
        self.premier_coup = True
        self.visible = True

    def maj_position(self):
        """
        met a jour la position de la piece en fonction de la case où elle est
        """
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]

    def coup_possible(self,detect_echec = False):
        """
        :param detect_echec: bool
        met dans self.coup tout les coup possible de la piece avec un empechement d'echec si detect_echec = True
        tous sinon
        """
        self.coup.clear()
        x = self.coordone[0]
        y = self.coordone[1]
        for i in range(x+1, 8):
            if y + i - x > 7 or  y + i - x < 0 :
                break
            elif not self.echiquier.jeu[i][y + i - x].piece is None and self.echiquier.jeu[i][y + i - x].piece.visible :
                if  self.echiquier.jeu[i][y + i - x].piece.color == self.color :
                    break
                else:
                    ajoute_coup_pas_echec(self, (i, y + i - x), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else :
                ajoute_coup_pas_echec(self, (i, y + i - x), self.echiquier, roi=False,calcul=detect_echec)

        for i in range(x-1,-1,-1):
            if  y - i + x > 7 or  y - i + x < 0 :
                break
            elif not self.echiquier.jeu[i ][y-i+x].piece is None and self.echiquier.jeu[i][y-i+x].piece.visible:
                if self.echiquier.jeu[i ][y-i+x].piece.color == self.color :
                    break
                else:
                    ajoute_coup_pas_echec(self, (i, y - i + x), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (i, y - i + x), self.echiquier, roi=False,calcul=detect_echec)

        for i in range(y-1,-1,-1):
            if x - i + y > 7 or x - i + y < 0 :
                break
            elif not self.echiquier.jeu[x - i + y][i].piece is None and self.echiquier.jeu[x - i + y][i].piece.visible :
                if self.echiquier.jeu[x - i + y][i].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (x - i + y, i), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (x - i + y, i), self.echiquier, roi=False,calcul=detect_echec)

        for i in range(y-1,-1,-1):
            if x + i - y > 7 or x + i - y < 0  :
                break
            elif not self.echiquier.jeu[x + i - y][i].piece is None and self.echiquier.jeu[x + i - y][i].piece.visible:
                if self.echiquier.jeu[x + i - y][i].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (x + i - y, i), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (x + i - y, i), self.echiquier, roi=False,calcul=detect_echec)

        return self.coup


class Tour(pygame.sprite.Sprite):

    def __init__(self,x,y,screen,color,equichier):
        super().__init__()
        self.piece='tour'
        self.peut_jouer = True
        self.echiquier=equichier
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height / 8
        self.color = color
        self.val = 50
        if color == 'blanc':
            self.image = pygame.image.load('pieces_echecs/tour_blanc.png')
        else:
            self.image = pygame.image.load('pieces_echecs/tour_noir.png')
        self.image = pygame.transform.scale(self.image, (self.taille_case, self.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.taille_case*x
        self.rect.y = self.taille_case*y
        self.coordone = (x,y)
        self.coup = []
        self.premier_coup = True
        self.visible = True

    def maj_position(self):
        """
        met a jour la position de la piece en fonction de la case où elle est
        """
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]

    def coup_possible(self,detect_echec = False):
        """
        :param detect_echec: bool
        met dans self.coup tout les coup possible de la piece avec un empechement d'echec si detect_echec = True
        tous sinon
        """
        self.coup.clear()
        x = self.coordone[0]
        y = self.coordone[1]
        for i in range(x + 1, 8):
            if not self.echiquier.jeu[i][y].piece is None and self.echiquier.jeu[i][y].piece.visible :
                if self.echiquier.jeu[i][y].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (i,y), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (i,y), self.echiquier, roi=False,calcul=detect_echec)
        for i in range(x-1,-1,-1):
            if not self.echiquier.jeu[i][y].piece is None and self.echiquier.jeu[i][y].piece.visible:
                if self.echiquier.jeu[i][y].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (i,y), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (i,y), self.echiquier, roi=False,calcul=detect_echec)
        for i in range(y+1, 8):
            if not self.echiquier.jeu[x][i].piece is None and self.echiquier.jeu[x][i].piece.visible:
                if self.echiquier.jeu[x][i].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (x,i), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (x,i), self.echiquier, roi=False,calcul=detect_echec)

        for i in range(y-1,-1,-1):
            if not self.echiquier.jeu[x][i].piece is None and self.echiquier.jeu[x][i].piece.visible :
                if self.echiquier.jeu[x][i].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (x,i), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (x,i), self.echiquier, roi=False,calcul=detect_echec)
        return self.coup


class Reine(pygame.sprite.Sprite):

    def __init__(self,x,y,screen,color,echiquier):
        self.piece='dame'
        self.peut_jouer = True
        self.echiquier=echiquier
        self.val = 90
        super().__init__()
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height / 8
        self.color = color
        if color == 'blanc':
            self.image = pygame.image.load('pieces_echecs/reine_blanc.png')
        else:
            self.image = pygame.image.load('pieces_echecs/reine_noir.png')
        self.image = pygame.transform.scale(self.image, (self.taille_case, self.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.taille_case*x
        self.rect.y = self.taille_case*y
        self.coordone = (x,y)
        self.coup=[]
        self.premier_coup = True
        self.visible = True

    def maj_position(self):
        """
        met a jour la position de la piece en fonction de la case où elle est
        """
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]

    def coup_possible(self,detect_echec = False):
        """
        :param detect_echec: bool
        met dans self.coup tout les coup possible de la piece avec un empechement d'echec si detect_echec = True
        tous sinon
        """
        self.coup.clear()
        x = self.coordone[0]
        y = self.coordone[1]

        for i in range(x + 1, 8):
            if not self.echiquier.jeu[i][y].piece is None and self.echiquier.jeu[i][y].piece.visible:
                if self.echiquier.jeu[i][y].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (i, y), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (i, y), self.echiquier, roi=False,calcul=detect_echec)
        for i in range(x - 1, -1, -1):
            if not self.echiquier.jeu[i][y].piece is None and self.echiquier.jeu[i][y].piece.visible:
                if self.echiquier.jeu[i][y].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (i, y), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (i, y), self.echiquier, roi=False,calcul=detect_echec)
        for i in range(y + 1, 8):
            if not self.echiquier.jeu[x][i].piece is None and self.echiquier.jeu[x][i].piece.visible:
                if self.echiquier.jeu[x][i].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (x, i), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (x, i), self.echiquier, roi=False,calcul=detect_echec)

        for i in range(y - 1, -1, -1):
            if not self.echiquier.jeu[x][i].piece is None and self.echiquier.jeu[x][i].piece.visible:
                if self.echiquier.jeu[x][i].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (x, i), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (x, i), self.echiquier, roi=False,calcul=detect_echec)


        for i in range(x + 1, 8):
            if y + i - x > 7 or y + i - x < 0:
                break
            elif not self.echiquier.jeu[i][y + i - x].piece is None and self.echiquier.jeu[i][y + i - x].piece.visible:
                if self.echiquier.jeu[i][y + i - x].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (i, y + i - x), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (i, y + i - x), self.echiquier, roi=False,calcul=detect_echec)

        for i in range(x - 1, -1, -1):
            if y - i + x > 7 or y - i + x < 0:
                break
            elif not self.echiquier.jeu[i][y - i + x].piece is None and self.echiquier.jeu[i][y - i + x].piece.visible:
                if self.echiquier.jeu[i][y - i + x].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (i, y - i + x), self.echiquier, roi=False,calcul=detect_echec )
                    break
            else:
                ajoute_coup_pas_echec(self, (i, y - i + x), self.echiquier, roi=False,calcul=detect_echec)

        for i in range(y - 1, -1, -1):
            if x - i + y > 7 or x - i + y < 0:
                break
            elif not self.echiquier.jeu[x - i + y][i].piece is None and self.echiquier.jeu[x - i + y][i].piece.visible:
                if self.echiquier.jeu[x - i + y][i].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (x - i + y, i), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (x - i + y, i), self.echiquier, roi=False,calcul=detect_echec)

        for i in range(y - 1, -1, -1):
            if x + i - y > 7 or x + i - y < 0:
                break
            elif not self.echiquier.jeu[x + i - y][i].piece is None and self.echiquier.jeu[x + i - y][i].piece.visible:
                if self.echiquier.jeu[x + i - y][i].piece.color == self.color:
                    break
                else:
                    ajoute_coup_pas_echec(self, (x + i - y, i), self.echiquier, roi=False,calcul=detect_echec)
                    break
            else:
                ajoute_coup_pas_echec(self, (x + i - y, i), self.echiquier, roi=False,calcul=detect_echec)

        return self.coup

class Roi(pygame.sprite.Sprite):

    def __init__(self,x,y,screen,color,echiquier):
        super().__init__()
        self.screen = screen
        self.echiquier = echiquier
        self.piece = 'roi'
        self.peut_jouer = True
        self.val = 900
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height / 8
        self.color = color
        if color == 'blanc':
            self.image = pygame.image.load('pieces_echecs/roi_blanc.png')
        else:
            self.image = pygame.image.load('pieces_echecs/roi_noir.png')
        self.image = pygame.transform.scale(self.image, (self.taille_case, self.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.taille_case*x
        self.rect.y = self.taille_case*y
        self.coordone = (x,y)
        self.premier_coup = True
        self.coup = []
        self.visible = True
        self.rockD=False
        self.rockG=False
        self.echec = False

    def maj_position(self):
        """
                met a jour la position de la piece en fonction de la case où elle est
                """
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]

    def coup_possible(self,detect_echec = False):
        """
        :param detect_echec: bool
        met dans self.coup tout les coup possible de la piece avec un empechement d'echec si detect_echec = True
        tous sinon
                """
        self.coup.clear()
        x = self.coordone[0]
        y = self.coordone[1]
        for elem in [(x + 1, y), (x + 1,y+1), (x+ 1, y -1), (x - 1, y), (x - 1, y - 1), (x - 1, y + 1),
                     (x, y - 1), (x, y + 1)]:
            a, b = elem
            if self.color == 'blanc':
                if out_of_board(elem) and self.echiquier.jeu[a][b].piece is None :
                    ajoute_coup_pas_echec(self, elem, self.echiquier, roi=True ,calcul=detect_echec )

                elif out_of_board(elem) and not self.echiquier.jeu[a][b].piece is None and self.echiquier.jeu[a][
                    b].piece.color != self.color :
                    ajoute_coup_pas_echec(self, elem, self.echiquier, roi=True,calcul=detect_echec )

            else:
                if out_of_board(elem) and self.echiquier.jeu[a][b].piece is None :
                    ajoute_coup_pas_echec(self, elem, self.echiquier, roi=True ,calcul=detect_echec)

                elif out_of_board(elem) and not self.echiquier.jeu[a][b].piece is None and self.echiquier.jeu[a][
                    b].piece.color != self.color :
                    ajoute_coup_pas_echec(self, elem, self.echiquier, roi=True,calcul=detect_echec )

        if self.color == 'blanc':
            if self.premier_coup and self.echiquier.jeu[0][7].piece is not None :
                if self.echiquier.jeu[0][7].piece.piece == 'tour' and self.echiquier.jeu[0][7].piece.premier_coup==True:
                    if self.echiquier.jeu[1][7].piece is None and self.echiquier.jeu[2][7].piece is None and self.echiquier.jeu[3][7].piece is None:
                        ajoute_coup_pas_echec(self, (2, 7), self.echiquier, roi=True)
                        self.rockG=True
                    else:
                        self.rockG = False


            if self.premier_coup and self.echiquier.jeu[7][7].piece is not None :
                if self.echiquier.jeu[7][7].piece.piece=='tour' and self.echiquier.jeu[7][7].piece.premier_coup==True:
                    if self.echiquier.jeu[5][7].piece is None and self.echiquier.jeu[6][7].piece is None:
                        ajoute_coup_pas_echec(self, (6, 7), self.echiquier, roi=True)
                        self.rockD = True
                    else:
                        self.rockD=False
        else:
            if self.premier_coup and self.echiquier.jeu[0][0].piece is not None :
                if self.echiquier.jeu[0][0].piece.piece == 'tour' and self.echiquier.jeu[0][0].piece.premier_coup==True:
                    if self.echiquier.jeu[1][0].piece is None and self.echiquier.jeu[2][0].piece is None and self.echiquier.jeu[3][0].piece is None:
                        ajoute_coup_pas_echec(self, (2, 0), self.echiquier, roi=True)
                        self.rockG = True
                    else:
                        self.rockG = False

            if self.premier_coup and self.echiquier.jeu[7][0].piece is not None :
                if self.echiquier.jeu[7][0].piece.piece == 'tour' and self.echiquier.jeu[7][0].piece.premier_coup==True:
                    if self.echiquier.jeu[5][0].piece is None and self.echiquier.jeu[6][0].piece is None :
                        ajoute_coup_pas_echec(self, (6, 0), self.echiquier, roi=True)
                        self.rockD = True
                    else:
                        self.rockD=False
        return self.coup

def out_of_board(a):
    """
    :param a: tuple modelisant un coordone
    :return: True si a est dans l'echiquier False sinon
    """
    x,y = a
    return 0 <= x <= 7 and 0 <= y <= 7

class PieceImaginaire:
    def __init__(self):
        self.piece = 'ima'
        self.color = 'pas'
        self.visible = True

def ajoute_coup_pas_echec(piece,coordonne,echiquier,roi=False,calcul=True):
    """
    :param piece: piece de l'echiquier
    :param coordonne: tuple( coordonner ou il veut se rendre)
    :param echiquier: l'echiquier
    :param roi: bool
    :param calcul: bool
    rajoute le coup a piece.coup si calcul = False sinon regarde si le coup met en echec le roi de la piece
    si oui ne l'ajoute pas sinon l'ajoute
    """
    if not calcul :
        piece.coup.append(coordonne)
        return

    x,y = coordonne
    piece.visible = False
    pieceima = PieceImaginaire()
    couleur = None
    if echiquier.jeu[x][y].piece is None :
        echiquier.jeu[x][y].piece = pieceima
    else:
        couleur = echiquier.jeu[x][y].piece.color
        echiquier.jeu[x][y].piece.color = 'pas'
        echiquier.jeu[x][y].piece.peut_jouer = False

    if piece.color == 'blanc':
        co_roi = echiquier.game.roi_blanc.coordone
        L_coup = echiquier.game.calcul_coup_noir(roi_mouv=True,calcul=False)
    else:
        co_roi = echiquier.game.roi_noir.coordone
        L_coup = echiquier.game.calcul_coup_blanc(roi_mouv=True,calcul=False)
    if echiquier.jeu[x][y].piece.piece == 'ima' :
        echiquier.jeu[x][y].piece = None
    else:
        echiquier.jeu[x][y].piece.color = couleur
        echiquier.jeu[x][y].piece.peut_jouer = True
    del(pieceima)
    piece.visible = True

    if roi:
        if coordonne in L_coup:
            return
    elif  co_roi in L_coup:
        return

    piece.coup.append(coordonne)


