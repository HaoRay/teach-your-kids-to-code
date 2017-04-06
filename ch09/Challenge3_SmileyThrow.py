import pygame
import random

BLACK = (0,0,0)
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Click and Drag to Throw Smileys')
mousedown = False
keep_going = True
clock = pygame.time.Clock()
pic = pygame.image.load('CrazySmile.bmp')
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
sprite_list = pygame.sprite.Group()

class Smiley(pygame.sprite.Sprite):
    pos = (0,0)
    xvel = 1
    yvel = 1
    scale = 100

    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pic
        self.scale = random.randrange(10,100)
        self.image = pygame.transform.scale(self.image, (self.scale,self.scale))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale/2
        self.rect.y = pos[1] - self.scale/2
        self.xvel = xvel
        self.yvel = yvel

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xvel = -self.xvel*.95
        if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
            self.yvel = -self.yvel*.95

while keep_going:
    pygame.mouse.get_rel()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    screen.fill(BLACK)
    sprite_list.update()
    sprite_list.draw(screen)
    clock.tick(60)
    pygame.display.update()
    if mousedown:
        (speedx,speedy) = pygame.mouse.get_rel()
        if speedx + speedy == 0:  # Move smiley even if mouse didn’t
            speedx = random.randrange(1,5)
            speedy = random.randrange(1,5)
        newSmiley = Smiley(pygame.mouse.get_pos(),speedx,speedy)
        sprite_list.add(newSmiley)
        
pygame.quit ()
