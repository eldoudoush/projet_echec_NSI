import pygame

class Fou(pygame.sprite.Sprite):

    def __init__(self,x,y,screen,color):
        super().__init__()
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height / 8
        self.color = color
        if color == 'blanc':
            self.image = pygame.image.load('pieces_echecs/fou_blanc.png')
        else:
            self.image = pygame.image.load('pieces_echecs/fou_noir.png')
        self.image = pygame.transform.scale(self.image, (self.taille_case, self.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.taille_case*x
        self.rect.y = self.taille_case*y
        self.coordone = (x,y)
        self.x = x
        self.y = y
        self.coup = []

    def maj_position(self):
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]

    """
    def coup_possible(self):
        x = 0
        y = 0
        for i in range (self.x,8):
            self.coup.append((i,y+1))
            if présence sur la case[i][y+1]:
                break()
                
        for i in range (0,self.x):
            self.coup.append((i,y-1))
            if présence sur la case[i][y-1]:
                break()
                
        for i in range (0,self.y):
            self.coup.append((x-1,i))
            if présence sur la case[x-1][i]:
                break()
                
        for i in range (self.y,8):
            self.coup.append((x+1,i))
            if présence sur la case[x+1][i]:
                break()
    """
