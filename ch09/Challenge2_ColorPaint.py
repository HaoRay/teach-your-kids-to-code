# ColorPaint.py
import pygame                           # setup
import random
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Click and drag to draw, using up to 3 mouse buttons')
keepGoing = True
ORANGE = (255,255,0)     # RGB color triplets for 3 mousebutton colors
GREEN = (0,255,0)
PURPLE = (128,0,128)
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
        if pygame.mouse.get_pressed()[0] : # boolean for button1
            button_color = ORANGE
        elif pygame.mouse.get_pressed()[1]: # boolean for button2
            button_color = GREEN
        else:   # must be button3
            button_color = PURPLE
        pygame.draw.circle(screen, button_color, spot, radius)
    pygame.display.update()             # update display
        
pygame.quit()                           # exit
