

class Case:
    def __init__(self,x,y,screen,echiquier):
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height/8
        self.coordone = (x, y)
        self.piece = None
        self.echiquier = echiquier

        self.rect = [self.taille_case*x,self.taille_case*y,self.taille_case,self.taille_case]


        if sum(self.coordone)%2 == 1:
            self.color = (255,255,255)
        else:
            self.color = (93, 190, 37)

    def changer_pion(self,piece):
         self.piece = piece
         for elem in self.echiquier.all_case:
             if piece.coordone == elem.coordone:
                 elem.piece = None
         piece.coordone = self.coordone
         piece.maj_position()

    def manger_pion(self, piece):
        if self.piece.color == 'blanc':
            self.echiquier.game.scene_droite.piece_noir_manger.append(self.piece)
        else:
            self.echiquier.game.scene_droite.piece_blanc_manger.append(self.piece)
        self.echiquier.game.all_piece.remove(self.piece)
        self.piece = piece
        for elem in self.echiquier.all_case:
            if piece.coordone == elem.coordone:
                elem.piece = None
        """self.echiquier.game.scene_droite.append(piece.coordone)
        self.echiquier.game.scene_droite.append(piece.piece)
        self.echiquier.game.scene_droite.append()"""
        piece.coordone = self.coordone
        piece.maj_position()






