# RandomPaint.py
import pygame                           # setup
import random
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Click and drag to draw')
keepGoing = True
YELLOW = (255,255,0)     # RGB color triplet for YELLOW
radius = 15
mousedown = False

while keepGoing:                        # game loop
    for event in pygame.event.get():    # handling events
        if event.type == pygame.QUIT: 
            keepGoing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:                       # draw/update graphics
        spot = pygame.mouse.get_pos()
        randcolor = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        pygame.draw.circle(screen, randcolor, spot, radius)
    pygame.display.update()             # update display
        
pygame.quit()                           # exit
