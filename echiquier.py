from case import Case

class Echiquier:
    def __init__(self,screen):
        self.screen = screen
        self.screen_with = screen.get_height()
        self.jeu = [[None for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                self.jeu[i][j] = Case(j*(self.screen_with/8),i*(self.screen_with/8),(self.screen_with/8),(self.screen_with/8),self.screen)
