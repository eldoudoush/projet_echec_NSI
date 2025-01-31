import pygame

def import_image_resize(image_input,size_x , size_y , x , y):
    image = pygame.image.load(image_input)
    image = pygame.transform.scale(image, (size_x, size_y))
    rect = image.get_rect()
    rect.x = x
    rect.y = y
    return image ,rect

# def