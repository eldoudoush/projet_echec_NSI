from time import sleep

import pygame

screen = pygame.display.set_mode((1420,1080))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    sleep(0.005)

