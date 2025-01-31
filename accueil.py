import pygame
from fonction_utile import import_image_resize

pygame.font.init()
print(pygame.font.get_fonts())
class Accueil:

     def __init__(self,screen):
         self.screen = screen
         self.screen_height = screen.get_height()
         self.screen_width = screen.get_width()
         self.all_bouton = []
         self.all_texte = []


         self.play_button0, self.play_button0_rect = import_image_resize('pieces_echecs/bouton_vierge.png',self.screen_width/4,screen.get_height()/7,screen.get_width()/8,screen.get_height()/3)
         self.all_bouton.append((self.play_button0, self.play_button0_rect))

         self.play_button1, self.play_button1_rect = import_image_resize('pieces_echecs/bouton_vierge.png',self.screen_width/4,screen.get_height()/7,screen.get_width()/8,screen.get_height() / 3 + self.play_button0_rect[3])
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
         self.font_petite = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.screen_width//37)

         self.texte_surface = self.font.render("jeu d'echec de julian et Maxence", True, (0, 0, 0))
         self.texte_surface_rect = self.texte_surface.get_rect()
         self.texte_surface_rect.x = screen.get_width()/8
         self.texte_surface_rect.y = screen.get_height()/4
         self.all_texte.append((self.texte_surface, self.texte_surface_rect))

         self.texte_surface0 = self.font_petite.render(" 1 v 1 ", True, (0, 0, 0))
         self.texte_surface0_rect = self.texte_surface.get_rect()
         self.texte_surface0_rect.x = screen.get_width() / 5
         self.texte_surface0_rect.y = screen.get_height()/3 + 0.3 * self.play_button1_rect[3]
         self.all_texte.append((self.texte_surface0, self.texte_surface0_rect))

         self.texte_surface1 = self.font_petite.render(" bot debile ", True, (0, 0, 0))
         self.texte_surface1_rect = self.texte_surface.get_rect()
         self.texte_surface1_rect.x = screen.get_width() / 7
         self.texte_surface1_rect.y = screen.get_height() / 3 + 1.3 * self.play_button1_rect[3]
         self.all_texte.append((self.texte_surface1, self.texte_surface1_rect))

         self.texte_surface2 = self.font_petite.render(" bot 1coup ", True, (0, 0, 0))
         self.texte_surface2_rect = self.texte_surface.get_rect()
         self.texte_surface2_rect.x = screen.get_width() / 7
         self.texte_surface2_rect.y = screen.get_height() / 3 + 2.3 * self.play_button2_rect[3]
         self.all_texte.append((self.texte_surface2, self.texte_surface2_rect))

         self.texte_surface3 = self.font_petite.render(" bot minmax ", True, (0, 0, 0))
         self.texte_surface3_rect = self.texte_surface.get_rect()
         self.texte_surface3_rect.x = screen.get_width() / 7
         self.texte_surface3_rect.y = screen.get_height() / 3 + 3.3 * self.play_button3_rect[3]
         self.all_texte.append((self.texte_surface3, self.texte_surface3_rect))


     def update(self):
         """
         :return: affiche tout les boutton de l'acceuil
         """
         for elem in self.all_bouton:
             elem_img, elem_rect = elem
             self.screen.blit(elem_img,elem_rect)

         for texte in self.all_texte:
             texte_img, texte_rect = texte
             self.screen.blit(texte_img, texte_rect)



