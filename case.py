

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
            self.color = (58,34,10) #(93, 190, 37)

    def changer_pion(self,piece,pas_suprimer=False,replacer_pion=False):
        """
        :param piece: piece
        :param pas_suprimer: bool
        :param replacer_pion: bool
        :return: change le pion de la case par celui pris en paramètre,
        si pas_suprimer alors n'applique pas les modifications pour le supprimer du jeu
        si replacer_pion alors remplace le pion de la possition precedente de la piece par un None
        """
        self.piece = piece
        if not replacer_pion :
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
        # print(self.piece)
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


        if self.piece.piece == 'pion':
            self.piece.premier_coup = False

        piece.coordone = self.coordone
        piece.maj_position()



    def rock_noir(self,click,tour):
        if click==(3,3):
            self.changer_pion(tour)


    def rock_noir_bis(self,click,rocks,king):
        if king.color=='noir' and not king.echec:
            if king.rockG and click==(0,1):
                ...
                #bouger tour en (0,2)

            elif king.rockD and click==(0,6):
                ...
                #bouger tour en (0,5)
        elif king.color == 'blanc' and not king.echec:
            if king.rockG and click==(7,1):
                ...
            # bouger tour en (7,2)
            elif king.rockD and click==(7,6):
                ...
        # bouger tour en (7,5)

