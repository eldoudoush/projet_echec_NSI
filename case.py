

class Case:
    def __init__(self,x,y,screen,echiquier):
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height/8
        self.coordone = (x, y)
        self.piece = None
        self.echiquier = echiquier

        self.rect = [self.taille_case*x,self.taille_case*y,self.taille_case,self.taille_case]


        if sum(self.coordone)%2 == 0:
            self.color = (255,255,255)
        else:
            self.color = (93, 190, 37)

    def changer_pion(self,piece,pas_suprimer=False):
        """
        :param piece: piece
        :param pas_suprimer: bool
        :return:
        """
        self.piece = piece
        self.echiquier.jeu[piece.coordone[0]][piece.coordone[1]].piece = None
        piece.coordone = self.coordone
        piece.maj_position()

        if not pas_suprimer:
            if self.piece.color == 'blanc':

                self.echiquier.game.scene_droite.coup_joue_blanc.append((piece.piece[0],piece.coordone))
                self.echiquier.game.scene_droite.cree_texte(piece.color)
            else:
                self.echiquier.game.scene_droite.coup_joue_noir.append((piece.piece[0],piece.coordone))
                self.echiquier.game.scene_droite.cree_texte(piece.color)
        if not self.piece is None and self.piece.piece == 'pion':
            self.piece.premier_coup = False

    def manger_pion(self, piece ,pas_suprimer=False):
        if self.piece.color == 'blanc':
            if not pas_suprimer:
                self.echiquier.game.scene_droite.piece_noir_manger.creer_texte(self.piece)

                self.echiquier.game.scene_droite.coup_joue_blanc.append((piece.piece[0],piece.coordone,self.piece.piece[0]))
                self.echiquier.game.scene_droite.cree_texte(piece.color)

            self.echiquier.game.piece_blanc.remove(self.piece)
        else:
            if not pas_suprimer:
                self.echiquier.game.scene_droite.piece_blanc_manger.creer_texte(self.piece)

                self.echiquier.game.scene_droite.coup_joue_noir.append((piece.piece[0],piece.coordone,self.piece.piece[0]))
                self.echiquier.game.scene_droite.cree_texte(piece.color)

            self.echiquier.game.piece_noir.remove(self.piece)
        if not pas_suprimer :
            self.echiquier.game.all_piece.remove(self.piece)
        self.piece = piece
        self.echiquier.jeu[piece.coordone[0]][piece.coordone[1]].piece = None
        if not self.piece is None and self.piece.piece == 'pion':
            self.piece.premier_coup = False

        piece.coordone = self.coordone
        piece.maj_position()






