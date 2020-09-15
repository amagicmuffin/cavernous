import pygame
from config import *




crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #print(event)
    
    #renderImg(dotImg,50,50)
    
    #pygame.display.update() #only update parts of thing
    #clock.tick(60) this piece of code crashes the thing after three or so seconds :)