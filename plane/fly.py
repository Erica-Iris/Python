import pygame

pygame.init()
icon = pygame.image.load('./b.png')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('plane')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
