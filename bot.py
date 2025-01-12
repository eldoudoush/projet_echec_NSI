from random import randint

class Bot():

    def __init__(self,game):
        self.game= game

    def calcule_coup_aleatoire(self):
        if len(self.game.coup_noir) == 0 :
            return 'check mate'
        val = randint(0, len(self.game.piece_noir) - 1)
        piece = self.game.piece_noir[val]
        while len(piece.coup) == 0 :
            val = randint(0,len(self.game.piece_noir)-1)
            piece = self.game.piece_noir[val]
        if len(piece.coup) <= 1 :
            val2 = 0
        else:
            val2 = randint(0,len(piece.coup)-1)
        print(val2)
        x,y = piece.coup[val2]

        if self.game.echiquier.jeu[x][y].piece is None :
            self.game.echiquier.jeu[x][y].changer_pion(piece)
        else :
            self.game.echiquier.jeu[x][y].manger_pion(piece)
        if piece.piece == 'pion':
            piece.premier_coup = False
        self.game.changer_couleur()

    def calcule_meilleur_coup(self,couleur,calcul=False):
        meilleur_coup = None
        meilleur_coup_piece = None
        meilleur_coup_score = 0
        if couleur == 'blanc':
            self.game.calcul_coup_noir()
            coup_blanc = self.game.calcul_coup_blanc(True)
            liste_piece = self.game.piece_blanc
            if len(coup_blanc) == 0:
                return 'check mate'
        else :
            liste_piece = self.game.piece_noir
            self.game.calcul_coup_blanc()
            coup_noir = self.game.calcul_coup_noir(True)
            if len(coup_noir) == 0:
                return 'check mate'

        for piece in liste_piece :
            for coup in piece.coup:
                x,y = coup
                if not self.game.echiquier.jeu[x][y].piece is None and self.game.echiquier.jeu[x][y].piece.piece != 'ima':
                    val = self.game.echiquier.jeu[x][y].piece.val
                    if val >= meilleur_coup_score :
                        meilleur_coup = coup
                        meilleur_coup_score = val
                        meilleur_coup_piece = piece
                else :
                    if meilleur_coup_score == 0:
                        meilleur_coup_piece = piece
                        meilleur_coup = coup

        x, y = meilleur_coup
        if calcul and self.game.echiquier.jeu[x][y].piece is None:
            meilleur_coup_piece_pos = meilleur_coup_piece.coordone
        elif calcul :
            piece_mange = self.game.echiquier.jeu[x][y].piece
        if self.game.echiquier.jeu[x][y].piece is None :
            self.game.echiquier.jeu[x][y].changer_pion(meilleur_coup_piece)
        else :
            self.game.echiquier.jeu[x][y].manger_pion(meilleur_coup_piece)
        if meilleur_coup_piece.piece == 'pion':
            meilleur_coup_piece.premier_coup = False
        self.game.changer_couleur()

        if calcul and self.game.echiquier.jeu[x][y].piece is None:
            return [meilleur_coup,meilleur_coup_piece_pos]
        elif calcul :
            return [meilleur_coup, meilleur_coup_piece_pos,piece_mange]


    def calcule_coup_minmax(self,depth,couleur,coup_precedent=None,d=0):


        if d == depth :
            return meilleur_coup
        if couleur == 'blanc':
            self.calcul_coup_minmax(depth,'noir',d=d+1)
        else :
            self.calcul_coup_minmax(depth, 'blanc', d=d + 1)
        if not coup_precedent is None:
            if len(coup_precedent) == 3:
                x,y = coup_precedent[0]
                x1,y1 = coup_precedent[1]
                piece = self.game.echiquier.jeu[x][y]
                self.game.echiquier.jeu[x1][y1].changer_pion(piece)
                self.game.echiquier.jeu[x][y].piece = coup_precedent[2]
            else :

                x, y = coup_precedent[0]
                x1, y1 = coup_precedent[1]
                piece = self.game.echiquier.jeu[x][y]
                self.game.echiquier.jeu[x1][y1].changer_pion(piece)