import pygame

class Pion(pygame.sprite.Sprite):

    def __init__(self,x,y,screen,color):
        super().__init__()
        self.piece = 'pion'
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height / 8
        self.color = color
        self.coup = [(1,1)]
        if color == 'blanc':
            self.image = pygame.image.load('pieces_echecs/pion_blanc.png')
        else:
            self.image = pygame.image.load('pieces_echecs/pion_noir.png')
        self.image = pygame.transform.scale(self.image, (self.taille_case, self.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.taille_case*x
        self.rect.y = self.taille_case*y
        self.coordone = (x,y)

    def maj_position(self):
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]

class Cheval(pygame.sprite.Sprite):

    def __init__(self,x,y,screen,color):
        super().__init__()
        self.piece = 'cheval'
        self.screen = screen
        self.screen_height = screen.get_height()
        self.taille_case = self.screen_height / 8
        self.color = color
        if color == 'blanc':
            self.image = pygame.image.load('pieces_echecs/cheval_blanc.png')
        else:
            self.image = pygame.image.load('pieces_echecs/cheval_noir.png')
        self.image = pygame.transform.scale(self.image, (self.taille_case, self.taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = self.taille_case*x
        self.rect.y = self.taille_case*y
        self.coordone = (x,y)

    def maj_position(self):
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]


class Fou(pygame.sprite.Sprite):

    def __init__(self,x,y, screen, color,echiquier):
        super().__init__()
        self.echiquier = echiquier
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
        self.rect.x = self.taille_case * x
        self.rect.y = self.taille_case * y
        self.coordone = (x, y)
        self.coup = []

    def maj_position(self):
        self.rect.x = self.taille_case * self.coordone[0]
        self.rect.y = self.taille_case * self.coordone[1]

    def coup_possible(self):
        self.coup.clear()
        x = self.coordone[0]
        y = self.coordone[1]
        for i in range(x+1, 8):
            if y + i - x > 7 or  y + i - x < 0:
                print('hors echiquier '+ str(y + i - x) )
                break
            elif not self.echiquier.jeu[i][y + i - x].piece is None:
                print("y'a un truc sur "+str(i)+' '+str(y + i - x) + '  ' + str(self.echiquier.jeu[i][y + i - x].piece))
                self.coup.append((i, y + i - x))
                break
            else :
                self.coup.append((i, y + i - x))

        for i in range(x-1,-1,-1):
            if  y - i + x > 7 or  y - i + x < 0 :
                break
            elif not self.echiquier.jeu[i ][y-i+x].piece is None :
                self.coup.append((i, y - i + x))
                break
            else:
                self.coup.append((i, y - i + x))

        for i in range(y-1,-1,-1):
            if x - i + y > 7 or x - i + y < 0 :
                break
            elif not self.echiquier.jeu[x - i + y][i].piece is None :
                self.coup.append((x - i + y, i))
                break
            else:
                self.coup.append((x - i + y, i))

        """for i in range(y+1, 8):
            if x + i - y > 7 or x + i - y < 0:
                break
            elif not self.echiquier.jeu[x + i - y][i].piece is None :
                self.coup.append((x + i - y, i))
                break
            else:
                self.coup.append((x + i - y, i))"""

        for i in range(y-1,-1,-1):
            if x + i - y > 7 or x + i - y < 0 :
                break
            elif not self.echiquier.jeu[x + i - y][i].piece is None :
                self.coup.append((x + i - y, i))
                break
            else:
                self.coup.append((x + i - y, i))

        return self.coup


