from game import Game
import pygame
from accueil import Accueil
import random

pygame.init()
# pygame.time.get_ticks pour avoir le nombre de tick ecoulé depuis lancement de la fenetre
screen = pygame.display.set_mode((1000,600))

running = True

passesecone = pygame.USEREVENT + 1
clock = pygame.time.Clock()
pygame.time.set_timer(passesecone, 1000)
changecouleur = pygame.USEREVENT + 2
pygame.time.set_timer(changecouleur, 250)
ga = Game(screen)


while running:
    #event pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == passesecone: #ce declanche chaque second
            if not ga.en_menu :
                if ga.couleur_joueur == 'noir':
                    ga.scene_droite.temp_noir_reduction()
                elif ga.couleur_joueur == 'blanc':
                    ga.scene_droite.temp_blanc_reduction()

        elif event.type == changecouleur: # ce declanche chaque quar second
            ga.rgb = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        elif event.type == pygame.MOUSEBUTTONDOWN: #click de la souri
            if ga.en_menu:
                if ga.ecran_accueil.play_button_rect.collidepoint(event.pos):
                    ga.en_menu = False

            if not ga.en_menu :
                click_case = (
                int(event.pos[0] // (screen.get_height() / 8)), int(event.pos[1] // (screen.get_height() / 8)))
                print(click_case)
                if ga.piece_selectione is None:
                    for elem in ga.echiquier.all_case :
                        if elem.coordone == click_case and not elem.piece is None and elem.piece.color == ga.couleur_joueur:
                            print(elem.piece)
                            ga.changer_piece_selectionner(elem.piece)
                else:
                    for elem in ga.echiquier.all_case:
                        if elem.coordone == click_case:
                            if elem.piece is None:
                                elem.changer_pion(ga.piece_selectione)
                                ga.changer_couleur()
                                if ga.piece_selectione.piece == 'pion' :
                                    ga.piece_selectione.premier_coup = False
                                ga.changer_piece_selectionner(None)

                            else:
                                elem.manger_pion(ga.piece_selectione)
                                ga.changer_couleur()
                                if ga.piece_selectione.piece == 'pion' :
                                    ga.piece_selectione.premier_coup = False
                                ga.changer_piece_selectionner(None)

        elif event.type == pygame.KEYDOWN : #quand un boutton est appuyer

            if event.key == pygame.K_SPACE:
                screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
                ga = Game(screen)

            elif event.key == pygame.K_e:
                screen = pygame.display.set_mode((500,400))
                ga = Game(screen)
            elif event.key == pygame.K_d:
                ga.echiquier.jeu[0][0].changer_pion(ga.echiquier.jeu[1][1].piece)
            elif event.key == pygame.K_q:
                ga.echiquier.jeu[1][1].changer_pion(ga.echiquier.jeu[0][0].piece)
            elif event.key == pygame.K_z:
                ga.piece_selectione = None
                print('pion deselectione')

            elif event.key == pygame.K_h:
                if ga.couleur_joueur == 'noir':
                    ga.couleur_joueur = 'blanc'
                else:
                    ga.couleur_joueur = 'noir'


    ga.update() #création de tout l'affichage graphique

    pygame.display.flip() #projection de tout l'affichage graphique


    clock.tick(60) # frame rate (60 fps ici)

