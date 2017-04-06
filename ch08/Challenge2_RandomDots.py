# RandomDots.py
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800, 600])

keep_going = True
BLACK = (0,0,0)

# colors, locations, sizes arrays for 100 random dots
colors = [0]*100
locations = [0]*100
sizes = [0]*100
# store random values in colors, locations, sizes
for n in range(100):
    colors[n] = (random.randint(0,255),random.randint(0,255),
                 random.randint(0,255))
    locations[n] = (random.randint(0,800),
                    random.randint(0,600))
    sizes[n] = random.randint(10, 100)

while keep_going:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keep_going = False
    for n in range(100):
        pygame.draw.circle(screen, colors[n], locations[n],
                           sizes[n])
    pygame.display.update()
    screen.fill(BLACK)
   
pygame.quit()
