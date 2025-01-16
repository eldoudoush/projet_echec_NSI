from random import randint

class Bot():

    def __init__(self,game):
        self.game= game
        self.coup_min_max = set()

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

    def calcule_meilleur_coup(self,couleur,calcul=False,compte_pos_neg=False):
        meilleur_coup_score = 0
        liste_coup_renvoye = []

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
                    if val > meilleur_coup_score :
                        liste_coup_renvoye.clear()
                        liste_coup_renvoye.append((coup,piece,piece.coordone,self.game.echiquier.jeu[x][y].piece))
                        meilleur_coup_score = val
                    elif val == meilleur_coup_score :
                        liste_coup_renvoye.append((coup, piece, piece.coordone,self.game.echiquier.jeu[x][y].piece))
                else :
                    if meilleur_coup_score == 0:
                        liste_coup_renvoye.append((coup, piece, piece.coordone))
        if compte_pos_neg:
            liste_coup_renvoye = [liste_coup_renvoye,-meilleur_coup_score]
        else:
            liste_coup_renvoye = [liste_coup_renvoye, meilleur_coup_score]

        if not calcul :
            jouer_coup(self,liste_coup_renvoye)
            self.game.changer_couleur()

        if calcul :
            return liste_coup_renvoye


    def calcule_coup_minmax(self,depth,couleur,coup_precedent=None,d=0):
        if d == depth :
            self.coup_min_max.add((coup_precedent[0],coup_precedent[1]))
            return
        if d%2 == 0 :
            couleur_actuelle = couleur
            pos_neg = True #dit si on compte en positif ou en negatif la valeur du coup True = positif
        elif couleur == 'blanc':
            couleur_actuelle = 'noir'
            pos_neg = False
        else :
            couleur_actuelle = 'blanc'
            pos_neg = False
        jouer_coup_exact(self,coup_precedent)
        meilleurcoup = self.calcule_meilleur_coup(couleur_actuelle,calcul=True,compte_pos_neg=pos_neg)
        dejouer_coup(self,coup_precedent)
        print('bot calcule fors :',d,' la liste a traite ',meilleurcoup)

        for i in range(len(meilleurcoup[0])-2) :
            if coup_precedent is None :
                coup_suivant = []
                coup_suivant.append(meilleurcoup[0][i])
                coup_suivant.append(meilleurcoup[1])
            else:
                coup_suivant = coup_precedent.copy()
                coup_suivant.append(meilleurcoup[0][i])
                coup_suivant.append(meilleurcoup[1]+coup_precedent[1])
            self.calcule_coup_minmax(depth, couleur,coup_precedent=coup_suivant ,d=d + 1)



    def coup_joue_min_max(self,depth,couleur):
        self.coup_min_max.clear()
        self.calcule_coup_minmax(depth,couleur)
        coup_a_joue =  []
        meilleur_score = -9999

        for coup in self.coup_min_max :
            if coup[1] > meilleur_score:
                coup_a_joue.clear()
                coup_a_joue.append(coup[0])
                meilleur_score = coup[1]
            elif coup[1] == meilleur_score:
                coup_a_joue.append(coup[0])
        print('les coup de la zion',coup_a_joue,'les autreeeeeeeeeeee ',self.coup_min_max)

        jouer_coup_random(self, coup_a_joue)
        self.game.changer_couleur()




def jouer_coup(bot,liste):
    for i in range(0,len(liste),2):
        randnb = randint(0, len(liste[i]) - 1)
        coup_jouer = liste[i][randnb]
        print("c'est le coup jouer ",coup_jouer)
        x, y = coup_jouer
        if len(coup_jouer) == 3:
            bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1])
        else:
            bot.game.echiquier.jeu[x][y].manger_pion(coup_jouer[1])
        if coup_jouer[1].piece == 'pion':
            coup_jouer[1].premier_coup = False

def jouer_coup_random(bot,liste):
    if len(liste) <= 1 :
        randnb = 0
    else:
        randnb = randint(0, len(liste) - 1)
    coup = liste[randnb]
    x,y = coup[0]
    if len(coup) == 3:
        bot.game.echiquier.jeu[x][y].changer_pion(coup[1])
    else:
        bot.game.echiquier.jeu[x][y].manger_pion(coup[1])
    if coup[1].piece == 'pion':
        coup[1].premier_coup = False

def jouer_coup_exact(bot,liste):
    if liste is None:
        return
    for i in range(0,len(liste),2):
        elem = liste[i]
        coup_jouer = elem
        x, y = elem[0]
        if len(elem) == 3:
            bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1])
        else:
            bot.game.echiquier.jeu[x][y].manger_pion(coup_jouer[1],pas_suprimer=True)
        if coup_jouer[1].piece == 'pion':
            coup_jouer[1].premier_coup = False

def dejouer_coup(bot,liste):
    if liste is None:
        return
    for i in range(len(liste)-2,-1,-2):
        elem = liste[i]
        coup_jouer = elem
        x, y = elem[2]
        a,b = elem[0]
        if len(coup_jouer) == 3:
            bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1])
        else:
            bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1])
            bot.game.echiquier.jeu[a][b].changer_pion(coup_jouer[3])
            if coup_jouer[3].color == 'blanc':
                bot.game.piece_blanc.append(coup_jouer[3])
            else:
                bot.game.piece_noir.append(coup_jouer[3])

            if coup_jouer[1].piece == 'pion' :
                coup_jouer[1].premier_coup = True
