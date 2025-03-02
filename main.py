from utilitaire.constante import screen
from game import Game
import pygame
import random


pygame.init()
# pygame.time.get_ticks pour avoir le nombre de tick ecoulé depuis lancement de la fenetre


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

            ga.scene_droite.temp_timer_reduction()


        elif event.type == changecouleur: # ce declanche chaque quar second
            # ga.rgb = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            # ga.rgb = (100,150,50)
            ...

        elif event.type == pygame.MOUSEBUTTONDOWN: #click de la souri


            if ga.en_menu:
                if ga.ecran_accueil.play_button0_rect.collidepoint(event.pos):
                    ga.choix_mode_jeu(None)
                elif ga.ecran_accueil.play_button1_rect.collidepoint(event.pos):
                    ga.choix_mode_jeu(1)
                elif ga.ecran_accueil.play_button2_rect.collidepoint(event.pos):
                    ga.choix_mode_jeu(2)
                elif ga.ecran_accueil.play_button3_rect.collidepoint(event.pos):
                    ga.choix_mode_jeu(3)

            if not ga.en_menu and not ga.parametre.est_afficher :

                if ga.afficher_mat and ga.bouton_restart_rect.collidepoint(event.pos):
                    ga.reset()
                click_case = (
                int(event.pos[0] // (screen.get_height() / 8)), int(event.pos[1] // (screen.get_height() / 8)))
                if ga.piece_selectione is None:
                    for elem in ga.echiquier.all_case :
                        #ga.echiquier.jeu[5][5].rock_noir(click_case,ga.echiquier.jeu[0][0].piece)
                        if elem.coordone == click_case and not elem.piece is None and elem.piece.color == ga.couleur_joueur:
                            ga.changer_piece_selectionner(elem.piece)
                else:
                    if click_case in ga.piece_selectione.coup :
                        elem = ga.echiquier.jeu[click_case[0]][click_case[1]]
                        if elem.piece is None:
                            elem.changer_pion(ga.piece_selectione)
                            ga.changer_couleur()
                            if ga.piece_selectione.piece == 'pion' :
                                ga.piece_selectione.premier_coup = False
                            ga.changer_piece_selectionner(None)

                        else:
                            elem.manger_pion(ga.piece_selectione)
                            ga.changer_couleur()
                            ga.changer_piece_selectionner(None)
                    else :
                        piece_selec = ga.piece_selectione
                        for elem in ga.echiquier.all_case:
                            if elem.coordone == click_case and not elem.piece is None and elem.piece.color == ga.couleur_joueur:
                                ga.changer_piece_selectionner(elem.piece)
                        if piece_selec == ga.piece_selectione:
                            ga.changer_piece_selectionner(None)
            ga.parametre.cliquer_parametre(event.pos)

        elif event.type == pygame.KEYDOWN : #quand un boutton est appuyer

            if event.key == pygame.K_SPACE:
                screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
                ga = Game(screen)
            elif event.key == pygame.K_e:
                ga.echiquier.jeu[5][5].changer_pion(ga.echiquier.jeu[0][0].piece)
            elif event.key == pygame.K_e:
                screen = pygame.display.set_mode((500,400))
                ga =  Game(pygame.display.set_mode((500,400)))
            elif event.key == pygame.K_d:
                x = input()
                print(ga.echiquier.jeu[x[0],x[1]].piece)
            elif event.key == pygame.K_3:
                ga.echiquier.jeu[3][3].changer_pion(ga.echiquier.jeu[0][0].piece)


            elif event.key == pygame.K_q:
                ga.afficher_mat = True

            elif event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()


            elif event.key == pygame.K_h:
                if ga.couleur_joueur == 'noir':
                    ga.couleur_joueur = 'blanc'
                else:
                    ga.couleur_joueur = 'noir'

            elif event.key == pygame.K_l:
                ga.afficher_mat = True
                ga.draw = True


    ga.update() #création de tout l'affichage graphique

    pygame.display.flip() #projection de tout l'affichage graphique


    clock.tick(60) # frame rate (60 fps ici)

