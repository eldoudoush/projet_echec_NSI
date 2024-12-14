import pygame

pygame.font.init()
print(pygame.font.get_fonts())
class Accueil:

    def __init__(self):
         self.play_button = pygame.image.load('piece/play_button.png')
         self.play_button_rect = self.play_button.get_rect()
         self.play_button_rect.x = 200
         self.play_button_rect.y = 100

         self.texte = pygame.font.Font(None, 50)
         self.texte_surface = self.texte.render("jeu d'échec de julian es Maxence !", True, (0, 0, 0))
         self.texte_surface_rect = self.texte_surface.get_rect()
         self.texte_surface_rect.x = 200
         self.texte_surface_rect.y = 150