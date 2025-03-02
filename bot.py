from random import randint
from math import inf

class Bot():

    def __init__(self,game):
        self.game= game
        self.coup_min_max = []

    def calcule_coup_aleatoire(self):
        if self.game.couleur_joueur == 'blanc' :
            liste_coup = self.game.coup_blanc
            liste_piece = self.game.piece_blanc
        else:
            liste_coup = self.game.coup_noir
            liste_piece = self.game.piece_noir

        if len(liste_coup) == 0 :
            return 'check mate'
        val = randint(0, len(liste_piece) - 1)
        piece = liste_piece[val]
        while len(piece.coup) == 0 :
            val = randint(0,len(liste_piece)-1)
            piece = liste_piece[val]
        if len(piece.coup) <= 1 :
            val2 = 0
        else:
            val2 = randint(0,len(piece.coup)-1)
        # print(val2)
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
            jouer_coup_random(self,liste_coup_renvoye[0])
            self.game.changer_couleur()

        if calcul :
            return liste_coup_renvoye


    def calcule_coup_minmax(self,depth,couleur,score=0,d=0):
        if d == depth :
            return score

        if d%2 == 0 :
            couleur_actuelle = couleur
            pos_neg = True #dit si on compte en positif ou en negatif la valeur du coup True = positif
        elif couleur == 'blanc':
            couleur_actuelle = 'noir'
            pos_neg = False
        else :
            couleur_actuelle = 'blanc'
            pos_neg = False

        meilleurcoup = self.calcule_meilleur_coup(couleur_actuelle,calcul=True,compte_pos_neg=pos_neg)
        # print('bot calcule fors :',d,' la liste a traite ',meilleurcoup)
        score_actuel = score + meilleurcoup[-1]

        for i in range(len(meilleurcoup[0])-2) :
            if score >= meilleurcoup[-1]:
                break
            coup_actuel = meilleurcoup[i]
            jouer_coup(self, coup_actuel)

            self.calcule_coup_minmax(depth, couleur, score=score_actuel  ,d=d + 1)
            dejouer_un_coup(self, coup_actuel)

    def min_max(self,d,est_maximisant,couleur,depht):
        if depht == d :
            return valeur_coup(self)

        if couleur == 'noir' :
            couleur_suivante = 'blanc'
        else :
            couleur_suivante = 'noir'

        all_coup = tout_les_coup(self,couleur)
        if all_coup == 'check mate':
            return inf if est_maximisant else -inf

        if est_maximisant:
            meilleur_score = -inf
            for mouvement in all_coup :
                jouer_coup(self, mouvement)
                score = self.min_max(d,False,couleur_suivante,depht +1)
                dejouer_un_coup(self)
                meilleur_score = max(meilleur_score, score)
                # print("c'est le coup jouer ", mouvement,'et la profonduer : ',depht, ' et le score: ',score)
            return meilleur_score
        else:
            meilleur_score = inf
            for mouvement in all_coup:
                jouer_coup(self,mouvement)
                score = self.min_max(d,True,couleur_suivante,depht + 1)
                dejouer_un_coup(self)
                meilleur_score = min(meilleur_score, score)
                # print("c'est le coup jouer ", mouvement, 'et la profonduer : ', depht, ' et le score: ', score)
            return meilleur_score

    def jouer_min_max(self,d,est_maximisant,couleur):
        self.coup_min_max.clear()
        meilleur_move = []
        meilleur_score = -inf
        couleur_suivante = 'blanc' if couleur == 'noir' else 'noir'
        for move in tout_les_coup(self,couleur):
            jouer_coup(self,move)
            score_actuelle = self.min_max( d , not est_maximisant,couleur_suivante,1)
            dejouer_un_coup(self)
            if score_actuelle > meilleur_score:
                meilleur_score = score_actuelle
                meilleur_move.append(move)
            elif score_actuelle == meilleur_score:
                meilleur_move.append(move)

        jouer_coup_random(self,meilleur_move)
        self.game.changer_couleur()


    def coup_joue_min_max(self,depth,couleur):
        self.coup_min_max.clear()
        self.calcule_coup_minmax(depth,couleur)
        coup_a_joue =  []
        meilleur_score = -inf

        for coup in self.coup_min_max :
            if coup[1] > meilleur_score:
                coup_a_joue.clear()
                coup_a_joue.append(coup[0])
                meilleur_score = coup[1]
            elif coup[1] == meilleur_score:
                coup_a_joue.append(coup[0])
        # print('les coup de la zion',coup_a_joue,'les autreeeeeeeeeeee ',self.coup_min_max)

        jouer_coup_random(self, coup_a_joue)
        self.game.changer_couleur()




def jouer_coup(bot,coup_jouer,pas_sup=True):
    """for i in range(0,len(liste),2):
        randnb = randint(0, len(liste[i]) - 1)
        coup_jouer = liste[i][randnb]
        print("c'est le coup jouer ",coup_jouer)
        x, y = coup_jouer[0]
        if len(coup_jouer) == 3:
            bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1])
        else:
            bot.game.echiquier.jeu[x][y].manger_pion(coup_jouer[1])
        if coup_jouer[1].piece == 'pion':
            coup_jouer[1].premier_coup = False"""
    bot.coup_min_max.append(coup_jouer)
    x, y = coup_jouer[0]
    if len(coup_jouer) == 3 :
        bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1],pas_suprimer=pas_sup)
    else:
        # print('!!!!!!!!!!!!!!!!!!!!!!!!',coup_jouer)
        # print('?????????????????????????',bot.game.echiquier.jeu[x][y].piece)
        bot.game.echiquier.jeu[x][y].manger_pion(coup_jouer[1],pas_suprimer=pas_sup)
    if coup_jouer[1].piece == 'pion':
        coup_jouer[1].premier_coup = False

def jouer_coup_random(bot,liste):
    if len(liste) <= 1 :
        randnb = 0
    else:
        randnb = randint(0, len(liste) - 1)
    if randnb > len(liste)-1 :
        return
    # print(liste)
    coup = liste[randnb]
    x,y = coup[0]
    if len(coup) == 3:
        bot.game.echiquier.jeu[x][y].changer_pion(coup[1])
    else:
        bot.game.echiquier.jeu[x][y].manger_pion(coup[1])

def jouer_coup_exact(bot,liste):
    if liste is None:
        return
    for i in range(0,len(liste),2):
        elem = liste[i]
        coup_jouer = elem
        x, y = elem[0]
        if len(elem) == 3:
            bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1],pas_suprimer=True)
        else:
            bot.game.echiquier.jeu[x][y].manger_pion(coup_jouer[1],pas_suprimer=True)
        if coup_jouer[1].piece == 'pion':
            coup_jouer[1].premier_coup = False

def dejouer_un_coup(bot):

    if len(bot.coup_min_max) == 0 :
        return 'probleme de bz'
    coup_jouer = bot.coup_min_max.pop(len(bot.coup_min_max)-1)

    x, y = coup_jouer[2]
    a, b = coup_jouer[0]
    if len(coup_jouer) == 3 :
        bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1],pas_suprimer=True)
    else:
        bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1],pas_suprimer=True)
        bot.game.echiquier.jeu[a][b].changer_pion(coup_jouer[3],True,True)
        if coup_jouer[3].color == 'blanc':
            bot.game.piece_blanc.append(coup_jouer[3])
        else:
            bot.game.piece_noir.append(coup_jouer[3])

    if coup_jouer[1].piece == 'pion':
        coup_jouer[1].premier_coup = True

def valeur_coup(bot) :
    score_coup = 0
    for elem in bot.game.piece_noir:
        score_coup += elem.val
    for elem in bot.game.piece_blanc:
        score_coup -= elem.val
    return score_coup

def tout_les_coup(bot,couleur):
    liste_coup_jouable = []

    if couleur == 'blanc':
        # bot.game.calcul_coup_blanc()
        bot.game.calcul_coup_noir()
        coup_blanc = bot.game.calcul_coup_blanc(True)
        liste_piece = bot.game.piece_blanc
        if len(coup_blanc) == 0:
            return 'check mate'
    else:
        liste_piece = bot.game.piece_noir
        # bot.game.calcul_coup_noir()
        bot.game.calcul_coup_blanc()
        coup_noir = bot.game.calcul_coup_noir(True)
        if len(coup_noir) == 0:
            return 'check mate'

    for piece in liste_piece:
        for mouvement in piece.coup:
            x, y = mouvement
            coup = (mouvement, piece, piece.coordone) if bot.game.echiquier.jeu[x][y].piece is None else (
                mouvement, piece, piece.coordone, bot.game.echiquier.jeu[x][y].piece)
            liste_coup_jouable.append(coup)
    return liste_coup_jouable


# for i in range(len(liste)-2,-1,-2):
#         elem = liste[i]
#         coup_jouer = elem
#         x, y = elem[2]
#         a,b = elem[0]
#         if len(coup_jouer) == 3:
#             bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1])
#         else:
#             bot.game.echiquier.jeu[x][y].changer_pion(coup_jouer[1])
#             bot.game.echiquier.jeu[a][b].changer_pion(coup_jouer[3])
#             if coup_jouer[3].color == 'blanc':
#                 bot.game.piece_blanc.append(coup_jouer[3])
#             else:
#                 bot.game.piece_noir.append(coup_jouer[3])
#
#             if coup_jouer[1].piece == 'pion' :
#                 coup_jouer[1].premier_coup = True