#Libraries
import pygame, sys
import time
import json
from pygame.locals import*


#Set up pygame.
pygame.init()

#Import image
img = json.loads(open('example.json','r').read())

#Set up the window.
windowSurface = pygame.display.set_mode((
    len(img['image']),
    len(img['image'][0])/3
    ), 0, 0)
pygame.display.set_caption("OJGI Image Demo")


#Draw the white background onto the surface.
windowSurface.fill((255,255,255))

#Get a pixel array of the surface. 
pixArray = pygame.PixelArray(windowSurface)
pixArray[0][0] = (0,0,0)
del pixArray

#Draw the window onto the screen.
pygame.display.update()

# region functions
def drawImage(json,offset = [0,0]):
    for y in range(len(json['image'])):
        for x in range(round(len(json['image'][0])/3)):
            pygame.draw.rect(windowSurface, 
                                (
                                    round((ord(json['image'][y][x*3])-65)*(256/10)),
                                    round((ord(json['image'][y][x*3+1])-65)*(256/10)),
                                    round((ord(json['image'][y][x*3+2])-65)*(256/10))
                                ),
                             pygame.Rect(x+offset[0],y+offset[1],1,1))

# draw image
drawImage(img,[0,0])
pygame.display.update()

# region game loop
while True:
    #Handle window close.
    for event in pygame.event.get():       
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    