import pygame

pygame.font.init()
print(pygame.font.get_fonts())
class Accueil:

     def __init__(self,screen):
         self.screen = screen
         self.screen_height = screen.get_height()
         self.screen_width = screen.get_width()
         self.all_bouton = []

         self.play_button0 = pygame.image.load('pieces_echecs/bouton_vierge.png')
         self.play_button0 = pygame.transform.scale(self.play_button0, (self.screen_width/4,screen.get_height()/7))
         self.play_button0_rect = self.play_button0.get_rect()
         self.play_button0_rect[0] = screen.get_width()/8
         self.play_button0_rect[1] = screen.get_height()/3
         self.all_bouton.append((self.play_button0,self.play_button0_rect))

         self.play_button1 = pygame.image.load('pieces_echecs/bouton_vierge.png')
         self.play_button1 = pygame.transform.scale(self.play_button1, (self.screen_width / 4, screen.get_height() / 7))
         self.play_button1_rect = self.play_button1.get_rect()
         self.play_button1_rect[0] = screen.get_width() / 8
         self.play_button1_rect[1] = screen.get_height() / 3 + self.play_button1_rect[3]
         self.all_bouton.append((self.play_button1,self.play_button1_rect))

         self.play_button2 = pygame.image.load('pieces_echecs/bouton_vierge.png')
         self.play_button2 = pygame.transform.scale(self.play_button2, (self.screen_width / 4, screen.get_height() / 7))
         self.play_button2_rect = self.play_button2.get_rect()
         self.play_button2_rect[0] = screen.get_width() / 8
         self.play_button2_rect[1] = screen.get_height() / 3 + 2 * self.play_button2_rect[3]
         self.all_bouton.append((self.play_button2,self.play_button2_rect))

         self.play_button3 = pygame.image.load('pieces_echecs/bouton_vierge.png')
         self.play_button3 = pygame.transform.scale(self.play_button3, (self.screen_width / 4, screen.get_height() / 7))
         self.play_button3_rect = self.play_button3.get_rect()
         self.play_button3_rect[0] = screen.get_width() / 8
         self.play_button3_rect[1] = screen.get_height() / 3 + 3 * self.play_button3_rect[3]
         self.all_bouton.append((self.play_button3,self.play_button3_rect))

         self.font = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.screen_width//30)
         self.texte_surface = self.font.render("jeu d'echec de julian et Maxence !", True, (0, 0, 0))
         self.texte_surface_rect = self.texte_surface.get_rect()
         self.texte_surface_rect.x = screen.get_width()/8
         self.texte_surface_rect.y = screen.get_height()/4

     def update(self):
          for elem in self.all_bouton:
               elem_img, elem_rect = elem
               self.screen.blit(elem_img,elem_rect)


