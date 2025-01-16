'''
main.py

Owen Ziegler
15 Jan 2025

Main driver program, which sets up the window and starts the game loop.
'''
import pygame
#constants
WIDTH = 640
HEIGHT = 480
#initializations
pygame.init()
#display screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
#display window title
pygame.display.set_caption("sixshooter")
#icon = pygame.image.load('images/iconImage.png') fill in when you have one
#pygame.display.set_icon(icon)
#game loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
exit()
