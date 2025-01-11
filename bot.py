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
        self.game.changer_couleur()