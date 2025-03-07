import pygame

def import_image_resize(image_input:str,size_x:int, size_y:int , x:int , y:int):
    image = pygame.image.load(image_input)
    image = pygame.transform.scale(image, (size_x, size_y))
    rect = image.get_rect()
    rect.x = x
    rect.y = y
    return image ,rect

def cree_texte(taille_font:int,message:str,x:int,y:int):
    font = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', taille_font)
    texte = font.render(message, True, 'black'), (x, y)
    return texte[0],texte[1]

def clicker(rect:list[int],pos:tuple) -> None:
    return rect[0] <= pos[0] <= rect[2] + rect[0] and rect[1] <= pos[1] <= rect[3] + rect[1]

class BoiteTexte:
    def __init__(self,screen,restriction:str,taille_limite,rect:list[int],texte_originel:str=''):
        self.texte = texte_originel
        self.restriction = restriction
        self.taille_limite = taille_limite
        self.rect = rect
        x,y,sx,sy = rect
        self.font_size = int(sy*2/3)
        self.est_clicker = False
        self.texte_afficher,self.pos_texte = cree_texte(self.font_size,self.texte,int(x+sx/12),int(y+sy/6))
        self.screen = screen

    def update(self):
        pygame.draw.rect(self.screen,'white',self.rect)
        pygame.draw.rect(self.screen, 'black', self.rect, 3)
        self.screen.blit(self.texte_afficher,self.pos_texte)

    def changer_texte(self,texte):
        self.texte = texte
        self.texte_afficher, self.pos_texte = cree_texte(self.font_size, self.texte, self.pos_texte[0], self.pos_texte[1])

    def ajouter_texte(self,input:str):
        if not input in self.restriction:
            return
        if len(self.texte) >= self.taille_limite:
            return
        self.texte += input
        self.texte_afficher, self.pos_texte = cree_texte(self.font_size, self.texte, self.pos_texte[0], self.pos_texte[1])

    def suprimer_texte(self):
        if self.texte == '':
            return
        self.texte = self.texte[:len(self.texte) - 1]
        self.texte_afficher, self.pos_texte = cree_texte(self.font_size, self.texte, self.pos_texte[0],
                                                         self.pos_texte[1])

class GestionnaireDeBoiteTexte:
    def __init__(self):
        self.liste_boitetexte = []

    def append(self,boitetexte:BoiteTexte):
        self.liste_boitetexte.append(boitetexte)

    def uptdate(self):
        for elem in self.liste_boitetexte:
            elem.update()

    def activer_boitetexte(self,pos_curseur):
        for elem in self.liste_boitetexte:
            elem.est_clicker = False
            if clicker(elem.rect,pos_curseur):
                elem.est_clicker = True
                print('activer')

    def ajouter_boitetexte(self,event):
        for elem in self.liste_boitetexte:
            if elem.est_clicker:
                if event.key == pygame.K_BACKSPACE:
                    elem.suprimer_texte()
                else:
                    elem.ajouter_texte(event.unicode)