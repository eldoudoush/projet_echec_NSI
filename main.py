from socket import fromfd
from time import sleep
from game import Game
import pygame


screen = pygame.display.set_mode((500,400))

running = True


ga = Game(screen)



while running:
    ga.update()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                screen = pygame.display.set_mode((1550, 790))
                ga = Game(screen)
            if event.key == pygame.K_e:
                screen = pygame.display.set_mode((500,400))
                ga = Game(screen)

