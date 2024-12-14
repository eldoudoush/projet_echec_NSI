

class Case:
    def __init__(self,x,y,largeur,longueur,screen):
        self.rect = [x,y,largeur,longueur]
        self.screen = screen
        if (x/(self.screen.get_height()/8)+y/(self.screen.get_height()/8))%2 == 1:
            self.color = (255,255,255)
        else:
            self.color = (93, 190, 37)