from socket import fromfd
from time import sleep
from game import Game
import pygame
import pygame.freetype
from accueil import Accueil

pygame.init()
# pygame.time.get_ticks pour avoir le nombre de tick ecoulé
screen = pygame.display.set_mode((1000,600))

running = True



clock = pygame.time.Clock()


ga = Game(screen)
ecran_accueil = Accueil()


while running:
    if ga.en_menu :
        screen.fill((42, 206, 166))
        #pygame.draw.rect(screen,(42, 206, 166),[0,0,screen.get_width(),screen.get_height()])
        screen.blit(ecran_accueil.texte_surface, ecran_accueil.texte_surface_rect)
        screen.blit(ecran_accueil.play_button,ecran_accueil.play_button_rect)


    else:
        ga.update()

    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()





        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ga.en_menu:
                if ecran_accueil.play_button_rect.collidepoint(event.pos):
                    ga.en_menu = False

            if not ga.en_menu :
                click_case = (
                int(event.pos[0] // (screen.get_height() / 8)), int(event.pos[1] // (screen.get_height() / 8)))
                print(click_case)
                if ga.piece_selectione == None:
                    for elem in ga.echiquier.all_case:
                        if elem.coordone == click_case:
                            print(elem.piece)
                            ga.piece_selectione = elem.piece
                else:
                    for elem in ga.echiquier.all_case:
                        if elem.coordone == click_case:
                            if elem.piece == None:
                                elem.changer_pion(ga.piece_selectione)

        elif event.type == pygame.KEYDOWN :

            if event.key == pygame.K_SPACE:
                screen = pygame.display.set_mode((1550, 790))
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
                print('hihi')

