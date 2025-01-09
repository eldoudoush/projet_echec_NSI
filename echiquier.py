from case import Case
from roi import Roi
from cheval import Cheval
from piece import Pion ,Fou, Tour, Reine


class Echiquier:
    def __init__(self,screen,game):
        self.screen = screen
        self.screen_with = screen.get_height()
        self.game = game
        self.all_case = []
        self.jeu = [[None for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                case = Case(j, i, self.screen,self)
                self.jeu[j][i] = case
                self.all_case.append(case)
        self.création_piece()

    def création_piece(self):

        for i in range(8):
            pion1 =Pion(i,1,self.screen,'noir',self)
            pion2 =Pion(i, 6, self.screen, 'blanc',self)
            self.game.all_piece.add(pion1)
            self.game.all_piece.add(pion2)
            self.jeu[i][1].piece = pion1
            self.jeu[i][6].piece = pion2
        for i in range(0,8,7):
            tour1 = Tour(i,0,self.screen,'noir',self)
            tour2 = Tour(i,7,self.screen,'blanc',self)
            self.game.all_piece.add(tour1)
            self.game.all_piece.add(tour2)
            self.jeu[i][0].piece =tour1
            self.jeu[i][7].piece = tour2
        for i in range(1,7,5):
            cheval1 = Cheval(i, 0, self.screen, 'noir')
            cheval2 = Cheval(i, 7, self.screen, 'blanc')
            self.game.all_piece.add(cheval1)
            self.game.all_piece.add(cheval2)
            self.jeu[i][0].piece = cheval1
            self.jeu[i][7].piece = cheval2
        for i in range(2,6,3):
            fou1 = Fou(i, 0, self.screen, 'noir',self)
            fou2 = Fou(i, 7, self.screen, 'blanc',self)
            self.game.all_piece.add(fou1)
            self.game.all_piece.add(fou2)
            self.jeu[i][0].piece = fou1
            self.jeu[i][7].piece = fou2
        roi1 = Roi(3, 0, self.screen, 'noir')
        roi2 = Roi(3, 7, self.screen, 'blanc')
        self.game.all_piece.add(roi1)
        self.game.all_piece.add(roi2)
        self.jeu[3][0].piece = roi1
        self.jeu[3][7].piece = roi2

        reine1 = Reine(4, 0, self.screen, 'noir',self)
        reine2 = Reine(4, 7, self.screen, 'blanc',self)
        self.game.all_piece.add(reine1)
        self.game.all_piece.add(reine2)
        self.jeu[4][0].piece = reine1
        self.jeu[4][7].piece = reine2