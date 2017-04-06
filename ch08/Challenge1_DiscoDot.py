# DiscoDot.py
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800, 600])

keepGoing = True
GREEN = (0,255,0) # RGB color triplet for GREEN
radius = 50

while keepGoing:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keepGoing = False
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.circle(screen, color, (100,100), radius)
    pygame.display.update()
   
pygame.quit()
