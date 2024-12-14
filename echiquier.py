from case import Case

class Echiquier:
    def __init__(self,screen):
        self.screen = screen
        self.screen_with = screen.get_height()
        self.all_case = []
        self.jeu = [[None for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                case = Case(j, i, self.screen,self)
                self.jeu[j][i] = case
                self.all_case.append(case)


