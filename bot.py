from random import randint
from math import inf

class Bot:

    def __init__(self,game):
        self.game= game #class game
        self.coup_min_max = [] #liste qui est géré comme une pile des coups joués par le bot s'il est en minmax

    def calcule_coup_aleatoire(self):
        """
        :return: joue un coup aléatoire parmie tous les coups possibles
        """
        tous_coup = tout_les_coup(self,self.game.couleur_bot)
        if tous_coup == 'check mate':
            print('check mate')
            return
        jouer_coup_random(self,tous_coup)

        self.game.changer_couleur()

    def calcule_meilleur_coup(self,couleur):
        meilleur_coup_score = -inf
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
                    if meilleur_coup_score < 0:
                        liste_coup_renvoye.append((coup, piece, piece.coordone))

        jouer_coup_random(self,liste_coup_renvoye[0])
        self.game.changer_couleur()




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
        tout_coup = tout_les_coup(self,couleur)
        if tout_coup == 'check mate' :
            return
        for move in tout_coup:
            jouer_coup(self,move)
            score_actuelle = self.min_max( d , not est_maximisant,couleur_suivante,1)
            dejouer_un_coup(self)
            if score_actuelle > meilleur_score:
                meilleur_move.clear()
                meilleur_score = score_actuelle
                meilleur_move.append(move)
            elif score_actuelle == meilleur_score:
                meilleur_move.append(move)

        jouer_coup_random(self,meilleur_move)
        self.game.changer_couleur()





def jouer_coup(bot,coup_jouer,pas_sup=True):
    """
    :param bot:  objet class Bot
    :param coup_jouer: tuple de 3 ou 4 element [case où bouger,piece,case actuelle,piece manger si piece sur la case en 1ere pos]
    :param pas_sup: a mettre True si le coup est pour le calcule pas pour etre jouer
    :return: joue le coup decrit dans coup_jouer
    """

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
    """
    :param bot: objet class Bot
    :param liste: liste de multiple coup chacun un tuple de 3 ou 4 element [case où bouger,piece,case actuelle,piece manger si piece sur la case en 1ere pos]
    :return: joue un coup aléatoire de la liste donner
    """
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

def dejouer_un_coup(bot):
    """
    :param bot: objet class Bot
    :return: dejou le dernier coup de la liste se situant dans bot
    """

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
        coup_jouer[1].compteur_coup -= 2
        if coup_jouer[1].compteur_coup == 0:
            coup_jouer[1].premier_coup = True

def valeur_coup(bot) :
    """
    :param bot: objet class Bot
    :return: renvoie la valeur du plateau selon la couleur du bot
    """
    score_coup = 0
    if bot.game.couleur_bot == 'noir':
        for elem in bot.game.piece_noir:
            score_coup += elem.val
        for elem in bot.game.piece_blanc:
            score_coup -= elem.val
    else:
        for elem in bot.game.piece_noir:
            score_coup -= elem.val
        for elem in bot.game.piece_blanc:
            score_coup += elem.val
    return score_coup

def tout_les_coup(bot,couleur):
    """
    :param bot: objet class Bot
    :param couleur: couleur dont on veut calculer tous les coups
    :return: liste contenant tous les coups jouables
    """
    liste_coup_jouable = []
    if couleur == 'blanc':
        bot.game.calcul_coup_noir()
        coup_blanc = bot.game.calcul_coup_blanc(True)
        liste_piece = bot.game.piece_blanc
        if len(coup_blanc) == 0:
            return 'check mate'
    else:
        liste_piece = bot.game.piece_noir

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

