import pygame, sys
from pygame.locals import *

#set up pygame.
pygame.init()

#set up the window
windowSurface=pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Hello World!')

#set up some colors
BLACK=(0,0,0)
WHITE=(225,225,225)
RED=(225,0,0)
GREEN=(0,225,0)
BLUE=(0,0,225)

#set up font
basicFont= pygame.font.SysFont(None,48)

#set up text
text=basicFont.render('Hello World!', True, WHITE, BLUE)
textRect=text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#draw white background
windowSurface.fill(WHITE)

#draw a green polygon
pygame.draw.polygon(windowSurface, GREEN, ((146,0), (291,106),(236, 277), (56,277),(0,106)))

#draw some blue lines
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60,120))
pygame.draw.line(windowSurface, BLUE, (60,120), (120,120), 4)

#blue circle
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

#red ellipse
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40 ,80), 1)

#text background
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width+40, textRect.height + 40)) 

#pixle Array
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380]=BLACK
del pixArray

#drawText
windowSurface.blit(text, textRect)

#draw window
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()













