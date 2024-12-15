import pygame

pygame.font.init()
print(pygame.font.get_fonts())
class Accueil:

    def __init__(self,screen):
         self.screen = screen
         self.screen_height = screen.get_height()
         self.screen_width = screen.get_width()

         self.play_button = pygame.image.load('piece/play_button.png')
         self.play_button = pygame.transform.scale(self.play_button, (self.screen_width/4,screen.get_height()/3))
         self.play_button_rect = self.play_button.get_rect()
         self.play_button_rect.x = screen.get_width()/8
         self.play_button_rect.y = screen.get_height()/4

         self.texte = pygame.font.Font(None,self.screen_width//20)
         self.texte_surface = self.texte.render("jeu d'échec de julian et Maxence !", True, (0, 0, 0))
         self.texte_surface_rect = self.texte_surface.get_rect()
         self.texte_surface_rect.x = screen.get_width()/8
         self.texte_surface_rect.y = screen.get_height()/4